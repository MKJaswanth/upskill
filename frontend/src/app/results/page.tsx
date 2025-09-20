'use client';

import { useState, useEffect } from 'react';
import { useRouter } from 'next/navigation';

interface CareerRecommendation {
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

interface RecommendationResponse {
  recommendations: CareerRecommendation[];
  total_careers_analyzed: number;
  user_profile: {
    skills: string[];
    interests: string[];
    experience_level: string;
    preferred_categories: string[];
  };
}

export default function ResultsPage() {
  const router = useRouter();
  const [recommendations, setRecommendations] = useState<RecommendationResponse | null>(null);
  const [isLoading, setIsLoading] = useState(true);

  useEffect(() => {
    // Get recommendations from sessionStorage
    const storedRecommendations = sessionStorage.getItem('recommendations');
    if (storedRecommendations) {
      setRecommendations(JSON.parse(storedRecommendations));
    }
    setIsLoading(false);
  }, []);

  const handleRetakeAssessment = () => {
    sessionStorage.removeItem('recommendations');
    router.push('/assessment');
  };

  const getScoreColor = (score: number) => {
    if (score >= 0.8) return 'from-green-500 to-emerald-500';
    if (score >= 0.6) return 'from-yellow-500 to-orange-500';
    if (score >= 0.4) return 'from-orange-500 to-red-500';
    return 'from-red-500 to-red-600';
  };

  const getScoreLabel = (score: number) => {
    if (score >= 0.8) return 'Excellent Match';
    if (score >= 0.6) return 'Good Match';
    if (score >= 0.4) return 'Fair Match';
    return 'Low Match';
  };

  const getScoreIcon = (score: number) => {
    if (score >= 0.8) return '🎯';
    if (score >= 0.6) return '👍';
    if (score >= 0.4) return '⚖️';
    return '📈';
  };

  if (isLoading) {
    return (
      <div className="min-h-screen bg-gradient-to-br from-blue-50 to-indigo-100 flex items-center justify-center">
        <div className="text-center">
          <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-blue-600 mx-auto mb-4"></div>
          <p className="text-gray-600">Loading your results...</p>
        </div>
      </div>
    );
  }

  if (!recommendations) {
    return (
      <div className="min-h-screen bg-gradient-to-br from-blue-50 to-indigo-100 flex items-center justify-center p-4">
        <div className="text-center max-w-md mx-auto">
          <div className="bg-white rounded-lg shadow-lg p-8">
            <h1 className="text-2xl font-bold text-gray-900 mb-4">No Results Found</h1>
            <p className="text-gray-600 mb-6">
              It looks like you haven&apos;t completed an assessment yet. Let&apos;s get started!
            </p>
            <button
              onClick={() => router.push('/assessment')}
              className="w-full bg-blue-600 hover:bg-blue-700 text-white font-semibold py-3 px-6 rounded-lg transition-colors"
            >
              Take Assessment
            </button>
          </div>
        </div>
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-50 to-indigo-100">
      {/* Header */}
      <div className="bg-white shadow-sm sticky top-0 z-10">
        <div className="max-w-4xl mx-auto px-4 py-4">
          <div className="flex items-center justify-between">
            <div>
              <h1 className="text-2xl font-bold text-gray-900">Your Career Matches</h1>
              <p className="text-gray-600 text-sm">Based on your assessment</p>
            </div>
            <button
              onClick={handleRetakeAssessment}
              className="bg-blue-600 hover:bg-blue-700 text-white font-medium py-2 px-4 rounded-lg transition-colors text-sm"
            >
              Retake Assessment
            </button>
          </div>
        </div>
      </div>

      {/* Main Content */}
      <div className="max-w-4xl mx-auto px-4 py-6">
        {/* Summary Stats */}
        <div className="bg-white rounded-lg shadow-sm p-4 mb-6">
          <div className="grid grid-cols-3 gap-4 text-center">
            <div>
              <div className="text-2xl font-bold text-blue-600">{recommendations.recommendations.length}</div>
              <div className="text-xs text-gray-600">Top Matches</div>
            </div>
            <div>
              <div className="text-2xl font-bold text-green-600">{recommendations.total_careers_analyzed}</div>
              <div className="text-xs text-gray-600">Careers Analyzed</div>
            </div>
            <div>
              <div className="text-2xl font-bold text-purple-600">
                {recommendations.user_profile.skills.length + recommendations.user_profile.interests.length}
              </div>
              <div className="text-xs text-gray-600">Skills & Interests</div>
            </div>
          </div>
        </div>

        {/* Career Recommendations */}
        <div className="space-y-4">
          {recommendations.recommendations.map((rec, index) => (
            <div key={rec.id} className="bg-white rounded-lg shadow-sm overflow-hidden">
              {/* Card Header */}
              <div className={`bg-gradient-to-r ${getScoreColor(rec.match_score)} p-4 text-white`}>
                <div className="flex items-center justify-between">
                  <div className="flex items-center space-x-3">
                    <span className="bg-white bg-opacity-20 px-2 py-1 rounded-full text-sm font-medium">
                      #{index + 1}
                    </span>
                    <div>
                      <h2 className="text-lg font-bold">{rec.title}</h2>
                      <p className="text-sm opacity-90">{rec.category}</p>
                    </div>
                  </div>
                  <div className="text-right">
                    <div className="text-2xl font-bold">
                      {(rec.match_score * 100).toFixed(0)}%
                    </div>
                    <div className="text-sm opacity-90 flex items-center">
                      <span className="mr-1">{getScoreIcon(rec.match_score)}</span>
                      {getScoreLabel(rec.match_score)}
                    </div>
                  </div>
                </div>
              </div>

              {/* Card Content */}
              <div className="p-4">
                {/* Description */}
                <p className="text-gray-600 text-sm mb-4 leading-relaxed">
                  {rec.description}
                </p>

                {/* Key Info */}
                <div className="grid grid-cols-1 sm:grid-cols-3 gap-3 mb-4">
                  <div className="bg-gray-50 rounded-lg p-3">
                    <div className="text-xs font-medium text-gray-500 mb-1">Experience</div>
                    <div className="text-sm text-gray-800">{rec.experience_level}</div>
                  </div>
                  <div className="bg-gray-50 rounded-lg p-3">
                    <div className="text-xs font-medium text-gray-500 mb-1">Salary Range</div>
                    <div className="text-sm text-gray-800">{rec.salary_range}</div>
                  </div>
                  <div className="bg-gray-50 rounded-lg p-3">
                    <div className="text-xs font-medium text-gray-500 mb-1">Education</div>
                    <div className="text-sm text-gray-800">{rec.education}</div>
                  </div>
                </div>

                {/* Skills Section */}
                <div className="space-y-3">
                  {/* Matched Skills */}
                  {rec.matched_skills.length > 0 && (
                    <div>
                      <div className="flex items-center mb-2">
                        <span className="text-sm font-medium text-green-700">✓ Your Matching Skills</span>
                        <span className="ml-2 bg-green-100 text-green-800 text-xs px-2 py-1 rounded-full">
                          {rec.matched_skills.length}
                        </span>
                      </div>
                      <div className="flex flex-wrap gap-2">
                        {rec.matched_skills.map((skill, idx) => (
                          <span
                            key={idx}
                            className="bg-green-100 text-green-800 px-3 py-1 rounded-full text-sm font-medium"
                          >
                            {skill}
                          </span>
                        ))}
                      </div>
                    </div>
                  )}

                  {/* Missing Skills */}
                  {rec.missing_skills.length > 0 && (
                    <div>
                      <div className="flex items-center mb-2">
                        <span className="text-sm font-medium text-orange-700">+ Skills to Develop</span>
                        <span className="ml-2 bg-orange-100 text-orange-800 text-xs px-2 py-1 rounded-full">
                          {rec.missing_skills.length}
                        </span>
                      </div>
                      <div className="flex flex-wrap gap-2">
                        {rec.missing_skills.map((skill, idx) => (
                          <span
                            key={idx}
                            className="bg-orange-100 text-orange-800 px-3 py-1 rounded-full text-sm font-medium"
                          >
                            {skill}
                          </span>
                        ))}
                      </div>
                    </div>
                  )}

                  {/* No Missing Skills */}
                  {rec.missing_skills.length === 0 && rec.matched_skills.length > 0 && (
                    <div className="bg-green-50 border border-green-200 rounded-lg p-3">
                      <div className="flex items-center">
                        <span className="text-green-600 mr-2">🎉</span>
                        <span className="text-green-800 text-sm font-medium">
                          Great! You have all the required skills for this career.
                        </span>
                      </div>
                    </div>
                  )}
                </div>
              </div>
            </div>
          ))}
        </div>

        {/* User Profile Summary */}
        <div className="bg-white rounded-lg shadow-sm p-4 mt-6">
          <h3 className="text-lg font-semibold text-gray-800 mb-3">Your Assessment Summary</h3>
          <div className="space-y-3">
            <div>
              <div className="text-sm font-medium text-gray-700 mb-2">
                Skills ({recommendations.user_profile.skills.length})
              </div>
              <div className="flex flex-wrap gap-2">
                {recommendations.user_profile.skills.map((skill, idx) => (
                  <span
                    key={idx}
                    className="bg-blue-100 text-blue-800 px-2 py-1 rounded text-xs"
                  >
                    {skill}
                  </span>
                ))}
              </div>
            </div>
            <div>
              <div className="text-sm font-medium text-gray-700 mb-2">
                Interests ({recommendations.user_profile.interests.length})
              </div>
              <div className="flex flex-wrap gap-2">
                {recommendations.user_profile.interests.map((interest, idx) => (
                  <span
                    key={idx}
                    className="bg-purple-100 text-purple-800 px-2 py-1 rounded text-xs"
                  >
                    {interest}
                  </span>
                ))}
              </div>
            </div>
            <div>
              <div className="text-sm font-medium text-gray-700 mb-1">Experience Level</div>
              <span className="bg-gray-100 text-gray-800 px-3 py-1 rounded-full text-sm">
                {recommendations.user_profile.experience_level}
              </span>
            </div>
          </div>
        </div>

        {/* Action Buttons */}
        <div className="flex flex-col sm:flex-row gap-3 mt-6">
          <button
            onClick={handleRetakeAssessment}
            className="flex-1 bg-blue-600 hover:bg-blue-700 text-white font-semibold py-3 px-6 rounded-lg transition-colors"
          >
            Retake Assessment
          </button>
          <button
            onClick={() => router.push('/')}
            className="flex-1 bg-gray-600 hover:bg-gray-700 text-white font-semibold py-3 px-6 rounded-lg transition-colors"
          >
            Back to Home
          </button>
        </div>
      </div>
    </div>
  );
}