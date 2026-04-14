import warnings
warnings.filterwarnings("ignore")
import streamlit as st
import joblib
import numpy as np
import os

# Page config
st.set_page_config(
    page_title="Customer Attrition Predictor",
    page_icon="🔮",
    layout="centered"
)

# Load saved scaler and model
base_path = os.path.dirname(__file__)
scaler = joblib.load(os.path.join(base_path, "scaler.pkl"))
model = joblib.load(os.path.join(base_path, "model.pkl"))

# Header
st.title("🔮 Customer Attrition Predictor")
st.markdown("""
<h4 style='text-align: center;'>About This App</h4>
This app uses a machine learning model trained on real customer data to predict whether a customer is likely to leave the company. 
Simply enter the customer's age, how long they have been with the company, how much they pay per month, and their gender. 
Once you have filled in all the details, click the <b>Predict</b> button and the app will instantly tell you whether that customer is likely to <b>stay</b> or <b>leave</b>.
This can help businesses take action early by identifying at-risk customers before they leave.
""", unsafe_allow_html=True)
st.divider()

# User inputs
age = st.number_input("🎂 Age", min_value=10, max_value=100, value=30)
st.caption("⚠️ Valid range: 10 to 100 years.")

tenure = st.number_input("📅 Tenure (months)", min_value=0, max_value=130, value=10)
st.caption("⚠️ Valid range: 0 to 130 months. How long the customer has been with the company.")

monthly_charge = st.number_input("💰 Monthly Charge ($)", min_value=30, max_value=150, value=50)
st.caption("⚠️ Valid range: $30 to $150. This app is designed for subscription based businesses such as phone carriers, internet providers, and insurance companies. The monthly charge is capped at $150 due to the limits of the training data — entering values outside this range may produce unreliable results.")

gender = st.selectbox("👤 Gender", ["Male", "Female"])
st.divider()

predict_button = st.button("🔮 Predict")

if predict_button:
    st.balloons()
    gender_selected = 1 if gender == "Female" else 0
    x = [[age, gender_selected, tenure, monthly_charge]]
    x_array = np.array(x)
    x_array = scaler.transform(x_array)
    prediction = model.predict(x_array)[0]

    if prediction == 1:
        st.error("⚠️ This customer is likely to LEAVE")
    else:
        st.success("✅ This customer is likely to STAY")
else:
    st.info("👆 Enter customer details above and click Predict to see the result.")
