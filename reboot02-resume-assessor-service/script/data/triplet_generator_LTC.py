import csv
import random
from faker import Faker
import pandas as pd
import frontend as frontend
import devops as devops

from datetime import datetime

fake = Faker()

# Tech company job description
job_description_java_one = """
Job Description Summary 

Experience : 4 - 6 years and 10 to 13 years

We are seeking a skilled and motivated Java Developer with strong experience in Cloud platforms, Kubernetes (K8s), and SQL to join our development team. The ideal candidate will be responsible for designing, developing, and deploying scalable applications in a cloud-native environment, ensuring high performance and reliability.
Job Description 

Required Skills:

Strong proficiency in Java (8 or above) and object-oriented programming.
Hands-on experience with Kubernetes for container orchestration.
Experience with cloud platforms such as AWS, Azure, or Google Cloud Platform.
Proficiency in SQL and working with relational databases like PostgreSQL, MySQL, or Oracle.
Familiarity with Spring Boot, REST APIs, and microservices architecture.
Understanding of CI/CD tools and practices (e.g., Jenkins, Git, Docker).
Good problem-solving skills and ability to work in an agile environment.
"""

job_description_java_two = """
Job Description Summary – Java Backend Architect
Experience: 10 to 14 years

We are looking for a highly experienced Java Backend Architect with deep expertise in designing scalable, distributed systems and building resilient microservices. The ideal candidate should have a strong foundation in Java and Spring Boot, and a proven track record of leading architecture initiatives for complex enterprise-grade systems.

Job Description
Required Skills:

Strong proficiency in Java (8 or above), Spring Boot, and microservices architecture.
Solid experience in system design and architecture, especially for scalable, high-throughput applications.
Expertise in design patterns, domain-driven design (DDD), and performance tuning of backend systems.
Hands-on experience with containerization and orchestration (Docker, Kubernetes).
Experience with cloud-native architecture on AWS, Azure, or Google Cloud.
Proficient in REST API design, message queues (Kafka/RabbitMQ), and asynchronous processing.
Familiar with CI/CD, GitOps, Infrastructure as Code (Terraform/CloudFormation), and DevOps best practices.
Ability to mentor junior developers and collaborate with cross-functional teams on technical direction.
"""

job_description_java_three = """
Job Description Summary – Java Full-Stack
Experience: 4 to 10 years

We are hiring a talented and versatile Java Full-Stack Developer with strong backend expertise and proficiency in modern front-end technologies. The candidate should be capable of building robust APIs and delivering rich UI experiences using industry-standard frameworks.

Job Description
Required Skills:

Proficient in Java (8 or above), Spring Boot, and RESTful service development.
Strong experience in front-end development using React.js, Angular, or Vue.js.
Hands-on with HTML5, CSS3, JavaScript (ES6+), and responsive web design.
Experience with microservices architecture and integration patterns.
Solid understanding of SQL and databases like MySQL, PostgreSQL, or Oracle.
Familiarity with Docker, Kubernetes, and cloud environments (AWS/Azure/GCP).
Good knowledge of CI/CD pipelines using tools like Jenkins, GitLab CI, or GitHub Actions.
Strong debugging and performance optimization skills on both front-end and back-end.
Experience in Agile/Scrum environments and excellent team collaboration.
"""

# Skills
engineer_title = ["Senior Software Engineer", "Software Engineer", "Software Developer", "Tech Lead", "Technical Lead", "Engineering Lead", "Software Development Engineer", "SSE", "SDE", "SE"]
tech_core_skills_Java = ["Java", "Spring Boot", "Kubernetes", "Hibernate", "AWS", "GCP", "Azure", "SQL", "Docker", "Jenkins", "Git",
                    "Microservices", "REST APIs"]
tech_core_skills_Java_Architect = ["Low Level Design", "System Design","Architecture", "AWS", "GCP", "LLD", "Azure", "Solution Design",
                    "Microservices", "High Level Design", "Distributed Systems", "HLD"]
tech_core_skills_Java_negative = ["React", "HTML/CSS", "SOAP" ,"Struts","Bootstrap", "WebLogic","Javascript", "EJB", "Servlets", "JSP", "JDBC"]
tech_core_skills_React = ["React", "HTML/CSS", "Bootstrap", "Javascript", "Angular", "ReactJs", "VueJs"]
tech_core_skills_Fullstack = ["Java", "Angular", "Spring Boot", "ReactJS", "Hibernate","HTML/CSS"
                    "Microservices", "Bootstrap", "REST APIs", "React", "Javascript"]
tech_core_skills_Devops = ["Kubernetes", "CI/CD", "Jenkins", "Docker", "Openshift", "Azure", "AWS", "GCP", "Harness", "Harbor", "GAR"]
tech_core_skills_Data_Science = ["AI/ML","Dataflow", "Machine Learning", "Data Analytics", "LLM", "VertexAI", "Google AI Studio", "Python", "AWS", "Azure", "GCP"]
tech_additional_skills = ["Kafka","Oracle","Spanner", "GraphQL", "PostgreSQL", "MongoDB", "Terraform", "Cassandra", "SQLServer", "Redis", "ElasticSearch"]
irrelevant_tech_skills = ["VBScript", "PowerBuilder", "Perl", "COBOL", "SAP ABAP", "Oracle Forms", "Lotus Notes"]


