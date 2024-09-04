/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    '../ads/templates/**/*.html',
    '../base/templates/**/*.html',
    '../chat/templates/**/*.html',
    '../only_marriage/templates/**/*.html',
  ],
  theme: {
    extend: {
      backgroundImage: {
        'login-bg': "url('/static/images/background.jpg')",
      }
    },
  },
  plugins: [],
}

