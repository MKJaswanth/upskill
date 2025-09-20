# Deployment Guide - Free Production Hosting

Complete step-by-step guide to deploy Pathway AI to free hosting platforms.

## 🎯 Overview

This guide will deploy:
- **Frontend (Next.js)**: Vercel (Free)
- **Backend (FastAPI)**: Render (Free)
- **Total Cost**: $0/month

## 📋 Prerequisites

- GitHub account
- Vercel account (free)
- Render account (free)
- Git installed locally

## 🚀 Part 1: Deploy Backend to Render

### Step 1: Prepare Backend for Deployment

The backend is already configured with:
- ✅ `app.py` - Main FastAPI application
- ✅ `requirements.txt` - Python dependencies
- ✅ `Dockerfile` - Container configuration
- ✅ `render.yaml` - Render configuration
- ✅ `careers.json` - Career data

### Step 2: Push to GitHub

```bash
# Initialize git repository (if not already done)
git init

# Add all files
git add .

# Commit changes
git commit -m "Initial commit with deployment configuration"

# Create GitHub repository and push
git remote add origin https://github.com/yourusername/pathway-ai.git
git branch -M main
git push -u origin main
```

### Step 3: Deploy to Render

1. **Go to Render**: https://render.com
2. **Sign up/Login** with GitHub
3. **Click "New +"** → **"Web Service"**
4. **Connect Repository**: Select your GitHub repository
5. **Configure Service**:
   - **Name**: `pathway-ai-backend`
   - **Environment**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `uvicorn app:app --host 0.0.0.0 --port $PORT`
   - **Plan**: `Free`
6. **Click "Create Web Service"**

### Step 4: Configure Environment Variables

In Render dashboard:
1. Go to your service
2. Click **"Environment"** tab
3. Add environment variables:
   - `PYTHON_VERSION`: `3.11.0`
   - `PORT`: `8000` (auto-set by Render)

### Step 5: Test Backend Deployment

Once deployed, test your backend:
- **Health Check**: `https://your-service-name.onrender.com/health`
- **API Docs**: `https://your-service-name.onrender.com/docs`
- **Recommendations**: `https://your-service-name.onrender.com/recommend`

## 🎨 Part 2: Deploy Frontend to Vercel

### Step 1: Update Frontend Configuration

1. **Update API URL** in `frontend/src/lib/api.ts`:
```typescript
const API_BASE_URL = process.env.NEXT_PUBLIC_API_URL || 'https://your-backend-url.onrender.com';
```

2. **Create Environment File**:
```bash
# In frontend directory
cp env.example .env.local
```

3. **Update `.env.local`**:
```env
NEXT_PUBLIC_API_URL=https://your-backend-url.onrender.com
```

### Step 2: Deploy to Vercel

1. **Go to Vercel**: https://vercel.com
2. **Sign up/Login** with GitHub
3. **Click "New Project"**
4. **Import Repository**: Select your GitHub repository
5. **Configure Project**:
   - **Framework Preset**: `Next.js`
   - **Root Directory**: `frontend`
   - **Build Command**: `npm run build`
   - **Output Directory**: `.next`
6. **Add Environment Variable**:
   - `NEXT_PUBLIC_API_URL`: `https://your-backend-url.onrender.com`
7. **Click "Deploy"**

### Step 3: Test Frontend Deployment

Once deployed, test your frontend:
- **Home Page**: `https://your-project.vercel.app`
- **Assessment**: `https://your-project.vercel.app/assessment`
- **Results**: `https://your-project.vercel.app/results`
- **Demo**: `https://your-project.vercel.app/results/demo`

## 🔧 Part 3: Configuration Files

### Backend Files Created:

#### `backend/app.py`
```python
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
# ... complete FastAPI application
```

#### `backend/requirements.txt`
```
fastapi==0.104.1
uvicorn[standard]==0.24.0
python-multipart==0.0.6
pydantic==2.5.0
```

#### `backend/Dockerfile`
```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 8000
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
```

#### `backend/render.yaml`
```yaml
services:
  - type: web
    name: pathway-ai-backend
    env: python
    buildCommand: pip install -r requirements.txt
    startCommand: uvicorn app:app --host 0.0.0.0 --port $PORT
    envVars:
      - key: PYTHON_VERSION
        value: 3.11.0
```

### Frontend Files Created:

#### `frontend/vercel.json`
```json
{
  "framework": "nextjs",
  "buildCommand": "npm run build",
  "devCommand": "npm run dev",
  "installCommand": "npm install",
  "outputDirectory": ".next"
}
```

