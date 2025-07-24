package org.ltc.reboot.hireassist.model;

import com.fasterxml.jackson.annotation.JsonProperty;
import lombok.*;

@Getter
@Setter
@NoArgsConstructor
@AllArgsConstructor
@Builder
public class Education {
    @JsonProperty("Degree")
    private String degree;

    @JsonProperty("Duration")
    private String duration;

    @JsonProperty("Ongoing")
    private boolean isOngoing;

    @JsonProperty("University")
    private String university;
}
