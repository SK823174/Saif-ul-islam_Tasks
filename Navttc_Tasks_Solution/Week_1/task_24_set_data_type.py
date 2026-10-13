# 1. Create a Set in Python

# Create a set of integer type
student_id = {112, 114, 116, 118, 115}
print('Student ID:', student_id)

# Create a set of string type
vowel_letters = {'a', 'e', 'i', 'o', 'u'}
print('Vowel Letters:', vowel_letters)

# Create a set of mixed data types
mixed_set = {'Hello', 101, -2, 'Bye'}
print('Set of mixed data types:', mixed_set)


# 2. Create an Empty Set in Python

# Create an empty set
empty_set = set()

# Create an empty dictionary
empty_dictionary = {}

# Check data type of empty_set
print('Data type of empty_set:', type(empty_set))

# Check data type of empty_dictionary
print('Data type of empty_dictionary:', type(empty_dictionary))


# 3. Duplicate Items in a Set

numbers = {2, 4, 6, 6, 2, 8}
print(numbers)  # Duplicate items are removed


# 4. Add Items to a Set in Python

numbers = {21, 34, 54, 12}

print('Initial Set:', numbers)

# Using add() method
numbers.add(32)

print('Updated Set:', numbers)


# 5. Update Python Set

companies = {'Lacoste', 'Ralph Lauren'}
tech_companies = ['apple', 'google', 'apple']

# Using update() method
companies.update(tech_companies)

print(companies)


# 6. Remove an Element from a Set

languages = {'Swift', 'Java', 'Python'}

print('Initial Set:', languages)

# Remove 'Java' from a set
removedValue = languages.discard('Java')

print('Set after remove():', languages)


# 7. Built-in Functions with Set

numbers = {10, 20, 30, 40, 50}

print(all(numbers))                # True
print(any(numbers))                # True
print(list(enumerate(numbers)))    # Index-value pairs
print(len(numbers))                # 5
print(max(numbers))                # 50
print(min(numbers))                # 10
print(sorted(numbers))             # Sorted list
print(sum(numbers))                # 150


# 8. Iterate Over a Set in Python

fruits = {"Apple", "Peach", "Mango"}

# For loop to access each fruit
for fruit in fruits:
    print(fruit)


# 9. Find Number of Set Elements

even_numbers = {2, 4, 6, 8}
print('Set:', even_numbers)

# Find number of elements
print('Total Elements:', len(even_numbers))


# 10. Union of Two Sets

# First set
A = {1, 3, 5}

# Second set
B = {0, 2, 4}

# Perform union operation using |
print('Union using |:', A | B)

# Perform union operation using union()
print('Union using union():', A.union(B))


# 11. Set Intersection

# First set
A = {1, 3, 5}

# Second set
B = {1, 2, 3}

# Perform intersection operation using &
print('Intersection using &:', A & B)

# Perform intersection operation using intersection()
print('Intersection using intersection():', A.intersection(B))


# 12. Difference between Two Sets

# First set
A = {2, 3, 5}

# Second set
B = {1, 2, 6}

# Perform difference operation using -
print('Difference using -:', A - B)

# Perform difference operation using difference()
print('Difference using difference():', A.difference(B))


# 13. Set Symmetric Difference

# First set
A = {2, 3, 5}

# Second set
B = {1, 2, 6}

# Perform symmetric difference operation using ^
print('Using ^:', A ^ B)

# Using symmetric_difference()
print('Using symmetric_difference():', A.symmetric_difference(B))


# 14. Check if Two Sets are Equal

# First set
A = {1, 3, 5}

# Second set
B = {3, 5, 1}

# Check whether sets are equal
if A == B:
    print('Set A and Set B are equal')
else:
    print('Set A and Set B are not equal')


# 15. Other Python Set Methods

# add() - Adds an element to the set
numbers = {1, 2, 3}
numbers.add(4)
print('After add():', numbers)

# clear() - Removes all elements from the set
numbers_copy = numbers.copy()
numbers_copy.clear()
print('After clear():', numbers_copy)

# copy() - Returns a copy of the set
copied_numbers = numbers.copy()
print('After copy():', copied_numbers)

# difference() - Returns the difference of two sets
A = {1, 2, 3}
B = {2, 3, 4}
print('difference():', A.difference(B))

# difference_update() - Removes elements found in another set
A = {1, 2, 3}
A.difference_update({2, 3})
print('After difference_update():', A)

# discard() - Removes an element if it exists
numbers = {1, 2, 3}
numbers.discard(2)
print('After discard():', numbers)

# intersection() - Returns common elements
A = {1, 2, 3}
B = {2, 3, 4}
print('intersection():', A.intersection(B))

# intersection_update() - Keeps only common elements
A = {1, 2, 3}
A.intersection_update({2, 3, 4})
print('After intersection_update():', A)

# isdisjoint() - Returns True if sets have no common elements
A = {1, 2}
B = {3, 4}
print('isdisjoint():', A.isdisjoint(B))

# issubset() - Checks whether a set is a subset of another
A = {1, 2}
B = {1, 2, 3}
print('issubset():', A.issubset(B))

# issuperset() - Checks whether a set contains another set
print('issuperset():', B.issuperset(A))

# pop() - Removes and returns an arbitrary set element
numbers = {1, 2, 3}
removed_item = numbers.pop()
print('Removed item using pop():', removed_item)
print('After pop():', numbers)

# remove() - Removes an element from the set
numbers = {1, 2, 3}
numbers.remove(2)
print('After remove():', numbers)

# symmetric_difference() - Returns non-common elements
A = {1, 2, 3}
B = {2, 3, 4}
print('symmetric_difference():', A.symmetric_difference(B))

# symmetric_difference_update() - Updates the set with non-common elements
A = {1, 2, 3}
A.symmetric_difference_update({2, 3, 4})
print('After symmetric_difference_update():', A)

# union() - Returns the union of sets
A = {1, 2}
B = {3, 4}
print('union():', A.union(B))

# update() - Updates a set with elements from another collection
A = {1, 2}
A.update([2, 3, 4])
print('After update():', A)

