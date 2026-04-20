@echo off
REM AWS Amplify Setup Script for Ethiopian Bible Guardian (Windows)
REM This script initializes the project for deployment to AWS Amplify

setlocal enabledelayedexpansion

echo 🙏 AWS Amplify Setup for Ethiopian Bible Guardian
echo ==================================================
echo.

REM Check prerequisites
echo 📋 Checking prerequisites...

where /q node
if errorlevel 1 (
  echo ❌ Node.js is not installed. Please install Node.js 18+ first.
  exit /b 1
)

where /q npm
if errorlevel 1 (
  echo ❌ npm is not installed. Please install npm first.
  exit /b 1
)

for /f "tokens=*" %%A in ('node -v') do set NODE_VER=%%A
for /f "tokens=*" %%A in ('npm -v') do set NPM_VER=%%A

echo ✅ Node.js %NODE_VER%
echo ✅ npm %NPM_VER%
echo.

REM Check AWS CLI
where /q aws
if errorlevel 1 (
  echo ⚠️  AWS CLI not found. Please install AWS CLI from: https://aws.amazon.com/cli/
  echo    Then run: aws configure
) else (
  echo ✅ AWS CLI installed
)
echo.

REM Install frontend dependencies
echo 📦 Installing frontend dependencies...
cd frontend
call npm ci
cd ..
if errorlevel 1 (
  echo ❌ Failed to install frontend dependencies
  exit /b 1
)
echo ✅ Frontend dependencies installed
echo.

REM Create environment files if they don't exist
echo ⚙️  Setting up environment files...

if not exist "frontend\.env.local" (
  echo Creating frontend\.env.local...
  (
    echo VITE_API_BASE_URL=http://127.0.0.1:8000
    echo VITE_APP_ENV=local
  ) > frontend\.env.local
)

if not exist "frontend\.env.staging" (
  echo Creating frontend\.env.staging...
  (
    echo VITE_API_BASE_URL=https://staging-api.example.com
    echo VITE_APP_ENV=staging
  ) > frontend\.env.staging
)

if not exist "frontend\.env.production" (
  echo Creating frontend\.env.production...
  (
    echo VITE_API_BASE_URL=https://api.example.com
    echo VITE_APP_ENV=production
  ) > frontend\.env.production
)

echo ✅ Environment files configured
echo.

REM Build frontend
echo 🔨 Building frontend...
cd frontend
call npm run build
cd ..
if errorlevel 1 (
  echo ❌ Frontend build failed
  exit /b 1
)
echo ✅ Frontend build successful
echo.

REM Instructions
echo ✨ Setup Complete!
echo.
echo Next steps to deploy to AWS Amplify:
echo.
echo 1. Go to AWS Amplify Console: https://console.aws.amazon.com/amplify
echo 2. Click 'Create app' -^> 'Host web app'
echo 3. Select GitHub and authorize
echo 4. Select DrNFJ/Ethiopian_Bible_Guardian repository
echo 5. Select 'main' branch
echo 6. In the build settings, confirm amplify.yml is detected
echo 7. Add environment variables:
echo    - VITE_API_BASE_URL=https://your-api-endpoint.com
echo    - VITE_APP_ENV=production
echo.
echo 8. Deploy!
echo.
echo For local development:
echo   cd frontend ^&^& npm run dev
echo.
echo For production build:
echo   cd frontend ^&^& npm run build
echo.

pause
