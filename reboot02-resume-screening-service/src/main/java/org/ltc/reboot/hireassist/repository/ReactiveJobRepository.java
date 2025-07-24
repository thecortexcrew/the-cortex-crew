package org.ltc.reboot.hireassist.repository;

import org.ltc.reboot.hireassist.entity.JobEntity;
import org.springframework.data.r2dbc.repository.Query;
import org.springframework.data.repository.reactive.ReactiveCrudRepository;
import org.springframework.stereotype.Repository;
import reactor.core.publisher.Flux;
import reactor.core.publisher.Mono;

@Repository
public interface ReactiveJobRepository extends ReactiveCrudRepository<JobEntity, String> {

    @Query("Select * from Job where JobID = :jobId")
    Flux<JobEntity> findByJobID(String jobId);

    @Query("Select * from Job where IsActive = 'Y'")
    Flux<JobEntity> findAllActiveJob();

    @Query("UPDATE Job SET L0Count = :l0Count, L1Count = :l1Count, IsActive = :isActive WHERE JobID = :jobId")
    Mono<Void> updateCandidateCount(Integer l0Count, Integer l1Count, String isActive, String jobId);
}
