#!/bin/bash

echo "🔄 Creating virtual environment..."
python3 -m venv .venv

echo "✅ Activating virtual environment..."
source .venv/bin/activate

echo "📦 Upgrading pip, setuptools, wheel..."
pip install --upgrade pip setuptools wheel

echo "📦 Installing Python dependencies..."
pip install -r requirements.txt

echo "🔍 Downloading spaCy model..."
python -m spacy download en_core_web_sm

echo "✅ Setup complete. Run 'source .venv/bin/activate' and 'python app.py' to start the app."
