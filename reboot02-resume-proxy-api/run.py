import os

import uvicorn

from app.main import create_app

app = create_app()

if __name__ == '__main__':
    uvicorn.run("app.main:app", host='0.0.0.0', port=int(os.environ.get("PORT", 5002)))