# Create a resume sample
def create_resume_java_set_one(n):
    name = fake.name()
    company = fake.company()
    project = fake.bs().title()
    role = fake.job()


    positive_resp_list = ["""Developed backend services using Java and Spring Boot, deployed on AWS using Kubernetes.
    Implemented CI/CD pipelines with Jenkins and Docker. Optimized SQL queries and REST APIs for scalability.
    """, """
       Developed secure and merchant-ready APIs using Spring Boot in Microservices architecture, updated logging, ensured JUnit coverage, handled deployment pipelines.
    """,
    """
      Built Scalable microservices with Java and Spring Boot, deployed on AWS using Kubernetes.
      Created Kafka based payment transaction systems with Confluent Kafka, Kubernetes, GCP.
    """,
    """
      Developed RESTful APIs using Java 8 and Spring Boot for microservices architecture.
      Integrated backend services with frontend applications using REST and JSON.
      Designed and implemented authentication and authorization using Spring Security.
    """,
    """
      Decomposed a monolithic Java application into independent Spring Boot microservices.
      Deployed microservices on Docker containers and orchestrated using Kubernetes.
      Integrated AWS S3 and RDS for scalable storage and data persistence.
    """,
    """
      Wrote complex SQL queries and procedures for Oracle/PostgreSQL databases.
      Used JPA/Hibernate for ORM and repository abstraction in a Spring Data application.
      Tuned queries and optimized indexing for high-performance data access.   
    """,
    """
      Developed Kafka consumers and producers to enable asynchronous message processing.
      Built real-time data ingestion pipelines using Apache Kafka and Spring Cloud Stream.
    """,
    """
      Configured Jenkins pipelines for automated builds and deployments of Java apps.
      Used Maven and Gradle for build lifecycle management and dependency resolution.
    """,
    """
      Developed Spring Boot-based microservices for an e-commerce platform handling order and payment workflows.
      Designed RESTful APIs and implemented service orchestration patterns.
      Integrated Apache Kafka for asynchronous communication and event-driven messaging.
      Built CI/CD pipelines using Jenkins for automated testing, Docker image builds, and Kubernetes deployments.
      Improved API response time by 30% through optimization of Kafka consumer patterns and caching.
    """,
    """
      Designed an event-driven architecture using Apache Kafka to handle 100K+ banking transactions daily.
      Built Java-based microservices to publish and consume Kafka messages for fraud detection and notifications.
      Managed schema evolution using Confluent Schema Registry.
      Automated deployment and quality checks using GitHub Actions and Helm for Kubernetes.
      Ensured fault tolerance and message replay using Kafka DLQs and partition strategies
    """,
    """
      Created backend services in Java 11 with Spring Boot for a logistics tracking platform.
      Consumed real-time IoT device data via Kafka and processed it using stream processors. 
      Deployed services using Docker and Helm charts into a Kubernetes environment.
      Automated tests, builds, and deployments using GitLab CI/CD pipelines.
      Implemented service health checks, centralized logging, and exception alerting.
    """,
    """
      Engineered real-time microservices for analytics using Java, Spring Cloud Stream, and Kafka Streams.
      Built services to process millions of Kafka messages per day from sensor data.
      Integrated WebSocket APIs to push processed insights to frontend dashboards.
      Containerized applications with Docker and deployed using Azure DevOps pipelines.
      Ensured high availability and rollback safety with blue-green deployments.
    """,
    """
      Developed microservices in Java 17 with Spring Boot for real-time financial transaction processing.
      Used Kafka producers and consumers for audit logging, notification delivery, and inter-service communication.
      Managed CI/CD workflows using Jenkins, SonarQube for code quality, and Nexus for artifact storage.
      Applied circuit breakers and retry logic using Resilience4j for robust service calls.
      Designed REST APIs with secure OAuth2 authentication and role-based access control.
    """,
                          """Designed and developed scalable microservices using Java 11 and Spring Boot, deployed on AWS ECS with Kubernetes. 
                              Implemented REST APIs and optimized PostgreSQL queries for high performance.""",

                          """Built and deployed containerized Java applications using Docker and Kubernetes on Google Cloud Platform.
                          Integrated CI/CD pipelines with Jenkins and Git. Worked on microservices and Spring Cloud configuration.""",

                          """Developed backend modules in Java and Spring Boot for a cloud-native application.
                          Used Kubernetes for orchestration and deployed services on Azure AKS. Tuned SQL queries and implemented schema migrations.""",

                          """Led the backend development of RESTful APIs using Java 17 and Spring Boot.
                          Set up end-to-end CI/CD using GitHub Actions and deployed services on AWS EKS with full observability.""",

                          """Worked in an Agile team to create microservices in Spring Boot, containerized with Docker, and deployed via Kubernetes on Azure Cloud.
                          Integrated backend services with Oracle DB and ensured 95% code coverage using JUnit."""
                          ]
    negative_resp_list = ["""
       Worked on enterprise level monolithic group of services using Java, .
       Upgraded existing security modules to use
    """,
    """
     Maintained and enhanced enterprise applications built on JSP, Servlets, and Struts 1.3 framework.

Refactored JDBC-based DAO layers to reduce memory leaks and improve connection pool reuse.

Consumed legacy SOAP web services using Apache Axis in a loan origination system.

Deployed WAR files manually to WebLogic 10.x servers across multiple environments.

Migrated existing ANT build scripts to Maven for better dependency management.
    """,
    """
     Developed dynamic single-page applications (SPA) using React.js and Redux for state management.

Created reusable functional components and applied Hooks for lifecycle optimization.

Integrated RESTful APIs via Axios and handled async error states using Redux-Saga.

Implemented role-based UI rendering and secured front-end routing using React Router.

Optimized load time using lazy loading, code splitting, and Webpack bundle analysis.
    """  ,
    """
    Analyzed 10M+ rows of sales and customer data using SQL queries and Excel pivot models.

Built interactive dashboards in Power BI and Tableau to track KPI trends and forecasts.

Automated report generation scripts in Python for weekly C-level business reports.

Performed data cleaning, normalization, and outlier detection using Pandas and NumPy.

Integrated Google BigQuery with analytics pipelines for near real-time reporting.
    """,
    """
     Designed and executed manual test cases across UI, API, and backend layers.

Developed automated test scripts using Selenium WebDriver and Java TestNG framework.

Validated REST APIs using Postman and automated regression tests with REST Assured.

Integrated test execution with Jenkins pipelines for CI and smoke testing.

Reported and tracked defects using JIRA and participated in Agile sprint planning.
    """,
    """
     Built RESTful microservices using Flask and integrated them with a PostgreSQL backend.

Automated ETL pipelines using Pandas and scheduled jobs via cron and APScheduler.

Created custom decorators for logging and token-based authentication.

Used SQLAlchemy ORM to abstract database operations and prevent SQL injection.

Wrote unit and integration tests using Pytest with 85%+ code coverage.
    """     ,
                          """Frontend Developer with 5 years of experience using React.js, Redux, and TailwindCSS. No experience with Java, backend APIs, or cloud infrastructure.""",
                          """UI Developer with hands-on Angular and Figma experience. Focused on user interfaces and responsive design. No backend, database, or DevOps knowledge.""",
                          """Vue.js Developer with a focus on component-driven design and web animations. Lacks exposure to Java, Spring Boot, or cloud platforms.""",
                          """Web Developer working primarily with WordPress and jQuery. No experience with Java, microservices, or cloud-native architecture.""",
                          """Frontend Engineer specializing in VanillaJS, HTML5, and CSS animations. No experience in REST APIs, SQL, or Kubernetes.""",

                          """Java Developer working on legacy Java EE systems with servlets and JSP. No Kubernetes or cloud exposure. Deployed on-premises.""",
                          """Spring Boot Developer creating backend APIs for internal tools. No exposure to CI/CD, Docker, or any cloud provider.""",
                          """Java developer with expertise in Swing and desktop applications. No experience in cloud-native development, REST APIs, or containerization.""",
                          """Backend developer with Python and Django expertise. No Java or Kubernetes exposure. Deployed on traditional servers.""",
                          """Software engineer maintaining legacy .NET applications. No background in Java, Spring Boot, microservices, or any cloud platforms.""",

                          """SAP ABAP consultant working on ERP customizations. No experience in Java, cloud, or modern development environments.""",
                          """QA Automation Engineer with Selenium and JUnit experience. No involvement in development, CI/CD, or cloud infrastructure.""",
                          """Data Analyst using Excel, SQL, and Tableau. No experience with Java, microservices, or Kubernetes.""",
                          """Mobile Developer building Android apps in Kotlin. No backend, REST API, or DevOps exposure.""",
                          """Mainframe Developer with COBOL and DB2 experience. No exposure to modern backend technologies or cloud ecosystems."""
                          ]

    positive_skills = tech_core_skills_Java + tech_additional_skills
    negative_skills = tech_core_skills_Java_negative + irrelevant_tech_skills

    result = []
    for _ in range(n):
            start1= fake.date_between(start_date='-8y', end_date='-2y')
            end1 = fake.date_between(start_date=start1, end_date='today')
            duration1 = f"{start1.strftime('%b %Y')} – {end1.strftime('%b %Y')}"
            responsibilities = random.choice(positive_resp_list)
            ranges = [(4,13)]
            selected_range = random.choice(ranges)
            exp = random.randint(selected_range[0], selected_range[1])
            resume_positive = (f"Name: {fake.name()}\n"
            f"Skillsets: {', '.join(random.sample(positive_skills, k=min(6, len(positive_skills))))}\n"
            f"Years of Experience: {exp}\n"
            f"Work Experience:\n"
            f"Company: {fake.company()}\n"
            f"Duration: {duration1}\n"
            f"Project: {fake.bs().title()}\n"
            f"Role: {random.choice(engineer_title)}\n"
            f"Responsibilities: {responsibilities}\n")

            start2 = fake.date_between(start_date='-8y', end_date='-2y')
            end2 = fake.date_between(start_date=start2, end_date='today')
            duration2 = f"{start2.strftime('%b %Y')} – {end2.strftime('%b %Y')}"
            responsibilities = random.choice(negative_resp_list)
            exp = random.randint(5, 13)
            resume_negative = (f"Name: {fake.name()}\n"
            f"Skillsets: {', '.join(random.sample(negative_skills, k=min(6, len(negative_skills))))}\n"
            f"Years of Experience: {exp}\n"
            f"Work Experience:\n"
            f"Company: {fake.company()}\n"
            f"Duration: {duration2}\n"
            f"Project: {fake.bs().title()}\n"
            f"Role: {random.choice(engineer_title)}\n"
            f"Responsibilities: {responsibilities}\n")

            result.append((job_description_java_one, resume_positive, resume_negative))
    print(result)
    return result

