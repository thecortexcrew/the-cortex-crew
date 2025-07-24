from dotenv import load_dotenv
import os

load_dotenv()

GEMINI_API_KEY = os.getenv("GOOGLE_API_KEY")
HUGGING_FACE_TOKEN = os.getenv("HUGGING_FACE_TOKEN")
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # points to project root
MODEL_DATA_PATH = os.path.join(BASE_DIR, "app", "model", "output_new_one")
PROJECT_ID = os.getenv("GCP_PROJECT_ID")
PROJECT_REGION = os.getenv("GCP_REGION")
# PROFILE = os.getenv("PROFILE")