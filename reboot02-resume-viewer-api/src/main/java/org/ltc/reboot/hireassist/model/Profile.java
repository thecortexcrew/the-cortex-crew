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
    @JsonProperty("Name")
    private String name;

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

}
