# Check the Data Type of an Integer Array
import numpy as np

arr = np.array([1, 2, 3, 4])

print(arr.dtype)


# Check the Data Type of a String Array
import numpy as np

arr = np.array(["apple", "banana", "cherry"])

print(arr.dtype)


# Create an Array with String Data Type
import numpy as np

arr = np.array([1, 2, 3, 4], dtype="S")

print(arr)
print(arr.dtype)


# Create an Array with 4-Byte Integer Data Type
import numpy as np

arr = np.array([1, 2, 3, 4], dtype="i4")

print(arr)
print(arr.dtype)


# Invalid Data Type Conversion
import numpy as np

try:
    arr = np.array(["a", "2", "3"], dtype="i")
    print(arr)
except ValueError as error:
    print(error)


# Convert Float to Integer Using astype("i")
import numpy as np

arr = np.array([1.1, 2.1, 3.1])

newarr = arr.astype("i")

print(newarr)
print(newarr.dtype)


# Convert Float to Integer Using int
import numpy as np

arr = np.array([1.1, 2.1, 3.1])

newarr = arr.astype(int)

print(newarr)
print(newarr.dtype)


# Convert Integer to Boolean
import numpy as np

arr = np.array([1, 0, 3])

newarr = arr.astype(bool)

print(newarr)
print(newarr.dtype)
