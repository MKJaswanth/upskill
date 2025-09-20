from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional, Dict, Any
from recommendation_engine import RecommendationEngine, CareerMatch
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

# Initialize recommendation engine
recommendation_engine = RecommendationEngine()

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

@app.get("/api/careers")
async def get_all_careers():
    """Get all available careers."""
    try:
        careers = recommendation_engine.get_all_careers()
        return {
            "careers": careers,
            "total_count": len(careers)
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching careers: {str(e)}")

@app.get("/api/careers/{career_id}")
async def get_career_by_id(career_id: int):
    """Get specific career by ID."""
    try:
        career = recommendation_engine.get_career_by_id(career_id)
        if not career:
            raise HTTPException(status_code=404, detail="Career not found")
        return career
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching career: {str(e)}")

@app.post("/recommend", response_model=RecommendationResponse)
async def get_recommendations(user_assessment: UserAssessment):
    """
    Get career recommendations based on user assessment.
    
    Accepts user responses as JSON and returns top 3 career matches
    with match scores and skill gaps.
    """
    try:
        # Validate input
        if not user_assessment.skills and not user_assessment.interests:
            raise HTTPException(
                status_code=400, 
                detail="At least one skill or interest must be provided"
            )
        
        # Get recommendations from engine
        career_matches = recommendation_engine.get_recommendations({
            "skills": user_assessment.skills,
            "interests": user_assessment.interests,
            "experience_level": user_assessment.experience_level,
            "preferred_categories": user_assessment.preferred_categories or []
        })
        
        # Convert CareerMatch objects to CareerRecommendation objects
        recommendations = []
        for match in career_matches:
            recommendations.append(CareerRecommendation(
                id=match.id,
                title=match.title,
                category=match.category,
                description=match.description,
                match_score=match.match_score,
                matched_skills=match.matched_skills,
                missing_skills=match.missing_skills,
                experience_level=match.experience_level,
                salary_range=match.salary_range,
                education=match.education
            ))
        
        return RecommendationResponse(
            recommendations=recommendations,
            total_careers_analyzed=len(recommendation_engine.get_all_careers()),
            user_profile=user_assessment
        )
        
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error generating recommendations: {str(e)}")

@app.get("/api/categories")
async def get_career_categories():
    """Get all available career categories."""
    try:
        careers = recommendation_engine.get_all_careers()
        categories = list(set(career.get("category", "") for career in careers if career.get("category")))
        return {
            "categories": sorted(categories),
            "total_count": len(categories)
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching categories: {str(e)}")

@app.get("/api/skills")
async def get_all_skills():
    """Get all unique skills from all careers."""
    try:
        careers = recommendation_engine.get_all_careers()
        all_skills = set()
        
        for career in careers:
            skills = career.get("required_skills", [])
            all_skills.update(skills)
        
        return {
            "skills": sorted(list(all_skills)),
            "total_count": len(all_skills)
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching skills: {str(e)}")
