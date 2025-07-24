package org.ltc.reboot.hireassist.service;

import jakarta.mail.MessagingException;
import jakarta.mail.internet.MimeMessage;
import org.ltc.reboot.hireassist.entity.CandidateEntity;
import org.ltc.reboot.hireassist.entity.JobEntity;
import org.ltc.reboot.hireassist.model.JobBatchConfig;
import org.ltc.reboot.hireassist.repository.ReactiveCandidateRepository;
import org.ltc.reboot.hireassist.repository.ReactiveJobRepository;
import org.ltc.reboot.hireassist.util.JsonObjectParserUtil;
import org.ltc.reboot.hireassist.util.TimeHelper;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.mail.javamail.JavaMailSender;
import org.springframework.mail.javamail.MimeMessageHelper;
import org.springframework.scheduling.annotation.Scheduled;
import org.springframework.stereotype.Repository;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;
import reactor.core.publisher.Flux;
import reactor.core.publisher.Mono;
import reactor.core.scheduler.Scheduler;
import reactor.core.scheduler.Schedulers;

import java.math.BigDecimal;
import java.time.Duration;
import java.util.*;

@Service
public class CandidateServiceImpl implements CandidateService {
    @Autowired
    private ReactiveCandidateRepository candidateRepository;

    @Autowired
    private ReactiveJobRepository jobRepository;
    List<CandidateEntity> candidateEntityList = new ArrayList<>();

    @Autowired
    private JavaMailSender mailSender;

    final Map<String, TreeSet<CandidateEntity>> scoredCandidateMap = new HashMap<>();

    Comparator<CandidateEntity> scoreComparator = (c1, c2) -> {
        if (c1.getScore().equals(c2.getScore()))
            return c1.getApplicantId().compareTo(c2.getApplicantId());
        return new BigDecimal(c2.getScore()).compareTo(new BigDecimal(c1.getScore()));
    };

    @Scheduled(cron = "0 0/3 * * * ?")
    @Override
    public void loadCandidateByJobId() {
        scoredCandidateMap.clear();
        jobRepository.findAllActiveJob()
                .flatMap(job ->
                        candidateRepository.findCountByJobId(job.getJobId())
                                .flatMap(countL0 -> {
                                    int batchSize = Math.min(1000, Math.max(20, (int) (50 * Math.log(countL0 + 1))));
                                    int concurrency = Math.min(10, Math.max(1, (int) Math.log10(countL0 + 10)));
                                    long remainingDays = TimeHelper.getRemainingActiveDuration(job.getCreatedAt());
                                    String isActive = remainingDays >= job.getActiveDuration() ? "N" : "Y";
                                    job.setL0Count(countL0);
                                    return jobRepository.updateCandidateCount(countL0, job.getL1Count(), isActive, job.getJobId())
                                            .thenReturn(new JobBatchConfig(job, batchSize, concurrency, isActive));
                                })
                )
                .groupBy(JobBatchConfig::concurrency)
                .flatMap(groupedFlux ->
                        groupedFlux.flatMap(config ->
                                        findScoreCandidateByJobId(config.job(), "", config.batchSize(), config.isActive()),
                                groupedFlux.key() // This is the concurrency level for this group
                        )
                )
                .then()
                .subscribe();
    }

