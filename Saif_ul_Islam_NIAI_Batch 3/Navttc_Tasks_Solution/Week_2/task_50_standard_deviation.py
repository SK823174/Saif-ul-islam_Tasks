import numpy as np

# Create a List of Speed Values
speed = [86, 87, 88, 86, 87, 85, 86]

# Calculate the Standard Deviation
x = np.std(speed)
print(x)

# Create a List of Speed Values with a Wider Range
speed = [32, 111, 138, 28, 59, 77, 97]

# Calculate the Standard Deviation
x = np.std(speed)
print(x)

# Calculate the Variance
x = np.var(speed)
print(x)

# Calculate the Standard Deviation Again
x = np.std(speed)
print(x)

# Calculate the Square Root of the Variance
x = np.sqrt(np.var(speed))
print(x)
