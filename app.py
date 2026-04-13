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
    layout="wide"
)

# Professional dark styling with gold accents
st.markdown("""
    <style>
        /* Main background */
        .stApp {
            background-color: #0d1117;
        }
        
        /* Sidebar */
        [data-testid="stSidebar"] {
            background-color: #161b22;
            border-right: 1px solid #f0a500;
        }
        
        /* All text */
        html, body, [class*="css"] {
            color: #ffffff;
            font-family: 'Segoe UI', sans-serif;
        }
        
        /* Title */
        h1 {
            color: #f0a500 !important;
            font-size: 42px !important;
            font-weight: 800 !important;
            letter-spacing: 1px;
        }
        
        /* Subheadings */
        h3, h4 {
            color: #f0a500 !important;
        }

        /* Divider */
        hr {
            border-color: #f0a500;
        }
        
        /* Input boxes */
        [data-testid="stNumberInput"] input,
        [data-testid="stSelectbox"] div {
            background-color: #1f2937 !important;
            color: white !important;
            border: 1px solid #f0a500 !important;
            border-radius: 8px !important;
        }

        /* Predict button */
        .stButton>button {
            background-color: #f0a500;
            color: #0d1117;
            border-radius: 8px;
            height: 3em;
            width: 100%;
            font-size: 18px;
            font-weight: bold;
            border: none;
            letter-spacing: 1px;
        }
        .stButton>button:hover {
            background-color: #d4920a;
            color: #0d1117;
        }

        /* Result banners */
        .result-yes {
            background: linear-gradient(135deg, #7f0000, #cc0000);
            padding: 30px;
            border-radius: 12px;
            text-align: center;
            font-size: 28px;
            font-weight: bold;
            color: white;
            border: 1px solid #ff4b4b;
            margin-top: 20px;
        }
        .result-no {
            background: linear-gradient(135deg, #004d00, #00800060);
            padding: 30px;
            border-radius: 12px;
            text-align: center;
            font-size: 28px;
            font-weight: bold;
            color: white;
            border: 1px solid #00c853;
            margin-top: 20px;
        }

        /* Caption text */
        .stCaption {
            color: #9ca3af !important;
            font-size: 12px !important;
        }

        /* Info box */
        .stAlert {
            background-color: #1f2937 !important;
            border: 1px solid #f0a500 !important;
            color: white !important;
            border-radius: 10px !important;
        }

        /* Remove whitespace padding */
        .block-container {
            padding-top: 2rem !important;
            padding-bottom: 0rem !important;
            padding-left: 3rem !important;
            padding-right: 3rem !important;
        }
    </style>
""", unsafe_allow_html=True)

# Load saved scaler and model
base_path = os.path.dirname(__file__)
scaler = joblib.load(os.path.join(base_path, "scaler.pkl"))
model = joblib.load(os.path.join(base_path, "model.pkl"))

# Header
st.title("🔮 Customer Attrition Predictor")
st.markdown("#### Use machine learning to predict whether a customer is likely to leave.")
st.divider()

# Sidebar inputs
with st.sidebar:
    st.markdown("### 📋 Customer Details")
    st.write("Fill in the details below and click Predict.")
    st.divider()

    age = st.number_input("🎂 Age", min_value=10, max_value=100, value=30)
    st.caption("⚠️ Valid range: 10 to 100 years.")
    st.divider()

    tenure = st.number_input("📅 Tenure (months)", min_value=0, max_value=130, value=10)
    st.caption("⚠️ Valid range: 0 to 130 months. How long the customer has been with the company.")
    st.divider()

    monthly_charge = st.number_input("💰 Monthly Charge ($)", min_value=30, max_value=150, value=50)
    st.caption("⚠️ Valid range: $30 to $150. Maximum charge seen in the training data.")
    st.divider()

    gender = st.selectbox("👤 Gender", ["Male", "Female"])
    st.divider()

    predict_button = st.button("🔮 Predict")

# Main area
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    st.markdown("### 📊 Prediction Result")
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
        st.info("👈 Enter customer details in the sidebar and click Predict to see the result here.")
