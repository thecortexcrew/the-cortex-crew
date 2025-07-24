package org.ltc.reboot.hireassist.service;

import org.ltc.reboot.hireassist.model.SelectedCandidate;

import java.util.List;

public interface CandidateService {

    public List<SelectedCandidate> loadCandidateByJobId(String jobId, String startAfter, int batchSize);
}
