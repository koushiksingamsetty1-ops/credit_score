import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load("credit_risk_model.pkl")

st.title("💳 Credit Risk Prediction System")

# Numerical Inputs
age = st.number_input("Age", 18, 100, 25)
income = st.number_input("Income", 0.0, 1000000.0, 50000.0)
loan_amount = st.number_input("Loan Amount", 0.0, 1000000.0, 100000.0)
credit_score = st.number_input("Credit Score", 300, 900, 700)
years_experience = st.number_input("Years Experience", 0, 50, 5)

# Dropdowns
gender = st.selectbox("Gender", ["Male", "Female"])

education = st.selectbox(
    "Education",
    ["High School", "Bachelor", "Master", "PhD"]
)

city = st.selectbox(
    "City",
    ["Hyderabad", "Mumbai", "Delhi", "Chennai", "Bangalore"]
)

employment = st.selectbox(
    "Employment Type",
    ["Salaried", "Self-Employed", "Business"]
)

# Manual encoding
gender_map = {
    "Male": 1,
    "Female": 0
}

education_map = {
    "High School": 0,
    "Bachelor": 1,
    "Master": 2,
    "PhD": 3
}

city_map = {
    "Hyderabad": 0,
    "Mumbai": 1,
    "Delhi": 2,
    "Chennai": 3,
    "Bangalore": 4
}

employment_map = {
    "Salaried": 0,
    "Self-Employed": 1,
    "Business": 2
}

if st.button("Predict"):

    input_data = pd.DataFrame({
        "Age": [age],
        "Income": [income],
        "LoanAmount": [loan_amount],
        "CreditScore": [credit_score],
        "YearsExperience": [years_experience],
        "Gender": [gender_map[gender]],
        "Education": [education_map[education]],
        "City": [city_map[city]],
        "EmploymentType": [employment_map[employment]]
    })

    prediction = model.predict(input_data)[0]

    if prediction == 1:
        st.success("✅ Loan Approved")
    else:
        st.error("❌ Loan Rejected")