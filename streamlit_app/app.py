import requests
import streamlit as st

st.set_page_config(
    page_title="Customer Retention Intelligence Platform",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Customer Retention Intelligence Platform")

st.write("Predict whether a customer is likely to churn.")

gender = st.selectbox("Gender", ["Male", "Female"])

senior = st.selectbox("Senior Citizen", [0, 1])

partner = st.selectbox("Partner", ["Yes", "No"])

dependents = st.selectbox("Dependents", ["Yes", "No"])

tenure = st.number_input(
    "Tenure (Months)",
    min_value=0,
    value=1
)

phone = st.selectbox(
    "Phone Service",
    ["Yes", "No"]
)

multiple = st.selectbox(
    "Multiple Lines",
    ["Yes", "No", "No phone service"]
)

internet = st.selectbox(
    "Internet Service",
    ["DSL", "Fiber optic", "No"]
)

online_security = st.selectbox(
    "Online Security",
    ["Yes", "No", "No internet service"]
)

online_backup = st.selectbox(
    "Online Backup",
    ["Yes", "No", "No internet service"]
)

device = st.selectbox(
    "Device Protection",
    ["Yes", "No", "No internet service"]
)

tech = st.selectbox(
    "Tech Support",
    ["Yes", "No", "No internet service"]
)

tv = st.selectbox(
    "Streaming TV",
    ["Yes", "No", "No internet service"]
)

movies = st.selectbox(
    "Streaming Movies",
    ["Yes", "No", "No internet service"]
)

contract = st.selectbox(
    "Contract",
    ["Month-to-month", "One year", "Two year"]
)

paperless = st.selectbox(
    "Paperless Billing",
    ["Yes", "No"]
)

payment = st.selectbox(
    "Payment Method",
    [
        "Electronic check",
        "Mailed check",
        "Bank transfer (automatic)",
        "Credit card (automatic)"
    ]
)

monthly = st.number_input(
    "Monthly Charges",
    value=70.0
)

total = st.number_input(
    "Total Charges",
    value=500.0
)

if st.button("Predict Churn"):

    payload = {

        "gender": gender,
        "SeniorCitizen": senior,
        "Partner": partner,
        "Dependents": dependents,
        "tenure": tenure,
        "PhoneService": phone,
        "MultipleLines": multiple,
        "InternetService": internet,
        "OnlineSecurity": online_security,
        "OnlineBackup": online_backup,
        "DeviceProtection": device,
        "TechSupport": tech,
        "StreamingTV": tv,
        "StreamingMovies": movies,
        "Contract": contract,
        "PaperlessBilling": paperless,
        "PaymentMethod": payment,
        "MonthlyCharges": monthly,
        "TotalCharges": total
    }

    response = requests.post(
        "http://127.0.0.1:8000/predict",
        json=payload
    )

    if response.status_code == 200:

        prediction = response.json()["prediction"]

        if prediction == "Yes":

            st.error("⚠️ Customer is likely to churn.")

        else:

            st.success("✅ Customer is likely to stay.")

    else:

        st.error("API Error")