# 💳 Credit Card Fraud Detection


## 📋 Overview

This project implements an end-to-end **Credit Card Fraud Detection** system using Machine Learning. It detects fraudulent transactions from credit card data using a trained Random Forest classifier deployed as an interactive [Streamlit](https://streamlit.io/) web application.

**Key Features:**
- 🧠 Pre-trained Random Forest model (ROC AUC optimized for imbalanced data)
- 🎛️ Manual transaction input (Time & Amount)
- 📁 CSV batch upload for accurate predictions (full 30 features)
- ⚡ Quick demo buttons for legitimate/fraud examples
- 🚀 Easy local deployment with one command


## 🚀 Quick Start

1. **Clone/Download** this project
2. **Install dependencies:**
   ```bash
   pip install -r project---3/requirements.txt
   ```
3. **Run the app:**
   ```bash
   cd project---3
   streamlit run app.py
   ```
4. Open [http://localhost:8501](http://localhost:8501) 🎉

**Dataset Download:** [creditcard.csv from Kaggle](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud/download)

## 🎯 Usage

### 1. Manual Input (Quick Demo) ⚠️ Limited Accuracy
**Important Note:** The dataset uses **PCA-transformed features V1-V28** which are non-interpretable. Manual input only uses Time & Amount (zeros for V1-V28), suitable for **basic demos only**.

- Enter `Transaction Time` (seconds since first) & `Amount`
- Click **Check Transaction** → Basic prediction

**For accurate predictions, use CSV upload with all 30 features!**

### 2. CSV Upload (Production-Ready) ✅ Accurate
- Upload CSV with **full columns: Time, V1-V28, Amount**
- Click **Predict from CSV** → Batch predictions using **all model features**

### 3. Quick Tests
- **Test Legitimate Example**: Small amount, normal time
- **Test Fraud Example**: Large amount, suspicious time

## 📊 Model Details

**Training Notebook:** [part1.ipynb](part1.ipynb)

**🔍 Feature Explanation:** The dataset uses **PCA-transformed features (V1–V28)** from original transaction data for privacy. These are non-interpretable, so:
- Manual input: Uses Time + Amount only (V1-V28=0) → **Demo only**
- CSV upload: Requires full features → **Accurate predictions**

- **Dataset:** 284,807 transactions, 31 features (Time, **V1-V28 (PCA)**, Amount), binary Class (0=Legit, 1=Fraud)
- **Preprocessing:** StandardScaler on Time & Amount
- **Model:** `RandomForestClassifier`
  | Hyperparam | Value |
  |------------|-------|
  | n_estimators | 400 |
  | max_depth | 8 |
  | random_state | 42 |
- **Split:** 80/20 stratified
- **Metrics:** ROC AUC & Accuracy (high due to imbalance handling)
- **Saved:** `model.pkl` (joblib + pickle protocol=4)

**Retraining:** Run `part1.ipynb` (download dataset first!)

## 📈 Performance

```
ROC AUC: ~0.98+ (excellent for fraud detection)
Accuracy: ~0.999 (imbalanced dataset)
```
*(Exact values from notebook rerun)*

## 🛠️ Tech Stack

| Component | Tech |
|-----------|------|
| Web App | Streamlit |
| ML Model | Scikit-learn (RandomForest) |
| Persistence | Joblib/Pickle |
| Data | Pandas, NumPy |
| Deployment | Streamlit Cloud / Gunicorn |

## 📁 File Structure

```
project---3/
├── app.py              # Streamlit app
├── part1.ipynb         # Training notebook
├── model.pkl           # Trained model
├── requirements.txt    # Dependencies
├── readme.md          # This file!
└── TODO.md            # Implementation tracker
```

## 🔧 Local Development

```bash
# Install & Run
pip install -r requirements.txt
streamlit run app.py

# Train model (needs creditcard.csv)
jupyter notebook part1.ipynb
```

**Issues?**
- Model not found: Run notebook first
- Port busy: `streamlit run app.py --server.port 8502`

## 🤝 Contributing

1. Fork & PR
2. Update model/dataset
3. Add features (e.g., SHAP explanations, auth)

## 📄 License

MIT License - feel free to use & modify!

---

**Built with ❤️ for Microsoft Projects** | Questions? Check [Streamlit Docs](https://docs.streamlit.io/)

