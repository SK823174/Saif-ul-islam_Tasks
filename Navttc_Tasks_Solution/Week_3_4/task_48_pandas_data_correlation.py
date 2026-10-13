import pandas as pd

# Load a CSV File into a DataFrame
df = pd.read_csv("data.csv")

# Calculate the Correlation Between Columns
print(df.corr())

# Correlation Values Range from -1 to 1
# 1.0  = Perfect Positive Correlation
# 0.0  = No Linear Correlation
# -1.0 = Perfect Negative Correlation

# Check the Correlation Between Duration and Calories
print(df["Duration"].corr(df["Calories"]))

# Check the Correlation Between Duration and Maxpulse
print(df["Duration"].corr(df["Maxpulse"]))
