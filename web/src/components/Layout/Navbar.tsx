import Link from 'next/link';

const Navbar = () => {
  return (
    <nav className="bg-accent-navy text-white">
      <div className="container mx-auto px-4">
        <div className="flex space-x-6 py-3">
          <Link href="/" className="hover:text-gray-300">Upload Resume</Link>
          <Link href="/results" className="hover:text-gray-300">Results</Link>
          <Link href="/companies" className="hover:text-gray-300">Companies</Link>
        </div>
      </div>
    </nav>
  );
};

export default Navbar; 