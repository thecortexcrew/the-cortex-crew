package org.hireassist.service.impl;

import com.google.cloud.storage.BlobInfo;
import com.google.cloud.storage.Storage;
import com.google.cloud.storage.StorageOptions;
import org.hireassist.service.BucketService;
import org.springframework.stereotype.Service;
import org.springframework.web.multipart.MultipartFile;

import java.io.IOException;

@Service
public class BucketServiceImpl implements BucketService {
    @Override
    public void uploadCvToBucket(MultipartFile file, String applicationId, String identificationID) throws IOException {

        String bucketName = "cv-storage-3";
        String fileName = "resumes/" + applicationId + "_" + identificationID + "_" + file.getOriginalFilename();
        Storage storage = StorageOptions.getDefaultInstance().getService();
        BlobInfo blobInfo = BlobInfo.newBuilder(bucketName, fileName).setContentType(file.getContentType()).build();
        storage.create(blobInfo, file.getBytes());
    }
}
