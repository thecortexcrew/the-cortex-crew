package org.ltc.reboot.hireassist.model;

import com.fasterxml.jackson.annotation.JsonProperty;
import lombok.*;

import java.util.List;

@Getter
@Setter
@NoArgsConstructor
@AllArgsConstructor
@Builder
public class WorkExperience {
    @JsonProperty("Company")
    private String company;

    @JsonProperty("Duration")
    private String duration;

    @JsonProperty("Project")
    private List<Project> projectList;
}
