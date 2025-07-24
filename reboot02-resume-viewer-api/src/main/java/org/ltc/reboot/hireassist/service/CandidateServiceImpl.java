package org.ltc.reboot.hireassist.service;

import com.fasterxml.jackson.databind.ObjectMapper;
import com.google.gson.JsonElement;
import com.google.gson.JsonObject;
import io.micrometer.common.util.StringUtils;
import org.apache.commons.lang3.ObjectUtils;
import org.ltc.reboot.hireassist.model.Profile;
import org.ltc.reboot.hireassist.model.SelectedCandidate;
import org.ltc.reboot.hireassist.repository.CandidateRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.ArrayList;
import java.util.List;
import java.util.stream.Collectors;

@Service
public class CandidateServiceImpl implements CandidateService {

    @Autowired
    private CandidateRepository candidateRepository;
    @Autowired
    private ObjectMapper objectmapper;

    @Override
    public List<SelectedCandidate> loadCandidateByJobId(String jobId, String startAfter, int batchSize) {
        List<SelectedCandidate> candidateList = new ArrayList<>();
        return candidateRepository.findScoredCandidateByJobId(jobId, startAfter, batchSize)
                .stream().map(candidate -> {
                    SelectedCandidate selectedCandidate;
                     try {
                         JsonObject profileEntity = candidate.getProfile();
                         selectedCandidate = SelectedCandidate.builder()
                                .applicantId(candidate.getApplicantId())
                                .identificationId(candidate.getIdentificationId())
                                .jobId(candidate.getJobId())
                                .createdAt(candidate.getCreatedAt())
                                .profile(Profile.builder()
                                        .name(getProperty(profileEntity.get("Name")))
                                        .gender(getProperty(profileEntity.get("Gender")))
                                        .dateOfBirth(getProperty(profileEntity.get("DateOfBirth")))
                                        .mobileNo(getProperty(profileEntity.get("MobileNo")))
                                        .emailId(getProperty(profileEntity.get("EmailId")))
                                        .skillSets(getProperty(profileEntity.get("SkillSets")))
                                        .yearsOfExp(getProperty(profileEntity.get("YearsOfExp")))
                                        .build())
                                .feedback(candidate.getFeedback())
                                .build();
                    } catch (Exception e) {
                        throw new RuntimeException(e);
                    }
                    return selectedCandidate;
                }).collect(Collectors.toList());
    }

    private String getProperty(JsonElement field) {
        return ObjectUtils.isEmpty(field) ? null : field.getAsString();
    }
}
