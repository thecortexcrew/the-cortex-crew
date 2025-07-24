package org.ltc.reboot.hireassist.model;

import com.fasterxml.jackson.annotation.JsonProperty;
import lombok.*;

@Getter
@Setter
@NoArgsConstructor
@AllArgsConstructor
@Builder
public class ProjectDTO {
    @JsonProperty("Name")
    private String name;

    @JsonProperty("Role")
    private String role;

    @JsonProperty("Responsibilities")
    private String responsibilities;
}
