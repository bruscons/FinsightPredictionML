# 🏦 Default Prediction System - Finnet Corp

Full web system for predicting default on bank payment slips (boletos), using the Machine Learning model developed by the Bill Hunters team.

## 🚀 Available Applications

### 1. Flask Application (Recommended)
Full web interface with an interactive dashboard.

**To start:**
```bash
# Method 1: Automatic script (Windows)
iniciar_app.bat

# Method 2: PowerShell (Windows)
.\iniciar_app.ps1

# Method 3: Manual
pip install -r requirements_flask.txt
python app_flask.py
```

**Access:** http://localhost:5000

### 2. Streamlit Application (Alternative)
Modern, responsive interface.

```bash
pip install -r requirements_app.txt
streamlit run app_predicao_inadimplencia.py
```

**Access:** http://localhost:8501

## 📋 Features

### 🔍 Existing Payer Analysis
- Full view of payment slip history
- Consolidated metrics (total slips, total amount, default rate)
- Detailed table with all of the payer's slips
- Automatic identification of behavior patterns

### 🎯 Prediction for New Payment Slips
- Intuitive data entry form
- Automatic validation of required fields
- Automated feature calculation (days to due date, etc.)
- Use of historical data when available

### 📊 Risk Classification System
- **🟢 LOW RISK (<30%)**: Reliable client
- **🟡 MEDIUM RISK (30-70%)**: Requires monitoring
- **🔴 HIGH RISK (>70%)**: Immediate action recommended

### 💡 Smart Recommendations
- Personalized suggestions based on risk level
- Preventive collection strategies
- Guidance for client relationship management

## 📈 How to Use

### Step 1: Payer Selection
1. **Existing Payer**: Choose from the list of registered payers
2. **New Payer**: Enter a new payer ID

### Step 2: History View (For Existing Payers)
- Summary metrics appear automatically
- Detailed history of all payment slips
- Payment behavior analysis

### Step 3: Prediction for a New Payment Slip
1. Fill in the required data:
   - Payment slip number
   - Original amount
   - Issue date
   - Due date
   - Group and beneficiary IDs

2. Click "Run Default Prediction"

3. Review the results:
   - Risk classification
   - Percentage probability
   - Final prediction (Compliant/Defaulted)
   - Specific recommendations

## 🎯 Interpreting the Results

### Main Metrics
- **Probability**: Percentage chance of default (0-100%)
- **Classification**: Low, Medium, or High risk
- **Prediction**: Compliant (≤50%) or Defaulted (>50%)

### Recommended Actions by Risk Level

#### 🔴 HIGH (>70%)
- Immediate contact with the client
- Offer special payment terms
- Preventive reduction of credit limit
- Implement preventive collection

#### 🟡 MEDIUM (30-70%)
- Close monitoring of behavior
- Send reminders close to the due date
- Additional client profile analysis
- Track trends

#### 🟢 LOW (<30%)
- Standard collection process
- Client considered reliable
- Possibility of additional product offers
- Maintain the relationship

## 📊 Data Used

### Main Features
- **Payment slip amount**: Original charge amount
- **Days to due date**: Period between issue and due date
- **Time-related data**: Month, year, day of issue and due date
- **Payer history**: Past behavior (when available)

### Historical Features (For Existing Payers)
- Number of previous charges
- Historical average amount
- Historical default rate
- Historical late-payment rate
- Standard deviation of amounts
- Time since first charge

## ⚙️ Technical Specifications

### Machine Learning Model
- **Algorithm**: RandomForestClassifier
- **Accuracy**: 96.44%
- **Recall**: 92.5%
- **Precision**: 91%
- **F1-Score**: 92%

### Technologies
- **Backend**: Flask/Streamlit + Python
- **Machine Learning**: Scikit-learn
- **Data**: Pandas + NumPy
- **Frontend**: Bootstrap + HTML/CSS/JavaScript
- **Serialization**: Joblib

### Required Files
```
├── app_flask.py                           # Flask application
├── app_predicao_inadimplencia.py         # Streamlit application
├── templates/index.html                   # Web interface
├── requirements_flask.txt                 # Flask dependencies
├── requirements_app.txt                   # Streamlit dependencies
├── iniciar_app.bat                       # Windows script
├── iniciar_app.ps1                       # PowerShell script
├── notebook/modelos salvos/
│   └── modelo_bill_hunters_latest.joblib # Trained model
└── dados/
    └── dados_treino_com_predicoes.csv    # Historical data
```

## 🔧 Troubleshooting

### ❌ "Model not found"
**Solution**: Check that `modelo_bill_hunters_latest.joblib` is in `notebook/modelos salvos/`

### ❌ "Data not found"
**Solution**: Confirm that `dados_treino_com_predicoes.csv` is in the `dados/` folder

### ❌ Dependency error
**Solution**:
```bash
pip install --upgrade pip
pip install -r requirements_flask.txt
```

### ❌ Port already in use
**Solution**:
- Flask: Change the port in `app_flask.py` (last line)
- Streamlit: Use `streamlit run app_predicao_inadimplencia.py --server.port 8502`

### ❌ Memory error
**Solution**: For very large datasets, consider sampling the historical data

## 🔒 Security Considerations

- ✅ Input data validation
- ✅ Robust error handling
- ✅ Prediction logs (in development)
- ⚠️ **Important**: This is a demo version. For production, implement:
  - User authentication
  - Sensitive data encryption
  - Access auditing
  - Rate limiting

## 📈 Upcoming Versions

- [ ] Management dashboard with aggregated metrics
- [ ] Integration with database APIs
- [ ] Automatic email/SMS alert system
- [ ] Automatic retraining module
- [ ] Report export (PDF/Excel)
- [ ] REST API for integration with other systems
- [ ] Time-series trend analysis
- [ ] Automatic client segmentation

## 📞 Support

**Team**: Bill Hunters
**Project**: Default Prediction System
**Client**: Finnet Corp
**Year**: 2025

For technical support, refer to the full documentation in the `modelo_definitivo.ipynb` notebook or contact the development team.

---

**⚡ Quick Start:**
1. Run `iniciar_app.bat` (Windows) or `python app_flask.py`
2. Access http://localhost:5000
3. Select an existing payer or create a new one
4. Fill in the payment slip data
5. Click "Run Prediction"
6. Review the results and recommendations
