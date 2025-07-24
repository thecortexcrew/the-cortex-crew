package org.ltc.reboot.hireassist.repository;

import com.google.cloud.spring.data.spanner.repository.SpannerRepository;
import com.google.cloud.spring.data.spanner.repository.query.Query;
import org.ltc.reboot.hireassist.entity.JobEntity;
import org.springframework.data.repository.CrudRepository;
import org.springframework.data.repository.reactive.ReactiveCrudRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface JobRepository extends SpannerRepository<JobEntity, String> {

    @Query("Select * from Job where JobID = :jobId")
    JobEntity findByJobID(String jobId);

    @Query("Select * from Job where IsActive = 'Y'")
    JobEntity findAllActiveJob();
}
