import pandas as pd
import random

countries = ["India", "USA", "UK", "Canada", "Australia"]
purposes = ["Coding", "Studying", "Research", "Writing", "Career Help"]
usage = ["Daily", "Weekly", "Monthly"]

data = []

for i in range(1, 1001):
    data.append([
        i,
        random.randint(18, 45),      # Age
        random.choice(countries),
        random.choice(usage),
        random.choice(purposes),
        random.randint(1, 5)         # Satisfaction
    ])

df = pd.DataFrame(data, columns=[
    "UserID",
    "Age",
    "Country",
    "UsageFrequency",
    "Purpose",
    "Satisfaction"
])

df.to_excel("dataset.xlsx", index=False)

print("Dataset created successfully!")