def create_resume_java_set_two(n):
    name = fake.name()
    company = fake.company()
    project = fake.bs().title()
    role = fake.job()


    positive_resp_list = ["""Developed backend services using Java and Spring Boot, deployed on AWS using Kubernetes.
    Implemented CI/CD pipelines with Jenkins and Docker. Optimized SQL queries and REST APIs for scalability.
    """, """
       Developed secure and merchant-ready APIs using Spring Boot in Microservices architecture, updated logging, ensured JUnit coverage, handled deployment pipelines.
    """,
    """
      Built Scalable microservices with Java and Spring Boot, deployed on AWS using Kubernetes.
      Created Kafka based payment transaction systems with Confluent Kafka, Kubernetes, GCP.
    """,
    """
      Developed RESTful APIs using Java 8 and Spring Boot for microservices architecture.
      Integrated backend services with frontend applications using REST and JSON.
      Designed and implemented authentication and authorization using Spring Security.
    """,
    """
      Decomposed a monolithic Java application into independent Spring Boot microservices.
      Deployed microservices on Docker containers and orchestrated using Kubernetes.
      Integrated AWS S3 and RDS for scalable storage and data persistence.
    """,
    """
      Wrote complex SQL queries and procedures for Oracle/PostgreSQL databases.
      Used JPA/Hibernate for ORM and repository abstraction in a Spring Data application.
      Tuned queries and optimized indexing for high-performance data access.   
    """,
    """
      Developed Kafka consumers and producers to enable asynchronous message processing.
      Built real-time data ingestion pipelines using Apache Kafka and Spring Cloud Stream.
    """,
    """
      Configured Jenkins pipelines for automated builds and deployments of Java apps.
      Used Maven and Gradle for build lifecycle management and dependency resolution.
    """,
    """
      Developed Spring Boot-based microservices for an e-commerce platform handling order and payment workflows.
      Designed RESTful APIs and implemented service orchestration patterns.
      Integrated Apache Kafka for asynchronous communication and event-driven messaging.
      Built CI/CD pipelines using Jenkins for automated testing, Docker image builds, and Kubernetes deployments.
      Improved API response time by 30% through optimization of Kafka consumer patterns and caching.
    """,
    """
      Designed an event-driven architecture using Apache Kafka to handle 100K+ banking transactions daily.
      Built Java-based microservices to publish and consume Kafka messages for fraud detection and notifications.
      Managed schema evolution using Confluent Schema Registry.
      Automated deployment and quality checks using GitHub Actions and Helm for Kubernetes.
      Ensured fault tolerance and message replay using Kafka DLQs and partition strategies
    """,
    """
      Created backend services in Java 11 with Spring Boot for a logistics tracking platform.
      Consumed real-time IoT device data via Kafka and processed it using stream processors. 
      Deployed services using Docker and Helm charts into a Kubernetes environment.
      Automated tests, builds, and deployments using GitLab CI/CD pipelines.
      Implemented service health checks, centralized logging, and exception alerting.
    """,
    """
      Engineered real-time microservices for analytics using Java, Spring Cloud Stream, and Kafka Streams.
      Built services to process millions of Kafka messages per day from sensor data.
      Integrated WebSocket APIs to push processed insights to frontend dashboards.
      Containerized applications with Docker and deployed using Azure DevOps pipelines.
      Ensured high availability and rollback safety with blue-green deployments.
    """,
    """
      Developed microservices in Java 17 with Spring Boot for real-time financial transaction processing.
      Used Kafka producers and consumers for audit logging, notification delivery, and inter-service communication.
      Managed CI/CD workflows using Jenkins, SonarQube for code quality, and Nexus for artifact storage.
      Applied circuit breakers and retry logic using Resilience4j for robust service calls.
      Designed REST APIs with secure OAuth2 authentication and role-based access control.
    """                      ]

    positive_skills = tech_core_skills_Java + tech_additional_skills
    negative_skills = tech_core_skills_Java_negative + irrelevant_tech_skills

    result = []
    for _ in range(n):
            start1= fake.date_between(start_date='-8y', end_date='-2y')
            end1 = fake.date_between(start_date=start1, end_date='today')
            duration1 = f"{start1.strftime('%b %Y')} – {end1.strftime('%b %Y')}"
            ranges = [(4,6), (10,13)]
            selected_range = random.choice(ranges)
            exp = random.randint(selected_range[0], selected_range[1])
            resume_positive = (f"Name: {fake.name()}\n"
            f"Skillsets: {', '.join(random.sample(positive_skills, k=min(6, len(positive_skills))))}\n"
            f"Years of Experience: {exp}\n"
            f"Work Experience:\n"
            f"Company: {fake.company()}\n"
            f"Duration: {duration1}\n"
            f"Project: {fake.bs().title()}\n"
            f"Role: {random.choice(engineer_title)}\n"
            f"Responsibilities: {random.choice(positive_resp_list)}\n")

            start2 = fake.date_between(start_date='-8y', end_date='-2y')
            end2 = fake.date_between(start_date=start2, end_date='today')
            duration2 = f"{start2.strftime('%b %Y')} – {end2.strftime('%b %Y')}"
            exp = random.randint(7, 9)
            resume_negative = (f"Name: {fake.name()}\n"
            f"Skillsets: {', '.join(random.sample(positive_skills, k=min(6, len(positive_skills))))}\n"
            f"Years of Experience: {exp}\n"
            f"Work Experience:\n"
            f"Company: {fake.company()}\n"
            f"Duration: {duration2}\n"
            f"Project: {fake.bs().title()}\n"
            f"Role: {random.choice(engineer_title)}\n"
            f"Responsibilities: {random.choice(positive_resp_list)}\n")

            result.append((job_description_java_one, resume_positive, resume_negative))
    print(result)
    return result

