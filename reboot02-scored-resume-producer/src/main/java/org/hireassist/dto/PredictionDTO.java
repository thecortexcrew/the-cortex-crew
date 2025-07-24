package org.hireassist.dto;

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
public class PredictionDTO {
    @JsonProperty("ApplicantId")
    @NotNull
    private String applicantId;

    @JsonProperty("Feedback")
    private String feedback;

    @JsonProperty("IdentificationID")
    @NotNull
    private String identificationID;

    @JsonProperty("JobDescription")
    private String jobDescription;

    @JsonProperty("JobID")
    @NotNull
    private String jobID;

    @JsonProperty("Profile")
    @NotNull
    private ProfileDTO profile;

    @JsonProperty("Score")
    private Double score;

    @JsonProperty("Status")
    private String status;

    @JsonProperty(value = "CreatedAt")
    @NotNull
    private String createdAt;

}