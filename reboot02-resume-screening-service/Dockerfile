# ----------- STEP 1: BUILD STAGE -----------
FROM maven:3.9.6-eclipse-temurin-17 AS build
WORKDIR /app
COPY pom.xml .
COPY src ./src
RUN mvn -T 3 clean package -DskipTests

# ----------- STEP 2: RUNTIME STAGE -----------
FROM eclipse-temurin:17-jdk
WORKDIR /app
COPY --from=build /app/target/*.jar app.jar
# Create a non-root user and use it
RUN useradd -u 1001 appuser && chown -R appuser /app
USER appuser
# Set the entry point to run the application
# This command will run the JAR file when the container starts
ENTRYPOINT ["java", "-jar", "app.jar"]