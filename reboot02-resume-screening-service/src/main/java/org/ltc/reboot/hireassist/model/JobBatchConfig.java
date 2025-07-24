package org.ltc.reboot.hireassist.model;

import org.ltc.reboot.hireassist.entity.JobEntity;

public record JobBatchConfig(JobEntity job, int batchSize, int concurrency, String isActive) {}
