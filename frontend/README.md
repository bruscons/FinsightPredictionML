# Bill Hunters - Default Prediction Dashboard

## 🚀 How to Run

### Option 1: Automatic Run
```bash
cd frontend
python run.py
```

### Option 2: Manual Run
```bash
cd frontend
pip install -r requirements.txt
streamlit run app.py
```

## 📊 Features

- **Interactive Dashboard**: Full visualization of prediction data
- **Dynamic Filters**: Filter by data type, status, and predictions
- **Real-Time Metrics**: Accuracy, recall, precision, and F1-score
- **Interactive Charts**: Distributions, time-series analysis, and correlations
- **Feature Analysis**: Variable importance in the model
- **Data Download**: Export results as CSV

## 🎯 Available Metrics

- Default Rate
- Model Accuracy
- Recall for Defaulters
- Precision and F1-Score
- Probability Distribution
- Time-Series Analysis
- Feature Importance

## 📁 Structure

```
frontend/
├── app.py              # Main Streamlit application
├── run.py              # Automatic run script
├── requirements.txt    # Python dependencies
└── README.md          # This file
```

## 🌐 Access

After running, go to: http://localhost:8501
