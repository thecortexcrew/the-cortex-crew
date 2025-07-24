package org.ltc.reboot.hireassist.model;

import com.fasterxml.jackson.annotation.JsonProperty;
import lombok.*;

@Getter
@Setter
@NoArgsConstructor
@AllArgsConstructor
@Builder
public class Project {
    @JsonProperty("Name")
    private String Name;

    @JsonProperty("Role")
    private String Role;

    @JsonProperty("Responsibilities")
    private String Responsibilities;
}
