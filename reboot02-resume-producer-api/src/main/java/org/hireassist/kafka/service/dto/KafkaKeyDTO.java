    package org.hireassist.kafka.service.dto;

    import com.fasterxml.jackson.annotation.JsonInclude;
    import com.fasterxml.jackson.annotation.JsonProperty;
    import jakarta.validation.constraints.NotNull;
    import lombok.*;

    @Getter
    @Setter
    @NoArgsConstructor
    @AllArgsConstructor
    @Builder
    @JsonInclude(JsonInclude.Include.NON_NULL)
    public class KafkaKeyDTO {
        @JsonProperty(value = "ApplicantId",required = true)
        @NotNull
        private String applicantId;
    }
