# Quick Fix for "Unexpected token '<', "<!DOCTYPE "... is not valid JSON" Error

## 🚨 Immediate Solution

The error occurs because the FastAPI backend is not running or not accessible. Here's how to fix it:

### **Step 1: Start the Backend (Choose One Method)**

#### **Method A: Use the Simplified Backend (Recommended)**
```bash
# Open Command Prompt or PowerShell
cd backend
python -m uvicorn simple_main:app --reload --host 0.0.0.0 --port 8000
```

#### **Method B: Use the Startup Script**
```bash
# Double-click the start-backend.bat file
# Or run in terminal:
start-backend.bat
```

#### **Method C: Manual Installation and Start**
```bash
cd backend
pip install fastapi uvicorn python-multipart
python -m uvicorn simple_main:app --reload --port 8000
```

### **Step 2: Verify Backend is Running**

Open a new browser tab and visit:
- **Health Check**: http://localhost:8000/health
- **API Docs**: http://localhost:8000/docs

You should see:
- Health endpoint returns: `{"status": "healthy", "message": "Backend is running"}`
- API documentation page loads

### **Step 3: Start the Frontend**

```bash
# Open a new terminal/command prompt
cd frontend
npm run dev
```

### **Step 4: Test the Application**

1. Visit http://localhost:3000
2. Look for green "Backend Online" indicator in the header
3. Click "Start Assessment"
4. Fill out the form and submit
5. Should work without JSON parsing errors

## 🔧 Alternative Solutions

### **If Backend Still Won't Start:**

#### **Option 1: Use Demo Mode**
- Visit http://localhost:3000/results/demo
- This shows sample results without requiring backend
- Perfect for demonstrations

#### **Option 2: Check Port Conflicts**
```bash
# Check if port 8000 is in use
netstat -ano | findstr :8000

# Use different port
python -m uvicorn simple_main:app --reload --port 8001
```

#### **Option 3: Fix the Original Backend**
The original backend has import issues. To fix:
```bash
cd backend
# Install missing dependencies
pip install pandas
# Try to start original backend
python -m uvicorn main:app --reload --port 8000
```

## 🎯 What's Fixed

### **Before (Error):**
```
Unexpected token '<', "<!DOCTYPE "... is not valid JSON
```

### **After (Working):**
- Backend returns proper JSON responses
- Frontend can parse the data correctly
- Assessment form works properly
- Results page displays career recommendations

## 📊 Success Indicators

- ✅ **Backend Status**: Green "Backend Online" on home page
- ✅ **Health Endpoint**: http://localhost:8000/health returns JSON
- ✅ **API Docs**: http://localhost:8000/docs loads properly
- ✅ **Assessment**: Form submission works without errors
- ✅ **Results**: Career recommendations display correctly

## 🚀 Quick Test Commands

```bash
# Test backend health
curl http://localhost:8000/health

# Test recommendation endpoint
curl -X POST "http://localhost:8000/recommend" \
     -H "Content-Type: application/json" \
     -d '{"skills": ["Python"], "interests": ["Technology"], "experience_level": "Entry", "preferred_categories": []}'
```

## 🆘 Emergency Fallback

If nothing works, use the demo results page:
1. Visit http://localhost:3000/results/demo
2. Shows sample career recommendations
3. No backend required
4. Perfect for demonstrations

The simplified backend (`simple_main.py`) provides mock data that works immediately without complex dependencies!
