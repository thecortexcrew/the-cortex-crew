import base64

# 1. INPUT PDF FILE
PDF_FILE = "sample_resumes/Emily_Carter_1.pdf"
OUTPUT_FILE = "output_base64_small.txt"

# 2. ENCODE PDF to base64
with open(PDF_FILE, "rb") as f:
    encoded_pdf = base64.b64encode(f.read()).decode("utf-8")

# 3. WRITE base64 to text file
with open(OUTPUT_FILE, "w") as f:
    f.write(encoded_pdf)

print(f"Base64 encoded content saved to {OUTPUT_FILE}")
