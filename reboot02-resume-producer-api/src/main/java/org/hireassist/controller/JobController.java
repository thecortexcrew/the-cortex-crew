package org.hireassist.controller;

import com.fasterxml.jackson.databind.*;
import com.jayway.jsonpath.JsonPath;
import jakarta.validation.Valid;
import org.hireassist.dto.JobRequestDTO;
import org.hireassist.kafka.service.JobKafkaProducer;
import org.hireassist.kafka.service.impl.JobKafkaProducerImpl;
import org.hireassist.service.BucketService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.kafka.KafkaException;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.multipart.MultipartFile;

@RestController
@RequestMapping("/api/jobs")
public class JobController {

    @Autowired
    JobKafkaProducer kafkaProducer;

    @Autowired
    BucketService bucketService;


    @PostMapping(consumes = "multipart/form-data")
    public ResponseEntity<String> receiveCvData(@Valid @RequestPart("job") String jobRequestJson, @RequestPart("file") MultipartFile file) {

        String response = null;
        try {
            String field = JsonPath.read(jobRequestJson, "$.JobDescription");
            if(field == null || field.isEmpty())
                throw new RuntimeException("JobDescription Field Missing!");
            // Convert JSON string to JobRequestDTO
            ObjectMapper mapper = new ObjectMapper();
            JobRequestDTO jobRequest = new JobRequestDTO();
            try {
                 jobRequest = mapper.readValue(jobRequestJson, JobRequestDTO.class);

            } catch (Exception ex) {
                System.out.println("Exception " + ex);
            }

            // Sanity checks
            if (jobRequest.getProfile() == null || jobRequest.getProfile().getName() == null) {
                return ResponseEntity.status(HttpStatus.BAD_REQUEST).body("Missing profile or applicant name in request.");
            }

            // Start async tasks
            bucketService.uploadCvToBucket(file, jobRequest.getApplicantId(), jobRequest.getIdentificationID());

            // send message to Kafka
            kafkaProducer.sendJob(jobRequest);

            response = String.format("Received job application '%s' for applicant '%s' with file '%s'", jobRequest.getJobID(), jobRequest.getProfile().getName(), file.getOriginalFilename());

        } catch (Exception e) {
            e.printStackTrace();
            if (e instanceof KafkaException)
                return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).body("Error processing job data: " + e.getMessage());
        }
        return ResponseEntity.ok(response);
    }
}
