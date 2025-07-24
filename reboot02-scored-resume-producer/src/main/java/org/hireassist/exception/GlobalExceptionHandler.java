package org.hireassist.exception;

import org.apache.kafka.common.errors.SerializationException;
import org.apache.kafka.common.errors.TimeoutException;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.kafka.KafkaException;
import org.springframework.web.bind.MethodArgumentNotValidException;
import org.springframework.web.bind.annotation.*;

import java.util.HashMap;
import java.util.Map;

@RestControllerAdvice
public class GlobalExceptionHandler {

    @ExceptionHandler(MethodArgumentNotValidException.class)
    public ResponseEntity<Map<String, String>> handleValidationErrors(MethodArgumentNotValidException ex) {
        Map<String, String> errors = new HashMap<>();
        ex.getBindingResult().getFieldErrors().forEach(error ->
                errors.put(error.getField(), error.getDefaultMessage()));
        return new ResponseEntity<>(errors, HttpStatus.BAD_REQUEST);
    }

    @ExceptionHandler(KafkaException.class)
    public ResponseEntity<String> handleKafkaException(KafkaException ex) {
        return ResponseEntity.status(HttpStatus.SERVICE_UNAVAILABLE)
                .body("Kafka error occurred: " + ex.getMessage());
    }

    @ExceptionHandler(SerializationException.class)
    public ResponseEntity<String> handleSerializationException(SerializationException ex) {
        return ResponseEntity.status(HttpStatus.BAD_REQUEST)
                .body("Message serialization failed: " + ex.getMessage());
    }

    @ExceptionHandler(TimeoutException.class)
    public ResponseEntity<String> handleKafkaTimeoutException(TimeoutException ex) {
        return ResponseEntity.status(HttpStatus.REQUEST_TIMEOUT)
                .body("Kafka timeout occurred: " + ex.getMessage());
    }

    @ExceptionHandler(Exception.class)
    public ResponseEntity<String> handleAll(Exception ex) {
        return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR)
                .body("Internal Error: " + ex.getMessage());
    }

}
