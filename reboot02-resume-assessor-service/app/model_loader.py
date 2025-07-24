import sys

from huggingface_hub import login

from app.config import MODEL_DATA_PATH, HUGGING_FACE_TOKEN, PROJECT_ID, PROJECT_REGION, GEMINI_API_KEY
from app.service.vertex_ai_init import init_vertex_ai
from app.logger import logger

_sbertModel = None
_geminiModel = None

# Singleton SBERT pretrained model
def load_sbert_model():
    global _sbertModel
    if _sbertModel is None:
        login(token=HUGGING_FACE_TOKEN)
        from sentence_transformers import SentenceTransformer
        # logger.info("SBERT Training file path: %s", MODEL_DATA_PATH)
        _sbertModel = SentenceTransformer('soumik060893/SBERTResumeTrained')
        # _sbertModel = SentenceTransformer('intfloat/e5-large-v2')
        # _sbertModel = SentenceTransformer(MODEL_DATA_PATH)
        logger.info("SBERT model loaded %s", _sbertModel)
    return _sbertModel

# Singleton Gemini model based on profile
def load_gemini_model(profile = "local"):
    global _geminiModel
    if _geminiModel is None:
        if profile == "vertexai":
            logger.info("Profile loaded for Gemini: %s", profile)
            from vertexai.preview.generative_models import GenerativeModel
            import vertexai

            init_vertex_ai()
            try:
              _geminiModel = GenerativeModel("gemini-2.5-flash")
              logger.info("Gemini model loaded %s", _geminiModel)
            except Exception as e:
                logger.info("Failed to load Gemini model: %s", e)
        elif profile == "local":
            import google.generativeai as genai
            genai.configure(api_key=GEMINI_API_KEY)
            _geminiModel = genai.GenerativeModel("gemini-1.5-pro")
        else:
            print("Unknown profile")
            sys.exit(1)
    return _geminiModel