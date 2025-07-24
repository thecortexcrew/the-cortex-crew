from dotenv import load_dotenv
import os

load_dotenv()

PROJECT_ID = os.getenv("PROJECT_ID")
PROJECT_REGION = os.getenv("PROJECT_REGION")
ASSESSOR_ENDPOINT_ID = os.getenv("ASSESSOR_ENDPOINT_ID")
PARSER_ENDPOINT_ID = os.getenv("PARSER_ENDPOINT_ID")
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # points to project root
MODEL_DATA_PATH = os.path.join(BASE_DIR, "app", "uploads")
