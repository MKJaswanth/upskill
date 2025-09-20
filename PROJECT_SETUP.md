# Smart India Hackathon Project - Setup Guide

This project contains multiple components that can be run independently or together.

## 🏗️ Project Structure

```
smartindiahackathon/
├── frontend/              # Next.js 14 + Tailwind CSS
├── backend/               # FastAPI Python backend
├── careers.json          # Career data (25 diverse careers)
├── careers_analyzer.py   # Python script to analyze career data
├── example_usage.py      # Example usage of careers analyzer
└── requirements.txt      # Python dependencies
```

## 🚀 How to Run Each Component

### 1. Frontend (Next.js 14 + Tailwind CSS)

**Prerequisites:**
- Node.js (v18 or higher)
- npm or yarn

**Steps:**
```bash
# Navigate to frontend directory
cd frontend

# Install dependencies (if not already done)
npm install

# Start the development server
npm run dev
```

**Access:** http://localhost:3000

### 2. Backend (FastAPI)

**Prerequisites:**
- Python 3.8 or higher
- pip

**Steps:**
```bash
# Navigate to backend directory
cd backend

# Install Python dependencies
pip install -r requirements.txt

# Start the FastAPI server
uvicorn main:app --reload
```

**Access:**
- API: http://localhost:8000
- Interactive docs: http://localhost:8000/docs
- Alternative docs: http://localhost:8000/redoc

### 3. Careers Data Analysis (Python Scripts)

**Prerequisites:**
- Python 3.7 or higher
- pip

**Steps:**
```bash
# Install dependencies (from project root)
pip install -r requirements.txt

# Run example usage
python example_usage.py

# Run interactive analyzer
python careers_analyzer.py --interactive

# Or use command line options
python careers_analyzer.py --category "Technology"
python careers_analyzer.py --skill "Python"
python careers_analyzer.py --high-salary 100000
```

## 🔧 Quick Start Commands

### Run Everything (3 separate terminals)

**Terminal 1 - Frontend:**
```bash
cd frontend && npm run dev
```

**Terminal 2 - Backend:**
```bash
cd backend && uvicorn main:app --reload
```

**Terminal 3 - Careers Analysis:**
```bash
python careers_analyzer.py --interactive
```

## 📊 Available API Endpoints (Backend)

- `GET /` - Welcome message
- `GET /health` - Health check
- `GET /api/hello` - Hello endpoint

## 🔍 Careers Data Analysis Features

### Interactive Mode
```bash
python careers_analyzer.py --interactive
```

### Command Line Options
```bash
# Search by category
python careers_analyzer.py --category "Technology"

# Search by skill
python careers_analyzer.py --skill "Python"

# Search by experience level
python careers_analyzer.py --experience "Entry"

# Show high-salary careers
python careers_analyzer.py --high-salary 100000

# Export to CSV
python careers_analyzer.py --export careers_export.csv
```

## 🛠️ Development Setup

### Frontend Development
- Hot reloading enabled
- TypeScript support
- Tailwind CSS for styling
- ESLint for code quality

### Backend Development
- Hot reloading with `--reload` flag
- CORS enabled for frontend communication
- Interactive API documentation
- Type hints and validation

### Careers Analysis
- Pandas for data manipulation
- Interactive and command-line interfaces
- CSV export functionality
- Comprehensive search capabilities

## 🔗 Integration

The backend includes CORS middleware configured to work with the frontend running on port 3000. You can:

1. Run both frontend and backend simultaneously
2. Make API calls from the frontend to the backend
3. Use the careers data in your applications

## 📝 Example Integration

```javascript
// Frontend API call example
const response = await fetch('http://localhost:8000/api/hello');
const data = await response.json();
console.log(data);
```

```python
# Backend can serve careers data
from careers_analyzer import CareersAnalyzer

analyzer = CareersAnalyzer()
tech_careers = analyzer.get_tech_careers()
```

## 🚨 Troubleshooting

### Common Issues:

1. **Port already in use:**
   - Frontend: Change port with `npm run dev -- -p 3001`
   - Backend: Change port with `uvicorn main:app --reload --port 8001`

2. **Python dependencies not found:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Node modules missing:**
   ```bash
   cd frontend && npm install
   ```

4. **CORS issues:**
   - Backend CORS is configured for localhost:3000
   - Update CORS origins in `backend/main.py` if needed

## 📚 Additional Resources

- [Next.js Documentation](https://nextjs.org/docs)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [Tailwind CSS Documentation](https://tailwindcss.com/docs)

## 🎯 Next Steps

1. Start with the careers analyzer to understand the data
2. Run the frontend to see the UI
3. Run the backend to test API endpoints
4. Integrate all components for a complete application
