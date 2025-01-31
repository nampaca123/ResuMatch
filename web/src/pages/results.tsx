import Header from '../components/Layout/Header';
import Navbar from '../components/Layout/Navbar';

export default function Results() {
  // 임시 데이터 (나중에 API 응답으로 대체)
  const analysis = {
    skills: ['React', 'TypeScript', 'Python', 'AWS'],
    experience: [
      { title: 'Senior Developer', company: 'Tech Corp', duration: '2020-2023' },
      { title: 'Full Stack Developer', company: 'StartUp Inc', duration: '2018-2020' }
    ],
    recommendations: [
      'Consider highlighting cloud computing skills',
      'Add more details about leadership experience',
      'Include certifications section'
    ]
  };

  return (
    <div className="min-h-screen bg-gray-50">
      <Header />
      <Navbar />
      <main className="container mx-auto px-4 py-8">
        <div className="max-w-3xl mx-auto space-y-6">
          <div className="bg-white rounded-lg shadow p-6">
            <h2 className="text-2xl font-bold text-accent-navy mb-4">Skills Analysis</h2>
            <div className="flex flex-wrap gap-2">
              {analysis.skills.map((skill, index) => (
                <span key={index} className="px-3 py-1 bg-blue-100 text-accent-navy rounded-full">
                  {skill}
                </span>
              ))}
            </div>
          </div>

          <div className="bg-white rounded-lg shadow p-6">
            <h2 className="text-2xl font-bold text-accent-navy mb-4">Experience Timeline</h2>
            <div className="space-y-4">
              {analysis.experience.map((exp, index) => (
                <div key={index} className="border-l-2 border-accent-navy pl-4">
                  <h3 className="font-semibold text-lg">{exp.title}</h3>
                  <p className="text-gray-600">{exp.company}</p>
                  <p className="text-sm text-gray-500">{exp.duration}</p>
                </div>
              ))}
            </div>
          </div>

          <div className="bg-white rounded-lg shadow p-6">
            <h2 className="text-2xl font-bold text-accent-navy mb-4">Recommendations</h2>
            <ul className="list-disc list-inside space-y-2">
              {analysis.recommendations.map((rec, index) => (
                <li key={index} className="text-gray-700">{rec}</li>
              ))}
            </ul>
          </div>
        </div>
      </main>
    </div>
  );
} 