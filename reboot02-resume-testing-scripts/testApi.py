import base64
import json
import requests
import subprocess

# 1. CONFIGURATION
PROJECT_ID = "hireassist"
REGION = "us-central1"
ENDPOINT_ID = "498735175824310272"
PDF_FILE = "PriyankaBanerjee_Resume_Java.pdf"

# 2. ENCODE PDF to base64
with open(PDF_FILE, "rb") as f:
    encoded_pdf = base64.b64encode(f.read()).decode("utf-8")
#print(encoded_pdf)

#3. GET ACCESS TOKEN using gcloud
access_token = subprocess.check_output(["gcloud", "auth", "print-access-token"]).decode("utf-8").strip()

#4. SETUP REQUEST
url = f"https://{REGION}-aiplatform.googleapis.com/v1/projects/{PROJECT_ID}/locations/{REGION}/endpoints/{ENDPOINT_ID}:predict"
headers = {
    "Authorization": f"Bearer {access_token}",
    "Content-Type": "application/json"
}
payload = {
    "instances": [
        {
            "mime_type": "application/pdf",
            "content": encoded_pdf
        }
    ]
}

# 5. SEND REQUEST
response = requests.post(url, headers=headers, json=payload)

#6. PRINT RESULT
print("Status Code:", response.status_code)
print("Response JSON:\n", json.dumps(response.json(), indent=2))
