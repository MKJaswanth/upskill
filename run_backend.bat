@echo off
echo Starting FastAPI Backend...
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
pause
