# 🚀 Deployment Guide

This guide provides deployment instructions for the Gold Coin Finance Consultancy Billing System on multiple platforms.

## 📌 Deployment Platforms

- **[Vercel](#vercel-deployment)** - Recommended for easy deployment (serverless)
- **[Render.com](#rendercom-deployment)** - Good for traditional hosting (free tier available)

---

# Vercel Deployment

Deploy your Flask billing system to Vercel's serverless platform in minutes.

## 📋 Prerequisites

- ✅ A GitHub account ([Sign up here](https://github.com/signup))
- ✅ A Vercel account ([Sign up here](https://vercel.com/signup))
- ✅ Git installed on your computer

## ⚠️ Important: Database Consideration

> **Note:** This application uses SQLite (`database.db`). Vercel's serverless functions are stateless and ephemeral, meaning:
> - ✅ The app will work perfectly
> - ⚠️ Data will reset on each deployment
> - ⚠️ Data won't persist between serverless function invocations
>
> **For production use**, consider migrating to:
> - Vercel Postgres
> - Supabase PostgreSQL
> - MongoDB Atlas
> - Any external database service

## 📤 Step 1: Push Code to GitHub

### Option A: Create New Repository via GitHub Web Interface

1. **Go to GitHub** and sign in
2. **Click** the "+" icon (top-right) → "New repository"
3. **Name** your repository: `gold-coin-billing-system`
4. **Set** to Public or Private (both work with Vercel)
5. **Do NOT** initialize with README (your code already has one)
6. **Click** "Create repository"

### Option B: Push from Command Line

Open your terminal/PowerShell in the project directory and run:

```powershell
# Navigate to project directory
cd "c:\01 Pratik\CLG\Projects\gold-coin-finance-consultancy-billing-system"

# Initialize git (if not already done)
git init

# Add all files
git add .

# Commit changes
git commit -m "Initial commit - Ready for Vercel deployment"

# Add your GitHub repository as remote (replace with your GitHub username)
git remote add origin https://github.com/YOUR_USERNAME/gold-coin-billing-system.git

# Push to GitHub
git push -u origin main
```

> **Note:** If you get an error about 'main' branch, try:
> ```powershell
> git branch -M main
> git push -u origin main
> ```

## 🌐 Step 2: Deploy to Vercel

### Method A: Using Vercel Dashboard (Easiest)

1. **Go to** [Vercel Dashboard](https://vercel.com/dashboard)
2. **Click** "Add New..." → "Project"
3. **Import** your GitHub repository
4. **Configure** your project:
   - **Framework Preset:** Other
   - **Build Command:** (leave empty)
   - **Output Directory:** (leave empty)
   - **Install Command:** `pip install -r requirements.txt`
5. **Click** "Deploy"
6. **Wait** 1-2 minutes for deployment

### Method B: Using Vercel CLI

```powershell
# Install Vercel CLI globally
npm install -g vercel

# Navigate to project directory
cd "c:\01 Pratik\CLG\Projects\gold-coin-finance-consultancy-billing-system"

# Deploy to Vercel
vercel

# Follow the prompts:
# - Set up and deploy? Yes
# - Which scope? (select your account)
# - Link to existing project? No
# - What's your project's name? gold-coin-billing-system
# - In which directory is your code? ./
# - Override settings? No
```

## ✅ Step 3: Verify Deployment

1. **Copy** your app URL (e.g., `https://gold-coin-billing-system.vercel.app`)
2. **Open** in a new browser tab
3. **Test** the following:
   - ✅ Home page loads
   - ✅ Add new customer
   - ✅ Add services from catalog
   - ✅ Record payment
   - ✅ View bill/ledger
   - ✅ Download PDF

## 🔄 Updating Your Deployed App

Vercel automatically deploys on every push to your main branch:

```powershell
# Make your code changes
# Then commit and push

git add .
git commit -m "Description of changes"
git push

# Vercel will automatically deploy the changes
```

## 🐛 Troubleshooting

### Build Failed

**Check logs in Vercel dashboard:**
- Go to your project → Deployments → Click failed deployment
- Review build logs

**Common issues:**
- Missing dependencies in `requirements.txt`
- Python version compatibility

### Application Error

**Check function logs:**
- Go to Vercel dashboard → Your project → Logs
- Look for Python errors

**Common issues:**
- Database initialization errors (expected on first run)
- Missing environment variables

### Data Not Persisting

**This is expected with SQLite on Vercel.**
- Each serverless function invocation starts fresh
- Consider migrating to external database for production

## 📱 Sharing Your App

Once deployed:
- **URL Format:** `https://your-project-name.vercel.app`
- Share with anyone - no login required
- Works on mobile and desktop browsers
- HTTPS enabled by default

## 💡 Next Steps

- **Custom Domain:** Add your domain in Vercel project settings
- **Database Migration:** Switch to Vercel Postgres or external database
- **Environment Variables:** Configure in Vercel dashboard
- **Analytics:** Enable Vercel Analytics for usage insights

---

# Render.com Deployment

Alternative deployment option with persistent storage on the free tier.

## 📋 Prerequisites


Before you begin, ensure you have:
- ✅ A GitHub account ([Sign up here](https://github.com/signup))
- ✅ A Render.com account ([Sign up here](https://render.com/signup))
- ✅ Git installed on your computer

## 📤 Step 1: Push Code to GitHub

### Option A: Create New Repository via GitHub Web Interface

1. **Go to GitHub** and sign in
2. **Click** the "+" icon (top-right) → "New repository"
3. **Name** your repository: `gold-coin-billing-system`
4. **Set** to Public or Private (both work with Render)
5. **Do NOT** initialize with README (your code already has one)
6. **Click** "Create repository"

### Option B: Push from Command Line

Open your terminal/PowerShell in the project directory and run:

```powershell
# Navigate to project directory
cd "c:\01 Pratik\CLG\Projects\gold-coin-finance-consultancy-billing-system"

# Initialize git (if not already done)
git init

# Add all files
git add .

# Commit changes
git commit -m "Initial commit - Ready for deployment"

# Add your GitHub repository as remote (replace with your GitHub username)
git remote add origin https://github.com/YOUR_USERNAME/gold-coin-billing-system.git

# Push to GitHub
git push -u origin main
```

> **Note:** If you get an error about 'main' branch, try:
> ```powershell
> git branch -M main
> git push -u origin main
> ```

## 🌐 Step 2: Deploy to Render.com

### 2.1 Connect GitHub to Render

1. **Go to** [Render.com](https://render.com) and sign in
2. **Click** "New +" button (top-right)
3. **Select** "Web Service"
4. **Click** "Connect account" under GitHub
5. **Authorize** Render to access your GitHub repositories

### 2.2 Select Repository

1. **Find** your repository: `gold-coin-billing-system`
2. **Click** "Connect"

### 2.3 Configure Web Service

Render will auto-detect the `render.yaml` file. Verify these settings:

- **Name:** `gold-coin-billing` (or choose your own)
- **Runtime:** `Python`
- **Build Command:** `pip install -r requirements.txt`
- **Start Command:** `gunicorn app:app`
- **Plan:** `Free`

### 2.4 Deploy

1. **Click** "Create Web Service"
2. **Wait** for deployment (3-5 minutes)
3. **Watch** the logs for any errors

## ✅ Step 3: Verify Deployment

Once deployment is complete:

1. **Copy** your app URL (e.g., `https://gold-coin-billing.onrender.com`)
2. **Open** in a new browser tab
3. **Test** the following:
   - ✅ Home page loads
   - ✅ Add new customer
   - ✅ Add services
   - ✅ Record payment
   - ✅ View/download bill PDF

## 🔧 Important Notes

### Database Persistence

> ⚠️ **Warning:** The free tier uses ephemeral storage. Your SQLite database will reset when:
> - The service restarts (after 15 minutes of inactivity)
> - You deploy a new version

**Solutions:**
- **For Testing:** This is fine - data resets are acceptable
- **For Production:**
  - Upgrade to Render's paid plan with persistent disk ($7/month)
  - Or migrate to PostgreSQL (Render offers free PostgreSQL database)

### Cold Starts

The free tier has a "spin down" feature:
- After 15 minutes of inactivity, your app sleeps
- First request takes 30-60 seconds to wake up
- Subsequent requests are fast

## 🐛 Troubleshooting

### Build Failed

**Check logs for:**
- Python version compatibility
- Missing dependencies

**Solution:**
```powershell
# Test locally first
pip install -r requirements.txt
python app.py
```

### Application Error 500

**Check application logs in Render dashboard**

**Common issues:**
- Database initialization errors
- Missing environment variables

### Cannot Access Application

**Verify:**
- Deployment status is "Live" (green)
- URL is correct
- No firewall blocking the connection

## 📱 Sharing Your App

Once deployed, share your app URL:
- **URL Format:** `https://your-app-name.onrender.com`
- Share with anyone - no login required (as designed)
- Works on mobile and desktop browsers

## 🔄 Updating Your App

To deploy changes:

```powershell
# Make your code changes
# Then commit and push

git add .
git commit -m "Description of changes"
git push

# Render auto-deploys on every push to main branch
```

## 💡 Next Steps

Consider these enhancements:
- **Custom Domain:** Add your own domain in Render settings
- **PostgreSQL:** Migrate from SQLite for persistence
- **HTTPS:** Automatically enabled on Render
- **Environment Variables:** Add via Render dashboard

---

**🎉 Congratulations!** Your billing system is now live on the internet!

For support, visit [Render Documentation](https://render.com/docs)
