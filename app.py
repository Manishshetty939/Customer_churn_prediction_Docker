import streamlit as st
import requests

st.set_page_config(page_title="Customer Churn Predictor", layout="centered")

st.title("🧠 Customer Churn Prediction")
st.markdown("Enter RFM (Recency, Frequency, Monetary) values to predict churn.")

# Input fields
recency = st.number_input("Recency (days since last purchase):", min_value=0, max_value=1000, value=100)
frequency = st.number_input("Frequency (number of purchases):", min_value=0, max_value=100, value=10)
monetary = st.number_input("Monetary (total spent):", min_value=0.0, max_value=10000.0, value=500.0)

if st.button("Predict Churn"):
    payload = {
        "Recency": recency,
        "Frequency": frequency,
        "Monetary": monetary
    }
    try:
        response = requests.post("http://localhost:8000/predict", json=payload)
        result = response.json()
        churn = result.get("churn_prediction")

        if churn == 1:
            st.error("⚠️ This customer is likely to CHURN.")
        elif churn == 0:
            st.success("✅ This customer is NOT likely to churn.")
        else:
            st.warning("result " + str(result))

    except Exception as e:
        st.error(f"API Error: {e}")
