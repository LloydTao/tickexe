module.exports = {
  purge: {
    enabled: true, // Set false for development
    content: ['../../**/templates/*.html', '../../**/templates/**/*.html'],
  },
  // Allow user to toggle dark mode manually
  // https://tailwindcss.com/docs/dark-mode#toggling-dark-mode-manually
  darkMode: 'class',
  theme: {
    extend: {},
  },
  variants: {
    extend: {},
  },
  plugins: [],
}
