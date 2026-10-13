# Import Pandas
import pandas

# Create a Dataset
mydataset = {
    "cars": ["BMW", "Volvo", "Ford"],
    "passings": [3, 7, 2]
}

# Create a DataFrame Using Pandas
myvar = pandas.DataFrame(mydataset)
print(myvar)

# Import Pandas Using the pd Alias
import pandas as pd

# Create a DataFrame Using the pd Alias
mydataset = {
    "cars": ["BMW", "Volvo", "Ford"],
    "passings": [3, 7, 2]
}

myvar = pd.DataFrame(mydataset)
print(myvar)

# Check the Pandas Version
print(pd.__version__)
