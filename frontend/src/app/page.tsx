import Link from "next/link";
import BackendStatus from "../components/BackendStatus";

export default function Home() {
  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-50 to-indigo-100">
      {/* Header */}
      <header className="bg-white shadow-sm">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="flex justify-between items-center py-6">
            <div className="flex items-center">
              <h1 className="text-2xl font-bold text-gray-900">Pathway AI</h1>
            </div>
            <div className="flex items-center space-x-8">
              <nav className="flex space-x-8">
                <Link href="/assessment" className="text-gray-600 hover:text-gray-900 font-medium">
                  Assessment
                </Link>
                <Link href="/results" className="text-gray-600 hover:text-gray-900 font-medium">
                  Results
                </Link>
                <Link href="/results/demo" className="text-gray-600 hover:text-gray-900 font-medium">
                  Demo
                </Link>
              </nav>
              <BackendStatus />
            </div>
          </div>
        </div>
      </header>

      {/* Hero Section */}
      <main className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-16">
        <div className="text-center">
          <h1 className="text-5xl font-bold text-gray-900 mb-6">
            Discover Your Perfect Career Path
          </h1>
          <p className="text-xl text-gray-600 mb-8 max-w-3xl mx-auto">
            Get personalized career recommendations based on your skills, interests, and experience. 
            Our AI-powered assessment analyzes 25+ diverse career paths to find your best matches.
          </p>
          
          <div className="flex flex-col sm:flex-row gap-4 justify-center">
            <Link
              href="/assessment"
              className="bg-blue-600 hover:bg-blue-700 text-white font-semibold py-4 px-8 rounded-lg text-lg transition-colors shadow-lg hover:shadow-xl"
            >
              Start Assessment
            </Link>
            <Link
              href="/results/demo"
              className="bg-green-600 hover:bg-green-700 text-white font-semibold py-4 px-8 rounded-lg text-lg transition-colors shadow-lg hover:shadow-xl"
            >
              View Demo Results
            </Link>
            <Link
              href="/results"
              className="bg-white hover:bg-gray-50 text-gray-700 font-semibold py-4 px-8 rounded-lg text-lg transition-colors border-2 border-gray-300 hover:border-gray-400"
            >
              View Results
            </Link>
          </div>
        </div>

        {/* Features Section */}
        <div className="mt-20">
          <h2 className="text-3xl font-bold text-center text-gray-900 mb-12">
            How It Works
          </h2>
          <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
            <div className="text-center">
              <div className="bg-blue-100 w-16 h-16 rounded-full flex items-center justify-center mx-auto mb-4">
                <span className="text-2xl">📝</span>
              </div>
              <h3 className="text-xl font-semibold text-gray-900 mb-2">Take Assessment</h3>
              <p className="text-gray-600">
                Complete a comprehensive assessment covering your skills, interests, and experience level.
              </p>
            </div>
            <div className="text-center">
              <div className="bg-green-100 w-16 h-16 rounded-full flex items-center justify-center mx-auto mb-4">
                <span className="text-2xl">🤖</span>
              </div>
              <h3 className="text-xl font-semibold text-gray-900 mb-2">AI Analysis</h3>
              <p className="text-gray-600">
                Our recommendation engine analyzes your profile against 25+ career paths using advanced matching algorithms.
              </p>
            </div>
            <div className="text-center">
              <div className="bg-purple-100 w-16 h-16 rounded-full flex items-center justify-center mx-auto mb-4">
                <span className="text-2xl">🎯</span>
              </div>
              <h3 className="text-xl font-semibold text-gray-900 mb-2">Get Results</h3>
              <p className="text-gray-600">
                Receive your top 3 career matches with detailed scores, skill gaps, and development recommendations.
              </p>
            </div>
          </div>
        </div>

        {/* Stats Section */}
        <div className="mt-20 bg-white rounded-lg shadow-lg p-8">
          <h2 className="text-3xl font-bold text-center text-gray-900 mb-8">
            Why Choose Pathway AI?
          </h2>
          <div className="grid grid-cols-1 md:grid-cols-4 gap-8 text-center">
            <div>
              <div className="text-3xl font-bold text-blue-600 mb-2">25+</div>
              <div className="text-gray-600">Career Paths</div>
            </div>
            <div>
              <div className="text-3xl font-bold text-green-600 mb-2">100+</div>
              <div className="text-gray-600">Skills Analyzed</div>
            </div>
            <div>
              <div className="text-3xl font-bold text-purple-600 mb-2">85%</div>
              <div className="text-gray-600">Accuracy Rate</div>
            </div>
            <div>
              <div className="text-3xl font-bold text-orange-600 mb-2">5min</div>
              <div className="text-gray-600">Assessment Time</div>
            </div>
          </div>
        </div>
      </main>

      {/* Footer */}
      <footer className="bg-white border-t mt-20">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
          <div className="text-center text-gray-600">
            <p>&copy; 2024 Pathway AI - Smart India Hackathon Project</p>
            <p className="mt-2">Empowering career decisions through AI-driven insights</p>
          </div>
        </div>
      </footer>
    </div>
  );
}