    private Mono<Void> findScoreCandidateByJobId(JobEntity job, String startAfter, int batchSize, String isActive) {
        return candidateRepository.findCandidateByJobId(job.getJobId(), startAfter)
                .take(batchSize)
                .collectList()
                .flatMap(batch -> {
                    String jobId = job.getJobId();
                    Integer hiringThreshold = job.getApplicantThreshold();
                    Integer activeDuration = job.getActiveDuration();
                    Integer l1Count = job.getL1Count();
                    scoredCandidateMap.putIfAbsent(jobId, new TreeSet<>(scoreComparator));
                    System.out.println("Batch size " + batch.size());
                    return Flux.fromIterable(batch)
//                                     .parallel()
//                                     .runOn(Schedulers.parallel())
                            .doOnNext(candidate -> {
                                System.out.println("Added " + candidate);
                                scoredCandidateMap.get(jobId).add(candidate);
//                                synchronized (scoredCandidateMap) {
//                                    scoredCandidateMap.get(jobId).add(candidate);
//                                }
                            })
//                                .sequential()
                            .then(Mono.defer(() -> {
                                if (batch.isEmpty()) {
                                    System.out.println("JobID: " + jobId);
                                    System.out.println(scoredCandidateMap.get(jobId).size());
                                    int availableCount = hiringThreshold - l1Count;
                                    int totalCandidates = scoredCandidateMap.get(jobId).size();
                                    int N;

                                    if ("Y".equals(isActive)) {
                                        if(totalCandidates < (int)(0.1 * availableCount))
                                            return Mono.empty();
                                        N = Math.min(totalCandidates,
                                                (int) Math.ceil((double) availableCount / activeDuration));
                                    } else {
                                        N = Math.min(totalCandidates, availableCount);
                                    }
                                    List<CandidateEntity> topCandidates = scoredCandidateMap.get(jobId)
                                            .stream()
                                            .limit(N)
                                            .toList();



                                    jobRepository.updateCandidateCount(job.getL0Count() - N,
                                            job.getL1Count() + N, isActive, jobId).subscribe();

                                    return Flux.fromIterable(topCandidates)
                                            .flatMap(candidate -> {
                                                candidateRepository.updateCandidateStatus(candidate.getApplicantId()).subscribe();
                                                String email = JsonObjectParserUtil.getMail(candidate.getProfile()); // assuming profile has email
                                                return sendEmailAsync(email, job, candidate);
                                            })
                                            .then();
//                                    return Mono.empty();
                                } else {
                                    String lastId = batch.get(batch.size() - 1).getCreatedAt();
                                    return findScoreCandidateByJobId(job, lastId, batchSize, isActive);
                                }
                            }));
                }).subscribeOn(Schedulers.boundedElastic());
    }

    @Override
    public SortedSet<CandidateEntity> getCandidateList(String jobId) {
        System.out.println("Total candidates: " + scoredCandidateMap.get(jobId).size());
        return scoredCandidateMap.get(jobId);
    }


    private Mono<Void> sendEmailAsync(String toEmail, JobEntity job, CandidateEntity candidate)
    {
        return Mono.fromRunnable(() -> {
            try {
                MimeMessage message = mailSender.createMimeMessage();
                MimeMessageHelper helper = new MimeMessageHelper(message, true);

                helper.setTo(toEmail);
                helper.setCc("thecortexcrew2@gmail.com");
                helper.setSubject("Congratulations! " + "Applicant ID: " + candidate.getApplicantId() + " is shortlisted");
                helper.setText(
                        "<p>Dear Candidate,</p>" +
                                "<p>You have been shortlisted for L1 round for the Job ID: <b>" + job.getJobId() + "</b>.</p>" +
                                "<p><b>Please provide the following details:</b></p>" +
                                "<ol>" +
                                "<li>Total Years of Experience:</li>" +
                                "<li>Relevant Years of Experience:</li>"+
                                "<li>Current CTC (fixed + variable):</li>" +
                                "<li>Expected CTC:</li>" +
                                "</ol>" +
                                "<p>Our HR team will contact you shortly.</p>" +
                                "<p>Regards,<br/>HireAssist Team</p>", true);

                helper.setFrom("thecortexcrew@gmail.com");
                mailSender.send(message);

                System.out.println("✅ Email sent to: " + toEmail);
            } catch (MessagingException e) {
                System.err.println("❌ Failed to send email to: " + toEmail + " - " + e.getMessage());
            }
        }).subscribeOn(Schedulers.boundedElastic()).then();
    }
}
