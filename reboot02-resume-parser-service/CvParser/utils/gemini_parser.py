import json
import re
from CvParser.utils.gemini_model_loader import gemini_model, GEMINI_MODE
from threading import Semaphore

# Limit concurrent Gemini calls to 3
GEMINI_LIMIT = 3
gemini_semaphore = Semaphore(GEMINI_LIMIT)

def parse_with_gemini_safely(resume_text):
    with gemini_semaphore:
        return parse_with_gemini(resume_text)


def parse_with_gemini(resume_text):

    prompt = f"""
You are a resume parser. Extract structured information from the resume text below.

⚠️ STRICTLY follow this JSON format (do NOT add any text before or after but please calculate YearsOfExp based on duration of different companies worked also give DateOfBirth in format YYYY-MM-DD):

{{
  "ApplicantId": "",
  "IdentificationID": "",
  "Profile": {{
    "Name": "",
    "DateOfApplication": "",
    "Gender": "",
    "DateOfBirth": "",
    "MobileNo": "",
    "EmailId": "",
    "SkillSets": "",
    "YearsOfExp": "",
    "Education": [
      {{
        "Degree": "",
        "University": "",
        "Duration": "",
        "Ongoing": false
      }}
    ],
    "WorkExp": [
      {{
        "Company": "",
        "Duration": "",
        "Project": [
          {{
            "Name": "",
            "Role": "",
            "Responsibilities": ""
          }}
        ]
      }}
    ]
  }}
}}

Resume:
\"\"\"
{resume_text}
\"\"\"
"""

    try:
        if GEMINI_MODE == "local":
            response = gemini_model.generate_content(prompt)
            result_text = response.text.strip()
        else:
            response = gemini_model.generate_content([prompt])
            result_text = response.candidates[0].content.parts[0].text.strip()

        # Extract JSON part only (if Gemini adds extra text)
        json_match = re.search(r'\{.*\}', result_text, re.DOTALL)
        if not json_match:
            return {
                "error": "Gemini response did not contain valid JSON.",
                "raw_output": result_text
            }

        json_str = json_match.group()
        return json.loads(json_str)

    except json.JSONDecodeError as je:
        return {
            "error": "Failed to parse Gemini response as JSON.",
            "details": str(je),
            "raw_output": result_text
        }

    except Exception as e:
        return {
            "error": f"Gemini exception: {str(e)}"
        }
