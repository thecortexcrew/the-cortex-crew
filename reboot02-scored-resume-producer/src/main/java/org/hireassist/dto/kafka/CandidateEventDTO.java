package org.hireassist.dto.kafka;
import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonProperty;
import jakarta.validation.constraints.NotNull;
import lombok.*;

import java.math.BigDecimal;

@Getter
@Setter
@NoArgsConstructor
@AllArgsConstructor
@Builder
@JsonInclude(JsonInclude.Include.NON_NULL)
public class CandidateEventDTO {

        @JsonProperty(value = "ApplicantId", required = true)
        @NotNull
        private String applicantId;

        @JsonProperty(value = "IdentificationID", required = true)
        @NotNull
        private String identificationID;

        @JsonProperty(value = "JobID", required = true)
        @NotNull
        private String jobID;

        @JsonProperty("JobDescription")
        private String jobDescription;

        @JsonProperty(value = "Profile", required = true)
        @NotNull
        private String profile;  // Serialized ProfileDTO as JSON string

        @JsonProperty("Feedback")
        private String feedback;

        @JsonProperty("Score")
        private String score;

        @JsonProperty("Status")
        private String status;

        @JsonProperty(value = "CreatedAt", required = true)
        @NotNull
        private String createdAt;
}
