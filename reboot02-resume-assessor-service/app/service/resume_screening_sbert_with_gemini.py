import asyncio
from concurrent.futures import ThreadPoolExecutor, as_completed

import pandas as pd
import torch
import numpy as np
import re
import os
# from vertexai.generative_models import GenerativeModel
from sentence_transformers import util, CrossEncoder
from app.logger import logger

from app.config import MODEL_DATA_PATH, HUGGING_FACE_TOKEN
# from app.service.vertex_ai_init import init_vertex_ai
from app.model_loader import load_sbert_model, load_gemini_model


class ResumeRanking:
    def filter_suitable_resumes(self, job_description, resume_list):

        # Load model trained with intfloat/e5-large-v2 and triplet loss
        # model = SentenceTransformer(MODEL_DATA_PATH)
        # model = SentenceTransformer('soumik060893/SBERTResumeTrained')

        resumes = [(resume['resume_text']) for resume in resume_list]

        # Compute contextual embeddings for resumes and job_description
        resume_embeddings = load_sbert_model().encode(resumes, convert_to_tensor=True)
        job_embedding = load_sbert_model().encode(job_description, convert_to_tensor=True)

        # Calculate cosine similarity between resumes and job_description
        cos_sim = util.pytorch_cos_sim(resume_embeddings, job_embedding)
        # print(cos_sim)

        # Calculate percentile
        cos_score_list = [score.item() for score in cos_sim]
        print(cos_score_list)
        threshold = np.percentile(cos_score_list, 60)
        print(threshold)

        # Filter resumes based on threshold
        filtered_indices = [i for i, score in enumerate(cos_score_list) if score>=0.75 and score>=threshold]
        filtered_resumes = [resumes[i] for i in filtered_indices]
        # filtered_resumes = [(resume_list[i]['ApplicantId'], resumes[i], float(score)) for i, score in list(zip(filtered_indices, cos_score_list))]
        filtered_resumes = [(resume_list[i]['ApplicantId'], resumes[i], float(cos_score_list[i])) for i in filtered_indices]
        logger.info("Showing selected resumes after SBERT filtering::::")
        for resume in filtered_resumes:
            logger.info("ApplicantID: %s Score: %s", resume[0], resume[2])
        print(filtered_resumes)
        return filtered_resumes

    def re_rank_resume(self, job_description, filtered_resumes, gemini_model):
        final_resumes = []
        def process_resume(application_id, resume, score):
            # loop = asyncio.new_event_loop()
            # asyncio.set_event_loop(loop)
            # Re rank resumes with reasoning using Gemini API
            generation_config = {
                "temperature": 0.4,  # Lower = faster, more deterministic
                "top_k": 20,
                "top_p": 0.8
            }
            prompt = f"""
                     You are a seasoned Recruiter.
                     Assess the below points very carefully and generate feedback strictly within 5000 characters:
                     1. Candidate Skill sets and Work Experience should tightly adhere with Skill sets, expertise required for the job
                     **Calculate Years of Experience only from **Duration** fields under each **Company** 
                        
                     Candidate should be flagged as Reject if above Criteria is not met.
                     
                     ## Job Description
                     {job_description}
                     
                     ## Candidate Resume:
                     {resume}
                     
                     Provide:
                     1. Match Score (0-100)
                     2. Top 3 strengths
                     3. Red Flags (if any)
                     4. Verdict: Strong Fit/Weak Fit/Reject
                     """
            return {
                    "resume_id": application_id,
                    "resume_summary": resume,
                    "score": score,
                    "feedback": gemini_model.generate_content(prompt).text
                }
        with ThreadPoolExecutor(max_workers=5) as executor:
            futures = [
                executor.submit(process_resume, application_id, resume, score)
                for application_id, resume, score in filtered_resumes
            ]
            for future in as_completed(futures):
                final_resumes.append(future.result())
        return final_resumes


    def resume_selection(self, job_application_list):
        resumes = [
            """Name: Soumik Nath
    Skillsets: Java, Spring Boot, Angular, Microservices, Kafka, Jenkins, Docker, SQL, GraphQL, Git, REST APIs, JIRA, Maven
    Years of Experience: 8+
    
    Work Experience:
    Company: Barclays
    Duration: May 2022 – Present
      Project: Payment Restful Service (PRS)
      Role: Senior FSE - Payment Merchant Services
      Responsibilities: Developed secure and merchant-ready APIs using Spring Boot, updated logging, ensured JUnit coverage, handled deployment pipelines.
    
    Company: Optum (UnitedHealthGroup)
    Duration: Mar 2021 – May 2022
      Project: PayPageST
      Role: Senior Software Engineer
      Responsibilities: Customized merchant payment pages, fixed bugs, enhanced accessibility testing, and resolved OWASP/Veracode issues.""",

            """Sarah Lee
            Frontend Engineer at Delta Corp
            2019 - 2024
            Built dynamic UI components in React. Worked on improving performance and accessibility.""",

            """Name: Ajay K
    Skillsets: React, HTML/CSS, Angular, Bootstrap
    Years of Experience: 8
    
    Work Experience:
    Company: Paytm
    Duration: May 2025 – Present
      Project: ICP
      Role: Software Engineer
      Responsibilities: Built scalable interactive UI components. Handled UI migration from Javascript to React based systems""",
            """Name: PRIYANKA BANERJEE
    Skillsets: CORE JAVA 8, SPRING BOOT, MICROSERVICES, HIBERNATE, DATA STRUCTURES & ALGORITHMS, SQL, ANGULAR 8, BOOTSTRAP, DOCKER, KUBERNETES, GCP, AZURE(AZ-900)
    Years of Experience: 4      
            Work Experience:
    Company: Lloyds Technology Centre (June 2024 - Present)
      Role: Software Developer
      Responsibilities:
        Involved in migration of on-prem confluent Kafka to GCP confluent cloud.
        Maintaining and adding new features to the backend services which serves as backend for mobile application.
    
    Company: Infosys (September 2021 — May 2024)
      Role: Senior Systems Engineer
      Project: Strategic Billing
      Responsibilities:
        Involved in end-to-end development of building the prototype for an enterprise level billing system.
      Role: Senior Systems Engineer
      Project: Mesh Migration
      Responsibilities:
        Involved in shifting deployment from on-premise servers to public cloud, where microservices are containerized and deployed in Kubernetes clust
    """
        ]

        job_decsription = """Job Description Summary   Experience : 4 - 6 years and 10 to 13 years  We are seeking a skilled and motivated Java Developer with strong experience in Cloud platforms, Kubernetes (K8s), and SQL to join our development team. The ideal candidate will be responsible for designing, developing, and deploying scalable applications in a cloud-native environment, ensuring high performance and reliability. Job Description   Key Responsibilities:  Design, develop, and maintain robust Java-based applications. Develop microservices and deploy them using Kubernetes. Work with cloud platforms (AWS, Azure, or GCP) to build scalable and secure solutions. Write efficient SQL queries and manage relational databases. Collaborate with DevOps and QA teams to ensure smooth CI/CD pipelines. Troubleshoot and resolve technical issues across environments. Participate in code reviews and contribute to best practices.  Required Skills:  Strong proficiency in Java (8 or above) and object-oriented programming. Hands-on experience with Kubernetes for container orchestration. Experience with cloud platforms such as AWS, Azure, or Google Cloud Platform. Proficiency in SQL and working with relational databases like PostgreSQL, MySQL, or Oracle. Familiarity with Spring Boot, REST APIs, and microservices architecture. Understanding of CI/CD tools and practices (e.g., Jenkins, Git, Docker). Good problem-solving skills and ability to work in an agile environment."""

        # Initializing Vertex AI
        # init_vertex_ai()

        # Load Gemini model via Vertex AI
        # model = GenerativeModel("gemini-2.0-flash")

        # Filtering resumes using SBERT
        layer1_filtered_resumes = ResumeRanking.filter_suitable_resumes(self, job_application_list['JobDescription'], job_application_list['Candidate'])

        # Re rank filtered resumes from SBERT scoring using Gemini Model API
        layer2_filtered_resumes = ResumeRanking.re_rank_resume(self, job_application_list['JobDescription'], layer1_filtered_resumes, load_gemini_model())
        final_resume_list = {resume['resume_id']:resume for resume in layer2_filtered_resumes if not (re.search(r"\*?\*?Verdict:\*?\*?\s(Reject|\*?\*?Reject\*?\*?)", resume["feedback"], flags=re.IGNORECASE))}            # for resume in layer2_filtered_resumes:

        for resume in job_application_list['Candidate']:
                # remove field resume_text since it is only used by the ML models for assessing the candidates
                resume.pop("resume_text", None)
                # set default values to fields Score, Feedback to mark the difference between selected and Status to 'Reject' for candidates filtered out by SBERT scoring
                resume['Score'] = -1
                resume['Feedback'] = 'N/A'
                resume['Status'] = 'Reject'

                # collect score and feedback data for selected candidates
                if resume['ApplicantId'] in final_resume_list:
                    resume['Score'] = final_resume_list[resume['ApplicantId']]['score']
                    resume['Feedback'] = final_resume_list[resume['ApplicantId']]['feedback']
                    resume.pop("Status", None)

                # # extract fields ApplicantId, IdentificationID, JobID, JobDescription at parent level outside "Profile"
                # resume['ApplicantId'] = resume['ApplicantId']
                # resume['IdentificationID'] = resume['IdentificationID']
                resume['JobID'] = job_application_list['JobID']
                resume['JobDescription'] = job_application_list['JobDescription']
        print(job_application_list)