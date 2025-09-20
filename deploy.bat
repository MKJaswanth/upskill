@echo off
echo 🚀 Pathway AI Deployment Script
echo ================================

REM Check if git is initialized
if not exist ".git" (
    echo 📦 Initializing Git repository...
    git init
    git add .
    git commit -m "Initial commit with deployment configuration"
    echo ✅ Git repository initialized
    echo ⚠️  Please create a GitHub repository and push your code:
    echo    git remote add origin https://github.com/yourusername/pathway-ai.git
    echo    git branch -M main
    echo    git push -u origin main
) else (
    echo ✅ Git repository already initialized
)

REM Check backend files
echo.
echo 🔍 Checking backend deployment files...
if exist "backend\app.py" (
    echo ✅ backend\app.py exists
) else (
    echo ❌ backend\app.py missing
)

if exist "backend\requirements.txt" (
    echo ✅ backend\requirements.txt exists
) else (
    echo ❌ backend\requirements.txt missing
)

if exist "backend\Dockerfile" (
    echo ✅ backend\Dockerfile exists
) else (
    echo ❌ backend\Dockerfile missing
)

if exist "backend\render.yaml" (
    echo ✅ backend\render.yaml exists
) else (
    echo ❌ backend\render.yaml missing
)

REM Check frontend files
echo.
echo 🔍 Checking frontend deployment files...
if exist "frontend\vercel.json" (
    echo ✅ frontend\vercel.json exists
) else (
    echo ❌ frontend\vercel.json missing
)

if exist "frontend\env.example" (
    echo ✅ frontend\env.example exists
) else (
    echo ❌ frontend\env.example missing
)

echo.
echo 📋 Next Steps:
echo 1. Push your code to GitHub
echo 2. Deploy backend to Render: https://render.com
echo 3. Deploy frontend to Vercel: https://vercel.com
echo 4. Update API URL in frontend environment variables
echo.
echo 📖 See DEPLOYMENT_GUIDE.md for detailed instructions
echo.
echo 🎉 Happy deploying!
pause
