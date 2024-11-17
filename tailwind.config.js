/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './trivia_app/templates/**/*.html',
  ],
  theme: {
    extend: {
      colors: {
        primary: '#5B6D92',
        secondary: '#D5E3E6',
        background: '#EFEEE5',
        text: '#364842',
        accent: '#D18266',
        accent2: '#D45E35',
      }
    },
    fontFamily: {
      sans: ['Inter', 'Helvetica', 'Arial', 'sans-serif'],
    },
  },
  plugins: [],
}

