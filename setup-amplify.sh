#!/bin/bash

# AWS Amplify Setup Script for Ethiopian Bible Guardian
# This script initializes the project for deployment to AWS Amplify

set -e

echo "🙏 AWS Amplify Setup for Ethiopian Bible Guardian"
echo "=================================================="
echo ""

# Check prerequisites
echo "📋 Checking prerequisites..."

if ! command -v node &> /dev/null; then
  echo "❌ Node.js is not installed. Please install Node.js 18+ first."
  exit 1
fi

if ! command -v npm &> /dev/null; then
  echo "❌ npm is not installed. Please install npm first."
  exit 1
fi

echo "✅ Node.js $(node -v)"
echo "✅ npm $(npm -v)"
echo ""

# Check AWS CLI
if ! command -v aws &> /dev/null; then
  echo "⚠️  AWS CLI not found. Installing globally..."
  npm install -g aws-cli
fi

echo "✅ AWS CLI installed"
echo ""

# Install frontend dependencies
echo "📦 Installing frontend dependencies..."
cd frontend
npm ci
cd ..
echo "✅ Frontend dependencies installed"
echo ""

# Create environment files if they don't exist
echo "⚙️  Setting up environment files..."

if [ ! -f "frontend/.env.local" ]; then
  echo "Creating frontend/.env.local..."
  cat > frontend/.env.local << EOF
VITE_API_BASE_URL=http://127.0.0.1:8000
VITE_APP_ENV=local
EOF
fi

if [ ! -f "frontend/.env.staging" ]; then
  echo "Creating frontend/.env.staging..."
  cat > frontend/.env.staging << EOF
VITE_API_BASE_URL=https://staging-api.example.com
VITE_APP_ENV=staging
EOF
fi

if [ ! -f "frontend/.env.production" ]; then
  echo "Creating frontend/.env.production..."
  cat > frontend/.env.production << EOF
VITE_API_BASE_URL=https://api.example.com
VITE_APP_ENV=production
EOF
fi

echo "✅ Environment files configured"
echo ""

# Build frontend
echo "🔨 Building frontend..."
cd frontend
npm run build
cd ..
echo "✅ Frontend build successful"
echo ""

# Instructions
echo "✨ Setup Complete!"
echo ""
echo "Next steps to deploy to AWS Amplify:"
echo ""
echo "1. Go to AWS Amplify Console: https://console.aws.amazon.com/amplify"
echo "2. Click 'Create app' → 'Host web app'"
echo "3. Select GitHub and authorize"
echo "4. Select DrNFJ/Ethiopian_Bible_Guardian repository"
echo "5. Select 'main' branch"
echo "6. In the build settings, confirm amplify.yml is detected"
echo "7. Add environment variables:"
echo "   - VITE_API_BASE_URL=https://your-api-endpoint.com"
echo "   - VITE_APP_ENV=production"
echo ""
echo "8. Deploy!"
echo ""
echo "For local development:"
echo "  cd frontend && npm run dev"
echo ""
echo "For production build:"
echo "  cd frontend && npm run build"
echo ""
