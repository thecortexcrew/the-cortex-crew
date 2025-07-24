package org.ltc.reboot.hireassist.model;

import com.fasterxml.jackson.annotation.JsonProperty;
import lombok.*;

import javax.validation.constraints.NotNull;

@Getter
@Setter
@ToString
@AllArgsConstructor
@NoArgsConstructor
public class Resume {
    @JsonProperty("ResumeId")
    @NotNull
    private String resumeId;
    @JsonProperty("Name")
    @NotNull
    private String name;
}
