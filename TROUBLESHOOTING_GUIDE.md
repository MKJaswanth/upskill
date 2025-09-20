# Troubleshooting Guide

## Common Issues and Solutions

### 1. "Unexpected token '<', "<!DOCTYPE "... is not valid JSON" Error

**Problem**: The frontend is trying to parse HTML as JSON, which happens when the API endpoint returns an HTML error page instead of JSON.

**Causes**:
- FastAPI backend is not running
- Backend is running on a different port
- CORS issues
- Network connectivity problems

**Solutions**:

#### Step 1: Check if Backend is Running
```bash
# Check if backend is running
curl http://localhost:8000/health

# Or visit in browser
http://localhost:8000/docs
```

#### Step 2: Start the Backend
```bash
# Navigate to backend directory
cd backend

# Install dependencies
pip install fastapi uvicorn python-multipart

# Start the server
python -m uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

#### Step 3: Verify Backend is Working
- Visit http://localhost:8000/docs to see the API documentation
- Visit http://localhost:8000/health to check health endpoint
- The backend status indicator on the home page should show "Backend Online"

#### Step 4: Check Frontend Configuration
- Ensure the frontend is running on http://localhost:3000
- Check that the API_BASE_URL is set to http://localhost:8000
- Verify CORS is configured in the backend

### 2. "Failed to fetch" Error

**Problem**: Network request failed, usually indicating the backend is not accessible.

**Solutions**:
- Ensure backend is running on port 8000
- Check firewall settings
- Verify no other service is using port 8000
- Try accessing http://localhost:8000 directly in browser

### 3. CORS Errors

**Problem**: Cross-Origin Resource Sharing issues between frontend and backend.

**Solutions**:
- Backend CORS is configured for http://localhost:3000
- If using different ports, update CORS origins in backend/main.py
- Ensure both frontend and backend are running on localhost

### 4. Port Conflicts

**Problem**: Port 8000 or 3000 is already in use.

**Solutions**:
```bash
# Check what's using port 8000
netstat -ano | findstr :8000

# Kill process using port 8000 (Windows)
taskkill /PID <PID> /F

# Use different port for backend
python -m uvicorn main:app --reload --port 8001

# Update frontend API URL
# In .env.local or directly in code
NEXT_PUBLIC_API_URL=http://localhost:8001
```

### 5. Python Dependencies Issues

**Problem**: Missing Python packages or version conflicts.

**Solutions**:
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Or install manually
pip install fastapi uvicorn python-multipart pandas
```

### 6. Node.js Dependencies Issues

**Problem**: Missing Node.js packages or version conflicts.

**Solutions**:
```bash
# Navigate to frontend directory
cd frontend

# Install dependencies
npm install

# Clear cache if needed
npm cache clean --force

# Delete node_modules and reinstall
rm -rf node_modules package-lock.json
npm install
```

### 7. File Path Issues

**Problem**: Backend can't find careers.json file.

**Solutions**:
- Ensure careers.json is in the project root directory
- Check file permissions
- Verify the file path in recommendation_engine.py

### 8. Memory Issues

**Problem**: Out of memory errors or slow performance.

**Solutions**:
- Close other applications
- Restart the development servers
- Check system resources
- Use smaller datasets for testing

## Debugging Steps

### 1. Check Backend Status
```bash
# Test backend endpoints
curl http://localhost:8000/health
curl http://localhost:8000/
curl http://localhost:8000/api/careers
```

### 2. Check Frontend Console
- Open browser developer tools (F12)
- Check Console tab for JavaScript errors
- Check Network tab for failed requests
- Look for CORS errors or 404 responses

### 3. Check Backend Logs
- Look at the terminal where uvicorn is running
- Check for Python errors or exceptions
- Verify request logs

### 4. Test API Endpoints Manually
```bash
# Test recommendation endpoint
curl -X POST "http://localhost:8000/recommend" \
     -H "Content-Type: application/json" \
     -d '{
       "skills": ["Python", "JavaScript"],
       "interests": ["Technology"],
       "experience_level": "Entry Level",
       "preferred_categories": ["Technology"]
     }'
```

### 5. Use Demo Mode
- If backend is not working, use the demo results page
- Visit http://localhost:3000/results/demo
- This shows sample data without requiring backend

## Prevention Tips

### 1. Always Start Backend First
```bash
# Terminal 1: Start backend
cd backend
python -m uvicorn main:app --reload

# Terminal 2: Start frontend
cd frontend
npm run dev
```

### 2. Use Backend Status Indicator
- The home page shows backend status
- Green = Online, Red = Offline
- Click "Check Again" to refresh status

### 3. Check Dependencies
- Keep requirements.txt updated
- Use virtual environments for Python
- Use package-lock.json for Node.js

### 4. Monitor Logs
- Watch backend terminal for errors
- Check browser console for frontend errors
- Use network tab to debug API calls

## Quick Fixes

### Reset Everything
```bash
# Stop all servers (Ctrl+C)

# Backend
cd backend
pip install -r requirements.txt
python -m uvicorn main:app --reload

# Frontend
cd frontend
npm install
npm run dev
```

### Use Demo Mode
If backend issues persist:
1. Visit http://localhost:3000/results/demo
2. This shows sample results without backend
3. Use this for demonstration purposes

### Alternative Backend Commands
```bash
# If uvicorn doesn't work
python -m fastapi dev main.py

# Or use gunicorn
pip install gunicorn
gunicorn main:app -w 4 -k uvicorn.workers.UvicornWorker
```

## Getting Help

### Check These First:
1. Backend status indicator on home page
2. Browser console for errors
3. Backend terminal for Python errors
4. Network tab for failed requests

### Common Error Messages:
- "Unexpected token '<'" → Backend not running
- "Failed to fetch" → Network/connection issue
- "CORS error" → Cross-origin configuration issue
- "Module not found" → Missing dependencies
- "Port already in use" → Port conflict

### Emergency Fallback:
If nothing works, use the demo results page at http://localhost:3000/results/demo to show the application functionality.
