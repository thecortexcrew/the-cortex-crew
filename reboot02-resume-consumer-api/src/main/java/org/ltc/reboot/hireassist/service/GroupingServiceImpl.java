package org.ltc.reboot.hireassist.service;

import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.ObjectMapper;
import org.ltc.reboot.hireassist.model.*;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.web.reactive.function.client.WebClient;
import reactor.core.publisher.Mono;

import java.util.ArrayList;
import java.util.List;

@Service
public class GroupingServiceImpl implements GroupingService {

    @Autowired
    private WebClient webClient;

    @Autowired
    private ObjectMapper objectMapper;
    @Override
    public void groupCandidatebyJob(List<JobApplicationRequest> jobApplicationRequestList) {
        List<JobApplication> jobApplicationResponseList = new ArrayList<>();
        for (JobApplicationRequest request : jobApplicationRequestList) {
            Profile profile = Profile.builder().build();
            try {
                profile = objectMapper.readValue(request.getProfile(), Profile.class);
            } catch(JsonProcessingException ex) {
                System.out.println("Exception while parsing candidate profile json string " + ex);
            }
            profile.setApplicantID(request.getApplicationID());
            profile.setIdentificationID(request.getIdentificationID());
            profile.setCreatedAt(request.getCreatedAt());
            if (jobApplicationResponseList.contains(request.getJobID())) {
                profile.setIdentificationID(request.getIdentificationID());
                jobApplicationResponseList.get(jobApplicationResponseList.indexOf(request)).getProfileList().add(profile);
            } else {
                List<Profile> profileList = new ArrayList<>();
                profileList.add(profile);
                JobApplication jobApplication = JobApplication.builder()
                        .JobID(request.getJobID())
                        .JobDescription(request.getJobDescription())
                        .profileList(profileList)
                        .build();
                jobApplicationResponseList.add(jobApplication);
            }
        }

        sendResumeForScreening(Instances.builder()
                .instanceList(List.of(JobApplicationResponse.builder().jobApplication(jobApplicationResponseList).build()))
                .build());
    }

    private void sendResumeForScreening(Instances candidateList) {
        Mono<Object> response = webClient.post()
                .uri("http://resumeassist.net/assessment")
                .header("Content-Type", "application/json")
                .bodyValue(candidateList)
                .retrieve()
                .bodyToMono(Object.class);
        response.subscribe(System.out::println);
    }
}
