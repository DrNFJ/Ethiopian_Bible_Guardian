# GitHub Actions CI/CD Configuration for AWS Amplify Deployment

## Purpose

This GitHub Actions workflow automatically deploys the frontend to AWS Amplify on each push to main or develop branches.

## Setup Instructions

1. Add AWS credentials to GitHub Secrets:
   - Go to your GitHub repository → **Settings** → **Secrets and variables** → **Actions**
   - Add the following secrets:
     - `AWS_ACCESS_KEY_ID`: Your AWS access key
     - `AWS_SECRET_ACCESS_KEY`: Your AWS secret key
     - `AWS_REGION`: Your AWS region (e.g., `us-east-1`)
     - `AMPLIFY_APP_ID`: Your Amplify App ID (from Amplify Console)

2. Create `.github/workflows/amplify-deploy.yml` (see sample below)

## Sample Workflow File

This workflow can be saved as `.github/workflows/amplify-deploy.yml`:

```yaml
name: Deploy to AWS Amplify

on:
  push:
    branches:
      - main
      - develop

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
        with:
          fetch-depth: 0

      - name: Set up Node.js
        uses: actions/setup-node@v3
        with:
          node-version: '18'

      - name: Install dependencies
        working-directory: ./frontend
        run: npm ci

      - name: Build
        working-directory: ./frontend
        run: npm run build
        env:
          VITE_API_BASE_URL: ${{ secrets.VITE_API_BASE_URL }}

      - name: Deploy to Amplify
        uses: aws-amplify/amplify-cli-action@2v1
        with:
          amplify_cli_version: 12.0.0
          amplifyDir: ./frontend
          aws_access_key_id: ${{ secrets.AWS_ACCESS_KEY_ID }}
          aws_secret_access_key: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
          aws_region: ${{ secrets.AWS_REGION }}
          amplify_app_id: ${{ secrets.AMPLIFY_APP_ID }}
          amplify_env: ${{ github.ref_name == 'main' && 'production' || 'staging' }}
```

## Alternative: Using AWS Amplify Console

AWS Amplify Console provides automatic deployment without requiring GitHub Actions:

1. Connect your GitHub repository to Amplify in the console
2. Select the branch to deploy
3. Amplify automatically detects `amplify.yml` and runs the build
4. Deploy happens automatically on each push

This is the recommended approach for most projects.
