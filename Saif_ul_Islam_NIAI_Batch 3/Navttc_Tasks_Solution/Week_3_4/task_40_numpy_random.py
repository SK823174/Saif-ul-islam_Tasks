import numpy as np
from numpy import random

# Generate a Random Integer from 0 to 100
x = random.randint(100)
print(x)

# Generate a Random Float Between 0 and 1
x = random.rand()
print(x)

# Generate a 1-D Array of 5 Random Integers
x = random.randint(100, size=5)
print(x)

# Generate a 2-D Array of 3 Rows and 5 Columns of Random Integers
x = random.randint(100, size=(3, 5))
print(x)

# Generate a 1-D Array of 5 Random Floats
x = random.rand(5)
print(x)

# Generate a 2-D Array of 3 Rows and 5 Columns of Random Floats
x = random.rand(3, 5)
print(x)

# Generate a Random Value from an Array
x = random.choice([3, 5, 7, 9])
print(x)

# Generate a 2-D Array Using Values from a Given Array
x = random.choice([3, 5, 7, 9], size=(3, 5))
print(x)