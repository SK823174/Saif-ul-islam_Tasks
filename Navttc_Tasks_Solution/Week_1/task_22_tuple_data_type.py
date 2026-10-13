# 1. Creating a Tuple

# Empty tuple
my_tuple = ()

# Tuple having integers
my_tuple = (1, 2, 3)

# Tuple with mixed datatypes
my_tuple = (1, "Hello", 3.4)

# Nested tuple
my_tuple = ("mouse", [8, 4, 6], (1, 2, 3))

# Tuple can be created without parentheses (tuple packing)
my_tuple = 3, 4.6, "dog"

# Tuple unpacking
a, b, c = my_tuple

# Creating a tuple with one element
my_tuple = ("hello")
print(type(my_tuple))  # <class 'str'>

my_tuple = ("hello",)
print(type(my_tuple))  # <class 'tuple'>

my_tuple = "hello",
print(type(my_tuple))  # <class 'tuple'>


# 2. Accessing Elements in a Tuple: Indexing

my_tuple = ('p', 'e', 'r', 'm', 'i', 't')

print(my_tuple[0])  # 'p'
print(my_tuple[5])  # 't'



# Nested indexing
n_tuple = ("mouse", [8, 4, 6], (1, 2, 3))

print(n_tuple[0][3])  # 's'
print(n_tuple[1][1])  # 4
print(n_tuple[2][0])  # 1


# 3. Accessing Elements in a Tuple: Negative Indexing

my_tuple = ('p', 'e', 'r', 'm', 'i', 't')

print(my_tuple[-1])  # 't'
print(my_tuple[-6])  # 'p'


# 4. Accessing Elements in a Tuple: Slicing

my_tuple = ('p', 'r', 'o', 'g', 'r', 'a', 'm', 'i', 'z')

print(my_tuple[1:4])  # ('r', 'o', 'g')
print(my_tuple[:-7])  # ('p', 'r')
print(my_tuple[7:])   # ('i', 'z')
print(my_tuple[:])    # Entire tuple


# 5. Changing or Deleting a Tuple

my_tuple = (4, 2, 3, [6, 5])

# Tuple elements cannot be changed
# my_tuple[1] = 9  # TypeError: tuple does not support item assignment
# my_tuple[3] = 9  # TypeError: tuple does not support item assignment

# Items inside a mutable element, such as a list, can be changed
my_tuple[3][0] = 9
print(my_tuple)  # (4, 2, 3, [9, 5])

# Tuples can be reassigned
my_tuple = ('p', 'r', 'o', 'g', 'r', 'a', 'm', 'i', 'z')
print(my_tuple)


# 6. Tuple Concatenation and Repetition

print((1, 2, 3) + (4, 5, 6))  # (1, 2, 3, 4, 5, 6)
print(("Repeat",) * 3)        # ('Repeat', 'Repeat', 'Repeat')


# 7. Deleting a Tuple

my_tuple = ('p', 'r', 'o', 'g', 'r', 'a', 'm', 'i', 'z')

del my_tuple


# 8. Python Tuple Methods

my_tuple = ('a', 'p', 'p', 'l', 'e')

print(my_tuple.count('p'))  # 2
print(my_tuple.index('l'))  # 3


# 9. Tuple Membership Test

my_tuple = ('a', 'p', 'p', 'l', 'e')

print('a' in my_tuple)      # True
print('b' in my_tuple)      # False
print('g' not in my_tuple)  # True


# 10. Iterating Through a Tuple

for name in ('John', 'Kate'):
    print("Hello", name)


# 11. Built-in Functions with Tuple

numbers = (10, 20, 30, 40, 50)

print(all(numbers))               # True
print(any(numbers))               # True

print(list(enumerate(numbers)))   # Index-value pairs
print(len(numbers))               # 5
print(max(numbers))               # 50
print(min(numbers))               # 10
print(sorted(numbers))            # Sorted list
print(sum(numbers))               # 150
print(tuple([1, 2, 3]))            # Convert list to tuple



