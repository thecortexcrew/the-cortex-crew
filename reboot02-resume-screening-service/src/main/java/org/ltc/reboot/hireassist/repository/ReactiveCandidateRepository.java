package org.ltc.reboot.hireassist.repository;

import org.ltc.reboot.hireassist.entity.CandidateEntity;
import org.springframework.data.r2dbc.repository.Query;
import org.springframework.data.repository.reactive.ReactiveCrudRepository;
import org.springframework.stereotype.Repository;
import reactor.core.publisher.Flux;
import reactor.core.publisher.Mono;

@Repository
public interface ReactiveCandidateRepository extends ReactiveCrudRepository<CandidateEntity, String> {

    @Query("select * from Candidate where JobID = :jobId and Score > 0")
    Flux<CandidateEntity> findScoredCandidateByJobId(String jobId);

    @Query("select * from Candidate where JobID = :jobId and Status = 'L0' and Score != '-1' and CreatedAt > :startAfter order by CreatedAt asc")
    Flux<CandidateEntity> findCandidateByJobId(String jobId, String startAfter);

    @Query("select count(*) from Candidate where JobID = :jobId AND Status = 'L0'")
    Mono<Integer> findCountByJobId(String jobId);

    @Query("update Candidate set Status = 'L1' where ApplicantId = :applicantId")
    Mono<Void> updateCandidateStatus(String applicantId);
}
