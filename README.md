# fastapi-starter

A minimal REST API built with FastAPI. Includes two example routes and auto-generated interactive documentation.

## Setup

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Run

```bash
uvicorn app.main:app --reload
```

The API will be available at http://127.0.0.1:8000.
Interactive docs are at http://127.0.0.1:8000/docs.

## Routes

- GET /               Returns a hello world message.
- GET /items/{item_id}  Returns the item id and an optional query parameter.

## Push to GitHub

```bash
git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/YOUR_USERNAME/fastapi-starter.git
git branch -M main
git push -u origin main
```
