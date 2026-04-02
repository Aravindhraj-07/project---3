#importing necessary libraries
import streamlit as st
import pickle
import numpy as np
import pandas as pd

# Page config
st.set_page_config(page_title="Fraud Detection", layout="centered")#page title and layout

# Custom styling
st.markdown("""
<style>
.stButton>button {
    background-color: #4CAF50;
    color: white;
    border-radius: 8px;
}
</style>
""", unsafe_allow_html=True)

# Load model
model = pickle.load(open("model.pkl", "rb"))

# Title
st.title("💳 Credit Card Fraud Detection")
st.markdown("---")

# ==============================
# SECTION 1: Manual Input
# ==============================
st.subheader("Manual Input (Basic Demo)")#subheader for manual input section

col1, col2 = st.columns(2)#creating two columns for input fields

with col1:
    amount = st.number_input("Transaction Amount", min_value=0.0)

with col2:
    time = st.number_input("Transaction Time", min_value=0.0)

# Create feature array
features = np.zeros(30)
features[0] = time
features[-1] = amount
features = features.reshape(1, -1)

if st.button("Check Transaction"):#button to trigger prediction
    prediction = model.predict(features)#predicting using the model and the input features

    if prediction[0] == 1:#if prediction is 1, it is a fraudulent transaction
        st.error("🚨 Fraudulent Transaction")
    else:#if prediction is 0, it is a legitimate transaction
        st.success("✅ Legitimate Transaction")

st.markdown("---")

# ==============================
# SECTION 2: CSV Upload (Accurate)
#The dataset uses PCA-transformed features (V1–V28), which are not interpretable, 
# so I provided alternative input methods like CSV upload and sample test buttons for demonstration purposes.
st.subheader("Upload CSV for Accurate Prediction")

uploaded_file = st.file_uploader("Upload transaction file", type=["csv"])

if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)

    st.write("Preview of Data:")
    st.write(data.head())

    if st.button("Predict from CSV"):
        prediction = model.predict(data)

        st.write("Predictions:")
        st.write(prediction)

st.markdown("---")

# ==============================
# SECTION 3: Sample Test Buttons
# for demonstration, we can create buttons that simulate typical legitimate
#  and fraudulent transactions based on the dataset's characteristics.
st.subheader("Quick Test Examples")

if st.button("Test Legitimate Example"):#button to test a sample legitimate transaction
    sample = np.zeros((1, 30))
    sample[0][0] = 10000
    sample[0][-1] = 50

    prediction = model.predict(sample)

    st.success(f"Prediction: {prediction[0]} (Likely Legitimate)")

if st.button("Test Fraud Example"):#button to test a sample fraudulent transaction
    sample = np.zeros((1, 30))
    sample[0][0] = 10
    sample[0][-1] = 5000

    prediction = model.predict(sample)

    st.error(f"Prediction: {prediction[0]} (Possible Fraud)")#displaying the prediction result for the sample fraudulent transaction