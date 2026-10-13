import numpy as np

# Find Indexes Where the Value Is 4
arr = np.array([1, 2, 3, 4, 5, 4, 4])
x = np.where(arr == 4)
print(x)

# Find Indexes Where the Values Are Odd
arr = np.array([10, 14, 93, 41, 8, 7])
x = np.where(arr % 2 == 1)
print(x)

# Find Indexes Where the Values Are Even
arr = np.array([10, 14, 93, 41, 8, 7])
x = np.where(arr % 2 == 0)
print(x)

# Search Sorted: Find Where 7 Should Be Inserted
arr = np.array([6, 7, 8, 9])
x = np.searchsorted(arr, 7)
print(x)

# Search From the Right Side
arr = np.array([6, 7, 8, 9])
x = np.searchsorted(arr, 7, side="right")
print(x)

# Search for Multiple Values
arr = np.array([1, 3, 5, 7])
x = np.searchsorted(arr, [2, 4, 6])
print(x)