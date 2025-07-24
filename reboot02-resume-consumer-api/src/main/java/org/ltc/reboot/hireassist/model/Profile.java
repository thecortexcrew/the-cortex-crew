package org.ltc.reboot.hireassist.model;

import com.fasterxml.jackson.annotation.JsonProperty;
import lombok.*;

import java.util.List;

@Getter
@Setter
@NoArgsConstructor
@AllArgsConstructor
@Builder
public class Profile {

    @JsonProperty("ApplicantId")
    private String applicantID;

    @JsonProperty("IdentificationID")
    private String identificationID;

    @JsonProperty("Name")
    private String name;

    @JsonProperty("DateOfApplication")
    private String dateOfApplication;

    @JsonProperty("CreatedAt")
    private String createdAt;

    @JsonProperty("Gender")
    private String gender;

    @JsonProperty("DateOfBirth")
    private String dateOfBirth;

    @JsonProperty("MobileNo")
    private String mobileNo;

    @JsonProperty("EmailId")
    private String email;

    @JsonProperty("SkillSets")
    private String skillSets;

    @JsonProperty("YearsOfExp")
    private String yearsOfExp;

    @JsonProperty("Education")
    private List<Education> educationList;

    @JsonProperty("WorkExp")
    private List<WorkExperience> workExperienceList;
}