def create_resume_java_set_three(n):
    name = fake.name()
    company = fake.company()
    project = fake.bs().title()
    role = fake.job()


    positive_resp_list = [
        """Designed and developed backend microservices in Java 11 and Spring Boot for an insurance claims engine.
        Applied DDD principles and introduced CQRS pattern for service segregation.
        Containerized apps using Docker and orchestrated deployment with Kubernetes on AWS.
        Led architecture design sessions and created reference architectures for new services.
        Configured centralized monitoring with Prometheus, Grafana, and ELK stack.""",
        """Architected a cloud-native billing system using Java 17 and Spring Cloud.
        Integrated Kafka for event-driven communication between decoupled services.
        Used Terraform and Helm for Infrastructure as Code and deployment automation.
        Implemented distributed tracing using OpenTelemetry and Jaeger.
        Defined architecture blueprints and mentored junior engineers on design practices.""",
        """Designed scalable backend platform for a video streaming service using Java, Spring WebFlux, and Redis.
        Implemented reactive microservices pattern and integrated rate-limiting middleware.
        Provisioned multi-region deployments on GCP using GKE and Istio service mesh.
        Led incident architecture reviews and bottleneck analysis.
        Standardized CI/CD with Jenkins pipelines and Canary deployments.""",
        """Created microservices for order and payment modules in Java 11.
        Led the decomposition of a monolith to microservices using Domain-Driven Design.
        Built reusable architecture components for logging, error handling, and retries.
        Established design review processes and technical documentation standards.
        Deployed on Azure Kubernetes Service with horizontal pod autoscaling.""",
        """Led architecture of an enterprise CRM platform on Spring Boot and PostgreSQL.
        Designed multi-tenant architecture with isolated compute and shared schema.
        Integrated with enterprise SSO using OAuth2 and Spring Security.
        Created architectural runbooks and service health dashboards.
        Ensured HA and DR strategies using AWS Multi-AZ deployment.""",
        """Designed and implemented microservices for telecom OSS/BSS system in Java 17.
        Adopted circuit breaker and bulkhead patterns using Resilience4j.
        Introduced event sourcing architecture with Kafka and PostgreSQL.
        Created Helm charts for repeatable deployments on OpenShift.
        Provided architecture decision records and technical PoCs.""",
        """Architected real-time anomaly detection system using Spring Boot, Kafka, and Spark.
        Designed modular service boundaries and API contracts.
        Defined scalability SLAs and SLOs for all core services.
        Developed GitHub Actions workflows for CI/CD with versioned deployments.
        Conducted quarterly architecture reviews and retrospectives.""",
        """Designed backend services for IoT device management on GCP using Java and Pub/Sub.
        Created scalable REST and gRPC APIs for high-throughput ingestion.
        Deployed apps in GKE with workload identity and IAM integration.
        Owned end-to-end logging and audit strategy using Stackdriver.
        Coached teams on architectural trade-offs and performance patterns.""",
        """Built scalable logistics platform with Java 11, Spring Boot, and Kafka Streams.
        Refactored existing services using hexagonal architecture.
        Used Prometheus, Grafana, and Loki for performance and observability.
        Managed API versioning and backward compatibility.
        Collaborated with SRE to define SLAs and runbooks.""",
        """Defined architecture for multi-tenant e-learning platform on AWS using Java and Spring Boot.
        Designed asynchronous job execution pipeline with SQS and Lambda.
        Implemented OpenAPI and auto-generated SDKs for client teams.
        Used Helm to deploy multiple environments with parameter overrides.
        Documented tech stack and performed spike analysis for upcoming features.""",
        """Developed Java microservices for e-commerce backend with Redis and Kafka.
        Introduced domain partitioning and vertical slicing for scalability.
        Used Docker Compose for local development and EKS for production.
        Authored infrastructure diagrams and architecture confluence pages.
        Integrated Sentry and PagerDuty for incident management.""",
        """Implemented async non-blocking services using Java and Spring WebFlux.
        Architected customer support backend with chat-based workflows.
        Used Istio for mTLS, retries, and fault injection in GKE.
        Defined error taxonomy and built retryable failure patterns.
        Participated in CTO office-led architecture council meetings.""",
        """Designed backend platform for high-scale flash sale events using Kafka and Java.
        Used gRPC for internal microservice communication and caching with Redis.
        Implemented rate-limiting middleware and multi-level queues.
        Owned autoscaling strategies and GC tuning.
        Conducted design audits and future-proofing assessments.""",
        """Designed an event-driven architecture for travel booking system.
        Used Kafka, Java 17, and Spring Boot with OAuth2 security.
        Automated deployments using ArgoCD and GitOps workflows.
        Introduced consumer lag monitoring and alerting systems.
        Presented architecture vision in quarterly business reviews.""",
        """Created backend services in Java 11 with Spring Boot for a logistics tracking platform.
        Consumed real-time IoT device data via Kafka and processed it using stream processors.
        Deployed services using Docker and Helm charts into a Kubernetes environment.
        Automated tests, builds, and deployments using GitLab CI/CD pipelines.
        Implemented service health checks, centralized logging, and exception alerting."""
    ]
    result = []

    positive_skills = tech_core_skills_Java_Architect
    negative_skills = tech_core_skills_Java

    negative_resp_list = ["""Built and maintained microservices using Java 11 and Spring Boot for a banking platform.
            Focused on business logic, database integrations, and API consumption.
            Worked closely with QA and DevOps teams to ensure stable delivery through Jenkins pipelines.""",
            """Implemented microservices for a healthcare product using Spring Boot and PostgreSQL.
            Handled request validation, persistence logic, and third-party API integration.
            Worked with predefined Swagger specs and consumed messages via Kafka.""",
            """Developed customer onboarding microservices for an insurance platform.
            Integrated REST APIs and added unit/integration test coverage using JUnit and Mockito.
            Used Docker and Jenkins for packaging and deployment.""",
            """Worked on Java-based backend services for retail order processing.
            Used Spring Boot, JPA, and MySQL for data persistence.
            Contributed to implementing new endpoints and maintaining existing ones.""",
            """Contributed to a suite of backend services in a logistics application using Java 11.
            Focused on data transformation, persistence, and message consumption via RabbitMQ.
            Used GitLab CI for build and deployment pipelines.""",
            """Built Spring Boot microservices for a telecom application handling user profile updates.
            Added input validation, caching with Redis, and error handling.
            REST APIs followed existing contracts documented via OpenAPI.""",
            """Created backend services in Java and integrated with external payment gateways.
            Used Spring Cloud, Feign clients, and service discovery via Eureka.
            Worked in agile teams with Jira-managed sprints.""",
            """Developed new features in existing microservices for an ed-tech platform.
            Wrote CRUD endpoints in Spring Boot and implemented database migrations with Flyway.
            Used Kafka templates and consumer patterns set up by the core platform.""",
            """Maintained microservices for HR management software.
            Used Java 11, PostgreSQL, and Spring Security for auth handling.
            Focused on implementing features based on requirements provided by the business team.""",
            """Contributed to backend logic for a real estate platform.
            Wrote service logic in Spring Boot and consumed downstream services via REST.
            CI/CD handled via Jenkins and Docker.""",
            """Built modules for invoice and payment microservices using Spring Boot.
            Worked with JPA entities, transaction management, and REST controllers.
            Collaborated with frontend and QA teams to deliver tested stories.""",
            """Developed backend services in a ride-hailing app using Java and MongoDB.
            Integrated push notifications and user activity tracking features.
            Used Kafka consumers configured using standard templates.""",
            """Implemented business logic for microservices in a banking CRM.
            Worked on JPA mappings, DTOs, and request-response objects.
            Used existing helm charts for deployment to Kubernetes.""",
            """Created backend APIs for survey and feedback microservices.
            Handled request parsing, validation, and persistence.
            Contributed to API documentation via Swagger and testing with Postman.""",
            """Wrote backend Java services for a food delivery platform.
            Handled input sanitization, data enrichment, and REST endpoints in Spring Boot.
            Participated in daily stand-ups, grooming, and retrospectives within a scrum team.""",
                          """Worked as part of the L2 production support team for a legacy banking application built in Java 6 and Struts.
                          Handled monitoring of system logs, incident ticket resolution, and service restarts.
                          No involvement in design, architecture, or feature development.
                          Skills: Java 6, Struts, Production Support, Incident Management, Legacy Systems""",
                          """Focused on building and enhancing UI screens using AngularJS, jQuery, and Bootstrap.
                      Worked exclusively on client-side validation and page responsiveness.
                      Limited to frontend tasks with no backend or architectural exposure.
                      Skills: AngularJS, jQuery, Bootstrap, Frontend Development, UI/UX""",
                          """Maintained a 12-year-old Java EE application with EJBs, JSP, and Servlets.
                      Handled patching bugs, updating config files, and fixing integration issues with legacy databases.
                      No experience with modern frameworks or scalable system design.
                      Skills: Java EE, EJB, JSP, Servlets, Legacy Systems""",
                          """Monitored Java production systems and responded to alert dashboards.
                      Routinely restarted failing services and triaged incidents without writing code.
                      Had no role in development or system design decisions.
                      Skills: Java, Monitoring, Production Support, Alerting, Triage""",
                          """Managed COBOL-Java batch jobs in a financial services environment.
                      Fixed nightly job failures and wrote SQL data patch scripts for broken records.
                      Did not contribute to development or architecture.
                      Skills: COBOL, Java, Batch Jobs, SQL, Legacy Integration""",
                          """Served as a UI developer responsible for implementing designs using React, HTML, and CSS.
                      Created mockups and translated them into interactive client-side components.
                      No involvement in backend services or system-level logic.
                      Skills: React, HTML, CSS, UI/UX, Frontend Development""",
                          """Worked on bug fixes and minor enhancements for a legacy Spring MVC system.
                      Performed regression testing and sanity checks during minor patch releases.
                      Lacked any architectural ownership or hands-on design work.
                      Skills: Spring MVC, Bug Fixing, Regression Testing, Legacy Codebase""",
                          """Maintained XML configs and upgraded deprecated dependencies in a 2008 Java application.
                      Focused on compatibility fixes and build stability.
                      No new development or architectural exposure.
                      Skills: Java, XML, Dependency Management, Legacy Systems""",
                          """Supported QA in defect resolution after production deployments.
                      Focused on fixing UI alignment issues and minor post-release bugs.
                      No backend or architectural contributions.
                      Skills: QA Collaboration, Bug Fixing, UI Debugging""",
                          """Built jQuery-based frontend forms and handled client-side validation.
                      Consumed REST APIs from backend teams but wrote no backend logic.
                      Focused solely on usability and interface correctness.
                      Skills: jQuery, JavaScript, Frontend Development, Form Validation""",
                          """Maintained Java apps running on legacy on-prem systems in the insurance domain.
                      Conducted log reviews and service restarts as part of L1/L2 triage.
                      Did not participate in design or code development.
                      Skills: Java, On-prem Systems, Triage Support, Production Maintenance""",
                          """Fixed UI issues and performed small updates in a Java Swing-based desktop app.
                      Focused on aligning UI elements and ensuring form behavior.
                      Had no involvement with backend logic or architecture.
                      Skills: Java Swing, UI Maintenance, Desktop Application""",
                          """Assisted with patch deployments and sanity testing for an aging Java ERP platform.
                      Followed client instructions for minor config changes.
                      No technical design, coding, or architectural responsibilities.
                      Skills: Java, ERP Systems, Patch Management, Sanity Testing""",
                          """Maintained SQL-based data pipelines for a Java-Oracle system.
                      Handled format mismatches and reconciliation reports.
                      Did not engage with business logic or system design.
                      Skills: Java, Oracle, SQL, Data Reconciliation, Legacy Systems""",
                          """Enhanced UI components using Angular and Bootstrap for internal tools.
                      Consumed pre-built REST endpoints and focused on frontend logic.
                      No contribution to service architecture or backend strategy.
                      Skills: Angular, Bootstrap, REST API Consumption, UI Styling""",
                          """Updated deprecated libraries in a legacy Java application during modernization efforts.
                      Ensured successful builds but performed no feature development.
                      Had no architectural input or system design work.
                      Skills: Java, Dependency Upgrades, Build Automation, Legacy Modernization""",
                          """Provided production support for enterprise apps, mainly handling service health and restarts.
                      Triage and escalation were key responsibilities.
                      Did not work with source code or system architecture.
                      Skills: Production Support, Monitoring, Triage, Service Management""",
                          """Performed database cleanup and ran manual patch scripts as part of a shared services team.
                      Fixed corrupted records using SQL but had no interaction with application code.
                      Skills: SQL, Data Maintenance, Shared Services, Manual Patching""",
                          """Supported a legacy enterprise portal built on JSP by managing static content and UI fixes.
                      Handled layout adjustments and minor changes with no backend exposure.
                      Skills: JSP, Static Content Management, UI Fixes, Legacy Web Systems""",
                          """Created screen wireframes and collaborated with product teams to refine UI flows.
                      Worked on visual designs and journey mapping without touching the tech stack.
                      Skills: Wireframing, Prototyping, Product Collaboration, UI/UX"""
                        ]
    for _ in range(n):
            start1= fake.date_between(start_date='-8y', end_date='-2y')
            end1 = fake.date_between(start_date=start1, end_date='today')
            duration1 = f"{start1.strftime('%b %Y')} – {end1.strftime('%b %Y')}"
            responsibilities = random.choice(positive_resp_list)
            ranges = [(4,8), (10,14)]
            selected_range = random.choice(ranges)
            exp = random.randint(selected_range[0], selected_range[1])
            resume_positive = (f"Name: {fake.name()}\n"
            f"Skillsets: {', '.join(random.sample(positive_skills, k=min(6, len(positive_skills))))}\n"
            f"Years of Experience: {exp}\n"
            f"Work Experience:\n"
            f"Company: {fake.company()}\n"
            f"Duration: {duration1}\n"
            f"Project: {fake.bs().title()}\n"
            f"Role: {random.choice(engineer_title)}\n"
            f"Responsibilities: {responsibilities}\n")

            start2 = fake.date_between(start_date='-8y', end_date='-2y')
            end2 = fake.date_between(start_date=start2, end_date='today')
            duration2 = f"{start2.strftime('%b %Y')} – {end2.strftime('%b %Y')}"
            responsibilities = random.choice(negative_resp_list)
            exp = random.randint(5, 13)
            resume_negative = (f"Name: {fake.name()}\n"
            f"Skillsets: {', '.join(random.sample(negative_skills, k=min(6, len(negative_skills))))}\n"
            f"Years of Experience: {exp}\n"
            f"Work Experience:\n"
            f"Company: {fake.company()}\n"
            f"Duration: {duration2}\n"
            f"Project: {fake.bs().title()}\n"
            f"Role: {random.choice(engineer_title)}\n"
            f"Responsibilities: {responsibilities}\n")

            result.append((job_description_java_two, resume_positive, resume_negative))
    print(result)
    return result

