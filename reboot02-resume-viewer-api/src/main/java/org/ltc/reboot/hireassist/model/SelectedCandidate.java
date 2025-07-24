package org.ltc.reboot.hireassist.model;

import com.fasterxml.jackson.annotation.JsonProperty;
import lombok.*;

@AllArgsConstructor
@NoArgsConstructor
@Data
@Builder
public class SelectedCandidate {

    @JsonProperty("ApplicantId")
    private String applicantId;

    @JsonProperty("IdentificationID")
    private String identificationId;

    @JsonProperty("JobID")
    private String jobId;

    @JsonProperty("Profile")
    private Profile profile;

    @JsonProperty("Feedback")
    private String feedback;

    @JsonProperty("CreatedAt")
    private String createdAt;

}
