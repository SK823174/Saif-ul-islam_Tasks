import pandas as pd

# Create a Simple Pandas Series from a List
a = [1, 7, 2]
myvar = pd.Series(a)
print(myvar)

# Access the First Value Using Its Index
print(myvar[0])

# Create a Series with Custom Labels
a = [1, 7, 2]
myvar = pd.Series(a, index=["x", "y", "z"])
print(myvar)

# Access a Value Using Its Label
print(myvar["y"])

# Create a Pandas Series from a Dictionary
calories = {
    "day1": 420,
    "day2": 380,
    "day3": 390
}
myvar = pd.Series(calories)
print(myvar)

# Create a Series Using Only Selected Dictionary Items
calories = {
    "day1": 420,
    "day2": 380,
    "day3": 390
}
myvar = pd.Series(calories, index=["day1", "day2"])
print(myvar)

# Create a DataFrame from Two Series-Like Lists
data = {
    "calories": [420, 380, 390],
    "duration": [50, 40, 45]
}
myvar = pd.DataFrame(data)
print(myvar)
