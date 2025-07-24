package org.hireassist;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class ScoredResumeProducerApplication {
    public static void main(String[] args) {

        SpringApplication.run(ScoredResumeProducerApplication.class,args);
        System.out.print("application started!");

    }
}