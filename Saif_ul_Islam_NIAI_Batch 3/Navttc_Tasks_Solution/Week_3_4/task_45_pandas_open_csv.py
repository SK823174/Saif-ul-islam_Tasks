import pandas as pd

# Load a CSV File into a DataFrame
df = pd.read_csv("data.csv")

# Print the Entire DataFrame
print(df.to_string())

# Print the DataFrame Without to_string()
df = pd.read_csv("data.csv")
print(df)

# Check the Maximum Number of Rows Displayed
print(pd.options.display.max_rows)

# Increase the Maximum Rows Displayed
pd.options.display.max_rows = 9999

# Load and Display the DataFrame
df = pd.read_csv("data.csv")
print(df)
