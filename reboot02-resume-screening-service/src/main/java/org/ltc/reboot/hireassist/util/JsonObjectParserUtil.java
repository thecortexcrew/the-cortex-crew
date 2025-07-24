package org.ltc.reboot.hireassist.util;

import com.fasterxml.jackson.databind.JsonNode;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.jayway.jsonpath.JsonPath;
import org.ltc.reboot.hireassist.model.ProfileDTO;
import org.springframework.beans.factory.annotation.Autowired;

public class JsonObjectParserUtil {

    @Autowired
    private static ObjectMapper objectMapper;

    public static ProfileDTO parseProfile(String profile) {
        ProfileDTO profileDto = null;
        try {
            profileDto = objectMapper.readValue(profile, ProfileDTO.class);
            //email = profileNode.path("email").asText();  //  Assuming profile JSON has {"email": "..."}
        } catch (Exception e) {
            System.err.println("Failed to parse profile JSON for candidate ");
        }

        return profileDto;
    }

    public static String getMail(String profile) {
        return JsonPath.read(profile, "$.EmailId");
    }
}
