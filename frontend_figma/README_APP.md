# 🏦 Default Prediction System - Finnet Corp

A Streamlit web application for predicting default on bank payment slips (boletos), using the Machine Learning model trained in the Bill Hunters project.

## 📋 Features

- **Existing Payer Analysis**: View the full billing history of already registered clients
- **Prediction for New Payment Slips**: Run default predictions for new payment slips
- **Risk Classification**: Automatic classification system (Low, Medium, High)
- **Smart Recommendations**: Suggested actions based on risk level
- **Intuitive Interface**: Interactive, easy-to-use dashboard

## 🚀 How to Run

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Installation

1. Clone the repository and navigate to the directory:
```bash
cd 2025-2A-T18-IN03-G05
```

2. Install the dependencies:
```bash
pip install -r requirements_app.txt
```

3. Run the application:
```bash
streamlit run app_predicao_inadimplencia.py
```

4. Access the application in your browser:
```
http://localhost:8501
```

## 📊 Data Structure

The application uses the following data:

### Input Data (Payment Slip)
- **Payment Slip Number**: Unique identifier
- **Original Amount**: Payment slip amount in R$
- **Issue Date**: Date the payment slip was created
- **Due Date**: Payment deadline
- **Payer ID**: Client identifier
- **Group ID**: Beneficiary group
- **Beneficiary ID**: Beneficiary identifier

### Historical Data (Automatically Calculated)
- Number of historical charges
- Historical average amount
- Historical default rate
- Historical late-payment rate
- Time since first charge
- Standard deviation of amounts

## 🎯 How to Use

### 1. Existing Payer Analysis

1. In the side menu, select "Existing Payer"
2. Choose a payer from the dropdown list
3. View the full payment slip history
4. Review the summary metrics (total slips, total amount, default rate)

### 2. Prediction for a New Payment Slip

1. Fill in the new payment slip data:
   - Payment slip number
   - Original amount
   - Issue date
   - Due date
   - Group and beneficiary IDs

2. Click "Run Default Prediction"

3. Review the results:
   - **Risk Classification**: High, Medium, or Low
   - **Probability**: Percentage chance of default
   - **Prediction**: Compliant or Defaulted
   - **Recommendations**: Suggested actions based on risk

## 📈 Interpreting the Results

### Risk Classification

- **🔴 HIGH (>70%)**: Requires immediate action
  - Preventive contact with the client
  - Special payment terms
  - Reduced credit limit

- **🟡 MEDIUM (30-70%)**: Requires monitoring
  - Close follow-up
  - Due-date reminders
  - Additional profile analysis

- **🟢 LOW (<30%)**: Reliable client
  - Standard collection process
  - Possible offer of additional products

## 🔧 Required Files

Make sure the following files are present:

```
├── app_predicao_inadimplencia.py          # Main application
├── requirements_app.txt                    # Dependencies
├── notebook/modelos salvos/
│   └── modelo_bill_hunters_latest.joblib  # Trained model
└── dados/
    └── dados_treino_com_predicoes.csv     # Historical data
```

## 🛠️ Technologies Used

- **Streamlit**: Web application framework
- **Pandas**: Data manipulation
- **NumPy**: Numerical computing
- **Scikit-learn**: Machine Learning
- **Joblib**: Model serialization

## 📝 Important Notes

1. **Model**: Uses a RandomForestClassifier trained in the `modelo_definitivo.ipynb` notebook
2. **Historical Data**: For existing payers, historical data is used for better accuracy
3. **New Payers**: For new clients, default values based on the current payment slip are used
4. **Performance**: Model with 96.44% accuracy and 92.5% recall

## 🔄 Next Steps

- Integration with database APIs
- Automatic alert system
- Management dashboard with aggregated metrics
- Automatic model retraining module
- PDF report export

## 🆘 Troubleshooting

### Error: "Model not found"
- Check that the `modelo_bill_hunters_latest.joblib` file is in the correct folder
- Make sure the path in the code is correct

### Error: "Data not found"
- Check that the `dados_treino_com_predicoes.csv` file is in the `dados/` folder
- Confirm the file is not corrupted

### Dependency errors
- Run: `pip install --upgrade -r requirements_app.txt`
- Use a virtual environment (venv) to avoid conflicts

---

**Developed by**: Bill Hunters Team
**Project**: Default Prediction System - Finnet Corp
**Year**: 2025
