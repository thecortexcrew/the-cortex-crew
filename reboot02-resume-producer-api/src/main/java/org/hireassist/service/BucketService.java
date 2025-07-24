package org.hireassist.service;

import org.springframework.web.multipart.MultipartFile;

import java.io.IOException;

public interface BucketService {

    public void uploadCvToBucket(MultipartFile file, String applicationId, String identificationID) throws IOException;

}
