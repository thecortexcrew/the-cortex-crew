package org.hireassist.kafka.service;

import org.hireassist.dto.JobRequestDTO;

public interface JobKafkaProducer {
    public void sendJob(JobRequestDTO jobRequestDTO);
}
