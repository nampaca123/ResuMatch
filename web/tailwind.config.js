/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        primary: {
          DEFAULT: '#FFFFFF',
          dark: '#F8F9FA'
        },
        accent: {
          navy: '#1E3A8A',
          gray: '#374151'
        }
      }
    }
  },
  plugins: [],
}

