import pandas as pd

# Load a CSV File into a DataFrame
df = pd.read_csv("data.csv")

# Print the First 10 Rows
print(df.head(10))

# Print the First 5 Rows
print(df.head())

# Print the Last 5 Rows
print(df.tail())

# Print the Last 10 Rows
print(df.tail(10))

# Display Information About the DataFrame
print(df.info())