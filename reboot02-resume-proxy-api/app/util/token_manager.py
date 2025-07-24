import google.auth
from google.auth.transport.requests import Request


class VertexAITokenManager:
    def __init__(self):
        self.credentials, project_id = google.auth.default(scopes=["https://www.googleapis.com/auth/cloud-platform"])
        self.request_adapter = Request()

    def get_token(self):
        if not self.credentials.valid or self.credentials.expired:
             self.credentials.refresh(self.request_adapter)
        return self.credentials.token

    def vertex_ai_endpoint(self, project_id, region_id, endpoint_id):
        return "https://{region}-aiplatform.googleapis.com/v1/projects/{project_id}/locations/{region}/endpoints/{endpoint_id}:predict".format(
                region=region_id, project_id=project_id, endpoint_id=endpoint_id
        )
