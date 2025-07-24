package org.hireassist.controller;

import jakarta.validation.Valid;
import org.hireassist.dto.PredictionRequestDTO;
import org.hireassist.service.ScoreProducerService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/api/score")
public class ScoreController {

    @Autowired
    ScoreProducerService scoreProducerService;

    @PostMapping(consumes = "application/json")
    public ResponseEntity<String> receiveScore(@Valid @RequestBody PredictionRequestDTO request) {
        scoreProducerService.sendJob(request.getPredictions());
        return ResponseEntity.ok("Predictions received");
    }
}
