import vertexai

from app.config import PROJECT_ID, PROJECT_REGION
from app.logger import logger

def init_vertex_ai():
    """Initializes the Vertex AI SDK.
    """
    try:
        vertexai.init(project=PROJECT_ID, location=PROJECT_REGION)
        logger.info("Initialized VertexAI using Project ID: %s; Region: %s", PROJECT_ID, PROJECT_REGION)
    except Exception as e:
        logger.error("VertexAI initialization failed: %s", e)
        raise