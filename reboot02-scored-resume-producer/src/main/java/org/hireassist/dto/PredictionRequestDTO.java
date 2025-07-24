package org.hireassist.dto;

import com.fasterxml.jackson.annotation.JsonProperty;
import lombok.*;

import java.util.List;

@Getter
@Setter
@NoArgsConstructor
@AllArgsConstructor
@Builder
public class PredictionRequestDTO {
    @JsonProperty("predictions")
    private List<PredictionDTO> predictions;
}
