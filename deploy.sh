#!/bin/bash

# Pathway AI Deployment Script
echo "🚀 Pathway AI Deployment Script"
echo "================================"

# Check if git is initialized
if [ ! -d ".git" ]; then
    echo "📦 Initializing Git repository..."
    git init
    git add .
    git commit -m "Initial commit with deployment configuration"
    echo "✅ Git repository initialized"
    echo "⚠️  Please create a GitHub repository and push your code:"
    echo "   git remote add origin https://github.com/yourusername/pathway-ai.git"
    echo "   git branch -M main"
    echo "   git push -u origin main"
else
    echo "✅ Git repository already initialized"
fi

# Check backend files
echo ""
echo "🔍 Checking backend deployment files..."
if [ -f "backend/app.py" ]; then
    echo "✅ backend/app.py exists"
else
    echo "❌ backend/app.py missing"
fi

if [ -f "backend/requirements.txt" ]; then
    echo "✅ backend/requirements.txt exists"
else
    echo "❌ backend/requirements.txt missing"
fi

if [ -f "backend/Dockerfile" ]; then
    echo "✅ backend/Dockerfile exists"
else
    echo "❌ backend/Dockerfile missing"
fi

if [ -f "backend/render.yaml" ]; then
    echo "✅ backend/render.yaml exists"
else
    echo "❌ backend/render.yaml missing"
fi

# Check frontend files
echo ""
echo "🔍 Checking frontend deployment files..."
if [ -f "frontend/vercel.json" ]; then
    echo "✅ frontend/vercel.json exists"
else
    echo "❌ frontend/vercel.json missing"
fi

if [ -f "frontend/env.example" ]; then
    echo "✅ frontend/env.example exists"
else
    echo "❌ frontend/env.example missing"
fi

echo ""
echo "📋 Next Steps:"
echo "1. Push your code to GitHub"
echo "2. Deploy backend to Render: https://render.com"
echo "3. Deploy frontend to Vercel: https://vercel.com"
echo "4. Update API URL in frontend environment variables"
echo ""
echo "📖 See DEPLOYMENT_GUIDE.md for detailed instructions"
echo ""
echo "🎉 Happy deploying!"
