import pandas as pd

# Sample data (you can load from JSON later)
data = [
    {"name": "Prem", "age": 20, "bp": 120, "sugar": 90, "city": "Vizag"},
    {"name": "Rahul", "age": 22, "bp": 140, "sugar": 110, "city": "Hyderabad"},
    {"name": "Anu", "age": 21, "bp": 130, "sugar": 100, "city": "Vizag"},
]

# Convert to DataFrame
df = pd.DataFrame(data)

print("\n--- Full Data ---")
print(df)

# Basic Analysis
print("\nAverage Age:", df["age"].mean())
print("Max BP:", df["bp"].max())

# Group By City
print("\n--- Patients by City ---")
print(df.groupby("city").size())

# Filter High BP
print("\n--- High BP Patients (>130) ---")
print(df[df["bp"] > 130])
