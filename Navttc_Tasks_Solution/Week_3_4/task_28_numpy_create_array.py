# Create a NumPy ndarray Object
import numpy as np

arr = np.array([1, 2, 3, 4, 5])

print(arr)
print(type(arr))


# Create a NumPy Array Using a Tuple
import numpy as np

arr = np.array((1, 2, 3, 4, 5))

print(arr)


# 0-D Array
import numpy as np

arr = np.array(42)

print(arr)


# 1-D Array
import numpy as np

arr = np.array([1, 2, 3, 4, 5])

print(arr)


# 2-D Array
import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6]])

print(arr)


# 3-D Array
import numpy as np

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(arr)


# Check Number of Dimensions
import numpy as np

a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)


# Higher Dimensional Array
import numpy as np

arr = np.array([1, 2, 3, 4], ndmin=5)

print(arr)
print("number of dimensions :", arr.ndim)
