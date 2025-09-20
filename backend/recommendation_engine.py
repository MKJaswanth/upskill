"""
Recommendation Engine Module
Computes match scores between user responses and career requirements.
"""

import json
import os
from typing import List, Dict, Any, Tuple
from dataclasses import dataclass
import math

@dataclass
class CareerMatch:
    """Data class for career match results."""
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

class RecommendationEngine:
    """Engine for computing career recommendations based on user input."""
    
    def __init__(self, careers_file: str = "../careers.json"):
        """Initialize the recommendation engine with careers data."""
        self.careers_data = self._load_careers_data(careers_file)
        self.skill_synonyms = self._create_skill_synonyms()
    
    def _load_careers_data(self, file_path: str) -> List[Dict[str, Any]]:
        """Load careers data from JSON file."""
        try:
            # Try relative path first
            if os.path.exists(file_path):
                with open(file_path, 'r', encoding='utf-8') as file:
                    return json.load(file)
            
            # Try absolute path from current directory
            current_dir = os.path.dirname(os.path.abspath(__file__))
            absolute_path = os.path.join(current_dir, file_path)
            
            if os.path.exists(absolute_path):
                with open(absolute_path, 'r', encoding='utf-8') as file:
                    return json.load(file)
            
            # Try from project root
            project_root = os.path.join(current_dir, '..')
            root_path = os.path.join(project_root, 'careers.json')
            
            if os.path.exists(root_path):
                with open(root_path, 'r', encoding='utf-8') as file:
                    return json.load(file)
            
            raise FileNotFoundError(f"Careers file not found: {file_path}")
            
        except Exception as e:
            print(f"Error loading careers data: {e}")
            return []
    
    def _create_skill_synonyms(self) -> Dict[str, List[str]]:
        """Create a mapping of skill synonyms for better matching."""
        return {
            "programming": ["coding", "development", "software development", "programming languages"],
            "python": ["python programming", "python development"],
            "javascript": ["js", "javascript programming", "web development"],
            "data analysis": ["analytics", "data analytics", "statistical analysis"],
            "machine learning": ["ml", "ai", "artificial intelligence", "deep learning"],
            "design": ["ui design", "ux design", "graphic design", "visual design"],
            "marketing": ["digital marketing", "online marketing", "brand marketing"],
            "communication": ["verbal communication", "written communication", "presentation"],
            "leadership": ["team leadership", "management", "team management"],
            "problem solving": ["analytical thinking", "critical thinking", "troubleshooting"],
            "project management": ["project planning", "agile", "scrum", "project coordination"],
            "database": ["sql", "database management", "data storage"],
            "web development": ["frontend", "backend", "full stack", "web programming"],
            "mobile development": ["ios", "android", "mobile apps", "app development"],
            "cloud computing": ["aws", "azure", "google cloud", "cloud platforms"],
            "cybersecurity": ["security", "information security", "network security"],
            "devops": ["deployment", "ci/cd", "infrastructure", "automation"],
            "testing": ["qa", "quality assurance", "test automation", "software testing"],
            "business analysis": ["requirements analysis", "business requirements", "process analysis"],
            "sales": ["business development", "client relations", "customer acquisition"],
            "finance": ["financial analysis", "accounting", "financial modeling"],
            "content creation": ["content writing", "copywriting", "content strategy"],
            "social media": ["social media marketing", "community management", "social platforms"],
            "research": ["market research", "user research", "data research"],
            "creativity": ["creative thinking", "innovation", "design thinking"]
        }
    
    def _normalize_skill(self, skill: str) -> str:
        """Normalize skill name for better matching."""
        skill_lower = skill.lower().strip()
        
        # Check if skill is a synonym key
        for main_skill, synonyms in self.skill_synonyms.items():
            if skill_lower == main_skill or skill_lower in synonyms:
                return main_skill
        
        return skill_lower
    
    def _calculate_skill_match_score(self, user_skills: List[str], career_skills: List[str]) -> Tuple[float, List[str], List[str]]:
        """Calculate match score between user skills and career requirements."""
        if not career_skills:
            return 0.0, [], []
        
        user_skills_normalized = [self._normalize_skill(skill) for skill in user_skills]
        career_skills_normalized = [self._normalize_skill(skill) for skill in career_skills]
        
        matched_skills = []
        missing_skills = []
        
        # Find exact matches
        for career_skill in career_skills_normalized:
            if career_skill in user_skills_normalized:
                matched_skills.append(career_skill)
            else:
                missing_skills.append(career_skill)
        
        # Calculate partial matches using fuzzy matching
        for career_skill in career_skills_normalized:
            if career_skill not in matched_skills:
                for user_skill in user_skills_normalized:
                    if self._is_skill_related(career_skill, user_skill):
                        if career_skill not in matched_skills:
                            matched_skills.append(career_skill)
                        if career_skill in missing_skills:
                            missing_skills.remove(career_skill)
        
        # Calculate score (percentage of matched skills)
        match_score = len(matched_skills) / len(career_skills_normalized)
        
        return match_score, matched_skills, missing_skills
    
    def _is_skill_related(self, skill1: str, skill2: str) -> bool:
        """Check if two skills are related using various methods."""
        # Check if one skill contains the other
        if skill1 in skill2 or skill2 in skill1:
            return True
        
        # Check for common keywords
        common_keywords = ["programming", "development", "analysis", "design", "management", "marketing"]
        for keyword in common_keywords:
            if keyword in skill1 and keyword in skill2:
                return True
        
        return False
    
    def _calculate_interest_match_score(self, user_interests: List[str], career_category: str) -> float:
        """Calculate match score based on user interests and career category."""
        if not user_interests:
            return 0.5  # Neutral score if no interests provided
        
        category_lower = career_category.lower()
        interest_matches = 0
        
        for interest in user_interests:
            interest_lower = interest.lower()
            
            # Direct category match
            if interest_lower == category_lower:
                interest_matches += 1
            # Related category matches
            elif self._is_interest_related(interest_lower, category_lower):
                interest_matches += 0.7
        
        return min(interest_matches / len(user_interests), 1.0)
    
    def _is_interest_related(self, interest: str, category: str) -> bool:
        """Check if interest is related to career category."""
        interest_category_mapping = {
            "technology": ["programming", "computers", "software", "tech", "coding", "ai", "data"],
            "design": ["art", "creativity", "visual", "graphics", "ui", "ux", "aesthetics"],
            "marketing": ["advertising", "promotion", "social media", "branding", "communication"],
            "business": ["management", "leadership", "strategy", "entrepreneurship", "finance"],
            "finance": ["money", "investment", "banking", "accounting", "economics"],
            "sales": ["selling", "negotiation", "customer service", "business development"],
            "human resources": ["people", "hiring", "training", "workplace", "employee relations"]
        }
        
        if category in interest_category_mapping:
            return any(keyword in interest for keyword in interest_category_mapping[category])
        
        return False
    
    def _calculate_experience_bonus(self, user_experience: str, career_experience: str) -> float:
        """Calculate bonus score based on experience level match."""
        if not user_experience or not career_experience:
            return 0.0
        
        user_exp_lower = user_experience.lower()
        career_exp_lower = career_experience.lower()
        
        # Exact match
        if user_exp_lower in career_exp_lower or career_exp_lower in user_exp_lower:
            return 0.2
        
        # Experience level hierarchy
        exp_levels = {"entry": 1, "junior": 1, "mid": 2, "senior": 3, "lead": 4, "principal": 5}
        
        user_level = 0
        career_level = 0
        
        for level, value in exp_levels.items():
            if level in user_exp_lower:
                user_level = value
            if level in career_exp_lower:
                career_level = value
        
        if user_level > 0 and career_level > 0:
            # Bonus for having more experience than required
            if user_level >= career_level:
                return 0.15
            # Small penalty for having less experience
            else:
                return -0.1
        
        return 0.0
    
    def get_recommendations(self, user_data: Dict[str, Any]) -> List[CareerMatch]:
        """
        Get career recommendations based on user data.
        
        Args:
            user_data: Dictionary containing user responses
                - skills: List of user skills
                - interests: List of user interests
                - experience_level: User's experience level
                - preferred_categories: List of preferred career categories (optional)
        
        Returns:
            List of CareerMatch objects sorted by match score (descending)
        """
        if not self.careers_data:
            return []
        
        user_skills = user_data.get("skills", [])
        user_interests = user_data.get("interests", [])
        user_experience = user_data.get("experience_level", "")
        preferred_categories = user_data.get("preferred_categories", [])
        
        career_matches = []
        
        for career in self.careers_data:
            # Calculate skill match score
            skill_score, matched_skills, missing_skills = self._calculate_skill_match_score(
                user_skills, career.get("required_skills", [])
            )
            
            # Calculate interest match score
            interest_score = self._calculate_interest_match_score(
                user_interests, career.get("category", "")
            )
            
            # Calculate experience bonus
            experience_bonus = self._calculate_experience_bonus(
                user_experience, career.get("experience_level", "")
            )
            
            # Category preference bonus
            category_bonus = 0.0
            if preferred_categories and career.get("category", "") in preferred_categories:
                category_bonus = 0.1
            
            # Calculate final match score
            # Weight: 60% skills, 30% interests, 10% experience + bonuses
            final_score = (
                skill_score * 0.6 +
                interest_score * 0.3 +
                experience_bonus +
                category_bonus
            )
            
            # Ensure score is between 0 and 1
            final_score = max(0.0, min(1.0, final_score))
            
            # Create CareerMatch object
            career_match = CareerMatch(
                id=career.get("id", 0),
                title=career.get("title", ""),
                category=career.get("category", ""),
                description=career.get("description", ""),
                match_score=round(final_score, 3),
                matched_skills=matched_skills,
                missing_skills=missing_skills,
                experience_level=career.get("experience_level", ""),
                salary_range=career.get("salary_range", ""),
                education=career.get("education", "")
            )
            
            career_matches.append(career_match)
        
        # Sort by match score (descending) and return top 3
        career_matches.sort(key=lambda x: x.match_score, reverse=True)
        return career_matches[:3]
    
    def get_career_by_id(self, career_id: int) -> Dict[str, Any]:
        """Get career details by ID."""
        for career in self.careers_data:
            if career.get("id") == career_id:
                return career
        return {}
    
    def get_all_careers(self) -> List[Dict[str, Any]]:
        """Get all careers data."""
        return self.careers_data
