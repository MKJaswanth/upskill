# Smart India Hackathon Project

This project consists of a Next.js 14 frontend with Tailwind CSS and a FastAPI backend.

## Project Structure

```
smartindiahackathon/
├── frontend/          # Next.js 14 application with Tailwind CSS
├── backend/           # FastAPI application
└── README.md         # This file
```

## Prerequisites

- Node.js (v18 or higher)
- Python (v3.8 or higher)
- npm or yarn
- pip

## Getting Started

### Frontend (Next.js 14 + Tailwind CSS)

1. Navigate to the frontend directory:
```bash
cd frontend
```

2. Install dependencies:
```bash
npm install
```

3. Run the development server:
```bash
npm run dev
```

The frontend will be available at [http://localhost:3000](http://localhost:3000)

### Backend (FastAPI)

1. Navigate to the backend directory:
```bash
cd backend
```

2. Install Python dependencies:
```bash
pip install -r requirements.txt
```

3. Run the FastAPI server:
```bash
uvicorn main:app --reload
```

The backend will be available at:
- API: [http://localhost:8000](http://localhost:8000)
- Interactive API docs: [http://localhost:8000/docs](http://localhost:8000/docs)
- Alternative API docs: [http://localhost:8000/redoc](http://localhost:8000/redoc)

## Quick Start Commands

### Run Frontend
```bash
cd frontend && npm run dev
```

### Run Backend
```bash
cd backend && uvicorn main:app --reload
```

## API Endpoints

- `GET /` - Welcome message
- `GET /health` - Health check
- `GET /api/hello` - Hello endpoint

## Development

Both servers support hot reloading:
- Frontend: Changes will automatically reload the browser
- Backend: Changes will automatically restart the server

## Technologies Used

### Frontend
- Next.js 14
- React 18
- TypeScript
- Tailwind CSS
- ESLint

### Backend
- FastAPI
- Python 3.8+
- Uvicorn (ASGI server)
- CORS middleware for frontend communication