#### `frontend/env.example`
```env
NEXT_PUBLIC_API_URL=http://localhost:8000
# NEXT_PUBLIC_API_URL=https://your-backend-url.onrender.com
```

## 🧪 Part 4: Testing Deployment

### Test Backend Endpoints

```bash
# Health check
curl https://your-backend-url.onrender.com/health

# Test recommendation
curl -X POST "https://your-backend-url.onrender.com/recommend" \
     -H "Content-Type: application/json" \
     -d '{
       "skills": ["Python", "JavaScript"],
       "interests": ["Technology"],
       "experience_level": "Entry Level",
       "preferred_categories": ["Technology"]
     }'
```

### Test Frontend Integration

1. **Visit Frontend**: `https://your-project.vercel.app`
2. **Check Backend Status**: Should show "Backend Online"
3. **Take Assessment**: Fill out form and submit
4. **View Results**: Should display career recommendations

## 🔄 Part 5: Continuous Deployment

### Automatic Deployments

Both platforms support automatic deployments:
- **Render**: Deploys on every push to main branch
- **Vercel**: Deploys on every push to main branch

### Update Process

1. **Make Changes**: Edit code locally
2. **Commit & Push**: `git add . && git commit -m "Update" && git push`
3. **Auto Deploy**: Both services automatically redeploy

## 🛠️ Part 6: Troubleshooting

### Common Issues

#### Backend Not Starting
- Check Render logs for errors
- Verify `requirements.txt` has all dependencies
- Ensure `app.py` is the main file

#### Frontend Can't Connect to Backend
- Verify `NEXT_PUBLIC_API_URL` environment variable
- Check CORS configuration in backend
- Test backend endpoints directly

#### CORS Errors
- Backend is configured with `allow_origins=["*"]`
- If issues persist, add specific frontend URL

### Debug Commands

```bash
# Test backend locally
cd backend
python -m uvicorn app:app --reload

# Test frontend locally
cd frontend
npm run dev

# Check environment variables
echo $NEXT_PUBLIC_API_URL
```

## 📊 Part 7: Monitoring & Analytics

### Render Monitoring
- **Logs**: Available in Render dashboard
- **Metrics**: CPU, Memory, Response time
- **Uptime**: 99.9% uptime on free tier

### Vercel Analytics
- **Performance**: Core Web Vitals
- **Usage**: Page views, visitors
- **Deployments**: Build logs and status

## 🎯 Part 8: Production Checklist

### Backend Checklist
- ✅ FastAPI app deployed to Render
- ✅ Health endpoint responding
- ✅ CORS configured for frontend
- ✅ Environment variables set
- ✅ Careers data loading

### Frontend Checklist
- ✅ Next.js app deployed to Vercel
- ✅ Environment variables configured
- ✅ API integration working
- ✅ All pages accessible
- ✅ Demo mode functional

### Integration Checklist
- ✅ Frontend can reach backend
- ✅ Assessment form submits successfully
- ✅ Results display correctly
- ✅ Error handling works
- ✅ Mobile responsive

## 🚀 Part 9: Going Live

### Final Steps

1. **Test Everything**: Run through complete user flow
2. **Share URLs**: 
   - Frontend: `https://your-project.vercel.app`
   - Backend: `https://your-backend-url.onrender.com`
3. **Monitor**: Check both dashboards for issues
4. **Document**: Update README with live URLs

### Performance Optimization

- **Backend**: Render free tier has cold starts (first request may be slow)
- **Frontend**: Vercel provides excellent performance with CDN
- **Caching**: Consider adding Redis for backend caching (paid tier)

## 💰 Cost Breakdown

### Free Tier Limits

#### Render (Backend)
- **Free**: 750 hours/month
- **Sleep**: After 15 minutes of inactivity
- **Cold Start**: ~30 seconds after sleep

#### Vercel (Frontend)
- **Free**: Unlimited static hosting
- **Bandwidth**: 100GB/month
- **Builds**: 100 builds/month

### Upgrade Options

- **Render Pro**: $7/month (always-on, custom domains)
- **Vercel Pro**: $20/month (unlimited builds, analytics)

## 🎉 Success!

Your Pathway AI application is now live with:
- ✅ **Frontend**: https://your-project.vercel.app
- ✅ **Backend**: https://your-backend-url.onrender.com
- ✅ **Cost**: $0/month
- ✅ **Auto-deploy**: On every code push
- ✅ **Production-ready**: Scalable and monitored

The application is now accessible worldwide with professional hosting! 🌍
