from fpdf import FPDF
import random
import os

# Sample data for random generation
names = ["John Doe", "Priyanka Banerjee", "Rahul Sharma", "Emily Carter", "Arjun Mehta"]
degrees = ["B.Tech in Computer Science", "MBA in Marketing", "M.Sc in Data Science", "B.Com", "B.A. in Economics"]
universities = ["IIT Delhi", "Stanford University", "Harvard University", "Delhi University", "IIM Ahmedabad"]
companies = ["Google", "Microsoft", "Amazon", "TCS", "Infosys", "Accenture"]
skills_list = ["Python, Java, SQL", "Marketing, SEO, Google Ads", "Data Analysis, Machine Learning", "Accounting, Taxation", "Public Speaking, Writing"]

def generate_resume_pdf(file_name, name, degree, university, company, skills, years_exp):
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

    pdf.ln(5)
    pdf.set_font("Arial", 'B', 14)
    pdf.cell(0, 10, "Education", ln=True)
    pdf.set_font("Arial", '', 12)
    pdf.multi_cell(0, 10, f"{degree}\n{university}\n2015 - 2019")

    pdf.ln(3)
    pdf.set_font("Arial", 'B', 14)
    pdf.cell(0, 10, "Work Experience", ln=True)
    pdf.set_font("Arial", '', 12)
    pdf.multi_cell(0, 10, f"{company}\nRole: Software Engineer\nDuration: {years_exp} years\n"
                          f"Responsibilities: Developed scalable applications and worked with cross-functional teams.")

    pdf.ln(3)
    pdf.set_font("Arial", 'B', 14)
    pdf.cell(0, 10, "Skills", ln=True)
    pdf.set_font("Arial", '', 12)
    pdf.multi_cell(0, 10, skills)

    pdf.ln(3)
    pdf.set_font("Arial", 'B', 14)
    pdf.cell(0, 10, "Projects", ln=True)
    pdf.set_font("Arial", '', 12)
    pdf.multi_cell(0, 10, "Project Name: Resume Parser\nRole: Developer\nResponsibilities: Built an AI-based resume parsing system.")

    pdf.output(file_name)

def generate_multiple_resumes(output_folder="sample_resumes", count=5):
    os.makedirs(output_folder, exist_ok=True)
    for i in range(count):
        name = random.choice(names)
        degree = random.choice(degrees)
        university = random.choice(universities)
        company = random.choice(companies)
        skills = random.choice(skills_list)
        years_exp = round(random.uniform(1, 10), 1)

        file_name = os.path.join(output_folder, f"{name.replace(' ', '_')}_{i+1}.pdf")
        generate_resume_pdf(file_name, name, degree, university, company, skills, years_exp)
        print(f"Generated: {file_name}")

if __name__ == "__main__":
    generate_multiple_resumes(count=5)
