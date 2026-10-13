import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn import metrics
from sklearn.metrics import classification_report

# Define the Column Names
col_names = [
    "diabetic",
    "glucose",
    "bp",
    "skin",
    "insulin",
    "bmi",
    "pedigree",
    "age",
    "label"
]

# Load the Diabetes Dataset
pima = pd.read_csv(
    "pima-indians-diabetes.csv",
    header=None,
    names=col_names
)

# Display the First 5 Rows
print(pima.head())

# Display Information About the Dataset
print(pima.info())

# Select the Feature Columns
feature_cols = [
    "pregnant",
    "insulin",
    "bmi",
    "age",
    "glucose",
    "bp",
    "pedigree"
]

# Separate Features and Target Variable
X = pima[feature_cols]
y = pima["label"]

# Split the Dataset into Training and Testing Sets
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.25,
    random_state=16,
    stratify=y
)

# Create the Logistic Regression Model
logreg = LogisticRegression(max_iter=1000, random_state=16)

# Train the Model
logreg.fit(X_train, y_train)

# Make Predictions on the Test Set
y_pred = logreg.predict(X_test)

# Calculate the Confusion Matrix
cnf_matrix = metrics.confusion_matrix(y_test, y_pred)
print("Confusion Matrix:")
print(cnf_matrix)

# Visualize the Confusion Matrix
class_names = [0, 1]

plt.figure(figsize=(6, 4))
sns.heatmap(
    pd.DataFrame(cnf_matrix),
    annot=True,
    cmap="YlGnBu",
    fmt="g",
    xticklabels=class_names,
    yticklabels=class_names
)

plt.title("Confusion Matrix")
plt.ylabel("Actual Label")
plt.xlabel("Predicted Label")
plt.tight_layout()
plt.show()

# Display the Classification Report
target_names = ["Without Diabetes", "With Diabetes"]

print("Classification Report:")
print(
    classification_report(
        y_test,
        y_pred,
        target_names=target_names,
        zero_division=0
    )
)

# Calculate the Model Accuracy
accuracy = metrics.accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

# Calculate Prediction Probabilities for the Positive Class
y_pred_proba = logreg.predict_proba(X_test)[:, 1]

# Calculate the ROC Curve
fpr, tpr, thresholds = metrics.roc_curve(y_test, y_pred_proba)

# Calculate the Area Under the ROC Curve
auc = metrics.roc_auc_score(y_test, y_pred_proba)
print("ROC AUC Score:", auc)

# Plot the ROC Curve
plt.figure(figsize=(6, 4))
plt.plot(fpr, tpr, label=f"ROC Curve (AUC = {auc:.2f})")
plt.plot([0, 1], [0, 1], linestyle="--", label="Random Classifier")

plt.title("ROC Curve")
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.legend(loc="lower right")
plt.tight_layout()
plt.show()
