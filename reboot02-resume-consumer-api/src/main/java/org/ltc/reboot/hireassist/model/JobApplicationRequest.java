package org.ltc.reboot.hireassist.model;

import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonProperty;
import jakarta.validation.constraints.NotNull;
import lombok.*;

@Getter
@Setter
@NoArgsConstructor
@AllArgsConstructor
@Builder
public class JobApplicationRequest {
    @JsonProperty("JobID")
    private String JobID;

    @JsonProperty("JobDescription")
    private String JobDescription;

    @JsonProperty("ApplicantId")
    private String applicationID;

    @JsonProperty("IdentificationID")
    private String identificationID;

    @JsonProperty("Profile")
    private String profile;

    @JsonProperty("Score")
    private String score;

    @JsonProperty("CreatedAt")
    private String CreatedAt;

}