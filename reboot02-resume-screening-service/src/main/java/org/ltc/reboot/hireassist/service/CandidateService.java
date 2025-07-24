package org.ltc.reboot.hireassist.service;

import org.ltc.reboot.hireassist.entity.CandidateEntity;
import reactor.core.publisher.Flux;
import reactor.core.publisher.Mono;

import java.util.List;
import java.util.SortedSet;

public interface CandidateService {

    void loadCandidateByJobId();

    SortedSet<CandidateEntity> getCandidateList(String jobId);
}
