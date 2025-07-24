import argparse

from flask import Flask
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes import api
# from app.config import PROFILE
from app.logger import logger

# Set allowed origins
origins = [
    "http://localhost:5173",  # Vite/React frontend
    "http://127.0.0.1:5173",
    # Add more origins here as needed
]

def create_app():
    app = FastAPI()
    app.include_router(api)
    # Apply CORS middleware
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],  # List of allowed origins - Allow All
        allow_credentials=True,  # Allow cookies and headers
        allow_methods=["*"],  # Allow all HTTP methods (GET, POST, etc.)
        allow_headers=["*"],  # Allow all headers
    )
    logger.info("Initialized app")
    return app
app = create_app()