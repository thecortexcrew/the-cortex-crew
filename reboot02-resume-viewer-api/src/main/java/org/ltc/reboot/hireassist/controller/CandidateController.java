package org.ltc.reboot.hireassist.controller;

//import org.ltc.reboot.hireassist.entity.JobEntity;
//import org.ltc.reboot.hireassist.repository.JobRepository;

import lombok.extern.log4j.Log4j2;
import org.ltc.reboot.hireassist.entity.JobEntity;
import org.ltc.reboot.hireassist.model.SelectedCandidate;
import org.ltc.reboot.hireassist.model.responseModel.FileResponse;
import org.ltc.reboot.hireassist.repository.JobRepository;
import org.ltc.reboot.hireassist.service.BucketService;
import org.ltc.reboot.hireassist.service.CandidateService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.core.io.InputStreamResource;
import org.springframework.core.io.Resource;
import org.springframework.http.HttpHeaders;
import org.springframework.http.MediaType;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RestController;
import reactor.core.publisher.Mono;

import java.io.InputStream;
import java.util.Arrays;
import java.util.List;

@Log4j2
@RestController
public class CandidateController {

//    @Autowired
//    private JobRepository jobRepository;

    private final BucketService bucketService;

    public CandidateController(BucketService bucketService) {
        this.bucketService = bucketService;
    }

    @Autowired
    private JobRepository jobRepository;

    @Autowired
    private CandidateService candidateService;

    @GetMapping("/check")
    public String check() {
        return "Working!";
    }

    @GetMapping("/load-candidate/{jobId}/{next}")
    public ResponseEntity<List<SelectedCandidate>> loadCandidates(@PathVariable String jobId, @PathVariable String next) {
        List<SelectedCandidate> selectedCandidateList = candidateService.loadCandidateByJobId(jobId, next, 30);
        return ResponseEntity.ok()
                .header("total-count", String.valueOf(selectedCandidateList.size()))
                .body(candidateService.loadCandidateByJobId(jobId, next, 30));
    }

//    @GetMapping("/candidates/{jobId}")
//    public SortedSet<CandidateEntity> getCandidates(@PathVariable String jobId) {
//        return candidateService.getCandidateList(jobId);
//    }

    @GetMapping("/download/{prefix}")
    public ResponseEntity<Resource> downloadFile(@PathVariable String prefix) {

        FileResponse fileResponse = bucketService.getFileWithNameByPrefix(prefix);
        log.atInfo().log(prefix);
        return ResponseEntity.ok()
                .contentType(MediaType.APPLICATION_PDF)
                .header(HttpHeaders.CONTENT_DISPOSITION,
                        "attachment; filename=\"" + fileResponse.getFileName() + "\"")
                .body(new InputStreamResource(fileResponse.getInputStream()));
    }

}
