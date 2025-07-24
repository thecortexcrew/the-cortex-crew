package org.ltc.reboot.hireassist.model.responseModel;

import lombok.*;

import java.io.InputStream;

@Getter
@Setter
@NoArgsConstructor
@AllArgsConstructor
@Builder
public class FileResponse {
    private InputStream inputStream;
    private String fileName;
}
