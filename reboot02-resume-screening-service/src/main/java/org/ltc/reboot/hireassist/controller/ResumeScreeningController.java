package org.ltc.reboot.hireassist.controller;

//import org.ltc.reboot.hireassist.entity.JobEntity;
//import org.ltc.reboot.hireassist.repository.JobRepository;
import org.ltc.reboot.hireassist.entity.CandidateEntity;
import org.ltc.reboot.hireassist.entity.JobEntity;
import org.ltc.reboot.hireassist.repository.ReactiveJobRepository;
import org.ltc.reboot.hireassist.service.CandidateService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
import reactor.core.publisher.Flux;
import reactor.core.publisher.Mono;

import java.util.Arrays;
import java.util.List;
import java.util.SortedSet;

@RestController
public class ResumeScreeningController {

//    @Autowired
//    private JobRepository jobRepository;

    @Autowired
    private ReactiveJobRepository reactiveJobRepository;

    @Autowired
    private CandidateService candidateService;

    @GetMapping("/check")
    public String check() {
        return "Working!";
    }

    @GetMapping("/job-data")
    public Mono<JobEntity> loadJobData() {
        List<String> list = Arrays.asList("JOB001");
        return reactiveJobRepository.findByJobID("JOB001").doOnNext(job -> {
            System.out.println("Job Details: " + job);
        }).next();
    }

    @GetMapping("/load-candidate")
    public void loadCandidates() {
         candidateService.loadCandidateByJobId();
    }

    @GetMapping("/candidates/{jobId}")
    public SortedSet<CandidateEntity> getCandidates(@PathVariable String jobId) {
        return candidateService.getCandidateList(jobId);
    }
}
