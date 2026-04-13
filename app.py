import warnings
warnings.filterwarnings("ignore")
import streamlit as st
import joblib
import numpy as np
import os

# Load saved scaler and model
base_path = os.path.dirname(__file__)
scaler = joblib.load(os.path.join(base_path, "scaler.pkl"))
model = joblib.load(os.path.join(base_path, "model.pkl"))

# App title and intro text
st.title("Customer Attrition Predictor")
st.divider()
st.write("Please enter the values and hit the predict button for getting a prediction.")
st.divider()

# User inputs
age = st.number_input("Enter age", min_value=10, max_value=100, value=30)
tenure = st.number_input("Enter tenure", min_value=0, max_value=130, value=10)
monthly_charge = st.number_input("Enter monthly charge", min_value=30, max_value=150, value=50)
gender = st.selectbox("Enter the gender", ["Male", "Female"])
st.divider()

predict_button = st.button("Predict")

if predict_button:
    st.divider()
    st.balloons()
    gender_selected = 1 if gender == "Female" else 0
    x = [[age, gender_selected, tenure, monthly_charge]]
    x_array = np.array(x)
    x_array = scaler.transform(x_array)
    prediction = model.predict(x_array)[0]
    predicted = "Yes" if prediction == 1 else "No"
    st.write(f"Predicted Attrition: {predicted}")
else:
    st.write("Please enter the values and use the predict button.")
