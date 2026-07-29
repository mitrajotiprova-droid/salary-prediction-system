import streamlit as st
import joblib
import pandas as pd


model = joblib.load("salary_model.pkl")

st.title("💼 Salary Prediction System")

st.write("Enter Employee Details")



age = st.number_input("Age", min_value=18, max_value=65, value=25)

gender = st.selectbox(
    "Gender",
    ["Female", "Male"]
)

education = st.selectbox(
    "Education Level",
    ["Bachelor's", "Master's", "PhD"]
)

experience = st.number_input(
    "Years of Experience",
    min_value=0,
    max_value=40,
    value=1
)

job = st.selectbox(
    "Job Title",
    [
        "Analyst",
        "Data Scientist",
        "Manager",
        "Software Engineer"
    ]
)

# -------------------------
# Manual Encoding
# -------------------------

gender = 0 if gender == "Female" else 1

education_map = {
    "Bachelor's": 0,
    "Master's": 1,
    "PhD": 2
}

job_map = {
    "Analyst": 0,
    "Data Scientist": 1,
    "Manager": 2,
    "Software Engineer": 3
}

education = education_map[education]
job = job_map[job]

# -------------------------
# Prediction
# -------------------------

if st.button("Predict Salary"):

    data = pd.DataFrame({
        "Age": [age],
        "Gender": [gender],
        "Education Level": [education],
        "Job Title": [job],
        "Years of Experience": [experience]
    })

    salary = model.predict(data)[0]

    st.success(f"Predicted Salary: {salary:.2f}")

    # Experience Category
    if experience < 3:
        category = "Fresher"
    elif experience < 8:
        category = "Mid-Level"
    else:
        category = "Experienced"

    st.write("### Experience Category")
    st.write(category)

    # HR Recommendation
    if salary >= 120000:
        recommendation = "Offer High Salary Package"
    elif salary >= 70000:
        recommendation = "Offer Standard Salary Package"
    else:
        recommendation = "Suitable for Entry-Level Position"

    st.write("### HR Recommendation")
    st.write(recommendation)