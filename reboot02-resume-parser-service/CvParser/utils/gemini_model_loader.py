import os
import requests
from vertexai import init as vertexai_init
from vertexai.generative_models import GenerativeModel
from dotenv import load_dotenv
from CvParser.utils.logger import logger

load_dotenv()

def is_running_on_gcp():
    try:
        response = requests.get("http://metadata.google.internal", timeout=0.2)
        return response.status_code == 200
    except Exception:
        return False

# Auto-select mode
GEMINI_MODE = "local"
logger.info("Gemini Mode %s", GEMINI_MODE)

gemini_model = None

if GEMINI_MODE == "local":
    import google.generativeai as genai
    genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
    #gemini_model = genai.GenerativeModel("gemini-1.5-pro-002")
    gemini_model = genai.GenerativeModel("gemini-1.5-pro")

else:
    logger.info("Loading Gemini model from VertexAI")
    vertexai_init(project=os.getenv("PROJECT_ID"), location=os.getenv("REGION"))
    gemini_model = GenerativeModel("gemini-2.5-flash")
    logger.info("Loaded Gemini model from VertexAI")
