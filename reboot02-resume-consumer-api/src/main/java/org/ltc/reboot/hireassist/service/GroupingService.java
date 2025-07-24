package org.ltc.reboot.hireassist.service;

import org.ltc.reboot.hireassist.model.JobApplicationRequest;

import java.util.List;

public interface GroupingService {
    public void groupCandidatebyJob(List<JobApplicationRequest> jobApplicationRequestList);
}
