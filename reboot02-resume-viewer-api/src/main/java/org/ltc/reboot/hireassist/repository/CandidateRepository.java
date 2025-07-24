package org.ltc.reboot.hireassist.repository;

import com.google.cloud.spring.data.spanner.repository.SpannerRepository;
import com.google.cloud.spring.data.spanner.repository.query.Query;
import org.ltc.reboot.hireassist.entity.CandidateEntity;
import org.springframework.stereotype.Repository;

import java.util.List;

@Repository
public interface CandidateRepository extends SpannerRepository<CandidateEntity, String> {

    @Query("select * from Candidate where JobID = @jobId and Status = 'L1' and CreatedAt > @startAfter order by CreatedAt asc limit @batchSize")
    List<CandidateEntity> findScoredCandidateByJobId(String jobId, String startAfter, int batchSize);

    @Query("select count(*) from Candidate where JobID = :jobId")

    Integer findCountByJobId(String jobId);

}
