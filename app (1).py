import streamlit as st
import joblib
import pandas as pd

st.set_page_config(page_title="Customer Churn Prediction")

model = joblib.load("churn_model.pkl")

st.title("Customer Churn Prediction")

credit_score = st.number_input("Credit Score", 300, 900, 600)
gender = st.selectbox("Gender", ["Male", "Female"])
age = st.number_input("Age", 18, 100, 35)
tenure = st.slider("Tenure", 0, 10, 5)
balance = st.number_input("Balance", 0.0, 300000.0, 50000.0)
num_products = st.slider("Number of Products", 1, 4, 1)
has_cr_card = st.selectbox("Has Credit Card", [0, 1])
is_active = st.selectbox("Is Active Member", [0, 1])
estimated_salary = st.number_input("Estimated Salary", 0.0, 300000.0, 50000.0)
geography = st.selectbox("Geography", ["France", "Germany", "Spain"])

gender = 1 if gender == "Male" else 0

geo_germany = 1 if geography == "Germany" else 0
geo_spain = 1 if geography == "Spain" else 0

data = pd.DataFrame({
    "CreditScore":[credit_score],
    "Gender":[gender],
    "Age":[age],
    "Tenure":[tenure],
    "Balance":[balance],
    "NumOfProducts":[num_products],
    "HasCrCard":[has_cr_card],
    "IsActiveMember":[is_active],
    "EstimatedSalary":[estimated_salary],
    "Geography_Germany":[geo_germany],
    "Geography_Spain":[geo_spain]
})

if st.button("Predict"):
    prediction = model.predict(data)[0]

    if prediction == 1:
        st.error("Customer will leave the bank.")
    else:
        st.success("Customer will stay with the bank.")
