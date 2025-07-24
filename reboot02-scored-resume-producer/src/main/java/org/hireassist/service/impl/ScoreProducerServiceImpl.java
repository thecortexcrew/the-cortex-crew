package org.hireassist.service.impl;

import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.ObjectMapper;
import lombok.AllArgsConstructor;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.hireassist.dto.PredictionDTO;
import org.hireassist.dto.kafka.KafkaKeyDTO;
import org.hireassist.dto.kafka.CandidateEventDTO;
import org.hireassist.service.ScoreProducerService;
import org.springframework.kafka.core.KafkaTemplate;
import org.springframework.stereotype.Service;

import java.math.BigDecimal;
import java.math.RoundingMode;
import java.util.List;

@Slf4j
@Service
@RequiredArgsConstructor
public class ScoreProducerServiceImpl implements ScoreProducerService {

    private final KafkaTemplate<KafkaKeyDTO, CandidateEventDTO> kafkaTemplate;
    private final ObjectMapper objectMapper; // Injected automatically if using Spring Boot
    private static final String TOPIC = "resume_score_topic_0";

    @Override
    public void sendJob(List<PredictionDTO> predictions) {

        predictions.stream()
                .map(prediction ->
                        {
                            try {
                                String profileJson = objectMapper.writeValueAsString(prediction.getProfile());

                                //kafka payload
                                CandidateEventDTO payload = CandidateEventDTO.builder()
                                        .applicantId(String.valueOf(prediction.getApplicantId()))
                                        .identificationID(prediction.getIdentificationID())
                                        .jobID(prediction.getJobID())
                                        .jobDescription(prediction.getJobDescription())
                                        .profile(profileJson)
                                        .feedback(prediction.getFeedback())
                                        .score(prediction.getScore().equals(-1.0) ? "-1" : prediction.getScore().toString())
                                        .status(prediction.getStatus())
                                        .createdAt(prediction.getCreatedAt())
                                        .build();

                                //kafka key
                                KafkaKeyDTO key = KafkaKeyDTO.builder()
                                        .applicantId(String.valueOf(prediction.getApplicantId()))
                                        .build();

                                return new KafkaMessage(key, payload);


                            } catch (JsonProcessingException e) {
                                log.error("❌ Error serializing profile for applicant {}: {}", prediction.getApplicantId(), e.getMessage(), e);
                                throw new RuntimeException("Serialization error", e);
                            }
                        }

                )
                .forEach(kafkaMessage -> kafkaTemplate.send(TOPIC, kafkaMessage.key, kafkaMessage.payload)
                        .whenComplete((res, ex) -> {
                            if (ex != null) {
                                log.error("❌ Kafka send failed for applicant {}: {}", kafkaMessage.key.getApplicantId(), ex.getMessage(), ex);
                                throw new RuntimeException("Kafka send failed: " + ex.getMessage(), ex);
                            } else {
                                log.info("✅ Kafka message sent to partition {}", res.getRecordMetadata().partition());
                            }
                        })
                );
    }

    @AllArgsConstructor
    private static class KafkaMessage {
        private final KafkaKeyDTO key;
        private final CandidateEventDTO payload;
    }
}
