// Simple test to check backend connection
const API_BASE_URL = 'http://localhost:8000';

async function testBackendConnection() {
  console.log('Testing backend connection...');
  
  try {
    // Test health endpoint
    const healthResponse = await fetch(`${API_BASE_URL}/health`);
    console.log('Health endpoint status:', healthResponse.status);
    
    if (healthResponse.ok) {
      const healthData = await healthResponse.json();
      console.log('Health response:', healthData);
    } else {
      console.log('Health endpoint failed');
    }
    
    // Test root endpoint
    const rootResponse = await fetch(`${API_BASE_URL}/`);
    console.log('Root endpoint status:', rootResponse.status);
    
    if (rootResponse.ok) {
      const rootData = await rootResponse.json();
      console.log('Root response:', rootData);
    } else {
      console.log('Root endpoint failed');
    }
    
    // Test recommend endpoint with sample data
    const sampleData = {
      skills: ["Python", "JavaScript"],
      interests: ["Technology"],
      experience_level: "Entry Level",
      preferred_categories: ["Technology"]
    };
    
    const recommendResponse = await fetch(`${API_BASE_URL}/recommend`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(sampleData),
    });
    
    console.log('Recommend endpoint status:', recommendResponse.status);
    
    if (recommendResponse.ok) {
      const recommendData = await recommendResponse.json();
      console.log('Recommend response keys:', Object.keys(recommendData));
    } else {
      const errorText = await recommendResponse.text();
      console.log('Recommend endpoint error:', errorText);
    }
    
  } catch (error) {
    console.error('Connection error:', error.message);
    console.log('Make sure the backend is running on http://localhost:8000');
  }
}

testBackendConnection();
