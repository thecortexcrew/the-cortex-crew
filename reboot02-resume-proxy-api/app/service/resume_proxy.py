import base64
from http.client import responses
from io import BytesIO
import httpx
import requests

from app.logger import logger
from app.config import PROJECT_ID, PROJECT_REGION, ASSESSOR_ENDPOINT_ID, PARSER_ENDPOINT_ID
from app.util.token_manager import VertexAITokenManager

vertexAI_token_manager = VertexAITokenManager()

class ResumeProxyService:
    async def score_resume(self, data):
        access_token = vertexAI_token_manager.get_token()
        vertex_ai_endpoint = vertexAI_token_manager.vertex_ai_endpoint(PROJECT_ID, PROJECT_REGION, ASSESSOR_ENDPOINT_ID)
        headers = {
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json"
        }
        # response = requests.post(
        #     vertex_ai_endpoint,
        #     headers={
        #         "Authorization": f"Bearer {access_token}",
        #         "Content-Type": "application/json"
        #     },
        #     json = data
        # )
        # logger.info("Invoked Resume Assessor Endpoint ID %s with Payload %s", vertex_ai_endpoint, data)
        # return response.json()
        try:
            async with httpx.AsyncClient(timeout=180.0) as client:
               logger.info("Invoking Resume Assessor Endpoint ID %s with Payload %s", vertex_ai_endpoint, data)
               response = await client.post(vertex_ai_endpoint, headers=headers, json=data)
               # response_json = await response.json()
               logger.info("Received response from Resume Assessor service %s", response.json())
        except Exception as e:
             logger.error("Error while submitting resume payload to the assessor %s", e)


    def parse_resume(self, file):
        access_token = vertexAI_token_manager.get_token()
        vertex_ai_endpoint = vertexAI_token_manager.vertex_ai_endpoint(PROJECT_ID, PROJECT_REGION, PARSER_ENDPOINT_ID)
        file_content = file.read()
        encoded_content = base64.b64encode(file_content).decode('utf-8')
        print(f"Base64 Length: {len(encoded_content)}")
        payload = {
            "instances": [
                {
                    "content": encoded_content,
                    "mime_type": "application/pdf"
                }
            ]
        }
        response = requests.post(
            vertex_ai_endpoint,
            # 'http://localhost:5001/',
            headers = {
                "Authorization": f"Bearer {access_token}",
                "Content-Type": "application/json"
            },
            json = payload
        )
        logger.info("Invoked Resume Parser Endpoint ID %s with Payload %s", vertex_ai_endpoint, payload)
        logger.info("Response from Resume Parser Endpoint ID %s", response)
        return response.json()

