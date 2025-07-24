package org.hireassist.dto;

import com.fasterxml.jackson.annotation.JsonProperty;
import lombok.*;
import java.util.List;

@Getter
@Setter
@NoArgsConstructor
@AllArgsConstructor
@Builder
public class ProfileDTO {
    @JsonProperty("Name")
    private String name;

    @JsonProperty("DateOfApplication")
    private String dateOfApplication;

    @JsonProperty("Gender")
    private String gender;

    @JsonProperty("EmailId")
    private String emailId;

    @JsonProperty("DateOfBirth")
    private String dateOfBirth;

    @JsonProperty("MobileNo")
    private String mobileNo;

    @JsonProperty("SkillSets")
    private String skillSets;

    @JsonProperty("YearsOfExp")
    private String yearsOfExp;

    @JsonProperty("Education")
    private List<EducationDTO> education;

    @JsonProperty("WorkExp")
    private List<WorkExpDTO> workExp;

}

