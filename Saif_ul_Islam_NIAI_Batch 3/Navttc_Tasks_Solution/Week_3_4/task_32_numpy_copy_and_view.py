# Copy an Array
import numpy as np

arr = np.array([1, 2, 3, 4, 5])
x = arr.copy()

arr[0] = 42

print(arr)
print(x)


# Create a View of an Array
import numpy as np

arr = np.array([1, 2, 3, 4, 5])
x = arr.view()

arr[0] = 42

print(arr)
print(x)


# Make Changes in the View
import numpy as np

arr = np.array([1, 2, 3, 4, 5])
x = arr.view()

x[0] = 31

print(arr)
print(x)


# Check if an Array Owns Its Data
import numpy as np

arr = np.array([1, 2, 3, 4, 5])

x = arr.copy()
y = arr.view()

print(x.base)
print(y.base)
