# AWS Amplify Frontend Integration - Quick Start

## What We've Set Up

✅ **AWS Amplify Configuration Files:**
- `amplify.yml` - Build and deployment configuration
- `.env.local` - Local development environment
- `.env.staging` - Staging deployment environment  
- `.env.production` - Production deployment environment
- `amplify-config.js` - Amplify services configuration

✅ **GitHub Actions CI/CD:**
- `.github/workflows/amplify-deploy.yml` - Automated deployment workflow

✅ **Vite Optimization:**
- Optimized build configuration for Amplify hosting
- Console drop-in production builds
- Terser minification for smaller bundles

✅ **Documentation:**
- `AMPLIFY_DEPLOYMENT.md` - Complete deployment guide
- `CI_CD_SETUP.md` - CI/CD configuration reference

## Quick Start (Windows)

### 1. Run Setup Script
```powershell
.\setup-amplify.bat
```

Or manually:
```powershell
cd frontend
npm install
npm run build
cd ..
```

### 2. Test Locally
```powershell
cd frontend
npm run dev
```
Visit `http://localhost:5173`

### 3. Push to GitHub
```powershell
git add -A
git commit -m "Add AWS Amplify integration"
git push origin main
```

### 4. Deploy to Amplify Console

1. **Create Amplify App:**
   - Go to [AWS Amplify Console](https://console.aws.amazon.com/amplify)
   - Click **"Host web app"**
   - Select **GitHub** → Authorize
   - Select **DrNFJ/Ethiopian_Bible_Guardian**
   - Select **main** branch

2. **Configure Build:**
   - Build settings will auto-detect `amplify.yml`
   - Click **Next**

3. **Set Environment Variables:**
   ```
   VITE_API_BASE_URL = https://your-api-endpoint.com
   VITE_APP_ENV = production
   ```

4. **Deploy:**
   - Click **"Save and deploy"**
   - Amplify builds and deploys automatically
   - Your site will be live at `https://main.xxxxx.amplifyapp.com`

## Environment Variables

Update these for your deployment:

**`.env.local`** (local development)
```
VITE_API_BASE_URL=http://127.0.0.1:8000
VITE_APP_ENV=local
```

**`.env.staging`** (staging deployment)
```
VITE_API_BASE_URL=https://staging-api.example.com
VITE_APP_ENV=staging
```

**`.env.production`** (production deployment)
```
VITE_API_BASE_URL=https://api.example.com
VITE_APP_ENV=production
```

## API Backend Integration

The frontend automatically connects to your backend API using the `VITE_API_BASE_URL` environment variable.

**Important:** Ensure your backend API:
- ✅ Has `/chat` POST endpoint
- ✅ Accepts `{ query: string, top_k: number }` 
- ✅ Has CORS enabled for your Amplify domain
- ✅ Returns `{ invocation, witness, exhortation, reflection, citations }`

## Deployment Flow

```
Push to GitHub
     ↓
GitHub webhook triggers Amplify
     ↓
Amplify reads amplify.yml
     ↓
Runs: npm ci && npm run build
     ↓
Artifacts deployed to CloudFront CDN
     ↓
Site live at https://your-domain.amplifyapp.com
```

## Custom Domain (Optional)

1. In Amplify Console → **"App settings"** → **"Domain management"**
2. Click **"Add domain"**
3. Point your DNS to the Amplify distribution
4. HTTPS certificate auto-provisioned

## Monitor Deployments

1. Go to **Amplify Console** → **"Deployments"**
2. View build logs, deployment status
3. Rollback to previous deployments if needed

## Troubleshooting

**Build fails:**
- Check Amplify Console **"Deployments"** tab
- Verify `amplify.yml` syntax
- Ensure Node.js 18+ is selected

**API connection fails:**
- Verify `VITE_API_BASE_URL` is correct in Amplify Console
- Check backend CORS headers
- Test API endpoint: `curl https://your-api/chat`

**Frontend not updating:**
- Clear browser cache (Ctrl+Shift+Delete)
- Invalidate CloudFront cache in AWS Console
- Check deployment completed successfully

## Next Steps

- [ ] Update API endpoint URLs for staging/production
- [ ] Set up custom domain
- [ ] Configure CDN caching headers
- [ ] Enable AWS WAF for DDoS protection
- [ ] Set up monitoring with CloudWatch
- [ ] Configure notifications for deployment failures

---

For more details, see `AMPLIFY_DEPLOYMENT.md` and `CI_CD_SETUP.md`
