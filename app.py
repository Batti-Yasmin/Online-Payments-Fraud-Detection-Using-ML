import streamlit as st
import numpy as np
import joblib

model = joblib.load("fraud_detection_model.pkl")
scaler = joblib.load("scaler.pkl")

st.title("💳 Online Payment Fraud Detection")

step = st.number_input("Step")
amount = st.number_input("Transaction Amount")
oldbalanceOrg = st.number_input("Old Balance Sender")
newbalanceOrig = st.number_input("New Balance Sender")
oldbalanceDest = st.number_input("Old Balance Receiver")
newbalanceDest = st.number_input("New Balance Receiver")

type_CASH_OUT = st.checkbox("CASH_OUT")
type_DEBIT = st.checkbox("DEBIT")
type_PAYMENT = st.checkbox("PAYMENT")
type_TRANSFER = st.checkbox("TRANSFER")

if st.button("Predict"):
    data = np.array([[step, amount, oldbalanceOrg, newbalanceOrig,
                      oldbalanceDest, newbalanceDest,
                      int(type_CASH_OUT), int(type_DEBIT),
                      int(type_PAYMENT), int(type_TRANSFER)]])
    
    data = scaler.transform(data)
    result = model.predict(data)
    
    if result[0] == 1:
        st.error("🚨 Fraud Transaction")
    else:
        st.success("✅ Normal Transaction")
