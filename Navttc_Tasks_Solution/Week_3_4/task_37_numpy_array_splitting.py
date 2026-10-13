import numpy as np

# Split a 1-D Array Into 3 Parts
arr = np.array([1, 2, 3, 4, 5, 6])
newarr = np.array_split(arr, 3)
print(newarr)

# Split a 1-D Array Into 4 Parts
arr = np.array([1, 2, 3, 4, 5, 6])
newarr = np.array_split(arr, 4)
print(newarr)

# Access the Split Arrays
arr = np.array([1, 2, 3, 4, 5, 6])
newarr = np.array_split(arr, 3)
print(newarr[0])
print(newarr[1])
print(newarr[2])

# Split a 2-D Array Into 3 Parts
arr = np.array([
    [1, 2],
    [3, 4],
    [5, 6],
    [7, 8],
    [9, 10],
    [11, 12]
])
newarr = np.array_split(arr, 3)
print(newarr)

# Split a 2-D Array With 3 Columns Into 3 Parts
arr = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [10, 11, 12],
    [13, 14, 15],
    [16, 17, 18]
])
newarr = np.array_split(arr, 3)
print(newarr)

# Split a 2-D Array Along Columns (axis=1)
arr = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [10, 11, 12],
    [13, 14, 15],
    [16, 17, 18]
])
newarr = np.array_split(arr, 3, axis=1)
print(newarr)

# Split a 2-D Array Along Columns Using hsplit()
arr = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [10, 11, 12],
    [13, 14, 15],
    [16, 17, 18]
])
newarr = np.hsplit(arr, 3)
print(newarr)
