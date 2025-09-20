/**
 * API utility functions for communicating with the FastAPI backend
 */

const API_BASE_URL = process.env.NEXT_PUBLIC_API_URL || 'https://pathway-ai-backend.onrender.com';

export interface UserAssessment {
  skills: string[];
  interests: string[];
  experience_level: string;
  preferred_categories: string[];
}

export interface CareerRecommendation {
  id: number;
  title: string;
  category: string;
  description: string;
  match_score: number;
  matched_skills: string[];
  missing_skills: string[];
  experience_level: string;
  salary_range: string;
  education: string;
}

export interface RecommendationResponse {
  recommendations: CareerRecommendation[];
  total_careers_analyzed: number;
  user_profile: UserAssessment;
}

export interface ApiError {
  detail: string;
  status_code?: number;
}

/**
 * Get career recommendations from the backend
 */
export async function getRecommendations(
  assessment: UserAssessment
): Promise<RecommendationResponse> {
  try {
    const response = await fetch(`${API_BASE_URL}/recommend`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(assessment),
    });

    if (!response.ok) {
      // Check if response is HTML (error page) instead of JSON
      const contentType = response.headers.get('content-type');
      if (contentType && contentType.includes('text/html')) {
        throw new Error('Backend server is not responding properly. Please check your internet connection and ensure the backend is accessible.');
      }
      
      try {
        const errorData: ApiError = await response.json();
        throw new Error(errorData.detail || `HTTP error! status: ${response.status}`);
      } catch {
        throw new Error(`Server error: ${response.status} ${response.statusText}`);
      }
    }

    const data: RecommendationResponse = await response.json();
    return data;
  } catch (error) {
    if (error instanceof Error) {
      // Handle specific network errors
      if (error.message.includes('fetch')) {
        throw new Error('Unable to connect to the server. Please check your internet connection and ensure the backend is accessible.');
      }
      throw error;
    }
    throw new Error('An unexpected error occurred while getting recommendations');
  }
}

/**
 * Get all available careers
 */
export async function getAllCareers() {
  try {
    const response = await fetch(`${API_BASE_URL}/api/careers`);
    
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    
    return await response.json();
  } catch (error) {
    console.error('Error fetching careers:', error);
    throw new Error('Failed to fetch careers');
  }
}

/**
 * Get career categories
 */
export async function getCareerCategories() {
  try {
    const response = await fetch(`${API_BASE_URL}/api/categories`);
    
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    
    return await response.json();
  } catch (error) {
    console.error('Error fetching categories:', error);
    throw new Error('Failed to fetch categories');
  }
}

/**
 * Get all available skills
 */
export async function getAllSkills() {
  try {
    const response = await fetch(`${API_BASE_URL}/api/skills`);
    
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    
    return await response.json();
  } catch (error) {
    console.error('Error fetching skills:', error);
    throw new Error('Failed to fetch skills');
  }
}

/**
 * Check if the backend is healthy
 */
export async function checkBackendHealth(): Promise<boolean> {
  try {
    const response = await fetch(`${API_BASE_URL}/health`);
    return response.ok;
  } catch (error) {
    console.error('Backend health check failed:', error);
    return false;
  }
}

/**
 * Handle API errors with user-friendly messages
 */
export function getErrorMessage(error: unknown): string {
  if (error instanceof Error) {
    // Check for common network errors
    if (error.message.includes('fetch')) {
      return 'Unable to connect to the server. Please check your internet connection and try again.';
    }
    
    if (error.message.includes('Failed to fetch')) {
      return 'Server is not responding. Please check your internet connection and try again.';
    }
    
    return error.message;
  }
  
  return 'An unexpected error occurred. Please try again.';
}
