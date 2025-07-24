FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 8083
# Create a non-root user and use it
RUN useradd -u 1001 appuser && chown -R appuser /app
USER appuser
#ENV PROFILE=vertexai
#CMD ["python", "run.py"] This is for debugging/troubleshooting dpeloyment logs in GCP VertexAI
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8083"]
