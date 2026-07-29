import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
import joblib

# Import the dataset
df = pd.read_csv("salary-pred.csv")

# 1. Display the first five records
print("First Five Records:")
print(df.head())

# 2. Check dataset dimensions
print("\nDataset Dimensions (Rows, Columns):")
print(df.shape)

# 3. Display data types
print("\nData Types:")
print(df.dtypes)

# 4. Check for missing values
print("\nMissing Values:")
print(df.isnull().sum())

# 5. Display descriptive statistics
print("\nDescriptive Statistics:")
print(df.describe(include='all'))





sns.set_style("whitegrid")


#years of experience vs salary 
plt.figure(figsize=(8,5))
sns.scatterplot(
    data=df,
    x="Years of Experience",
    y="Salary",
    color="blue"
)

plt.title("Years of Experience vs Salary")
plt.xlabel("Years of Experience")
plt.ylabel("Salary")
plt.show()

#Education level count 

plt.figure(figsize=(8,5))
sns.countplot(
    data=df,
    x="Education Level",
    palette="Set2"
)

plt.title("Education Level Count")
plt.xlabel("Education Level")
plt.ylabel("Number of Employees")
plt.xticks(rotation=20)
plt.show()


#salary distribution

plt.figure(figsize=(8,5))
sns.boxplot(
    y=df["Salary"],
    color="lightgreen"
)

plt.title("Boxplot of Salary")
plt.ylabel("Salary")
plt.show()


# salary vs job title

avg_salary = df.groupby("Job Title")["Salary"].mean().sort_values()
plt.figure(figsize=(12,6))
plt.bar(avg_salary.index, avg_salary.values, color="skyblue")

plt.title("Average Salary by Job Title")
plt.xlabel("Job Title")
plt.ylabel("Average Salary")
plt.xticks(rotation=90)

plt.show()


# 1. Handle Missing Values


df.dropna(inplace=True)


# 2. Encode Categorical Variables


le = LabelEncoder()

df["Gender"] = le.fit_transform(df["Gender"])
df["Education Level"] = le.fit_transform(df["Education Level"])
df["Job Title"] = le.fit_transform(df["Job Title"])


# 3. Select Input and Target Variables


X = df.drop("Salary", axis=1)
y = df["Salary"]

print("Input Variables:")
print(X.head())

print("\nTarget Variable:")
print(y.head())


# 4. Split Dataset


X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("\nTraining Data Shape:", X_train.shape)
print("Testing Data Shape:", X_test.shape)

# Machine Learning Model

model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)


r2 = r2_score(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)

print("R² Score :", r2)
print("Mean Absolute Error :", mae)
print("Mean Squared Error :", mse)

#Streamlit Application 

joblib.dump(model, "salary_model.pkl")
