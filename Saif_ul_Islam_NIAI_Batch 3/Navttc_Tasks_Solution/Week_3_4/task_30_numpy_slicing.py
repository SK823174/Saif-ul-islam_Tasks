# Slice Elements from Index 1 to Index 5
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[1:5])


# Slice Elements from Index 4 to the End
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[4:])


# Slice Elements from the Beginning to Index 4
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[:4])


# Negative Slicing
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[-3:-1])


# Slicing with Step
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[1:5:2])


# Return Every Other Element
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[::2])


# Slicing 2-D Arrays: Second Row
import numpy as np

arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

print(arr[1, 1:4])


# Access Index 2 from Both Rows
import numpy as np

arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

print(arr[0:2, 2])


# Slice a 2-D Array
import numpy as np

arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

print(arr[0:2, 1:4])
