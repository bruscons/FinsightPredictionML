# 🚀 FINNET BILL HUNTERS - Vercel Deploy

## Final Deploy Structure

This is the clean, optimized version for deploying to Vercel with only the essential files.

### 📁 Main Files:

- **`app.py`** - Main Flask application
- **`app_super_simples.py`** - Local version (backup)
- **`templates/index_simples.html`** - Web interface
- **`requirements.txt`** - Python dependencies
- **`vercel.json`** - Vercel configuration
- **`.vercelignore`** - Files ignored during deploy

### 📦 To Deploy on Vercel:

1. **Connect to Git**: Push to a GitHub repository
2. **Import into Vercel**: Connect the repository
3. **Automatic Deploy**: Vercel will detect `vercel.json`

### 🎯 Features:

- ✅ 3 payers with different risk profiles
- ✅ Real-time default prediction
- ✅ Modern interface with dark theme
- ✅ Dashboard with metrics
- ✅ Professional footer
- ✅ Responsive design

### 🔧 Technologies:

- **Backend**: Flask + Python
- **Frontend**: HTML5 + Bootstrap + JavaScript
- **Deploy**: Vercel Serverless

### 📊 Available Payers:

- **João Silva** (ID: 2793444) - Low Risk
- **Maria Santos** (ID: 4606075) - Medium Risk
- **Carlos Oliveira** (ID: 5362811) - High Risk

### 🌐 API Endpoints:

- `GET /` - Main interface
- `GET /api/pagadores` - List of payers
- `GET /api/pagador/<id>` - Payer details
- `POST /api/predict` - Default prediction

Ready to deploy! 🚀
