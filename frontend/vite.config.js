import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// https://vite.dev/config/
export default defineConfig({
  plugins: [react()],
  build: {
    outDir: 'dist',
    emptyOutDir: true,
    sourcemap: false,
    minify: 'esbuild',
  },
  define: {
    'process.env.AMPLIFY_APP_ID': JSON.stringify(process.env.AMPLIFY_APP_ID || ''),
  },
})
