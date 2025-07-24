import re
import spacy
from datetime import datetime
from dateutil import parser as date_parser

nlp = spacy.load("en_core_web_sm")


def parse_locally(cv_text):
    profile = {
        "Profile": {
            "Name": "",
            "ApplicationID": "",
            "IdentificationID": "",
            "DateOfApplication": "",
            "Gender": "",
            "DateOfBirth": "",
            "MobileNo": "",
            "Skillsets": "",
            "YearsOfExp": "",
            "Education": [],
            "WorkExp": []
        }
    }

    doc = nlp(cv_text)
    lines = [line.strip() for line in cv_text.split("\n") if line.strip()]

    # --- Name Extraction ---
    for line in lines[:10]:
        if re.match(r"^[A-Z][a-z]+\s[A-Z][a-z]+$", line):
            profile["Profile"]["Name"] = line
            break
        for ent in nlp(line).ents:
            if ent.label_ == "PERSON" and 1 < len(ent.text.split()) <= 3:
                profile["Profile"]["Name"] = ent.text.strip()
                break
        if profile["Profile"]["Name"]:
            break

    # --- Mobile No ---
    phone = re.search(r"(\+91[-\s]?[0-9]{10})", cv_text)
    if phone:
        profile["Profile"]["MobileNo"] = phone.group()

    # --- Date of Birth ---
    dob_match = re.search(r"Date of Birth\s*[:\-]?(.*?\d{4})", cv_text, re.IGNORECASE)
    if dob_match:
        profile["Profile"]["DateOfBirth"] = dob_match.group(1).strip()

    # --- Skills ---
    skill_keywords = [
        "Java", "Python", "SQL", "Spring Boot", "Docker", "Kubernetes",
        "Microservices", "Angular", "REST API", "AWS", "GCP", "Hibernate"
    ]
    found_skills = [skill for skill in skill_keywords if re.search(rf"\\b{skill}\\b", cv_text, re.IGNORECASE)]
    profile["Profile"]["Skillsets"] = ", ".join(found_skills)

    # --- Education ---
    edu_keywords = [
        "B.Tech", "B Tech", "M.Tech", "M Tech", "B.E", "M.E", "Diploma", "Bachelor", "Master",
        "MBA", "BCA", "MCA", "PhD", "High School", "Secondary", "CBSE", "ICSE"
    ]
    profile["Profile"]["Education"] = [line for line in lines if any(kw.lower() in line.lower() for kw in edu_keywords) and len(line) > 10 and not line.isupper()]

    # --- Work Experience ---
    total_months = 0
    added_companies = set()
    experience = []
    block = ""

    for line in lines:
        if re.search(r"(Company|Experience|Organisation|Employer)", line, re.IGNORECASE):
            if block:
                experience.append(block.strip())
                block = ""
        block += line + "\n"
    if block:
        experience.append(block.strip())

    for block in experience:
        block = block.strip()
        if len(block) < 50:
            continue

        company_match = re.search(r"(?:Company|Organisation|Employer)?[:\-\s]*([A-Z][a-zA-Z&,.\s]{2,40})", block)
        duration_match = re.search(r"((Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*[\s,]*\d{4}\s*[-\u2013to]+\s*(Present|[A-Za-z]+\s*\d{4}))", block, re.IGNORECASE)
        role_match = re.search(r"(?:Role|Position)?[:\-\s]*([A-Za-z\s]{2,40})", block)
        resp_match = re.search(r"(?:Responsibilities|Work Description|Duties)[:\-\s]*(.*)", block, re.IGNORECASE)

        company = company_match.group(1).strip() if company_match else ""
        if not company or company.upper() in {"REFERENCES", "PROJECTS", "SKILLS", "EDUCATION", "ADDRESS"} or company in added_companies:
            continue
        added_companies.add(company)

        months = 0
        if duration_match:
            try:
                dates = re.split(r"[-\u2013to]+", duration_match.group(0))
                start = date_parser.parse(dates[0].strip(), fuzzy=True)
                end = datetime.today() if "present" in dates[1].lower() else date_parser.parse(dates[1].strip(), fuzzy=True)
                months = max((end.year - start.year) * 12 + (end.month - start.month), 0)
                total_months += months
            except:
                pass

        profile["Profile"]["WorkExp"].append({
            "Company": company,
            "Duration": duration_match.group(1).strip() if duration_match else "",
            "Project": [{
                "Name": "",
                "Role": role_match.group(1).strip() if role_match else "",
                "Responsibilities": resp_match.group(1).strip() if resp_match else ""
            }]
        })

    if total_months:
        profile["Profile"]["YearsOfExp"] = f"{round(total_months / 12, 1)} years"

    return profile
