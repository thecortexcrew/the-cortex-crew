from fpdf import FPDF
import random
import os

# ------------ SAMPLE DATA ------------

names = [
    "John Doe", "Priyanka Banerjee", "Rahul Sharma", "Emily Carter",
    "Arjun Mehta", "Sophia Johnson", "Rajesh Kumar", "Olivia Brown"
]
degrees = [
    "B.Tech in Computer Science", "MBA in Marketing", "M.Sc in Data Science",
    "B.Com", "B.A. in Economics", "PhD in Artificial Intelligence"
]
universities = [
    "IIT Delhi", "Stanford University", "Harvard University",
    "Delhi University", "IIM Ahmedabad", "MIT"
]
companies = [
    "Google", "Microsoft", "Amazon", "TCS", "Infosys", "Accenture",
    "Adobe", "Flipkart", "Meta", "Tesla"
]
skills_list = [
    "Python, Java, SQL, Docker, Kubernetes",
    "Marketing, SEO, Google Ads, HubSpot",
    "Data Analysis, Machine Learning, TensorFlow, PyTorch",
    "Accounting, Taxation, Financial Modeling",
    "Public Speaking, Writing, Leadership"
]
project_templates = [
    ("AI Chatbot", "AI Developer",
     "Developed an AI-based conversational chatbot using NLP and deployed it on cloud."),
    ("E-commerce Platform", "Backend Developer",
     "Designed and implemented REST APIs, improved response time by 30%."),
    ("Resume Parser", "Data Scientist",
     "Built ML models to parse unstructured resumes into structured JSON format."),
    ("Marketing Automation Tool", "Marketing Analyst",
     "Automated campaign performance analysis, increasing ROI by 25%.")
]

# ------------ RESUME GENERATION ------------

def generate_large_resume_pdf(file_name, name, degree, university, work_entries=10, project_entries=20):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()

    # Title
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(0, 10, f"Resume - {name}", ln=True, align="C")

    pdf.set_font("Arial", '', 12)
    pdf.ln(5)

    # Contact Info
    pdf.cell(0, 10, f"Email: {name.lower().replace(' ', '.')}@example.com", ln=True)
    pdf.cell(0, 10, f"Mobile: +91-{random.randint(7000000000, 9999999999)}", ln=True)

    # Education Section
    pdf.ln(5)
    pdf.set_font("Arial", 'B', 14)
    pdf.cell(0, 10, "Education", ln=True)
    pdf.set_font("Arial", '', 12)
    for _ in range(random.randint(1, 3)):
        pdf.multi_cell(0, 10, f"{random.choice(degrees)}\n{random.choice(universities)}\n2012 - 2016")
        pdf.ln(2)

    # Work Experience Section (Multiple Companies)
    pdf.ln(3)
    pdf.set_font("Arial", 'B', 14)
    pdf.cell(0, 10, "Work Experience", ln=True)
    pdf.set_font("Arial", '', 12)
    for _ in range(work_entries):
        company = random.choice(companies)
        years_exp = round(random.uniform(0.5, 5), 1)
        pdf.multi_cell(0, 10,
            f"{company}\nRole: Software Engineer\nDuration: {years_exp} years\n"
            f"Responsibilities: Developed and optimized systems, collaborated with cross-functional teams.")
        pdf.ln(2)

    # Skills Section
    pdf.ln(3)
    pdf.set_font("Arial", 'B', 14)
    pdf.cell(0, 10, "Skills", ln=True)
    pdf.set_font("Arial", '', 12)
    pdf.multi_cell(0, 10, random.choice(skills_list))

    # Projects Section (Lots of Projects to Extend Pages)
    pdf.ln(3)
    pdf.set_font("Arial", 'B', 14)
    pdf.cell(0, 10, "Projects", ln=True)
    pdf.set_font("Arial", '', 12)
    for _ in range(project_entries):
        project_name, role, resp = random.choice(project_templates)
        pdf.multi_cell(0, 10, f"Project Name: {project_name}\nRole: {role}\nResponsibilities: {resp}")
        pdf.ln(2)

    pdf.output(file_name)

def generate_bulk_resumes(output_folder="large_sample_resumes", count=5, long_resume=True):
    os.makedirs(output_folder, exist_ok=True)
    for i in range(count):
        name = random.choice(names)
        degree = random.choice(degrees)
        university = random.choice(universities)

        # Generate long or normal resume
        if long_resume:
            work_entries = random.randint(8, 12)  # multiple companies
            project_entries = random.randint(25, 40)  # multiple projects → 6-7 pages
        else:
            work_entries = random.randint(2, 5)
            project_entries = random.randint(5, 10)

        file_name = os.path.join(output_folder, f"{name.replace(' ', '_')}_{i+1}.pdf")
        generate_large_resume_pdf(file_name, name, degree, university, work_entries, project_entries)
        print(f"Generated: {file_name}")

if __name__ == "__main__":
    # Example: Generate 10 long resumes for stress-testing
    generate_bulk_resumes(count=10, long_resume=True)
