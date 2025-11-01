# Deploying Forecasting Service to Render

This guide explains how to deploy the forecasting service to Render.

## Prerequisites

1. A Render account (sign up at [render.com](https://render.com))
2. Your forecasting repository connected to GitHub

## Deployment Options

### Option 1: Using Render Dashboard (Recommended)

1. **Connect Repository**
   - Go to [Render Dashboard](https://dashboard.render.com)
   - Click "New +" → "Web Service"
   - Connect your GitHub account if not already connected
   - Select the `forecasting` repository (or the repository containing the forecasting folder)

2. **Configure Service**
   - **Name**: `forecasting-service` (or your preferred name)
   - **Region**: Choose closest to your users
   - **Branch**: `main`
   - **Root Directory**: Leave empty if deploying from the root, or set to `forecasting` if the repo is the parent folder
   - **Runtime**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app --bind 0.0.0.0:$PORT --workers 2 --timeout 120`

3. **Environment Variables**
   Add the following environment variables in Render dashboard:
   ```
   FORECASTING_PORT=10000  # Render sets $PORT automatically, but you can set this for compatibility
   FLASK_DEBUG=False
   DB_HOST=your-database-host
   DB_PORT=5432
   DB_NAME=your-database-name
   DB_USER=your-database-user
   DB_PASS=your-database-password
   DATABASE_URL=your-full-database-url (if using connection string)
   ```

4. **Deploy**
   - Click "Create Web Service"
   - Render will automatically build and deploy your service

### Option 2: Using render.yaml (Declarative)

1. Ensure `render.yaml` is in your repository root (already created)
2. Go to Render Dashboard → "New +" → "Blueprint"
3. Connect your repository
4. Render will automatically detect and use `render.yaml`

## Important Notes

- **Port**: Render automatically sets the `$PORT` environment variable. The Procfile uses this.
- **Database**: You'll need a PostgreSQL database (Render offers managed PostgreSQL)
- **Model Files**: Ensure `model/` directory files (xgboost_peak_model.joblib, prophet_peak_model.json) are committed to the repository
- **Build Time**: First build may take 5-10 minutes due to ML library installations (XGBoost, Prophet, etc.)

## Health Check

Once deployed, test the service:
```
GET https://your-service-name.onrender.com/health
```

## Troubleshooting

1. **Build fails**: Check that all dependencies in `requirements.txt` are correct
2. **Models not loading**: Ensure model files are committed to the repository
3. **Database connection fails**: Verify environment variables are set correctly
4. **Service crashes**: Check logs in Render dashboard for errors

## Cost

- Free tier: Service spins down after 15 minutes of inactivity
- Paid tiers: Service stays up 24/7

