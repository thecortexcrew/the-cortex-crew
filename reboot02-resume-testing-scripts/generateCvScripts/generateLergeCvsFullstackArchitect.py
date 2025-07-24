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
    """Parses the given JSON into a structured format for the resume."""
    profile = json_data["Profile"]

    # ✅ FIX: Handle SkillSets as list or string
    if isinstance(profile["SkillSets"], list):
        skills_list = [s.strip() for s in profile["SkillSets"] if s.strip()]
    else:
        skills_list = [s.strip() for s in profile["SkillSets"].replace("TOOLS :", ",").split(",") if s.strip()]

    architect_keywords = ["ARCHITECTURE", "SYSTEM DESIGN", "MICROSERVICES", "GRAPHQL", "SCALABILITY"]
    frontend_keywords = ["ANGULAR", "REACT", "JAVASCRIPT", "HTML", "CSS", "BOOTSTRAP"]
    devops_keywords = ["DEVOPS", "KUBERNETES", "DOCKER", "TERRAFORM", "AWS", "AZURE", "GCP"]

    architectural_skills, frontend_skills, technical_skills = [], [], []
    for skill in skills_list:
        s_upper = skill.upper()
        if any(k in s_upper for k in architect_keywords):
            architectural_skills.append({"name": skill, "level": 85})
        elif any(k in s_upper for k in frontend_keywords):
            frontend_skills.append({"name": skill, "level": 75})
        elif any(k in s_upper for k in devops_keywords):
            architectural_skills.append({"name": skill, "level": 80})
        else:
            technical_skills.append({"name": skill, "level": 70})

    if architectural_skills and frontend_skills:
        title = f"Full-Stack Architect | {profile['YearsOfExp']} years experience"
    elif architectural_skills:
        title = f"Software Architect | {profile['YearsOfExp']} years experience"
    elif frontend_skills:
        title = f"Full-Stack Engineer | {profile['YearsOfExp']} years experience"
    else:
        title = f"Software Engineer | {profile['YearsOfExp']} years experience"

    summary = f"Experienced professional with {profile['YearsOfExp']} years of expertise in software development, scalable systems, and modern application design."

    education = [f"{e['Degree']} – {e['University']} ({e['Duration']})" for e in profile["Education"]]
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
        "title": title,
        "contact": {
            "phone": profile["MobileNo"],
            "email": profile["EmailId"],
            "location": "India"
        },
        "photo": "",  # will override later
        "architectural_skills": architectural_skills[:6],
        "frontend_skills": frontend_skills[:5],
        "technical_skills": technical_skills[:8],
        "education": education,
        "summary": summary,
        "experience": experience
    }

def draw_left_sidebar(c, data, height, show_photo=True):
    """Draws the left sidebar including background, (photo only if show_photo=True)."""
    c.setFillColor(colors.HexColor("#E6EEF5"))
    c.rect(0, 0, 180, height, fill=True, stroke=0)

    if show_photo and data.get("photo"):
        try:
            c.drawImage(data["photo"], 40, height - 130, width=100, height=100, preserveAspectRatio=True, mask='auto')
        except Exception as e:
            print(f"⚠️ Could not load photo: {e}")

    y_pos = height - (150 if show_photo else 40)
    c.setFont("Helvetica-Bold", 10)
    c.setFillColor(colors.black)
    c.drawString(20, y_pos, "CONTACT")
    y_pos -= 15
    for line in [data['contact']['phone'], data['contact']['email'], data['contact']['location']]:
        y_pos = draw_wrapped_text(c, line, 20, y_pos, max_width=150)

    if data['architectural_skills']:
        c.setFont("Helvetica-Bold", 10)
        c.drawString(20, y_pos - 5, "ARCHITECTURAL SKILLS")
        y_pos -= 25
        for s in data['architectural_skills']:
            draw_skill_bar(c, 20, y_pos, s['name'], s['level'])
            y_pos -= 25

    if data['frontend_skills']:
        c.setFont("Helvetica-Bold", 10)
        c.drawString(20, y_pos - 1, "FRONTEND SKILLS")
        y_pos -= 20
        for s in data['frontend_skills']:
            draw_skill_bar(c, 20, y_pos, s['name'], s['level'])
            y_pos -= 25

    if data['technical_skills']:
        c.setFont("Helvetica-Bold", 10)
        c.drawString(20, y_pos - 1, "TECHNICAL SKILLS")
        y_pos -= 20
        for s in data['technical_skills']:
            draw_skill_bar(c, 20, y_pos, s['name'], s['level'])
            y_pos -= 25

    if data['education']:
        c.setFont("Helvetica-Bold", 10)
        c.drawString(20, y_pos - 5, "EDUCATION")
        y_pos -= 20
        for edu in data['education']:
            y_pos = draw_wrapped_text(c, f"• {edu}", 20, y_pos, max_width=150)

def generate_creative_resume(data, output_file):
    c = canvas.Canvas(output_file, pagesize=A4)
    width, height = A4

    def new_page():
        c.showPage()
        draw_left_sidebar(c, data, height, show_photo=False)  # ✅ No photo on next pages
        return height - 120

    draw_left_sidebar(c, data, height, show_photo=True)

    # Name & Title (only on first page top)
    c.setFillColor(colors.HexColor("#003366"))
    c.setFont("Helvetica-Bold", 18)
    c.drawString(200, height - 60, data['name'])
    c.setFont("Helvetica", 12)
    c.setFillColor(colors.black)
    c.drawString(200, height - 80, data['title'])

    text_y = height - 120
    c.setFont("Helvetica-Bold", 12)
    c.setFillColor(colors.HexColor("#003366"))
    c.drawString(200, text_y, "PROFESSIONAL SUMMARY")
    text_y -= 15
    c.setFont("Helvetica", 9)
    c.setFillColor(colors.black)
    text_y = draw_wrapped_text(c, data['summary'], 200, text_y, max_width=360, line_height=12)

    text_y -= 10
    c.setFont("Helvetica-Bold", 12)
    c.setFillColor(colors.HexColor("#003366"))
    c.drawString(200, text_y, "EXPERIENCE")
    text_y -= 20
    c.setFillColor(colors.black)

    for exp in data['experience']:
        if text_y < 100:
            text_y = new_page()
        c.setFont("Helvetica-Bold", 10)
        text_y = draw_wrapped_text(c, f"{exp['role']} - {exp['company']} ({exp['duration']})",
                                   200, text_y, max_width=360, font="Helvetica-Bold", size=10)
        c.setFont("Helvetica", 8)
        for d in exp['details']:
            if text_y < 80:
                text_y = new_page()
            text_y = draw_wrapped_text(c, f"• {d}", 210, text_y, max_width=350, font="Helvetica", size=8)
        text_y -= 5

    c.save()
    print(f"✅ Resume generated: {output_file}")

# === Load JSON & Generate Resume ===
with open("/Users/priyankapc/PycharmProjects/TestScript/jsons/SoumikJson.json", "r") as f:
    json_data = json.load(f)

data = parse_json_to_data(json_data)
data["photo"] = "/Users/priyankapc/PycharmProjects/TestScript/generateCvScripts/rsz_soumik_nath_pic.jpg"

generate_creative_resume(data, f"{data['name'].replace(' ', '_')}_FullStack_Architect_CV.pdf")
