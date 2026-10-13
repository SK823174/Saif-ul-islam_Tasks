import numpy as np
from scipy import stats

# Create a List of Speed Values
speed = [99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86]

# Calculate the Mean (Average Value)
x = np.mean(speed)
print(x)

# Calculate the Median (Middle Value)
x = np.median(speed)
print(x)

# Calculate the Mode (Most Common Value)
x = stats.mode(speed)
print(x)
