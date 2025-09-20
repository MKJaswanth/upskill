# Backend - FastAPI

This is the FastAPI backend for the Smart India Hackathon project.

## Setup

1. Install Python dependencies:
```bash
pip install -r requirements.txt
```

## Running the Backend

To run the FastAPI backend server:

```bash
uvicorn main:app --reload
```

The API will be available at:
- API: http://localhost:8000
- Interactive API docs: http://localhost:8000/docs
- Alternative API docs: http://localhost:8000/redoc

## API Endpoints

- `GET /` - Welcome message
- `GET /health` - Health check
- `GET /api/hello` - Hello endpoint
