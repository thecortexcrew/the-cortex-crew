package org.ltc.reboot.hireassist.util;

import com.google.cloud.Timestamp;

import java.time.Duration;
import java.time.Instant;

public class TimeHelper {

    public static long getRemainingActiveDuration(Timestamp timeStamp) {
        Instant creationDate = Instant.parse(timeStamp.toString());
        Instant now = Instant.now();
        return Duration.between(creationDate, now).toDays();
    }
}
