package org.ltc.reboot.hireassist.service;

import org.ltc.reboot.hireassist.model.responseModel.FileResponse;

import java.io.InputStream;

public interface BucketService {

    public InputStream getFileByPrefix(String prefix);
    public FileResponse getFileWithNameByPrefix(String prefix);


}
