'use client';

import { useState } from 'react';
import { useRouter } from 'next/navigation';

interface UserAssessment {
  skills: string[];
  interests: string[];
  experience_level: string;
  preferred_categories: string[];
}

const SKILLS_OPTIONS = [
  'Programming', 'Python', 'JavaScript', 'Java', 'C++', 'React', 'Node.js',
  'Data Analysis', 'SQL', 'Excel', 'Statistics', 'Machine Learning',
  'Design', 'Figma', 'Adobe Creative Suite', 'UI/UX Design', 'Graphic Design',
  'Marketing', 'SEO/SEM', 'Social Media Marketing', 'Content Marketing',
  'Project Management', 'Agile/Scrum', 'Leadership', 'Communication',
  'Problem Solving', 'Critical Thinking', 'Analytical Thinking',
  'Database Management', 'Cloud Computing', 'DevOps', 'Cybersecurity',
  'Business Analysis', 'Financial Analysis', 'Sales', 'Customer Service',
  'Research', 'Writing', 'Presentation', 'Team Management'
];

const INTERESTS_OPTIONS = [
  'Technology', 'Programming', 'Software Development', 'AI/Machine Learning',
  'Data Science', 'Web Development', 'Mobile Development', 'Game Development',
  'Design', 'Art', 'Creativity', 'User Experience', 'Visual Design',
  'Marketing', 'Digital Marketing', 'Social Media', 'Branding',
  'Business', 'Entrepreneurship', 'Strategy', 'Finance', 'Investment',
  'Sales', 'Customer Relations', 'Business Development',
  'Education', 'Teaching', 'Training', 'Research', 'Writing',
  'Healthcare', 'Medicine', 'Psychology', 'Counseling',
  'Engineering', 'Architecture', 'Construction', 'Manufacturing',
  'Media', 'Journalism', 'Photography', 'Video Production',
  'Sports', 'Fitness', 'Wellness', 'Travel', 'Food', 'Music'
];

const EXPERIENCE_LEVELS = [
  'Entry Level (0-2 years)',
  'Mid Level (3-5 years)',
  'Senior Level (6+ years)',
  'Lead/Principal (8+ years)'
];

const CATEGORIES = [
  'Technology', 'Design', 'Marketing', 'Business', 'Finance', 
  'Sales', 'Human Resources', 'Healthcare', 'Education', 'Engineering'
];

