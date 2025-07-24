import csv
import random
from faker import Faker
import pandas as pd

from datetime import datetime

fake = Faker()


# Tech company job description
job_description_devops_one = """Job Description Summary

Experience: 4 - 6 years and 10 to 13 years

We are seeking a skilled and motivated DevOps Engineer with strong experience in cloud platforms, Kubernetes, and CI/CD pipelines to join our engineering team. The ideal candidate will be responsible for automating deployment processes, managing scalable cloud infrastructure, and ensuring system reliability and security. This role involves close collaboration with software engineers, cloud architects, and QA to drive operational excellence in a modern, cloud-native environment.

Job Description

Required Skills:

Automate deployment, monitoring, and infrastructure management using CI/CD tools.
Design and implement scalable cloud-native solutions on AWS, Azure, or GCP.
Manage and optimize Kubernetes clusters for high availability and performance.
Ensure system reliability, security, and compliance across environments.
Collaborate with development teams to streamline build and release pipelines.
Troubleshoot infrastructure and deployment issues with timely resolution.
Maintain technical documentation and contribute to DevOps best practices.
Strong experience with CI/CD tools such as Jenkins, GitHub Actions, or GitLab CI.
Proficiency in managing cloud platforms like AWS, Azure, or GCP.
Hands-on expertise in Kubernetes and container orchestration tools.
Experience with Infrastructure as Code tools like Terraform or CloudFormation.
Familiarity with monitoring/logging solutions like Prometheus, Grafana, or ELK Stack.
Strong scripting skills in Python, Bash, or similar languages.
Excellent problem-solving, debugging, and communication skills.
"""

engineer_title = ["Senior Software Engineer", "Software Engineer", "Software Developer", "Tech Lead", "Technical Lead", "Engineering Lead", "Software Development Engineer", "SSE", "SDE", "SE"]
tech_core_skills_Devops = ["Kubernetes", "JFrog", "Grafana", "CI/CD", "Jenkins", "HashiCorp Vault","Docker","Jaegar", "Openshift", "Azure", "Podman", "AWS", "GCP",
                           "Harness", "Ansible", "AquaSec", "OCI", "Splunk", "Nexus", "Terraform", "Harbor", "Helm", "Prometheus", "GAR", "Podman", "Spinnaker"]
tech_core_skills_React = ["React", "HTML/CSS", "Bootstrap", "UX", "Javascript", "Accessibility", "Angular", "ReactJs", "VueJs",
                          "Figma", "Typescript", "Material UI", "Redux", "CSS", "ES6", "React.js", "CSS3", "Node.js", "NodeJs", "Express",
                          "ExpressJs", "Express.js", "WCAG", "UI/UX", "Frontend", "UI", "Wiremocks"]
tech_core_skills_others = ["Java", "Python", "Selenium", "Spring Boot", "CI/CD", ".NET", "Scala", "Hibernate", "Apache Spark",
                    "Microservices", "REST APIs"]
tech_core_skills_Java = ["Java", "Spring Boot", "Kubernetes", "Hibernate", "AWS", "GCP", "Azure", "SQL", "Docker", "Jenkins", "Git",
                    "Microservices", "REST APIs"]

