# Access Array Elements
import numpy as np

arr = np.array([1, 2, 3, 4])

print(arr[0])


# Access the Second Element
import numpy as np

arr = np.array([1, 2, 3, 4])

print(arr[1])


# Add the Third and Fourth Elements
import numpy as np

arr = np.array([1, 2, 3, 4])

print(arr[2] + arr[3])


# Access 2-D Arrays: First Row, Second Column
import numpy as np

arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

print("2nd element on 1st row:", arr[0, 1])


# Access 2-D Arrays: Second Row, Fifth Column
import numpy as np

arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

print("5th element on 2nd row:", arr[1, 4])


# Access 3-D Arrays
import numpy as np

arr = np.array([
    [[1, 2, 3], [4, 5, 6]],
    [[7, 8, 9], [10, 11, 12]]
])

print(arr[0, 1, 2])


# Negative Indexing
import numpy as np

arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

print("Last element from 2nd dim:", arr[1, -1])
