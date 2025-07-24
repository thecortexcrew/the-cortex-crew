package org.ltc.reboot.hireassist.entity;

import com.google.cloud.spring.data.spanner.core.mapping.Column;
import com.google.cloud.spring.data.spanner.core.mapping.PrimaryKey;
import com.google.cloud.spring.data.spanner.core.mapping.Table;
import com.google.gson.JsonObject;
import com.google.spanner.v1.TypeCode;
import lombok.Data;
import org.springframework.data.annotation.Transient;

@Table(name = "Candidate")
@Data
public class CandidateEntity {
//    ApplicantId STRING(50) NOT NULL,
//    IdentificationID STRING(50) NOT NULL,
//    JobID STRING(50) NOT NULL,
//    JobDescription STRING(5000),
//    Profile JSON NOT NULL,
//    Score NUMERIC DEFAULT (-1),
//    Feedback STRING(300) DEFAULT ("N/A"),
//    CreatedAt TIMESTAMP DEFAULT (CURRENT_TIMESTAMP()),
//    Status STRING(10) DEFAULT ("L0")

    @Column(name = "ApplicantId")
    @PrimaryKey
    private String applicantId;

    @Column(name = "IdentificationID")
    private String identificationId;

    @Column(name = "JobID")
    private String jobId;

    @Transient
    private JobEntity jobEntity;

    @Column(name = "Profile", spannerType = TypeCode.JSON)
    private JsonObject profile;

    @Column(name = "Score")
    private String score;

    @Column(name = "Feedback")
    private String feedback;

    @Column(name = "CreatedAt")
    private String createdAt;

    @Column(name = "Status")
    private String status;
}
