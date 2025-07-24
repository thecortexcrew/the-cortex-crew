package org.hireassist;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.scheduling.annotation.EnableAsync;

@SpringBootApplication
@EnableAsync
public class HireAssistProducerServiceApplication {
    public static void main(String[] args) {
        SpringApplication.run(HireAssistProducerServiceApplication.class, args);
        System.out.println("HireAssist Producer Started!");
    }
}