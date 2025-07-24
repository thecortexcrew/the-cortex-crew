package org.ltc.reboot.hireassist.entity;


import com.google.cloud.Timestamp;
import com.google.gson.JsonObject;
import com.google.spanner.v1.TypeCode;
import lombok.Data;
import org.springframework.data.annotation.Id;
import com.google.cloud.spring.data.spanner.core.mapping.Column;
import com.google.cloud.spring.data.spanner.core.mapping.PrimaryKey;
import com.google.cloud.spring.data.spanner.core.mapping.Table;

import java.time.Instant;

@Table(name = "Job")
@Data
public class JobEntity {
//    JobID STRING(50) NOT NULL,
//    JobDetails JSON NOT NULL,
//    JobDescription STRING(5000) NOT NULL,
//    IsActive STRING(1) DEFAULT ("Y"),
//    CreatedAt TIMESTAMP DEFAULT (CURRENT_TIMESTAMP()),
//    ActiveDuration INT64 DEFAULT (2),
//    ApplicantThreshold  INT64 DEFAULT (10)

    @Column(name = "JobID")
    @PrimaryKey(keyOrder = 1)
    private String jobId;

    @Column(name = "JobDetails", spannerType = TypeCode.JSON)
    private JsonObject jobDetails;

    @Column(name = "JobDescription")
    private String jobDescription;

    @Column(name = "IsActive")
    private String isActive;

    @Column(name = "CreatedAt")
    private Instant createdAt;

    @Column(name = "ActiveDuration")
    private Integer activeDuration;

    @Column(name = "ApplicantThreshold")
    private Integer ApplicantThreshold;
}
