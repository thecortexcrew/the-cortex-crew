package org.hireassist.kafka.service.impl;

import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.ObjectMapper;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.hireassist.dto.JobRequestDTO;
import org.hireassist.kafka.service.JobKafkaProducer;
import org.hireassist.kafka.service.dto.CandidateEventDTO;
import org.hireassist.kafka.service.dto.KafkaKeyDTO;
import org.springframework.kafka.core.KafkaTemplate;
import org.springframework.scheduling.annotation.Async;
import org.springframework.stereotype.Service;

import java.time.LocalDateTime;


@Slf4j
@Service
@RequiredArgsConstructor
@Async
public class JobKafkaProducerImpl implements JobKafkaProducer {

    private final KafkaTemplate<KafkaKeyDTO, CandidateEventDTO> kafkaTemplate;
    private static final String TOPIC = "resume_assessor_topic_0";

    public void sendJob(JobRequestDTO jobRequestDTO) {

        KafkaKeyDTO key = KafkaKeyDTO.builder()
                .applicantId(jobRequestDTO.getApplicantId()).build();

        // Convert Profile object to JSON string
        ObjectMapper mapper = new ObjectMapper();
        String profileJson = "";

        try {
            profileJson = mapper.writeValueAsString(jobRequestDTO.getProfile());
        } catch (JsonProcessingException e) {
            e.printStackTrace();  // Or log.error(...)
        }

        // Value
        CandidateEventDTO event = CandidateEventDTO.builder()
                .applicantId(jobRequestDTO.getApplicantId())
                .identificationID(jobRequestDTO.getIdentificationID())
                .jobID(jobRequestDTO.getJobID())
                .jobDescription(jobRequestDTO.getJobDescription())
                .profile(profileJson)
               // .feedback("Pending")  // default
               // .score(0.0)           // default
               // .status("IN_REVIEW")  // default
                .createdAt(LocalDateTime.now().toString())
                .build();
        log.info("event time"+event.getCreatedAt());

        kafkaTemplate.send(TOPIC, key, event);
    }
}
