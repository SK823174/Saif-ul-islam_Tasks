# Reshape from 1-D to 2-D
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

newarr = arr.reshape(4, 3)

print(newarr)


# Reshape from 1-D to 3-D
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

newarr = arr.reshape(2, 3, 2)

print(newarr)


# Reshape into an Invalid Shape
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

try:
    newarr = arr.reshape(3, 3)
    print(newarr)
except ValueError as error:
    print(error)


# Check if Reshaped Array is a Copy or View
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

print(arr.reshape(2, 4).base)


# Reshape Using an Unknown Dimension
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

newarr = arr.reshape(2, 2, -1)

print(newarr)


# Flatten a Multidimensional Array
import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6]])

newarr = arr.reshape(-1)

print(newarr)
