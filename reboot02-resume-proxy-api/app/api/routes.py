import asyncio
import base64
import os

import requests
from fastapi.openapi.utils import status_code_ranges
from flask import Blueprint, jsonify, request
from fastapi import APIRouter, status, UploadFile, File, Request
from starlette.responses import JSONResponse

from app.logger import logger

from app import logger
from app.config import PROJECT_ID, PROJECT_REGION, ASSESSOR_ENDPOINT_ID, PARSER_ENDPOINT_ID, MODEL_DATA_PATH
from app.service.resume_proxy import ResumeProxyService
from app.util.token_manager import VertexAITokenManager

api = APIRouter()
proxy_service = ResumeProxyService()


@api.get('/health')
def health():
    return {'health': 'OK'}


@api.post('/assessment')
async def resume_score(resume_payload: Request):
    payload = await resume_payload.json()
    asyncio.create_task(proxy_service.score_resume(payload))
    return JSONResponse(
        status_code=status.HTTP_202_ACCEPTED,
        content={
              "Message" : "Resume Payload is submitted"
        }
    )
    # return proxy_service.score_resume(request.json())


@api.post('/upload')
def resume_parse(cv: UploadFile = File(...)):
    file = cv.file
    return proxy_service.parse_resume(file)

