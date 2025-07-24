package org.hireassist.kafka.service.dto;

import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonProperty;
import jakarta.validation.constraints.NotNull;
import lombok.*;

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

    @JsonProperty(value = "JobDescription")
    private String jobDescription;

    @JsonProperty(value = "Profile", required = true)  // Profile should be sent as a stringified JSON
    @NotNull
    private String profile;

    @JsonProperty(value = "Feedback")
    private String feedback;

    @JsonProperty(value = "Score")
    private String score;

    @JsonProperty("Status")
    private String status;

    @JsonProperty(value = "CreatedAt", required = true)
    @NotNull
    private String createdAt;
}

