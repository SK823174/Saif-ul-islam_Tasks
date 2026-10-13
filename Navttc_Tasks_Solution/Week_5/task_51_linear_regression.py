# Task 51: Machine Learning - Linear Regression

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error

# Load the Student Scores Dataset
df = pd.read_csv("student_scores.csv")

# Display the First 5 Rows
print(df.head())

# Display the Shape of the Dataset
print(df.shape)

# Create a Scatter Plot of Hours and Scores
df.plot.scatter(x="Hours", y="Scores", title="Hours vs Scores")
plt.show()

# Calculate the Correlation Between Columns
print(df.corr())

# Display Descriptive Statistics
print(df.describe())

# Separate Features and Target
X = df["Hours"].values.reshape(-1, 1)
y = df["Scores"].values.reshape(-1, 1)

# Split the Dataset into Training and Testing Sets
SEED = 42
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=SEED
)

# Create a Linear Regression Model
regressor = LinearRegression()

# Train the Model
regressor.fit(X_train, y_train)

# Display the Intercept
print(regressor.intercept_)

# Display the Slope (Coefficient)
print(regressor.coef_)

# Predict the Score for 9.5 Hours of Study
score = regressor.predict([[9.5]])
print(score)

# Predict Scores for the Test Dataset
y_pred = regressor.predict(X_test)

# Compare Actual and Predicted Scores
df_preds = pd.DataFrame({
    "Actual": y_test.squeeze(),
    "Predicted": y_pred.squeeze()
})
print(df_preds)

# Calculate Mean Absolute Error (MAE)
mae = mean_absolute_error(y_test, y_pred)
print(f"Mean absolute error: {mae:.2f}")

# Calculate Mean Squared Error (MSE)
mse = mean_squared_error(y_test, y_pred)
print(f"Mean squared error: {mse:.2f}")

# Calculate Root Mean Squared Error (RMSE)
rmse = np.sqrt(mse)
print(f"Root mean squared error: {rmse:.2f}")

# Display the Model's R² Score
print("R² Score:", regressor.score(X_test, y_test))


# Multiple Linear Regression

# Load the Petrol Consumption Dataset
df = pd.read_csv("petrol_consumption.csv")

# Display the First 5 Rows
print(df.head())

# Display the Shape of the Dataset
print(df.shape)

# Display Descriptive Statistics
print(df.describe().round(2).T)

# Define the Independent Variables (Features)
X = df[
    [
        "Average_income",
        "Paved_Highways",
        "Population_Driver_licence(%)",
        "Petrol_tax"
    ]
]

# Define the Dependent Variable (Target)
y = df["Petrol_Consumption"]

# Split the Dataset into Training and Testing Sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=SEED
)

# Create and Train the Multiple Linear Regression Model
regressor = LinearRegression()
regressor.fit(X_train, y_train)

# Display the Intercept
print(regressor.intercept_)

# Display the Coefficients
print(regressor.coef_)

# Display Feature Names and Their Coefficients
coefficients_df = pd.DataFrame(
    data=regressor.coef_,
    index=X.columns,
    columns=["Coefficient value"]
)
print(coefficients_df)

# Predict Petrol Consumption
y_pred = regressor.predict(X_test)

# Compare Actual and Predicted Values
results = pd.DataFrame({
    "Actual": y_test,
    "Predicted": y_pred
})
print(results)

# Calculate Mean Absolute Error (MAE)
mae = mean_absolute_error(y_test, y_pred)
print(f"Mean absolute error: {mae:.2f}")

# Calculate Mean Squared Error (MSE)
mse = mean_squared_error(y_test, y_pred)
print(f"Mean squared error: {mse:.2f}")

# Calculate Root Mean Squared Error (RMSE)
rmse = np.sqrt(mse)
print(f"Root mean squared error: {rmse:.2f}")

# Calculate R² Score for the Test Dataset
print("Test R² Score:", regressor.score(X_test, y_test))

# Calculate R² Score for the Training Dataset
print("Training R² Score:", regressor.score(X_train, y_train))
