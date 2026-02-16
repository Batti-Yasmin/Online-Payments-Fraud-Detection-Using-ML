🛡️ Online Payments Fraud Detection Using ML

A machine learning web application that detects fraudulent online payment transactions in real time using a trained classification model and an interactive Streamlit interface.

Built using:

- Streamlit (Frontend & Deployment)  
- Python (Backend & ML Model)  
- Random Forest Classifier  
- PaySim Financial Fraud Dataset  

---

 🚀 Project Overview

This system predicts whether a financial transaction is:  

- ✅ Legitimate  
- ⚠ Fraudulent  

It also provides:  

- Fraud probability score  
- Risk classification (Low / Medium / High)  
- Real-time prediction via web app  

The architecture separates UI, backend logic, and ML model into independent layers.  

---

 🏗️ Architecture

Streamlit Web App (Frontend / UI)
⬇
Python Backend Logic
⬇
Trained Random Forest Model
⬇
Fraud Prediction Output

---

 📂 Project Structure

online-payments-fraud-detection/
│
├── app.py
├── fraud_detection_model.pkl
├── scaler.pkl
├── requirements.txt
├── README.md


---

📊 Dataset

Dataset Used: PaySim Synthetic Financial Dataset  

Features:  

- step  
- amount  
- oldbalanceOrg  
- newbalanceOrig  
- oldbalanceDest  
- newbalanceDest  
- isFraud  

Fraud detection is highly imbalanced, handled using:

- `class_weight = "balanced"`  

---

🧠 Machine Learning Model

Model Used: Random Forest Classifier  

Techniques Applied:

- Data sampling (200k rows for efficient training)  
- One-hot encoding  
- Stratified train-test split  
- Class imbalance handling  
- ROC-AUC evaluation  
- Probability-based risk scoring  

Sample Performance:

- ROC-AUC ≈ 0.96  
- Fraud Recall ≈ 0.76  

---

⚙️ Setup Instructions

1️⃣ Install Python & Dependencies 

2️⃣ Run the ML Web App (Frontend + Backend in one)

Your Streamlit app combines UI and ML backend:  

```bash
streamlit run app.py

3️⃣ ML Service / Model

- fraud_detection_model.pkl
- scaler.pkl

Workflow:

User Input → Scaler → Random Forest Model → Fraud Prediction → Output on Streamlit

📈 Risk Classification Logic

- Probability ≥ 0.8 → High Risk

- 0.5 ≤ Probability < 0.8 → Medium Risk

- < 0.5 → Low Risk

💡 Key Features

- Real-time Fraud Prediction
- Probability-Based Scoring
- Modular Architecture
- Safe Model Loading
- Clean and Interactive UI
- Backend-ML Integration
- Production-Ready Structure

🛠️ Technologies Used

Frontend / UI:

- Streamlit

Machine Learning / Backend:

- Python 3.10.2
- Pandas
- NumPy
- Scikit-learn
- Joblib

Other Tools:

- Git / GitHub
- Streamlit Cloud

🎯 Future Improvements

- Replace Random Forest with XGBoost
- Add MongoDB transaction storage
- Add user authentication (JWT)
- Add dashboard analytics
- Deploy to cloud (Render + Vercel)
- Docker containerization


---











