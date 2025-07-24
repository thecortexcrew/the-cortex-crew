package org.hireassist.dto;

import com.fasterxml.jackson.annotation.JsonProperty;
import jakarta.validation.Valid;
import jakarta.validation.constraints.NotNull;
import lombok.*;

@Getter
@Setter
@NoArgsConstructor
@AllArgsConstructor
@Builder
@Valid
public class JobRequestDTO {
    @NotNull(message = "JobID is required")
    @JsonProperty("JobID")
    private String jobID;

    @JsonProperty("JobDescription")
    @NotNull
    private String jobDescription;

    @JsonProperty("ApplicantId")
    private String applicantId;

    @JsonProperty("IdentificationID")
    private String identificationID;

    @JsonProperty("Profile")
    private ProfileDTO profile;
}
