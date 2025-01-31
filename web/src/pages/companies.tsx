import Header from '../components/Layout/Header';
import Navbar from '../components/Layout/Navbar';

export default function Companies() {
  // 임시 데이터 (나중에 API 응답으로 대체)
  const companies = [
    {
      name: 'Tech Giants Inc',
      industry: 'Software Development',
      location: 'San Francisco, CA',
      matchRate: 95,
      positions: ['Senior Software Engineer', 'Full Stack Developer']
    },
    {
      name: 'Innovation Labs',
      industry: 'AI/ML',
      location: 'Seattle, WA',
      matchRate: 88,
      positions: ['ML Engineer', 'Backend Developer']
    },
    {
      name: 'Future Systems',
      industry: 'Cloud Computing',
      location: 'Austin, TX',
      matchRate: 82,
      positions: ['Cloud Architect', 'DevOps Engineer']
    }
  ];

  return (
    <div className="min-h-screen bg-gray-50">
      <Header />
      <Navbar />
      <main className="container mx-auto px-4 py-8">
        <div className="max-w-4xl mx-auto">
          <h1 className="text-3xl font-bold text-accent-navy mb-6">Recommended Companies</h1>
          <div className="space-y-4">
            {companies.map((company, index) => (
              <div key={index} className="bg-white rounded-lg shadow p-6">
                <div className="flex justify-between items-start">
                  <div>
                    <h2 className="text-xl font-semibold text-accent-navy">{company.name}</h2>
                    <p className="text-gray-600">{company.industry}</p>
                    <p className="text-gray-500 text-sm">{company.location}</p>
                    <div className="mt-3">
                      <h3 className="text-sm font-medium text-gray-700">Open Positions:</h3>
                      <ul className="mt-1 space-y-1">
                        {company.positions.map((position, idx) => (
                          <li key={idx} className="text-sm text-gray-600">{position}</li>
                        ))}
                      </ul>
                    </div>
                  </div>
                  <div className="text-right">
                    <div className="inline-flex items-center px-3 py-1 rounded-full bg-green-100">
                      <span className="text-green-800 font-medium">{company.matchRate}% Match</span>
                    </div>
                  </div>
                </div>
              </div>
            ))}
          </div>
        </div>
      </main>
    </div>
  );
} 