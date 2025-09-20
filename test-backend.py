import requests
import json

def test_backend():
    base_url = "http://localhost:8000"
    
    print("Testing backend endpoints...")
    
    # Test health endpoint
    try:
        response = requests.get(f"{base_url}/health")
        print(f"Health endpoint: {response.status_code}")
        if response.status_code == 200:
            print(f"Response: {response.json()}")
        else:
            print(f"Error: {response.text}")
    except Exception as e:
        print(f"Health endpoint error: {e}")
    
    # Test root endpoint
    try:
        response = requests.get(f"{base_url}/")
        print(f"Root endpoint: {response.status_code}")
        if response.status_code == 200:
            print(f"Response: {response.json()}")
        else:
            print(f"Error: {response.text}")
    except Exception as e:
        print(f"Root endpoint error: {e}")
    
    # Test recommend endpoint
    try:
        test_data = {
            "skills": ["Python", "JavaScript"],
            "interests": ["Technology"],
            "experience_level": "Entry Level",
            "preferred_categories": ["Technology"]
        }
        
        response = requests.post(
            f"{base_url}/recommend",
            json=test_data,
            headers={"Content-Type": "application/json"}
        )
        print(f"Recommend endpoint: {response.status_code}")
        if response.status_code == 200:
            data = response.json()
            print(f"Recommendations: {len(data.get('recommendations', []))}")
        else:
            print(f"Error: {response.text}")
    except Exception as e:
        print(f"Recommend endpoint error: {e}")

if __name__ == "__main__":
    test_backend()
