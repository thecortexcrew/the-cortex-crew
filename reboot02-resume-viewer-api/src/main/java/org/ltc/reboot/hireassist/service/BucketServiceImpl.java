package org.ltc.reboot.hireassist.service;

import com.google.cloud.storage.Blob;
import com.google.cloud.storage.Storage;
import com.google.cloud.storage.StorageOptions;
import lombok.extern.log4j.Log4j2;
import org.ltc.reboot.hireassist.model.responseModel.FileResponse;
import org.springframework.stereotype.Service;

import java.io.ByteArrayInputStream;
import java.io.InputStream;

@Log4j2
@Service
public class BucketServiceImpl implements BucketService {
    private final Storage storage;
    private final String BUCKET_NAME = "cv-storage-3";

    public BucketServiceImpl() {
        this.storage = StorageOptions.getDefaultInstance().getService();
    }

    @Override
    public InputStream getFileByPrefix(String prefix) {
        Iterable<Blob> blobs = storage.list(BUCKET_NAME, Storage.BlobListOption.prefix("resumes/" +prefix)).iterateAll();
        for (Blob blob : blobs) {
            if (!blob.isDirectory()) {
                // Return the first match
                return new ByteArrayInputStream(blob.getContent());
            }
        }
        throw new RuntimeException("No file found for prefix: " + prefix);
    }

    @Override
    public FileResponse getFileWithNameByPrefix(String prefix) {
        Iterable<Blob> blobs = storage.list(
                BUCKET_NAME,
                Storage.BlobListOption.prefix("resumes/" + prefix) // add resumes/ if needed
        ).iterateAll();

        for (Blob blob : blobs) {
            //System.out.print(blob.getName());
            log.atInfo().log(blob.getName());
            if (!blob.isDirectory()) {
                return new FileResponse(
                        new ByteArrayInputStream(blob.getContent()),
                        blob.getName()
                );
            }
        }
        throw new RuntimeException("No file found for prefix: " + prefix);
    }
}
