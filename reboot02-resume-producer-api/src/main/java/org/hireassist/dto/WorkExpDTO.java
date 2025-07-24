package org.hireassist.dto;

import com.fasterxml.jackson.annotation.JsonProperty;
import lombok.*;
import java.util.List;

@Getter
@Setter
@NoArgsConstructor
@AllArgsConstructor
@Builder
public class WorkExpDTO {
    @JsonProperty("Company")
    private String company;

    @JsonProperty("Duration")
    private String duration;

    @JsonProperty("Project")
    private List<ProjectDTO> project;
}

