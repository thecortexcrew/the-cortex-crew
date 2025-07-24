from flask import Blueprint, jsonify, request

from app.service.resume_screen_service import ResumeScreeningService

api = Blueprint('api', __name__)

@api.route('/health', methods=['GET'])
def health():
    return {'health': 'OK'}

@api.route('/', methods=['POST'])
def resume_screen():
    resume_screen_service = ResumeScreeningService()
    data = request.json
    job_application = data['instances'][0]['JobApplication']
    return jsonify(resume_screen_service.accept_resume_application(job_application))