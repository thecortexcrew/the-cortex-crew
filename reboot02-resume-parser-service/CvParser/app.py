from flask import Flask, request, jsonify
import os
import pdfplumber
import base64
import tempfile
from datetime import datetime
from CvParser.parser import parse_cv_text
from CvParser.utils.applicantIdHelper import generate_application_id
from CvParser.utils.identificationIdHelper import generate_identification_id
from flask_cors import CORS

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

CORS(app, resources={r"/*": {"origins": "http://localhost:5173"}})

def extract_text_from_pdf(pdf_path):
    all_text = []
    try:
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    all_text.append(page_text.strip())
    except Exception as e:
        print(f"Error extracting PDF: {e}")
    return "\n".join(all_text)

def enrich_parsed_result(parsed_result):
    """Add IDs and date if missing."""
    profile = parsed_result.get("Profile", {})
    if not parsed_result.get("ApplicantId"):
        parsed_result["ApplicantId"] = str(generate_application_id())
    if not parsed_result.get("IdentificationID"):
        parsed_result["IdentificationID"] = str(generate_identification_id())
    if not profile.get("DateOfApplication"):
        profile["DateOfApplication"] = datetime.today().strftime("%Y-%m-%d")
    return parsed_result

@app.route("/upload", methods=["POST"])
def upload():
    try:
        file = request.files.get("cv")
        if not file:
            return jsonify({"error": "No file uploaded."}), 400

        if not file.filename.lower().endswith(".pdf"):
            return jsonify({"error": "Only PDF files are supported."}), 400

        file_path = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(file_path)

        extracted_text = extract_text_from_pdf(file_path)
        os.remove(file_path)

        if not extracted_text:
            return jsonify({"error": "Could not extract text from the PDF."}), 400

        parsed_result = parse_cv_text(extracted_text)
        parsed_result = enrich_parsed_result(parsed_result)

        return jsonify(parsed_result)

    except Exception as e:
        return jsonify({"error": f"Unexpected server error: {str(e)}"}), 500


@app.route("/", methods=["POST"])
def predict():
    try:
        req = request.get_json()
        if not req or "instances" not in req or not req["instances"]:
            return jsonify({"error": "Invalid request format"}), 400

        instance = req["instances"][0]
        if "content" not in instance or "mime_type" not in instance:
            return jsonify({"error": "Missing 'content' or 'mime_type'"}), 400

        if instance["mime_type"] != "application/pdf":
            return jsonify({"error": "Only 'application/pdf' is supported"}), 400

        # Decode base64 PDF
        pdf_bytes = base64.b64decode(instance["content"])

        # Save to temporary file
        with tempfile.NamedTemporaryFile(suffix=".pdf", delete=False) as temp_pdf:
            temp_pdf.write(pdf_bytes)
            temp_pdf_path = temp_pdf.name

        extracted_text = extract_text_from_pdf(temp_pdf_path)
        os.remove(temp_pdf_path)

        if not extracted_text:
            return jsonify({"error": "Could not extract text from the PDF."}), 400

        parsed_result = parse_cv_text(extracted_text)
        parsed_result = enrich_parsed_result(parsed_result)

        return jsonify({"predictions": [parsed_result]})

    except Exception as e:
        return jsonify({"error": f"Unexpected error: {str(e)}"}), 500


@app.route("/health", methods=["GET"])
def health_check():
    return jsonify({"status": "ok"}), 200


