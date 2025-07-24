//package org.hireassist.config;
//
//
//import io.confluent.kafka.serializers.json.KafkaJsonSchemaSerializer;
//import org.apache.kafka.clients.producer.ProducerConfig;
//
//import org.hireassist.kafka.service.dto.JobEventDTO;
//import org.hireassist.kafka.service.dto.KafkaKeyDTO;
//import org.springframework.context.annotation.Bean;
//import org.springframework.context.annotation.Configuration;
//import org.springframework.kafka.core.DefaultKafkaProducerFactory;
//import org.springframework.kafka.core.KafkaTemplate;
//import org.springframework.kafka.core.ProducerFactory;
//
//
//import java.util.HashMap;
//import java.util.Map;
//
//@Configuration
//public class KafkaProducerConfig {
//
//    @Bean
//    public ProducerFactory<KafkaKeyDTO, JobEventDTO> producerFactory() {
//        Map<String, Object> props = new HashMap<>();
//
//        // Replace with your actual Confluent settings
//        props.put(ProducerConfig.BOOTSTRAP_SERVERS_CONFIG, "pkc-619z3.us-east1.gcp.confluent.cloud:9092");
//
//        props.put("schema.registry.url", "https://psrc-v1593j.us-central1.gcp.confluent.cloud");
//        props.put("basic.auth.credentials.source", "USER_INFO");
//        props.put("basic.auth.user.info", "D6SUFQYVZZDDUMPM:AtMcIi3qj8xznPbSD3hdX64m7TYKAiAycxtqwCb9BOeHX+RSRqjKf+UBumQ8540t");
//
//        props.put(ProducerConfig.KEY_SERIALIZER_CLASS_CONFIG, KafkaJsonSchemaSerializer.class);
//        props.put(ProducerConfig.VALUE_SERIALIZER_CLASS_CONFIG, KafkaJsonSchemaSerializer.class);
//
//        props.put("auto.register.schemas", true);
//        props.put("acks", "all");
//        props.put("retries", 10);
//        props.put("delivery.timeout.ms", 120000);
//        props.put("enable.idempotence", true);
//        props.put("retry.backoff.ms", 1000);
//
//        return new DefaultKafkaProducerFactory<>(props);
//    }
//
//    @Bean
//    public KafkaTemplate<KafkaKeyDTO, JobEventDTO> kafkaTemplate() {
//        return new KafkaTemplate<>(producerFactory());
//    }
//}
//
