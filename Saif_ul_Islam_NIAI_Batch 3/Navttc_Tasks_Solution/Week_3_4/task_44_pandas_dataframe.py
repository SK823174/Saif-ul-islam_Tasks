import pandas as pd

# Create a Simple Pandas DataFrame
data = {
    "calories": [420, 380, 390],
    "duration": [50, 40, 45]
}

# Load Data into a DataFrame
df = pd.DataFrame(data)
print(df)

# Locate Row 0
print(df.loc[0])

# Locate Rows 0 and 1
print(df.loc[[0, 1]])

# Create a DataFrame with Named Indexes
data = {
    "calories": [420, 380, 390],
    "duration": [50, 40, 45]
}

df = pd.DataFrame(data, index=["day1", "day2", "day3"])
print(df)

# Locate a Row Using Its Named Index
print(df.loc["day2"])

# Load a CSV File into a DataFrame
df = pd.read_csv("data.csv")
print(df)