export default function AssessmentPage() {
  const router = useRouter();
  const [formData, setFormData] = useState<UserAssessment>({
    skills: [],
    interests: [],
    experience_level: '',
    preferred_categories: []
  });
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const handleSkillToggle = (skill: string) => {
    setFormData(prev => ({
      ...prev,
      skills: prev.skills.includes(skill)
        ? prev.skills.filter(s => s !== skill)
        : [...prev.skills, skill]
    }));
  };

  const handleInterestToggle = (interest: string) => {
    setFormData(prev => ({
      ...prev,
      interests: prev.interests.includes(interest)
        ? prev.interests.filter(i => i !== interest)
        : [...prev.interests, interest]
    }));
  };

  const handleCategoryToggle = (category: string) => {
    setFormData(prev => ({
      ...prev,
      preferred_categories: prev.preferred_categories.includes(category)
        ? prev.preferred_categories.filter(c => c !== category)
        : [...prev.preferred_categories, category]
    }));
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    
    // Validation
    if (formData.skills.length === 0 && formData.interests.length === 0) {
      setError('Please select at least one skill or interest.');
      return;
    }

    if (!formData.experience_level) {
      setError('Please select your experience level.');
      return;
    }

    setIsLoading(true);
    setError(null);

    try {
      const apiUrl = process.env.NEXT_PUBLIC_API_URL || 'https://pathway-ai-backend.onrender.com';
      console.log('Using API URL:', apiUrl);
      console.log('Form data being sent:', formData);
      
      const response = await fetch(`${apiUrl}/recommend`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(formData),
      });

      if (!response.ok) {
        // Check if response is HTML (error page) instead of JSON
        const contentType = response.headers.get('content-type');
        if (contentType && contentType.includes('text/html')) {
          throw new Error('Backend server is not responding properly. Please check your internet connection and ensure the backend is accessible.');
        }
        
        try {
          const errorData = await response.json();
          throw new Error(errorData.detail || 'Failed to get recommendations');
        } catch {
          throw new Error(`Server error: ${response.status} ${response.statusText}`);
        }
      }

      const recommendations = await response.json();
      
      // Store results in sessionStorage and navigate to results page
      sessionStorage.setItem('recommendations', JSON.stringify(recommendations));
      router.push('/results');
      
    } catch (err) {
      console.error('Assessment error:', err);
      if (err instanceof Error) {
        console.error('Error message:', err.message);
        console.error('Error name:', err.name);
        // Handle specific network errors
        if (err.message.includes('fetch') || err.message.includes('Failed to fetch')) {
          setError('Unable to connect to the server. Please check your internet connection and ensure the backend is accessible.');
        } else {
          setError(err.message);
        }
      } else {
        setError('An error occurred while getting recommendations');
      }
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-50 to-indigo-100 py-8 px-4">
      <div className="max-w-4xl mx-auto">
        {/* Header */}
        <div className="text-center mb-8">
          <h1 className="text-4xl font-bold text-gray-900 mb-4">
            Career Assessment
          </h1>
          <p className="text-lg text-gray-600 max-w-2xl mx-auto">
            Tell us about your skills, interests, and experience to get personalized career recommendations.
          </p>
        </div>

        {/* Form */}
        <form onSubmit={handleSubmit} className="bg-white rounded-lg shadow-lg p-8">
          {/* Skills Section */}
          <div className="mb-8">
            <h2 className="text-2xl font-semibold text-gray-800 mb-4">
              Skills & Expertise
            </h2>
            <p className="text-gray-600 mb-4">
              Select all the skills you have or are familiar with:
            </p>
            <div className="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-3">
              {SKILLS_OPTIONS.map((skill) => (
                <button
                  key={skill}
                  type="button"
                  onClick={() => handleSkillToggle(skill)}
                  className={`px-4 py-2 rounded-lg border-2 transition-all duration-200 ${
                    formData.skills.includes(skill)
                      ? 'bg-blue-500 border-blue-500 text-white'
                      : 'bg-white border-gray-300 text-gray-700 hover:border-blue-300'
                  }`}
                >
                  {skill}
                </button>
              ))}
            </div>
            {formData.skills.length > 0 && (
              <p className="text-sm text-gray-500 mt-2">
                Selected: {formData.skills.length} skills
              </p>
            )}
          </div>

          {/* Interests Section */}
          <div className="mb-8">
            <h2 className="text-2xl font-semibold text-gray-800 mb-4">
              Interests & Passions
            </h2>
            <p className="text-gray-600 mb-4">
              What areas are you most interested in or passionate about?
            </p>
            <div className="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-3">
              {INTERESTS_OPTIONS.map((interest) => (
                <button
                  key={interest}
                  type="button"
                  onClick={() => handleInterestToggle(interest)}
                  className={`px-4 py-2 rounded-lg border-2 transition-all duration-200 ${
                    formData.interests.includes(interest)
                      ? 'bg-green-500 border-green-500 text-white'
                      : 'bg-white border-gray-300 text-gray-700 hover:border-green-300'
                  }`}
                >
                  {interest}
                </button>
              ))}
            </div>
            {formData.interests.length > 0 && (
              <p className="text-sm text-gray-500 mt-2">
                Selected: {formData.interests.length} interests
              </p>
            )}
          </div>

          {/* Experience Level */}
          <div className="mb-8">
            <h2 className="text-2xl font-semibold text-gray-800 mb-4">
              Experience Level
            </h2>
            <p className="text-gray-600 mb-4">
              What&apos;s your current experience level?
            </p>
            <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
              {EXPERIENCE_LEVELS.map((level) => (
                <button
                  key={level}
                  type="button"
                  onClick={() => setFormData(prev => ({ ...prev, experience_level: level }))}
                  className={`p-4 rounded-lg border-2 transition-all duration-200 text-left ${
                    formData.experience_level === level
                      ? 'bg-purple-500 border-purple-500 text-white'
                      : 'bg-white border-gray-300 text-gray-700 hover:border-purple-300'
                  }`}
                >
                  {level}
                </button>
              ))}
            </div>
          </div>

          {/* Preferred Categories */}
          <div className="mb-8">
            <h2 className="text-2xl font-semibold text-gray-800 mb-4">
              Preferred Career Categories
            </h2>
            <p className="text-gray-600 mb-4">
              Which career categories interest you most? (Optional)
            </p>
            <div className="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-5 gap-3">
              {CATEGORIES.map((category) => (
                <button
                  key={category}
                  type="button"
                  onClick={() => handleCategoryToggle(category)}
                  className={`px-4 py-2 rounded-lg border-2 transition-all duration-200 ${
                    formData.preferred_categories.includes(category)
                      ? 'bg-orange-500 border-orange-500 text-white'
                      : 'bg-white border-gray-300 text-gray-700 hover:border-orange-300'
                  }`}
                >
                  {category}
                </button>
              ))}
            </div>
            {formData.preferred_categories.length > 0 && (
              <p className="text-sm text-gray-500 mt-2">
                Selected: {formData.preferred_categories.length} categories
              </p>
            )}
          </div>

          {/* Error Message */}
          {error && (
            <div className="mb-6 p-4 bg-red-100 border border-red-400 text-red-700 rounded-lg">
              {error}
            </div>
          )}

          {/* Submit Button */}
          <div className="text-center">
            <button
              type="submit"
              disabled={isLoading}
              className={`px-8 py-4 rounded-lg font-semibold text-lg transition-all duration-200 ${
                isLoading
                  ? 'bg-gray-400 cursor-not-allowed'
                  : 'bg-blue-600 hover:bg-blue-700 text-white shadow-lg hover:shadow-xl'
              }`}
            >
              {isLoading ? (
                <div className="flex items-center justify-center">
                  <svg className="animate-spin -ml-1 mr-3 h-5 w-5 text-white" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
                    <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4"></circle>
                    <path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
                  </svg>
                  Getting Recommendations...
                </div>
              ) : (
                'Get My Career Recommendations'
              )}
            </button>
          </div>
        </form>

        {/* Navigation */}
        <div className="text-center mt-8">
          <button
            onClick={() => router.push('/')}
            className="text-blue-600 hover:text-blue-800 font-medium"
          >
            ← Back to Home
          </button>
        </div>
      </div>
    </div>
  );
}
