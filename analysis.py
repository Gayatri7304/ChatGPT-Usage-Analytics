import pandas as pd
df = pd.read_excel("dataset.xlsx", engine="openpyxl")
print(df.head())

print("Total Users:", len(df))
print("\nPurpose Count:")
print(df["Purpose"].value_counts())

print("\nUsage Frequency:")
print(df["UsageFrequency"].value_counts())

print("\nAverage Satisfaction:")
print(round(df["Satisfaction"].mean(), 2))

import matplotlib.pyplot as plt

# Purpose Chart
df["Purpose"].value_counts().plot(kind="bar")
plt.title("Purpose of ChatGPT Usage")
plt.xlabel("Purpose")
plt.ylabel("Number of Users")
plt.show()

# Usage Frequency Chart
df["UsageFrequency"].value_counts().plot(kind="pie", autopct="%1.1f%%")
plt.ylabel("")
plt.title("Usage Frequency")
plt.show()


# Country Distribution
df["Country"].value_counts().plot(kind="bar")
plt.title("Users by Country")
plt.xlabel("Country")
plt.ylabel("Users")
plt.show()


# Age Group Analysis
bins = [18, 25, 35, 45]
labels = ["18-25", "26-35", "36-45"]

df["AgeGroup"] = pd.cut(df["Age"], bins=bins, labels=labels)

print("\nAge Group Distribution:")
print(df["AgeGroup"].value_counts())