def create_resume_java_set_four(n):
    name = fake.name()
    company = fake.company()
    project = fake.bs().title()
    role = fake.job()

    positive_resp_list = [
        """Built RESTful microservices using Java 11 and Spring Boot for a retail application.
    Integrated the backend with a responsive React.js frontend for order management.
    Used Docker to containerize services and deployed on AWS ECS.
    Implemented CI/CD pipelines with GitHub Actions and Helm charts.
    Handled database design using PostgreSQL and Flyway for migrations.""",
        """Developed a ticket booking web app using React.js and Spring Boot.
    Implemented JWT-based security and user authentication with Spring Security.
    Used MySQL for persistent storage and Redis for caching frequently used data.
    Built CI/CD workflows using Jenkins for both backend and frontend.
    Optimized frontend performance using React hooks and code splitting.""",
        """Created dashboards for internal reporting using React.js and Chart.js.
    Spring Boot backend exposed REST endpoints for data analytics.
    Dockerized services and deployed the stack on Azure Kubernetes Service.
    Implemented Agile practices with daily stand-ups and sprint planning.
    Handled accessibility compliance and responsive layouts across devices.""",
        """Designed an employee onboarding system using Spring Boot and Angular.
    Frontend forms supported dynamic validation and state persistence.
    Used RabbitMQ for asynchronous messaging between services.
    Set up GitLab CI/CD pipelines and Docker containers for deployment.
    Logged application events with ELK stack integration.""",
        """Led the development of a customer support portal using Java and React.js.
    Wrote reusable UI components and connected them to Spring REST APIs.
    Backend services used JPA and Hibernate for DB interactions.
    Configured monitoring and alerting using Prometheus and Grafana.
    Worked closely with QA to write integration tests in Postman and Cypress.""",
        """Built microservices in Java (Spring Boot) for a telecom billing system.
    Integrated React.js frontend with API gateway and used Redux for state.
    Managed cloud deployments on AWS using Terraform and Docker Compose.
    Implemented role-based access and secure login with OAuth2.
    Wrote unit and integration tests using JUnit and React Testing Library.""",
        """Worked on dynamic form generation in React.js for healthcare claims processing.
    Backend used Spring Boot and MongoDB with domain-driven design patterns.
    CI/CD pipeline built using Jenkins and Docker.
    Wrote detailed Swagger documentation for API consumers.
    Handled state management and error boundaries in frontend components.""",
        """Contributed to travel itinerary platform with React and Java backend.
    Created drag-and-drop UI features and calendar integrations.
    Backend handled business logic with Spring Boot and PostgreSQL.
    Used Kubernetes for container orchestration on GCP.
    Automated testing pipeline using GitHub Actions and Selenium.""",
        """Refactored monolith into microservices for a banking application using Spring Boot.
    Developed frontend screens in Angular with lazy-loaded modules.
    Used Kafka for real-time communication between services.
    Maintained build pipelines using GitLab CI and container registries.
    Wrote health checks and implemented API rate limiting.""",
        """Developed expense management module in a finance app using Java 17.
    Created frontend components in React.js and styled using Material UI.
    Used REST APIs secured with Spring Security and JWT.
    Implemented server-side validation and schema mapping with Hibernate.
    Followed TDD principles using JUnit and React Testing Library.""",
        """Built an internal inventory tool using React.js and Spring Boot backend.
    Managed shared UI libraries and maintained TypeScript-based components.
    Backend used Flyway and Liquibase for schema versioning.
    Automated cloud deployment using Azure DevOps pipelines.
    Worked on cross-browser compatibility and responsive design.""",
        """Created notification microservices in Java using Spring Cloud and Kafka.
    Developed a user dashboard in Vue.js with data visualization components.
    Dockerized all components and deployed on EKS using Helm.
    Enabled OpenTelemetry tracing for distributed debugging.
    Integrated user authentication using Keycloak and RBAC.""",
        """Redesigned legacy JSP frontend into modern React components.
    Spring Boot backend supported GraphQL and REST endpoints.
    Used PostgreSQL with custom indexing strategies for faster reads.
    Created Jenkins pipelines with parallel testing and build caching.
    Collaborated with designers for pixel-perfect UI conversion.""",
        """Built a microservices-based CMS platform using Spring Boot and Angular.
    Integrated frontend with backend via REST APIs and WebSockets.
    Set up Prometheus metrics and custom Grafana dashboards.
    Handled frontend localization and theme switching features.
    Ensured 90%+ test coverage on all modules with unit and E2E tests.""",
        """Worked on compliance management app using Java, Spring Security, and React.
    Enabled SSO using OAuth2 and integrated Okta.
    Used Redux Toolkit for frontend state handling and side-effects.
    Managed multi-stage Docker builds for both backend and frontend.
    Conducted regular code reviews and mentored junior developers."""
    ]

    result = []

    positive_skills = tech_core_skills_Java + tech_core_skills_React
    negative_skills = tech_core_skills_React + irrelevant_tech_skills + tech_additional_skills

    negative_resp_list = [
        """Worked extensively on backend systems using Java and Spring Boot.
    Developed microservices with Spring Cloud and Eureka for service discovery.
    Integrated RabbitMQ for asynchronous communication.
    Used Liquibase for DB migrations and PostgreSQL for persistence.
    Configured Jenkins pipelines and Docker-based deployments.""",
        """Designed backend APIs for an insurance processing platform using Java 17.
    Built event-driven services using Kafka and Spring Boot.
    Handled batch jobs using Spring Batch for claims processing.
    Implemented RBAC and token-based security using OAuth2.
    No involvement in frontend or UI development.""",
        """Contributed to backend for banking transaction engine using Java and Hibernate.
    Created REST APIs and handled database integrations with MySQL.
    Managed deployments with Helm on EKS.
    Focused solely on middleware and message broker integrations.
    Frontend work handled by another team.""",
        """Built secure microservices using Spring Boot and Spring Security.
    Implemented multithreaded processing logic for data ingestion pipelines.
    Used GitLab CI and Docker Swarm for backend deployments.
    Did not contribute to frontend, React or UI development.
    Worked mostly on backend authentication modules.""",
        """Worked on backend APIs in Java for managing payroll data in a financial SaaS app.
    Designed REST endpoints and implemented audit logging.
    Used PostgreSQL for DB interactions and JPA for ORM.
    Set up CI/CD pipelines using Azure DevOps.
    No tasks related to frontend design or integration.""",
        """Engineered scalable services using Java and Micronaut for high-volume data processing.
    Worked with Redis for caching and Kafka for event streaming.
    Managed cloud infrastructure on AWS using Terraform.
    Did not collaborate with UI/UX or frontend teams.
    Responsibilities confined to backend scalability and performance tuning.""",
        """Developed data synchronization services in Spring Boot with Kafka Streams.
    Wrote health monitoring and logging services using Micrometer and Prometheus.
    Managed schema versions using Avro and Confluent Schema Registry.
    Tested services using JUnit, Mockito, and Postman.
    No exposure to HTML, CSS, React, or frontend frameworks.""",
        """Designed backend interfaces for internal HR automation using Java and Spring WebFlux.
    Integrated with LDAP and internal REST services for authentication.
    Used Vault for secret management and AWS S3 for document storage.
    Backend-only role, did not work on UI or web components.""",
        """Built server-side components in Java for fraud detection platform.
    Created async event handlers using Kafka and implemented retry mechanisms.
    Managed observability using ELK stack and Grafana dashboards.
    Interfaced with DB using Spring Data JPA and Oracle.
    No contribution to frontend development or design logic.""",
        """Developed machine learning workflows using Python and TensorFlow.
    Worked on training and evaluating NLP models for chatbot intent detection.
    Integrated models with Flask REST APIs and deployed on GCP.
    Tech stack did not involve Java, Spring, or frontend development.""",
        """Built ETL data pipelines using Apache Spark and Scala.
    Managed large-scale data transformations on Hadoop clusters.
    No experience in web development, Java, or frontend stacks.
    Primarily focused on data engineering and batch processing workloads.""",
        """Worked as a WordPress Developer customizing themes and plugins.
    Handled SEO optimization, content management, and web analytics integration.
    No exposure to Java, Spring Boot, or backend system design.
    Work focused on CMS platforms and marketing tools.""",
        """Developed iOS applications using Swift and UIKit for a food delivery startup.
    Built UI screens and handled local storage with Core Data.
    No backend or Java-related development involved.
    Worked exclusively on mobile native development.""",
        """Worked as a Salesforce Developer customizing Lightning components and Apex triggers.
    Handled CRM workflows and automated report generation.
    Did not work on any Java/Spring stack or web-based frontend.
    Experience limited to Salesforce ecosystem.""",
        """Built frontends using PHP and jQuery for a legacy ERP product.
    Worked with XAMPP and MySQL for development and testing.
    No knowledge of React, Angular, Java, or Spring Boot.
    Primarily focused on LAMP stack projects.""",
        """Worked extensively on React.js to build modular UI components for a B2C travel site.
       Used Redux for global state management and integrated charting with D3.js.
       Handled accessibility and mobile responsiveness across devices.
       Did not work on backend services or Java-based technologies.""",
        """Built dynamic forms and wizards using Angular 11 and RxJS.
    Handled API integration via Axios with third-party services (no internal backend).
    Focused on frontend routing, error handling, and localization support.
    No involvement in Java, Spring Boot, or backend stack.""",
        """Led frontend development of an ecommerce portal using Vue.js and Vuex.
    Used SCSS and BEM methodology for styling consistency.
    Implemented animations and transitions using GSAP.
    Did not participate in backend or service-layer development.""",
        """Created interactive dashboards using React and Material UI for marketing analytics.
    Built reusable chart widgets with Chart.js and Highcharts.
    All backend integration was mocked or handled by another team.
    No experience in backend systems or Java stack.""",
        """Developed landing pages and product pages using plain JavaScript, HTML5, and CSS3.
    Used Webpack and Babel for frontend bundling.
    Optimized performance with lazy loading and image compression.
    Backend development was out of scope for the role.""",
        """Worked on redesign of a legacy app using Figma designs and implemented with Angular.
    Implemented global error handler and UI alerts using Angular services.
    Wrote unit tests using Jasmine and Karma for components.
    Did not work on backend architecture or Java frameworks.""",
        """Contributed to mobile-first UI designs using React Native and Styled Components.
    Worked on cross-platform compatibility and gesture-based navigation.
    Integrated Firebase for user authentication and data sync.
    No exposure to backend technologies such as Java or Spring.""",
        """Built a design system for internal UI components using Storybook and Tailwind CSS.
    Collaborated with UX team for accessibility compliance and contrast ratios.
    All backend services were consumed as REST endpoints provided externally.
    No direct contribution to backend code or logic.""",
        """Specialized in frontend theming and layout engineering using SCSS and Bootstrap 5.
    Worked closely with designers to convert mockups to production-ready HTML.
    Used jQuery for DOM manipulation and animations in legacy apps.
    Never involved in writing or maintaining backend Java code."""
    ]

    for _ in range(n):
            start1= fake.date_between(start_date='-8y', end_date='-2y')
            end1 = fake.date_between(start_date=start1, end_date='today')
            duration1 = f"{start1.strftime('%b %Y')} – {end1.strftime('%b %Y')}"
            responsibilities = random.choice(positive_resp_list)
            ranges = [(4,8), (10,14)]
            selected_range = random.choice(ranges)
            exp = random.randint(selected_range[0], selected_range[1])
            resume_positive = (f"Name: {fake.name()}\n"
            f"Skillsets: {', '.join(random.sample(positive_skills, k=min(6, len(positive_skills))))}\n"
            f"Years of Experience: {exp}\n"
            f"Work Experience:\n"
            f"Company: {fake.company()}\n"
            f"Duration: {duration1}\n"
            f"Project: {fake.bs().title()}\n"
            f"Role: {random.choice(engineer_title)}\n"
            f"Responsibilities: {responsibilities}\n")

            start2 = fake.date_between(start_date='-8y', end_date='-2y')
            end2 = fake.date_between(start_date=start2, end_date='today')
            duration2 = f"{start2.strftime('%b %Y')} – {end2.strftime('%b %Y')}"
            responsibilities = random.choice(negative_resp_list)
            exp = random.randint(5, 13)
            resume_negative = (f"Name: {fake.name()}\n"
            f"Skillsets: {', '.join(random.sample(negative_skills, k=min(6, len(negative_skills))))}\n"
            f"Years of Experience: {exp}\n"
            f"Work Experience:\n"
            f"Company: {fake.company()}\n"
            f"Duration: {duration2}\n"
            f"Project: {fake.bs().title()}\n"
            f"Role: {random.choice(engineer_title)}\n"
            f"Responsibilities: {responsibilities}\n")

            result.append((job_description_java_three, resume_positive, resume_negative))
    print(result)
    return result

# Main generator
def generate_tech_triplets_csv(filename, n):
        java_set_one = create_resume_java_set_one(n)
        # java_set_two = create_resume_java_set_two(n)
        java_set_three = create_resume_java_set_three(n)
        java_set_four = create_resume_java_set_four(n)
        react_set_one = frontend.create_resume_react_set_one(n)
        devops_set_one = devops.create_resume_devops_set_one(n)

        data = java_set_one + java_set_three + java_set_four + react_set_one + devops_set_one
        # data = java_set_one
        # data = react_set_one
        # data = devops_set_one
        random.shuffle(data)
        df = pd.DataFrame(data, columns=['job_description', 'resume_positive', 'resume_negative'])
        df.to_csv(filename, index=False)
        # for _ in range(n):
        #     anchor = job_description_java_one.strip().replace('\n', ' ')
        #     positive = create_resume_java_set_one(tech_core_skills_Java + tech_additional_skills, is_positive=True)
        #     negative = create_resume_java_set_one(tech_core_skills_Java_negative + irrelevant_tech_skills, is_positive=False)
        #     writer.writerow([anchor, positive, negative])


# Run generator
if __name__ == "__main__":
    generate_tech_triplets_csv("tech_company_triplets_LTC_one.csv", n=100)
