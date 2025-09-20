#!/usr/bin/env python3
"""
Test script for the recommendation engine.
Demonstrates how to use the /recommend endpoint.
"""

import requests
import json

# API base URL
BASE_URL = "http://localhost:8000"

def test_recommendation_endpoint():
    """Test the recommendation endpoint with sample data."""
    
    # Sample user assessment data
    sample_assessments = [
        {
            "name": "Tech Student",
            "data": {
                "skills": ["Python", "JavaScript", "Problem Solving", "Data Structures"],
                "interests": ["Technology", "Programming", "AI", "Web Development"],
                "experience_level": "Entry",
                "preferred_categories": ["Technology"]
            }
        },
        {
            "name": "Creative Professional",
            "data": {
                "skills": ["Design", "Adobe Creative Suite", "Communication", "Project Management"],
                "interests": ["Design", "Art", "Creativity", "Marketing"],
                "experience_level": "Mid",
                "preferred_categories": ["Design", "Marketing"]
            }
        },
        {
            "name": "Business Analyst",
            "data": {
                "skills": ["Data Analysis", "Excel", "SQL", "Communication", "Problem Solving"],
                "interests": ["Business", "Analytics", "Strategy", "Finance"],
                "experience_level": "Mid",
                "preferred_categories": ["Business", "Finance"]
            }
        },
        {
            "name": "Career Changer",
            "data": {
                "skills": ["Leadership", "Communication", "Project Management", "Problem Solving"],
                "interests": ["Technology", "Business", "Innovation"],
                "experience_level": "Senior",
                "preferred_categories": []
            }
        }
    ]
    
    print("🧪 Testing Recommendation Engine")
    print("=" * 50)
    
    for assessment in sample_assessments:
        print(f"\n👤 Testing: {assessment['name']}")
        print("-" * 30)
        
        try:
            # Make POST request to /recommend endpoint
            response = requests.post(
                f"{BASE_URL}/recommend",
                json=assessment["data"],
                headers={"Content-Type": "application/json"}
            )
            
            if response.status_code == 200:
                result = response.json()
                
                print(f"✅ Success! Found {len(result['recommendations'])} recommendations")
                print(f"📊 Analyzed {result['total_careers_analyzed']} careers")
                
                for i, rec in enumerate(result['recommendations'], 1):
                    print(f"\n🏆 #{i}: {rec['title']}")
                    print(f"   Category: {rec['category']}")
                    print(f"   Match Score: {rec['match_score']:.1%}")
                    print(f"   Experience Level: {rec['experience_level']}")
                    print(f"   Salary: {rec['salary_range']}")
                    print(f"   Matched Skills: {', '.join(rec['matched_skills'])}")
                    print(f"   Missing Skills: {', '.join(rec['missing_skills'])}")
                    print(f"   Description: {rec['description'][:100]}...")
                
            else:
                print(f"❌ Error: {response.status_code}")
                print(f"Response: {response.text}")
                
        except requests.exceptions.ConnectionError:
            print("❌ Connection Error: Make sure the backend is running on http://localhost:8000")
            break
        except Exception as e:
            print(f"❌ Error: {e}")

def test_other_endpoints():
    """Test other API endpoints."""
    print("\n\n🔍 Testing Other Endpoints")
    print("=" * 50)
    
    endpoints = [
        ("GET", "/", "Root endpoint"),
        ("GET", "/health", "Health check"),
        ("GET", "/api/hello", "Hello endpoint"),
        ("GET", "/api/careers", "All careers"),
        ("GET", "/api/categories", "Career categories"),
        ("GET", "/api/skills", "All skills"),
        ("GET", "/api/careers/1", "Specific career (ID: 1)")
    ]
    
    for method, endpoint, description in endpoints:
        try:
            if method == "GET":
                response = requests.get(f"{BASE_URL}{endpoint}")
            
            if response.status_code == 200:
                data = response.json()
                print(f"✅ {description}: {endpoint}")
                if isinstance(data, dict) and len(str(data)) < 200:
                    print(f"   Response: {data}")
                elif isinstance(data, list):
                    print(f"   Response: List with {len(data)} items")
                else:
                    print(f"   Response: {type(data).__name__}")
            else:
                print(f"❌ {description}: {endpoint} - Status {response.status_code}")
                
        except requests.exceptions.ConnectionError:
            print(f"❌ {description}: Connection Error")
        except Exception as e:
            print(f"❌ {description}: Error - {e}")

def main():
    """Main test function."""
    print("🚀 Recommendation Engine Test Suite")
    print("=" * 60)
    print("Make sure the FastAPI backend is running on http://localhost:8000")
    print("Start it with: cd backend && python -m uvicorn main:app --reload")
    print()
    
    # Test other endpoints first
    test_other_endpoints()
    
    # Test recommendation endpoint
    test_recommendation_endpoint()
    
    print("\n\n🎉 Test completed!")
    print("\nTo test manually:")
    print("1. Visit http://localhost:8000/docs for interactive API documentation")
    print("2. Use the /recommend endpoint with your own data")
    print("3. Try different combinations of skills and interests")

if __name__ == "__main__":
    main()
