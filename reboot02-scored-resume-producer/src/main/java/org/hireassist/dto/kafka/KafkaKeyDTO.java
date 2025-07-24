package org.hireassist.dto.kafka;
import com.fasterxml.jackson.annotation.JsonProperty;
import jakarta.validation.constraints.NotNull;
import lombok.*;

@Getter
@Setter
@NoArgsConstructor
@AllArgsConstructor
@Builder
public class KafkaKeyDTO {
    @JsonProperty(value = "ApplicantId",required = true)
    @NotNull
    private String applicantId;
}
