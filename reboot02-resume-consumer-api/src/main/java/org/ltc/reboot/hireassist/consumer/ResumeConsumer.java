package org.ltc.reboot.hireassist.consumer;

import org.apache.commons.lang3.StringUtils;
import org.ltc.reboot.hireassist.model.JobApplicationRequest;
import org.ltc.reboot.hireassist.model.Resume;
import org.ltc.reboot.hireassist.service.GroupingService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.messaging.Message;

import java.util.ArrayList;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.function.Consumer;
import java.util.stream.Collectors;

@Configuration
public class ResumeConsumer {

    @Autowired
    private GroupingService groupingService;

    @Bean
    public Consumer<Message<List<JobApplicationRequest>>> input() {
        // This is our listener block
        return message -> {
            List<LinkedHashMap<String, String>> list1 = (ArrayList)message.getHeaders().get("kafka_receivedMessageKey");
            List<JobApplicationRequest> resumeList = ((ArrayList)message.getPayload());
            for(int i=0;i<list1.size();++i) {
                System.out.println("Key --> " + ((LinkedHashMap)list1.get(i)).get("ApplicantId") + " : " + "Payload --> " + resumeList.get(i));
            }
            List<JobApplicationRequest> filteredList = resumeList.stream()
                    .filter(resume -> StringUtils.isEmpty(resume.getScore())).
                    collect(Collectors.toList());
            groupingService.groupCandidatebyJob(filteredList);
            System.out.println("Received message from Confluent: " + message);
        };
    }
}
