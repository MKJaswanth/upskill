from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
import json
import os

app = FastAPI(title="Pathway AI Backend", version="1.0.0")

# Add CORS middleware - allow all origins for production
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Pydantic models
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

# Load careers data
def load_careers_data():
    try:
        if os.path.exists("careers.json"):
            with open("careers.json", "r", encoding="utf-8") as file:
                return json.load(file)
        return []
    except Exception:
        return []

careers_data = load_careers_data()

# Add explicit OPTIONS handlers for CORS preflight requests
@app.options("/")
@app.options("/health")  
@app.options("/recommend")
@app.options("/api/careers")
@app.options("/api/categories")
@app.options("/api/skills")
async def options_handler():
    return {"message": "OK"}

@app.get("/")
async def root():
    return {"message": "Welcome to Pathway AI Backend API", "status": "running"}

@app.get("/health")
async def health_check():
    return {"status": "healthy", "message": "Backend is running", "careers_loaded": len(careers_data)}

@app.post("/recommend", response_model=RecommendationResponse)
async def get_recommendations(user_assessment: UserAssessment):
    try:
        if not user_assessment.skills and not user_assessment.interests:
            raise HTTPException(status_code=400, detail="At least one skill or interest must be provided")
        
        recommendations = []
        for career in careers_data:
            matched_skills = []
            missing_skills = []
            
            for skill in career.get("required_skills", []):
                if skill.lower() in [s.lower() for s in user_assessment.skills]:
                    matched_skills.append(skill)
                else:
                    missing_skills.append(skill)
            
            total_skills = len(career.get("required_skills", []))
            match_score = len(matched_skills) / total_skills if total_skills > 0 else 0.0
            
            if career.get("category", "").lower() in [c.lower() for c in user_assessment.preferred_categories]:
                match_score += 0.1
            
            match_score = min(1.0, max(0.0, match_score))
            
            recommendations.append(CareerRecommendation(
                id=career.get("id", 0),
                title=career.get("title", ""),
                category=career.get("category", ""),
                description=career.get("description", ""),
                match_score=round(match_score, 3),
                matched_skills=matched_skills,
                missing_skills=missing_skills,
                experience_level=career.get("experience_level", ""),
                salary_range=career.get("salary_range", ""),
                education=career.get("education", "")
            ))
        
        recommendations.sort(key=lambda x: x.match_score, reverse=True)
        
        return RecommendationResponse(
            recommendations=recommendations[:3],
            total_careers_analyzed=len(careers_data),
            user_profile=user_assessment
        )
        
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error generating recommendations: {str(e)}")

@app.get("/api/careers")
async def get_all_careers():
    return {"careers": careers_data, "total_count": len(careers_data)}

@app.get("/api/categories")
async def get_career_categories():
    categories = list(set(career.get("category", "") for career in careers_data if career.get("category")))
    return {"categories": sorted(categories), "total_count": len(categories)}

@app.get("/api/skills")
async def get_all_skills():
    all_skills = set()
    for career in careers_data:
        all_skills.update(career.get("required_skills", []))
    return {"skills": sorted(list(all_skills)), "total_count": len(all_skills)}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
