package org.ltc.reboot.hireassist.model;

import com.fasterxml.jackson.annotation.JsonProperty;
import lombok.*;

import java.util.List;

@Getter
@Setter
@NoArgsConstructor
@AllArgsConstructor
@Builder
public class JobApplication {

    @JsonProperty("JobID")
    private String JobID;

    @JsonProperty("JobDescription")
    private String JobDescription;

    @JsonProperty("Candidate")
    List<Profile> profileList;
}
