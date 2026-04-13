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

# Dark mode custom styling
st.markdown("""
    <style>
        body { background-color: #0e1117; color: white; }
        .main { background-color: #0e1117; }
        .stButton>button {
            background-color: #4f8bf9;
            color: white;
            border-radius: 10px;
            height: 3em;
            width: 100%;
            font-size: 18px;
            font-weight: bold;
            border: none;
        }
        .stButton>button:hover {
            background-color: #2563eb;
            color: white;
        }
        .result-yes {
            background-color: #ff4b4b;
            padding: 20px;
            border-radius: 10px;
            text-align: center;
            font-size: 24px;
            font-weight: bold;
            color: white;
        }
        .result-no {
            background-color: #00c853;
            padding: 20px;
            border-radius: 10px;
            text-align: center;
            font-size: 24px;
            font-weight: bold;
            color: white;
        }
    </style>
""", unsafe_allow_html=True)

# Load saved scaler and model
base_path = os.path.dirname(__file__)
scaler = joblib.load(os.path.join(base_path, "scaler.pkl"))
model = joblib.load(os.path.join(base_path, "model.pkl"))

# Header
st.title("🔮 Customer Attrition Predictor")
st.markdown("#### Predict whether a customer is likely to leave using machine learning.")
st.divider()

# Sidebar inputs
with st.sidebar:
    st.header("📋 Enter Customer Details")
    st.write("Fill in the details below and click Predict.")
    st.divider()
    age = st.number_input("🎂 Age", min_value=10, max_value=100, value=30)
    tenure = st.number_input("📅 Tenure (months)", min_value=0, max_value=130, value=10)
    monthly_charge = st.number_input("💰 Monthly Charge ($)", min_value=30, max_value=150, value=50)
    gender = st.selectbox("👤 Gender", ["Male", "Female"])
    st.divider()
    predict_button = st.button("🔮 Predict")

# Main area
st.markdown("### 📊 Prediction Result")
st.write("Enter the customer details in the left sidebar and click **Predict** to see the result.")
st.divider()

if predict_button:
    st.balloons()
    gender_selected = 1 if gender == "Female" else 0
    x = [[age, gender_selected, tenure, monthly_charge]]
    x_array = np.array(x)
    x_array = scaler.transform(x_array)
    prediction = model.predict(x_array)[0]

    if prediction == 1:
        st.markdown('<div class="result-yes">⚠️ This customer is likely to LEAVE</div>', unsafe_allow_html=True)
    else:
        st.markdown('<div class="result-no">✅ This customer is likely to STAY</div>', unsafe_allow_html=True)
else:
    st.info("👈 Enter customer details in the sidebar to get started.")
