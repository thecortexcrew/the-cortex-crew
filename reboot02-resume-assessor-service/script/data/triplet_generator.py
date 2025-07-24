import pandas as pd
import random
from faker import Faker
from datetime import datetime

fake = Faker()

def random_year_range():
    start_year = random.randint(2012, 2020)
    end_year = random.randint(start_year + 2, 2024)
    return f"{start_year} - {end_year}"

def generate_java_profile_one_cloud_triplets(n):
    clouds = ["AWS", "Azure", "GCP", "Cloud"]
    triplets = []

    for _ in range(n):
        cloud = random.choice(clouds)
        jd = f"Looking for a Java backend developer with experience in Spring Boot and {cloud}."

        name = fake.name()
        company = fake.company()
        years = random_year_range()
        resume_pos = (
            f"{name}\n"
            f"Java Backend Developer at {company}\n"
            f"{years}\n"
            f"Developed scalable systems using Java, Spring Boot, REST APIs, and {cloud}. "
            f"Led migration projects involving microservices and {cloud}."
        )

        name = fake.name()
        company = fake.company()
        years = random_year_range()
        resume_neg = (
            f"{name}\n"
            f"Frontend Developer at {company}\n"
            f"{years}\n"
            f"Specialized in React, Redux, and UI design. No experience in Java or {cloud}."
        )

        triplets.append((jd, resume_pos, resume_neg))
    return triplets

def generate_java_profile_two_cloud_triplets(n):
    clouds = ["AWS", "Azure", "GCP", "Cloud"]
    triplets = []

    for _ in range(n):
        cloud = random.choice(clouds)
        jd = f"Looking for a Java backend developer with experience in Spring Boot and {cloud}."

        name = fake.name()
        company = fake.company()
        years = random_year_range()
        resume_pos = (
            f"{name}\n"
            f"Java Backend Developer at {company}\n"
            f"{years}\n"
            f"Developed scalable systems using Java, Spring Boot, REST APIs, and {cloud}. "
            f"Led migration projects involving microservices and {cloud}."
        )

        name = fake.name()
        company = fake.company()
        years = random_year_range()
        resume_neg = (
            f"{name}\n"
            f"Frontend Developer at {company}\n"
            f"{years}\n"
            f"Specialized in React, Redux, and UI design. No experience in Java or {cloud}."
        )

        triplets.append((jd, resume_pos, resume_neg))
    return triplets

def generate_general_triplets(n):
    roles = ["React Developer", "Python Engineer", "DevOps Engineer", "Data Analyst"]
    skills = {
        "React Developer": "React, Redux, TypeScript, HTML/CSS",
        "Python Engineer": "Python, Flask, Django, REST APIs",
        "DevOps Engineer": "Docker, Kubernetes, Jenkins, Linux",
        "Data Analyst": "SQL, Pandas, PowerBI, Excel"
    }

    triplets = []
    for _ in range(n):
        role = random.choice(roles)
        jd = f"Hiring a {role} with expertise in {skills[role]}."

        name = fake.name()
        company = fake.company()
        years = random_year_range()
        resume_pos = (
            f"{name}\n"
            f"{role} at {company}\n"
            f"{years}\n"
            f"Worked extensively with {skills[role]}. Led successful delivery of production-grade projects."
        )

        neg_role = random.choice([r for r in roles if r != role])
        name = fake.name()
        company = fake.company()
        years = random_year_range()
        resume_neg = (
            f"{name}\n"
            f"{neg_role} at {company}\n"
            f"{years}\n"
            f"Worked with {skills[neg_role]}. Limited or no exposure to {skills[role]}."
        )

        triplets.append((jd, resume_pos, resume_neg))
    return triplets

def create_and_save_dataset(filename="triplet_resume_dataset_5k.csv", java_cloud_n=2000, general_n=3000):
    java_cloud = generate_java_profile_one_cloud_triplets(java_cloud_n)
    general = generate_general_triplets(general_n)

    all_data = java_cloud + general
    random.shuffle(all_data)

    df = pd.DataFrame(all_data, columns=["job_description", "resume_positive", "resume_negative"])
    df.to_csv(filename, index=False)
    print(f"✅ Saved {len(df)} records to '{filename}'")

# Run the script
if __name__ == "__main__":
    create_and_save_dataset()
