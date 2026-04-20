# AWS Amplify Deployment Guide

## Overview

This React + Vite frontend is configured for AWS Amplify Hosting with integration to your RAG backend API.

## Prerequisites

1. AWS Account with Amplify service enabled
2. GitHub account with the Ethiopian_Bible_Guardian repository
3. AWS CLI configured locally (optional, for manual deployments)

## Deployment Steps

### 1. Connect Repository to AWS Amplify

1. Go to [AWS Amplify Console](https://console.aws.amazon.com/amplify)
2. Click **"Create app"** → **"Host web app"**
3. Select **GitHub** as your source repository
4. Authorize AWS to access your GitHub account
5. Select the **Ethiopian_Bible_Guardian** repository
6. Select the **main** branch (or your deployment branch)
7. Click **Next**

### 2. Configure Build Settings

The `amplify.yml` file at the project root defines the build process:

- **Frontend Build:** Runs `npm run build` in the `frontend/` directory
- **Backend Integration:** (Optional) Can trigger backend deployment simultaneously
- **Artifacts:** Outputs from `frontend/dist/` are deployed

**Key Build Variables:**
- `VITE_API_BASE_URL`: API endpoint URL (set per deployment environment)
- `AMPLIFY_ENVIRONMENT`: Environment name (local, staging, production)

### 3. Set Environment Variables in Amplify Console

For each deployment environment, set these variables:

**Development/Staging:**
```
VITE_API_BASE_URL=https://staging-api.your-domain.com
VITE_APP_ENV=staging
```

**Production:**
```
VITE_API_BASE_URL=https://api.your-domain.com
VITE_APP_ENV=production
```

### 4. Configure Backend API

Update your backend API URL in the Amplify Console:

1. In Amplify, go to **App settings** → **Environment variables**
2. Add the backend API endpoint for each branch:
   - `main` → production API
   - `develop` → staging API

### 5. Deploy

**Automatic Deployment (Recommended):**
- Push to your GitHub branch
- AWS Amplify automatically detects changes
- Build process runs (uses `amplify.yml`)
- Site is deployed to the preview or production URL

**Manual Deployment:**
```bash
# Install AWS CLI if not already installed
aws configure

# Deploy using Amplify CLI (if set up)
amplify publish
```

## Local Development

### Run Locally with Local Backend

```bash
cd frontend
npm install
npm run dev
```

Visit `http://localhost:5173` and it will connect to the local backend at `http://127.0.0.1:8000`.

### Run Locally with Remote Backend

Create `.env.local`:
```
VITE_API_BASE_URL=https://staging-api.your-domain.com
VITE_APP_ENV=staging
```

Then:
```bash
cd frontend
npm run dev
```

## Environment Branching Strategy

| Branch | Env File | API Endpoint | Amplify URL |
|--------|----------|--------------|-------------|
| `main` | `.env.production` | `api.example.com` | `production.example.amplifyapp.com` |
| `develop` | `.env.staging` | `staging-api.example.com` | `develop.example.amplifyapp.com` |
| `feature/*` | `.env.local` | `localhost:8000` | `branch-name.example.amplifyapp.com` |

## Troubleshooting

### Build Failures

1. Check Amplify Console **"Deployments"** tab for build logs
2. Verify environment variables are set correctly
3. Ensure API backend is running and accessible

### API Connection Issues

1. Check `VITE_API_BASE_URL` in Amplify Console environment variables
2. Verify CORS is enabled on your backend API
3. Test API endpoint manually: `curl https://your-api-endpoint/chat`

### Frontend Not Loading

1. Check Amplify **"Hosting"** tab for deployment status
2. Clear browser cache and reload
3. Verify domain DNS settings if using custom domain

## Security Best Practices

- Use **HTTPS** for all API endpoints
- Store sensitive credentials (API keys, auth tokens) in AWS Secrets Manager
- Enable **AWS WAF** to protect against DDoS attacks
- Use **IAM roles** for backend service authentication
- Implement **authentication** using Amazon Cognito (optional)

## Next Steps

1. Create GitHub branch `develop` for staging deployments
2. Set up domain mapping in Amplify for custom URLs
3. Configure CDN caching for static assets
4. Enable monitoring with AWS CloudWatch
5. Set up notifications for deployment failures

## Additional Resources

- [AWS Amplify Hosting Docs](https://docs.amplify.aws/gen1/react/start/getting-started/hosting/)
- [Vite Environment Variables](https://vitejs.dev/guide/env-and-modes.html)
- [AWS Amplify CLI Reference](https://docs.amplify.aws/cli/)
