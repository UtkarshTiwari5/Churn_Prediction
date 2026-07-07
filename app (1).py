import streamlit as st
import joblib
import pandas as pd

# Page Config
st.set_page_config(page_title="Customer Churn Prediction")

# Load Model
model = joblib.load("churn_model.pkl")

# Title
st.title("Customer Churn Prediction")

# Inputs
credit_score = st.slider("Credit Score", 300, 900, 600)

gender = st.selectbox("Gender", ["Male", "Female"])

age = st.slider("Age", 18, 100, 35)

tenure = st.slider("Tenure", 0, 10, 5)

balance = st.slider(
    "Balance",
    min_value=0.0,
    max_value=300000.0,
    value=50000.0,
    step=1000.0
)

num_products = st.slider("Number of Products", 1, 4, 1)

has_cr_card = st.selectbox("Has Credit Card", [0, 1])

is_active = st.selectbox("Is Active Member", [0, 1])

estimated_salary = st.slider(
    "Estimated Salary",
    min_value=0.0,
    max_value=300000.0,
    value=50000.0,
    step=1000.0
)

geography = st.selectbox(
    "Geography",
    ["France", "Germany", "Spain"]
)

# Encoding
gender = 1 if gender == "Male" else 0
geo_germany = 1 if geography == "Germany" else 0
geo_spain = 1 if geography == "Spain" else 0

# DataFrame
data = pd.DataFrame({
    "CreditScore": [credit_score],
    "Gender": [gender],
    "Age": [age],
    "Tenure": [tenure],
    "Balance": [balance],
    "NumOfProducts": [num_products],
    "HasCrCard": [has_cr_card],
    "IsActiveMember": [is_active],
    "EstimatedSalary": [estimated_salary],
    "Geography_Germany": [geo_germany],
    "Geography_Spain": [geo_spain]
})

# Prediction
if st.button("Predict"):
    prediction = model.predict(data)[0]

    if prediction == 1:
        st.error("⚠️ Customer is likely to Churn.")
    else:
        st.success("✅ Customer is Not likely to Churn.")
