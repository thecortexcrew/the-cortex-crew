from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.pdfbase.pdfmetrics import stringWidth

def draw_skill_bar(c, x, y, skill, level, max_width=120):
    """Draws a skill bar (0 to 100%)"""
    c.setFillColor(colors.lightgrey)
    c.rect(x, y, max_width, 8, fill=True, stroke=0)
    c.setFillColor(colors.HexColor("#003366"))
    c.rect(x, y, max_width * (level / 100.0), 8, fill=True, stroke=0)
    c.setFillColor(colors.black)
    c.setFont("Helvetica", 8)
    c.drawString(x, y + 10, skill)

def draw_wrapped_text(c, text, x, y, max_width, font="Helvetica", size=8, line_height=10):
    """Automatically wraps text within a given width"""
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

def generate_creative_resume(data, output_file):
    c = canvas.Canvas(output_file, pagesize=A4)
    width, height = A4

    # === Left Column Background ===
    c.setFillColor(colors.HexColor("#E6EEF5"))
    c.rect(0, 0, 180, height, fill=True, stroke=0)

    # === PHOTO (optional) ===
    if data.get("photo"):
        c.drawImage(data["photo"], 40, height - 120, width=100, height=100, mask='auto')

    # === NAME & TITLE ===
    c.setFillColor(colors.HexColor("#003366"))
    c.setFont("Helvetica-Bold", 18)
    c.drawString(200, height - 60, data['name'])
    c.setFont("Helvetica", 12)
    c.setFillColor(colors.black)
    c.drawString(200, height - 80, data['title'])

    # === CONTACT INFO (Left Column) ===
    c.setFont("Helvetica-Bold", 10)
    c.drawString(20, height - 150, "CONTACT")
    y_pos = height - 165
    for line in [data['contact']['phone'], data['contact']['email'], data['contact']['location']]:
        y_pos = draw_wrapped_text(c, line, 20, y_pos, max_width=150)

    # === ARCHITECTURAL SKILLS (Skill Bars) ===
    c.setFont("Helvetica-Bold", 10)
    c.drawString(20, y_pos - 15, "ARCHITECTURAL SKILLS")
    y_pos -= 35
    for s in data['architectural_skills']:
        draw_skill_bar(c, 20, y_pos, s['name'], s['level'])
        y_pos -= 25

    # === TECHNICAL SKILLS ===
    c.setFont("Helvetica-Bold", 10)
    c.drawString(20, y_pos - 5, "TECHNICAL SKILLS")
    y_pos -= 20
    for s in data['technical_skills']:
        draw_skill_bar(c, 20, y_pos, s['name'], s['level'])
        y_pos -= 25

    # === EDUCATION (Auto-Wrapped) ===
    c.setFont("Helvetica-Bold", 10)
    c.drawString(20, y_pos - 5, "EDUCATION")
    y_pos -= 20
    c.setFont("Helvetica", 8)
    for edu in data['education']:
        y_pos = draw_wrapped_text(c, f"• {edu}", 20, y_pos, max_width=150)

    # === PROFESSIONAL SUMMARY (Right Column, wrapped) ===
    text_y = height - 120
    c.setFont("Helvetica-Bold", 12)
    c.setFillColor(colors.HexColor("#003366"))
    c.drawString(200, text_y, "PROFESSIONAL SUMMARY")
    text_y -= 15
    c.setFont("Helvetica", 9)
    c.setFillColor(colors.black)
    text_y = draw_wrapped_text(c, data['summary'], 200, text_y, max_width=360, font="Helvetica", size=9, line_height=12)

    # === EXPERIENCE (Timeline Style, wrapped) ===
    text_y -= 10
    c.setFont("Helvetica-Bold", 12)
    c.setFillColor(colors.HexColor("#003366"))
    c.drawString(200, text_y, "EXPERIENCE")
    text_y -= 20
    c.setFillColor(colors.black)

    for exp in data['experience']:
        c.setFont("Helvetica-Bold", 10)
        text_y = draw_wrapped_text(c, f"{exp['role']} - {exp['company']} ({exp['duration']})",
                                   200, text_y, max_width=360, font="Helvetica-Bold", size=10, line_height=12)
        c.setFont("Helvetica", 8)
        for d in exp['details']:
            text_y = draw_wrapped_text(c, f"• {d}", 210, text_y, max_width=350, font="Helvetica", size=8, line_height=10)
        text_y -= 5

    c.save()
    print(f"✅ Creative resume saved: {output_file}")

# ==== SAMPLE DATA ====
data = {
    "name": "Priyanka Banerjee",
    "title": "Java Developer | Software & Cloud Architecture",
    "contact": {
        "phone": "+91 8910983449",
        "email": "priyankabanerjee206@gmail.com",
        "location": "Kolkata, India 700057"
    },
    "photo": None,  # Replace with "photo.jpg" if you want to include a photo
    "summary": ("Java and cloud professional with strong expertise in system design, "
                "microservices architecture, and cloud migration. Experienced in "
                "scalable enterprise applications and optimizing backend services."),
    "architectural_skills": [
        {"name": "System Design", "level": 90},
        {"name": "Microservices Architecture", "level": 85},
        {"name": "Cloud Migration", "level": 80},
        {"name": "CI/CD Pipeline Design", "level": 75}
    ],
    "technical_skills": [
        {"name": "Core Java 8", "level": 95},
        {"name": "Spring Boot", "level": 90},
        {"name": "Hibernate", "level": 80},
        {"name": "Kubernetes", "level": 75},
        {"name": "GCP", "level": 70}
    ],
    "experience": [
        {
            "role": "Software Developer",
            "company": "Lloyds Technology Centre",
            "duration": "June 2024 – Present",
            "details": [
                "Designed and migrated Confluent Kafka from on-prem to GCP.",
                "Enhanced backend services architecture for mobile apps."
            ]
        },
        {
            "role": "Senior Systems Engineer",
            "company": "Infosys",
            "duration": "Sept 2021 – May 2024",
            "details": [
                "Migrated WestPac core banking apps to cloud using Kubernetes.",
                "Redesigned account dashboard microservice with Spring Boot."
            ]
        }
    ],
    "education": [
        "B.Tech – Camellia Institute Of Technology (2018 – 2021)",
        "Diploma – Women’s Polytechnic Jodhpur Park (2014 – 2017)"
    ]
}

# === Generate Resume ===
generate_creative_resume(data, "Priyanka_Banerjee_Creative_CV.pdf")
