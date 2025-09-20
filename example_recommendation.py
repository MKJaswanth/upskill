#!/usr/bin/env python3
"""
Simple example of using the recommendation engine directly.
This doesn't require the FastAPI server to be running.
"""

import sys
import os

# Add backend directory to path
sys.path.append(os.path.join(os.path.dirname(__file__), 'backend'))

from recommendation_engine import RecommendationEngine

def main():
    print("🎯 Recommendation Engine Example")
    print("=" * 40)
    
    # Initialize the recommendation engine
    try:
        engine = RecommendationEngine()
        print("✅ Recommendation engine initialized successfully")
    except Exception as e:
        print(f"❌ Error initializing engine: {e}")
        return
    
    # Example user assessments
    examples = [
        {
            "name": "Tech Student",
            "data": {
                "skills": ["Python", "JavaScript", "Problem Solving", "Data Structures"],
                "interests": ["Technology", "Programming", "AI"],
                "experience_level": "Entry",
                "preferred_categories": ["Technology"]
            }
        },
        {
            "name": "Creative Professional", 
            "data": {
                "skills": ["Design", "Adobe Creative Suite", "Communication"],
                "interests": ["Design", "Art", "Creativity"],
                "experience_level": "Mid",
                "preferred_categories": ["Design", "Marketing"]
            }
        },
        {
            "name": "Business Analyst",
            "data": {
                "skills": ["Data Analysis", "Excel", "SQL", "Communication"],
                "interests": ["Business", "Analytics", "Strategy"],
                "experience_level": "Mid",
                "preferred_categories": ["Business"]
            }
        }
    ]
    
    for example in examples:
        print(f"\n👤 User: {example['name']}")
        print("-" * 30)
        print(f"Skills: {', '.join(example['data']['skills'])}")
        print(f"Interests: {', '.join(example['data']['interests'])}")
        print(f"Experience: {example['data']['experience_level']}")
        
        # Get recommendations
        try:
            recommendations = engine.get_recommendations(example['data'])
            
            print(f"\n🏆 Top 3 Career Matches:")
            for i, rec in enumerate(recommendations, 1):
                print(f"\n{i}. {rec.title}")
                print(f"   Category: {rec.category}")
                print(f"   Match Score: {rec.match_score:.1%}")
                print(f"   Experience Level: {rec.experience_level}")
                print(f"   Salary: {rec.salary_range}")
                print(f"   Matched Skills: {', '.join(rec.matched_skills)}")
                print(f"   Missing Skills: {', '.join(rec.missing_skills)}")
                print(f"   Description: {rec.description[:80]}...")
                
        except Exception as e:
            print(f"❌ Error getting recommendations: {e}")
    
    print(f"\n\n📊 Available Careers: {len(engine.get_all_careers())}")
    print("✅ Example completed successfully!")

if __name__ == "__main__":
    main()
