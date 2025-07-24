import logging
from CvParser.app import app

logging.basicConfig(level=logging.INFO)

if __name__ == "__main__":
    app.run(debug=True)
