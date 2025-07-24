import json
import time
import random
import string
from datetime import datetime, timedelta

# ----------- ID Generators -----------

def generate_application_id():
    date_part = datetime.today().strftime("%Y%m%d")
    millis = str(int(time.time() * 1000))[-6:]
    rand = ''.join(random.choices(string.ascii_uppercase + string.digits, k=3))
    return f"APP{date_part}-{millis}{rand}"

def generate_identification_id():
    date_part = datetime.today().strftime("%Y%m%d")
    millis = str(int(time.time() * 1000))[-6:]
    rand = ''.join(random.choices(string.ascii_uppercase + string.digits, k=3))
    return f"ID{date_part}-{millis}{rand}"

# ----------- Profile Generator -----------

def get_sample_profile(i):
    return {
        "Name": f"Candidate {i}",
        "Email": f"candidate{i}@example.com",
        "Phone": f"+91-90000000{i:02d}",
        "Skills": ["Java", "Spring", "Microservices", "Cloud"],
        "Experience": [
            {"Company": "Company A", "Title": "Developer", "Years": 2},
            {"Company": "Company B", "Title": "Senior Developer", "Years": 3}
        ],
        "Education": [
            {"Degree": "B.Tech", "Major": "CS", "Year": 2017, "Institute": "Tech University"}
        ],
        "Certifications": ["Certified Java Developer"],
        "Projects": [f"Project {i} for enterprise platform"]
    }

# ----------- SQL Generator -----------

def generate_insert_statements(count=10, job_id="JOB001"):
    base_ts = datetime(2025, 7, 13, 23, 58, 40, 900000)
    sql_lines = []
    used_offsets = set()

    for i in range(count):
        applicant_id = generate_application_id()
        identification_id = generate_identification_id()

        profile = get_sample_profile(i)
        profile_json = json.dumps(profile).replace("'", "''")

        # High-precision score string
        score_value = round(random.uniform(0.7, 0.99), 17)
        score = f"{score_value:.17f}"
        feedback = f"Feedback for candidate {i}"

        # Random time offset in nanoseconds (spread across ~10 seconds)
        while True:
            rand_nanos = random.randint(0, 10_000_000_000)  # up to 10 seconds in nanos
            if rand_nanos not in used_offsets:
                used_offsets.add(rand_nanos)
                break
        created_at = (base_ts + timedelta(microseconds=rand_nanos // 1000)).strftime('%Y-%m-%dT%H:%M:%S.') + f"{rand_nanos % 1_000_000_000:09d}"

        stmt = f"""INSERT INTO Candidate(ApplicantId, IdentificationID, JobID, Profile, Score, Feedback, CreatedAt, Status)
VALUES ('{applicant_id}', '{identification_id}', '{job_id}', JSON'{profile_json}', '{score}', '{feedback}', '{created_at}', 'L0');"""

        sql_lines.append(stmt)

    return "\n\n".join(sql_lines)

# ----------- Main Execution -----------

if __name__ == "__main__":
    sql_script = generate_insert_statements(count=20, job_id="JOB001")

    with open("insert_candidates_generated.sql", "w") as file:
        file.write(sql_script)

    print("✅ SQL insert script generated: insert_candidates_generated.sql")