def create_resume_devops_set_one(n):
    name = fake.name()
    company = fake.company()
    project = fake.bs().title()
    role = fake.job()


    positive_resp_list = [ """Implemented CI/CD pipelines using GitLab CI for microservices on AWS.
Used Terraform for infrastructure provisioning and managed Kubernetes workloads.
Monitored systems with Prometheus and Grafana, ensuring 99.9% uptime.""",
    """Managed cloud infrastructure on Azure using ARM templates and Terraform.
Configured Jenkins pipelines for application deployment on Kubernetes clusters.
Wrote Python scripts for log rotation and backup automation.""",
    """Set up EKS clusters on AWS with autoscaling and rolling updates.
Used GitHub Actions for CI/CD and built alerting dashboards in Grafana.
Handled system hardening and network policies in Kubernetes.""",
    """Automated provisioning of GCP infrastructure using Terraform.
Implemented CI/CD with Jenkins and integrated security scans.
Wrote Bash scripts to monitor pod health and restart failed containers.""",
    """Worked on multi-cloud CI/CD strategy across AWS and Azure.
Containerized applications with Docker and deployed on Kubernetes via Helm.
Used ELK stack for centralized logging and incident analysis.""",
    """Built robust release pipelines using Jenkins and GitHub Actions.
Managed Kubernetes clusters and secrets with HashiCorp Vault.
Wrote Python utilities for automated node health checks.""",
    """Deployed services on Azure Kubernetes Service (AKS) using Helm charts.
Implemented blue-green deployment strategy via GitLab CI.
Integrated monitoring with Datadog and Slack alerts.""",
    """Managed infrastructure using Terraform and Packer for reproducibility.
Configured CI/CD using GitLab runners and Docker executors.
Optimized pod scheduling and resource limits in GKE clusters.""",
    """Wrote shell scripts for log backups, DNS updates, and metric collection.
Maintained and updated CI pipelines using Jenkins Shared Libraries.
Worked closely with developers to troubleshoot container orchestration issues.""",
    """Provisioned cloud resources on AWS using Terraform modules.
Created Jenkins pipelines for Java and Node.js microservices.
Managed K8s config maps, secrets, and service discovery.""",
    """Led DevOps migration from on-prem to AWS EKS.
Created Grafana dashboards for latency and throughput KPIs.
Used Bash and Python for automation of backups and log cleanup jobs.""",
    """Implemented Canary deployments with Kubernetes and ArgoCD.
Created self-healing Kubernetes operators for custom workloads.
Wrote shell scripts to enforce Git commit policies in CI.""",
    """Used GitHub Actions to build and deploy Docker containers to ECR.
Managed multi-zone GCP infrastructure using Terraform.
Performed root cause analysis of failed deployments using ELK Stack.""",
    """Built CI/CD templates in GitLab with job-level caching and approvals.
Managed secrets with AWS Secrets Manager and injected via Kubernetes.
Integrated Dynatrace for APM and trace correlation.""",
    """Refactored monolithic deployment scripts into modular Terraform stacks.
Implemented environment promotion pipelines in Jenkins.
Trained junior engineers on Helm templating and CI/CD workflows."""
                           ]

    negative_resp_list = [ """Developed REST APIs using Spring Boot and Hibernate for a fintech platform.
Deployed manually via Tomcat on virtual machines.
No experience in CI/CD or cloud environments.""",
    """Worked as a full-stack developer using React and Node.js.
Managed local development with npm and docker-compose.
No infrastructure automation or Kubernetes usage.""",
    """Built machine learning models in Python and deployed using Flask.
Used AWS EC2 for testing but no automation or pipeline experience.""",
    """Created iOS apps using Swift for e-commerce client.
Used Xcode build pipeline but did not interact with CI/CD or cloud tools.""",
    """Built web dashboards in Angular and consumed REST APIs.
Deployment handled by DevOps team, no Kubernetes or Terraform used.""",
    """Worked on data pipelines using Apache Spark and Airflow.
Focused on ETL orchestration, not infrastructure or CI/CD.""",
    """Developed monolithic applications in Java EE and deployed on WebLogic.
No exposure to containerization, cloud-native, or CI tooling.""",
    """Implemented API Gateway in Node.js and configured routes.
Used PM2 for process management, no experience with CI/CD pipelines.""",
                           """Developed RESTful APIs using Java 11 and Spring Boot for insurance services.
                          Used traditional WAR deployments on Tomcat with no exposure to CI/CD or containerization.""",

                           """Built microservices with Spring Cloud and Eureka.
                       Handled API gateway routing but relied on DevOps team for deployments and infrastructure.""",

                           """Worked on backend modules using Spring Boot and JPA.
                       All deployment and infrastructure handled manually on on-prem servers; no cloud or Kubernetes experience.""",

                           """Implemented async messaging with Kafka and Spring Boot.
                       Did not participate in CI/CD configuration or cloud provisioning.""",

                           """Maintained microservices-based backend using Java 17.
                       Services were deployed by another team to OpenShift; I was not involved in pipeline or infra automation.""",

                           """Built API integrations in Java and used Hibernate for ORM.
                       Focused solely on application logic—DevOps tasks were performed by a separate SRE team.""",

                           """Created CRUD services for logistics app using Spring Boot and PostgreSQL.
                       Used local builds and manual deployment scripts without Docker or pipelines.""",

                           """Developed business services using Spring MVC and SOAP APIs.
                       Project followed legacy practices with FTP deployments and no containerization or cloud usage.""",

                           """Built user authentication flows using Spring Security and JWT.
                       Not involved in CI/CD, cloud deployment, or infrastructure-as-code tasks.""",

                           """Worked on monolithic Java EE applications migrating to Spring Boot.
                       Participated in code refactoring only; DevOps tooling and deployment were out of scope.""",
    """Created batch jobs for telecom client using Python and SQL.
All deployment was manual, no infrastructure-as-code or K8s experience.""",
                           """Managed supply chain optimization models in Excel and VBA.
                          No experience in DevOps, scripting, or cloud infrastructure.""",
                           """Designed brochures and digital content using Adobe XD and Photoshop.
                       Role entirely creative; no technical or infrastructure exposure.""",
                           """Worked on mainframe applications using COBOL and JCL.
                       No knowledge of cloud, containers, or modern DevOps stack.""",
                           """Built educational games in Unity using C# and physics engines.
                       All assets and builds handled within game engine tools.""",
                           """Wrote quantitative models in R and published reports via Shiny dashboards.
                       No DevOps, cloud, or automation exposure.""",
                           """Provided L1 IT support for desktop systems and printer networks.
                       Role limited to end-user support and not infrastructure automation."""
                           ]

    positive_skills = tech_core_skills_Devops
    negative_skills = tech_core_skills_others + tech_core_skills_React

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

            result.append((job_description_devops_one, resume_positive, resume_negative))
    print(result)
    return result