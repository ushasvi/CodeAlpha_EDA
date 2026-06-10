import pandas as pd
import matplotlib.pyplot as plt

# Load Dataset
df = pd.read_csv("Titanic-Dataset.csv")

# Basic Information
print(df.head())
print(df.info())
print(df.describe())

# Missing Values
print(df.isnull().sum())

# Survival Count
survival = df['Survived'].value_counts()
print(survival)

# Visualization
survival.plot(kind='bar')
plt.title("Survival Count")
plt.xlabel("Survived")
plt.ylabel("Passengers")
plt.show()

# Gender Analysis
gender_survival = pd.crosstab(df['Sex'], df['Survived'])
print(gender_survival)

gender_survival.plot(kind='bar')
plt.title("Gender vs Survival")
plt.show()
