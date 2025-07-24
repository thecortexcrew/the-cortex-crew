package org.ltc.reboot.hireassist.entity;

//import com.google.cloud.spring.data.spanner.core.mapping.Column;
//import com.google.cloud.spring.data.spanner.core.mapping.PrimaryKey;
//import com.google.cloud.spring.data.spanner.core.mapping.Table;
import com.google.cloud.Timestamp;
import com.google.gson.JsonObject;
import com.google.spanner.v1.TypeCode;
import lombok.Data;
import org.springframework.core.annotation.Order;
import org.springframework.data.annotation.Transient;
import org.springframework.data.relational.core.mapping.Column;
import org.springframework.data.relational.core.mapping.Table;

import java.math.BigDecimal;
import java.time.Instant;

@Table( "Candidate")
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

    @Column( "ApplicantId")
    private String applicantId;

    @Column( "IdentificationID")
    private String identificationId;

    @Column( "JobID")
    private String jobId;

    @Transient
    private JobEntity jobEntity;

    @Column( "JobDescription")
    private String jobDescription;

    @Column( "Profile" )
    private String profile;

    @Column( "Score")
    private String score;

    @Column( "Feedback")
    private String feedback;

    @Column( "CreatedAt")
    private String createdAt;

    @Column( "Status")
    private String status;
}
