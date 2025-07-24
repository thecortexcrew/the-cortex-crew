FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN python -m spacy download en_core_web_sm
COPY . .
EXPOSE 8080
#ENV PROFILE=vertexai
#CMD ["python", "run.py"] This is for debugging/troubleshooting dpeloyment logs in GCP VertexAI
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "CvParser.app:app"]