package org.hireassist.service;

import org.hireassist.dto.PredictionDTO;

import java.util.List;

public interface ScoreProducerService {

    public void sendJob(List<PredictionDTO> predictions);
}
