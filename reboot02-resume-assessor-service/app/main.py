import argparse

from flask import Flask

from app.api.routes import api
from app.model_loader import load_sbert_model, load_gemini_model
# from app.config import PROFILE
from app.logger import logger


def create_app():
    app = Flask(__name__)
    app.register_blueprint(api)
    logger.info("Loading SBERT Model...")
    load_sbert_model()
    # parser = argparse.ArgumentParser(description="Run Gemini from selected profile.")
    # parser.add_argument("--profile", choices=["vertexai", "local"], required=True,
    #                     help="Profile to use: vertexai or local")
    # args = parser.parse_args()
    logger.info("Loading GEMINI Model...")
    load_gemini_model()
    return app
app = create_app()