// Test frontend connection to backend
const API_URL = process.env.NEXT_PUBLIC_API_URL || 'https://pathway-ai-backend.onrender.com';

console.log('Testing connection to:', API_URL);

async function testConnection() {
  try {
    console.log('Testing health endpoint...');
    const healthResponse = await fetch(`${API_URL}/health`);
    console.log('Health response status:', healthResponse.status);
    
    if (healthResponse.ok) {
      const healthData = await healthResponse.text();
      console.log('Health data:', healthData);
    }

    console.log('\nTesting recommend endpoint...');
    const testData = {
      skills: ["Python", "Machine Learning"],
      interests: ["Technology", "Innovation"],
      experience_level: "intermediate",
      preferred_categories: ["Technology"]
    };

    console.log('Sending request with data:', JSON.stringify(testData, null, 2));
    
    const response = await fetch(`${API_URL}/recommend`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(testData),
    });

    console.log('Recommend response status:', response.status);
    console.log('Recommend response headers:', Object.fromEntries(response.headers.entries()));

    if (response.ok) {
      const data = await response.json();
      console.log('Success! Received recommendations:', data.recommendations?.length || 0);
      console.log('Sample recommendation:', data.recommendations?.[0]?.title || 'None');
    } else {
      const errorText = await response.text();
      console.log('Error response:', errorText);
    }

  } catch (error) {
    console.error('Connection error:', error.message);
    console.error('Error type:', error.constructor.name);
  }
}

testConnection();
