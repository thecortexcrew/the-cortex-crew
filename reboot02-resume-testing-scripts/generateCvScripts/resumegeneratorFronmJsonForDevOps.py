import json
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.pdfgen import canvas
from reportlab.pdfbase.pdfmetrics import stringWidth

def draw_skill_bar(c, x, y, skill, level, max_width=120):
    """Draws a skill bar with percentage level."""
    c.setFillColor(colors.lightgrey)
    c.rect(x, y, max_width, 8, fill=True, stroke=0)
    c.setFillColor(colors.HexColor("#003366"))
    c.rect(x, y, max_width * (level / 100.0), 8, fill=True, stroke=0)
    c.setFillColor(colors.black)
    c.setFont("Helvetica", 8)
    c.drawString(x, y + 10, skill)

def draw_wrapped_text(c, text, x, y, max_width, font="Helvetica", size=8, line_height=10):
    """Draws wrapped text within a specific max width."""
    c.setFont(font, size)
    words = text.split(" ")
    line = ""
    for word in words:
        test_line = f"{line} {word}".strip()
        if stringWidth(test_line, font, size) < max_width:
            line = test_line
        else:
            c.drawString(x, y, line)
            y -= line_height
            line = word
    if line:
        c.drawString(x, y, line)
        y -= line_height
    return y

def parse_json_to_data(json_data):
    profile = json_data["Profile"]

    # === Skill Categorization ===
    skills_list = [s.strip() for s in profile["SkillSets"].replace("TOOLS :", ",").split(",") if s.strip()]

    devops_keywords = [
        "DEVOPS", "CI/CD", "INFRASTRUCTURE", "KUBERNETES", "DOCKER", "TERRAFORM",
        "CLOUDFORMATION", "AWS", "AZURE", "GCP", "PROMETHEUS", "GRAFANA", "ANSIBLE",
        "GITOPS", "HELM", "SERVICE MESH", "ISTIO", "SECURITY", "CLOUD", "COST OPTIMIZATION"
    ]

    architectural_skills = []
    technical_skills = []

    for skill in skills_list:
        if any(keyword in skill.upper() for keyword in devops_keywords):
            architectural_skills.append({"name": skill, "level": 80})
        else:
            technical_skills.append({"name": skill, "level": 70})

    # === Education ===
    education = [f"{e['Degree']} – {e['University']} ({e['Duration']})" for e in profile["Education"]]

    # === Work Experience ===
    experience = []
    for w in profile["WorkExp"]:
        for p in w["Project"]:
            details = [line.strip() for line in p["Responsibilities"].split("\n") if line.strip()]
            experience.append({
                "role": p["Role"],
                "company": w["Company"],
                "duration": w["Duration"],
                "details": details
            })

    return {
        "name": profile["Name"].title(),
        "title": f"DevOps Engineer | {profile['YearsOfExp']} years experience",
        "contact": {
            "phone": profile["MobileNo"],
            "email": profile["EmailId"],
            "location": "India"
        },
        "photo": None,  # You can pass a file path if you want to add a photo
        "summary": (f"Experienced DevOps engineer with {profile['YearsOfExp']} years "
                    f"of expertise in CI/CD, cloud infrastructure automation, and containerized workloads. "
                    f"Strong background in optimizing deployment pipelines, monitoring, and cost-efficient cloud operations."),
        "architectural_skills": architectural_skills[:6],   # Show top 6 DevOps-related skills
        "technical_skills": technical_skills[:8],           # Show top 8 other technical skills
        "experience": experience,
        "education": education
    }

def generate_creative_resume(data, output_file):
    c = canvas.Canvas(output_file, pagesize=A4)
    width, height = A4

    # === Left Column Background ===
    c.setFillColor(colors.HexColor("#E6EEF5"))
    c.rect(0, 0, 180, height, fill=True, stroke=0)

    # === Name & Title ===
    c.setFillColor(colors.HexColor("#003366"))
    c.setFont("Helvetica-Bold", 18)
    c.drawString(200, height - 60, data['name'])
    c.setFont("Helvetica", 12)
    c.setFillColor(colors.black)
    c.drawString(200, height - 80, data['title'])

    # === Contact Info ===
    c.setFont("Helvetica-Bold", 10)
    c.drawString(20, height - 150, "CONTACT")
    y_pos = height - 165
    for line in [data['contact']['phone'], data['contact']['email'], data['contact']['location']]:
        y_pos = draw_wrapped_text(c, line, 20, y_pos, max_width=150)

    # === Architectural (DevOps) Skills ===
    c.setFont("Helvetica-Bold", 10)
    c.drawString(20, y_pos - 15, "ARCHITECTURAL SKILLS")
    y_pos -= 35
    for s in data['architectural_skills']:
        draw_skill_bar(c, 20, y_pos, s['name'], s['level'])
        y_pos -= 25

    # === Technical Skills ===
    c.setFont("Helvetica-Bold", 10)
    c.drawString(20, y_pos - 1, "TECHNICAL SKILLS")
    y_pos -= 20
    for s in data['technical_skills']:
        draw_skill_bar(c, 20, y_pos, s['name'], s['level'])
        y_pos -= 25

    # === Education ===
    c.setFont("Helvetica-Bold", 10)
    c.drawString(20, y_pos - 5, "EDUCATION")
    y_pos -= 20
    for edu in data['education']:
        y_pos = draw_wrapped_text(c, f"• {edu}", 20, y_pos, max_width=150)

    # === Professional Summary ===
    text_y = height - 120
    c.setFont("Helvetica-Bold", 12)
    c.setFillColor(colors.HexColor("#003366"))
    c.drawString(200, text_y, "PROFESSIONAL SUMMARY")
    text_y -= 15
    c.setFont("Helvetica", 9)
    c.setFillColor(colors.black)
    text_y = draw_wrapped_text(c, data['summary'], 200, text_y, max_width=360, line_height=12)

    # === Experience ===
    text_y -= 10
    c.setFont("Helvetica-Bold", 12)
    c.setFillColor(colors.HexColor("#003366"))
    c.drawString(200, text_y, "EXPERIENCE")
    text_y -= 20
    c.setFillColor(colors.black)

    for exp in data['experience']:
        c.setFont("Helvetica-Bold", 10)
        text_y = draw_wrapped_text(c, f"{exp['role']} - {exp['company']} ({exp['duration']})",
                                   200, text_y, max_width=360, font="Helvetica-Bold", size=10)
        c.setFont("Helvetica", 8)
        for d in exp['details']:
            text_y = draw_wrapped_text(c, f"• {d}", 210, text_y, max_width=350, font="Helvetica", size=8)
        text_y -= 5

    c.save()
    print(f"✅ Resume generated: {output_file}")

# === Load JSON and Generate Resume ===
with open("/Users/priyankapc/PycharmProjects/TestScript/jsons/devOpsArchitectLevel.json", "r") as f:  # replace with your JSON file
    json_data = json.load(f)

data = parse_json_to_data(json_data)
generate_creative_resume(data, f"{data['name'].replace(' ', '_')}_Architect_DevOps_CV.pdf")
