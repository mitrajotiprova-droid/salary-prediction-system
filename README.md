# 💼 Salary Prediction System using Machine Learning

A Machine Learning project that predicts an employee's salary based on their profile, including age, gender, education level, years of experience, and job title. The project also includes a simple Streamlit web application for real-time salary prediction.

---

## 📌 Project Overview

ABC Technologies wants to automate the salary estimation process for job applicants. Instead of manually deciding salary packages, this application uses a **Linear Regression** model trained on historical employee data to predict an appropriate salary.

---

## 🚀 Features

- Data Understanding
- Exploratory Data Analysis (EDA)
- Data Preprocessing
- Linear Regression Model
- Model Evaluation
- Streamlit Web Application
- Predict Employee Salary
- Experience Category
- HR Recommendation

---

## 📂 Dataset Features

- Age
- Gender
- Education Level
- Job Title
- Years of Experience
- Salary (Target Variable)

---

## 🛠 Technologies Used

- Python
- Pandas
- Matplotlib
- Seaborn
- Scikit-learn
- Joblib
- Streamlit

---

## 📊 Exploratory Data Analysis

The project includes the following visualizations:

- Years of Experience vs Salary
- Education Level Count
- Salary Distribution (Boxplot)
- Average Salary by Job Title

---

## ⚙️ Data Preprocessing

The following preprocessing steps were performed:

- Removed missing values
- Encoded categorical variables using LabelEncoder
- Selected input and target variables
- Split dataset into training and testing sets

---

## 🤖 Machine Learning Model

**Algorithm Used**

- Linear Regression

---

## 📈 Evaluation Metrics

The model was evaluated using:

- R² Score
- Mean Absolute Error (MAE)
- Mean Squared Error (MSE)

---

## 💻 Streamlit Application

The web application allows users to enter:

- Age
- Gender
- Education Level
- Years of Experience
- Job Title

The application displays:

- Predicted Salary
- Experience Category
- HR Recommendation

---

## 📁 Project Structure

```
Salary-Prediction-System/
│
├── salary-pred.csv
├── train_model.py
├── app.py
├── salary_model.pkl
├── README.md
└── requirements.txt
```

---

## ▶️ Installation

Clone the repository

```bash
git clone https://github.com/your-username/Salary-Prediction-System.git
```

Go to the project folder

```bash
cd Salary-Prediction-System
```

Install dependencies

```bash
pip install -r requirements.txt
```

Train the model

```bash
python train_model.py
```

Run the Streamlit application

```bash
python -m streamlit run app.py
```

---

## 📷 Output

The application predicts:

- Employee Salary
- Experience Category
- HR Recommendation

---

## 🎯 Future Improvements

- Random Forest Regressor
- Decision Tree Regressor
- Better UI Design
- Model Comparison
- Deployment on Streamlit Community Cloud

---

## 👨‍💻 Author

**Jotiprova Mitra**

Computer Science & Engineering Student

---

## ⭐ If you like this project

Please consider giving this repository a **Star ⭐** on GitHub.
