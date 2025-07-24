import threading

import requests

from app.service.json_to_predefined_text_with_jinja2 import ResumeJsonToText
from app.service.resume_screening_sbert_with_gemini import ResumeRanking
from app.logger import logger


class ResumeScreeningService:

  def send_to_score_producer(self, prediction_payload):
      try:
          acknowledgement = requests.post(
              "http://resumeassist.net/api/score",
              headers = {
                  "Content-Type": "application/json"
              },
              json = prediction_payload
          )
          # response = requests.post(
          #     vertex_ai_endpoint,
          #     # 'http://localhost:5001/',
          #     headers={
          #         "Authorization": f"Bearer {access_token}",
          #         "Content-Type": "application/json"
          #     },
          #     json=payload
          # )
          logger.info("Response from score producer %s", acknowledgement)
      except Exception as e:
          logger.error("Failed to send prediction to score api %s", e)


  def accept_resume_application(self, job_application):
      candidate_list = []
      jsonToText = ResumeJsonToText()
      resumeRanking = ResumeRanking()
      response = {}
      for job in job_application:
          job = jsonToText.convert_resume_json_to_text(job)
          resumeRanking.resume_selection(job)
          for resume in job['Candidate']:
              candidate = {}
              # extract fields ApplicantId, IdentificationID, JobID, JobDescription at parent level outside "Profile"
              candidate['ApplicantId'] = resume['ApplicantId']
              candidate['IdentificationID'] = resume['IdentificationID']
              candidate['JobID'] = resume['JobID']
              candidate['JobDescription'] = resume['JobDescription']
              candidate['Score'] = resume['Score']
              candidate['Feedback'] = resume['Feedback']
              candidate['CreatedAt'] = resume['CreatedAt']
              if 'Status' in resume:
                 candidate['Status'] = resume['Status']
                 resume.pop('Status', None)
              # copy resume "Profile" json into candidate "Profile"
              candidate['Profile'] = resume
              # remove ApplicantId, IdentificationID, JobID, JobDescription from "Profile" since it will be outside "Profile" json
              candidate['Profile'].pop('ApplicantId', None)
              candidate['Profile'].pop('IdentificationID', None)
              candidate['Profile'].pop('JobID', None)
              candidate['Profile'].pop('JobDescription', None)
              candidate['Profile'].pop('Score', None)
              candidate['Profile'].pop('Feedback', None)
              candidate['Profile'].pop('CreatedAt', None)

              candidate_list.append(candidate)
      response['predictions'] = candidate_list
      print("Final Response: ", response)
      self.send_to_score_producer(response)
      return response