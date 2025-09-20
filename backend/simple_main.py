from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional, Dict, Any
import json

app = FastAPI(title="Smart India Hackathon Backend", version="1.0.0")

# Add CORS middleware to allow frontend to communicate with backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Next.js default port
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Pydantic models for request/response
class UserAssessment(BaseModel):
    skills: List[str]
    interests: List[str]
    experience_level: str
    preferred_categories: Optional[List[str]] = []

class CareerRecommendation(BaseModel):
    id: int
    title: str
    category: str
    description: str
    match_score: float
    matched_skills: List[str]
    missing_skills: List[str]
    experience_level: str
    salary_range: str
    education: str

class RecommendationResponse(BaseModel):
    recommendations: List[CareerRecommendation]
    total_careers_analyzed: int
    user_profile: UserAssessment

@app.get("/")
async def root():
    return {"message": "Welcome to Smart India Hackathon Backend API"}

@app.get("/health")
async def health_check():
    return {"status": "healthy", "message": "Backend is running"}

@app.get("/api/hello")
async def hello():
    return {"message": "Hello from FastAPI backend!"}

@app.post("/recommend", response_model=RecommendationResponse)
async def get_recommendations(user_assessment: UserAssessment):
    """
    Get career recommendations based on user assessment.
    This is a simplified version that returns mock data.
    """
    try:
        # Validate input
        if not user_assessment.skills and not user_assessment.interests:
            raise HTTPException(
                status_code=400, 
                detail="At least one skill or interest must be provided"
            )
        
        # Mock recommendations for testing
        mock_recommendations = [
            CareerRecommendation(
                id=1,
                title="Software Engineer",
                category="Technology",
                description="Design, develop, and maintain software applications and systems using various programming languages and frameworks.",
                match_score=0.85,
                matched_skills=user_assessment.skills[:3] if user_assessment.skills else ["Programming"],
                missing_skills=["Data Structures", "Algorithms", "Version Control"],
                experience_level="Entry to Senior",
                salary_range="$60,000 - $150,000",
                education="Bachelor's in Computer Science or related field"
            ),
            CareerRecommendation(
                id=2,
                title="Data Scientist",
                category="Technology",
                description="Analyze complex data sets to extract insights and build predictive models using statistical methods and machine learning.",
                match_score=0.72,
                matched_skills=user_assessment.skills[:2] if user_assessment.skills else ["Python"],
                missing_skills=["R", "Statistics", "Machine Learning", "SQL"],
                experience_level="Mid to Senior",
                salary_range="$80,000 - $180,000",
                education="Master's in Data Science, Statistics, or related field"
            ),
            CareerRecommendation(
                id=3,
                title="UX/UI Designer",
                category="Design",
                description="Create user-centered designs for digital products, focusing on usability, accessibility, and visual appeal.",
                match_score=0.58,
                matched_skills=user_assessment.skills[:1] if user_assessment.skills else ["Design"],
                missing_skills=["Figma", "Adobe Creative Suite", "User Research", "Prototyping"],
                experience_level="Entry to Senior",
                salary_range="$50,000 - $120,000",
                education="Bachelor's in Design, HCI, or related field"
            )
        ]
        
        return RecommendationResponse(
            recommendations=mock_recommendations,
            total_careers_analyzed=25,
            user_profile=user_assessment
        )
        
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error generating recommendations: {str(e)}")

@app.get("/api/careers")
async def get_all_careers():
    """Get all available careers."""
    return {
        "careers": [
            {
                "id": 1,
                "title": "Software Engineer",
                "category": "Technology",
                "description": "Design, develop, and maintain software applications and systems using various programming languages and frameworks.",
                "required_skills": ["Programming", "Problem Solving", "Data Structures", "Algorithms", "Version Control"],
                "experience_level": "Entry to Senior",
                "salary_range": "$60,000 - $150,000",
                "education": "Bachelor's in Computer Science or related field"
            }
        ],
        "total_count": 1
    }

@app.get("/api/categories")
async def get_career_categories():
    """Get all available career categories."""
    return {
        "categories": ["Technology", "Design", "Marketing", "Business", "Finance"],
        "total_count": 5
    }

@app.get("/api/skills")
async def get_all_skills():
    """Get all unique skills from all careers."""
    return {
        "skills": ["Programming", "Python", "JavaScript", "Design", "Marketing", "Problem Solving"],
        "total_count": 6
    }
