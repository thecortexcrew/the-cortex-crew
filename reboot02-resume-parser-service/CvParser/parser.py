from CvParser.utils.gemini_parser import parse_with_gemini_safely
from CvParser.utils.local_parser import parse_locally

def parse_cv_text(cv_text):
    try:
        result = parse_with_gemini_safely(cv_text)
        if "error" in result:
            print("⚠️ Gemini failed, using local parser.")
            return parse_locally(cv_text)
        return result
    except Exception as e:
        print("❌ Error in parse_cv_text:", str(e))
        return parse_locally(cv_text)