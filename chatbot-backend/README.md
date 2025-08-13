# Chatbot Backend

A FastAPI-based backend for the chatbot system.

## Setup

1. Install Python dependencies:
```bash
pip install -r requirements.txt
```

2. Run the server:
```bash
python main.py
```

Or using uvicorn directly:
```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

The API will be available at `http://localhost:8000`

## API Endpoints

- `GET /` - Health check
- `GET /jobs` - Get all jobs
- `GET /clients` - Get all clients  
- `GET /jobs/{id}/questions` - Get questions for a specific job
- `GET /clients/{id}/questions` - Get questions for a specific client

## API Documentation

Once running, visit `http://localhost:8000/docs` for interactive API documentation.

