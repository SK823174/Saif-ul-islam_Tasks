# 1. Creating a List
cart = ["T-shirt", "Lamp", "Pen"]
print(cart)

# Creating a List with Mixed Data Types
my_list = [1, "Python", 3.14]
print(my_list)

# Creating an Empty List
my_list = []
print(my_list)


# 2. Converting a String into a List
vowels = "aeiou"
vowels_list = list(vowels)
print(vowels_list)


# 3. Accessing List Items Using Positive Indexing
languages = ["Python", "Swift", "C++"]
print(f"languages[0] = {languages[0]}")
print(f"languages[2] = {languages[2]}")


# 4. Accessing List Items Using Negative Indexing
languages = ["Python", "Swift", "C++"]
print('languages[-1] =', languages[-1])
print('languages[-3] =', languages[-3])


# 5. Updating List Items
cart = ["T-shirt", "Lamp", "Pen"]
cart[1] = "Shoes"
print(cart)


# 6. Adding an Item Using append()
cart = ["T-shirt", "Lamp", "Pen"]
cart.append("Book")
print(cart)


# 7. Adding Multiple Items Using extend()
cart = ["T-shirt", "Lamp", "Pen"]
fav_items = ["Headphones", "Phone"]
cart.extend(fav_items)
print(cart)


# 8. Inserting an Item at a Specific Position
cart = ["T-shirt", "Lamp", "Pen"]
cart.insert(2, "Book")
print(cart)


# 9. Removing Items Using remove(), pop() and clear()
cart = ["T-shirt", "Lamp", "Pen", "Book"]

cart.remove("Pen")

last_item = cart.pop()
print(cart)
print(last_item)

cart.clear()
print(cart)


# 10. Deleting List Items Using del
cart = ['T-shirt', 'Lamp', 'Pen', 'Book']
del cart[2]
print(cart)

del cart
# print(cart)


# 11. Copying a List Using Assignment
favorite_items = ["T-shirt", "Lamp", "Pen"]
cart = favorite_items

favorite_items.append("Book")

print(f"favorite_items = {favorite_items}")
print(f"cart = {cart}")


# 12. Copying a List Using copy()
favorite_items = ["T-shirt", "Lamp", "Pen"]
cart = favorite_items.copy()

favorite_items.append("Book")

print(f"favorite_items = {favorite_items}")
print(f"cart = {cart}")


# 13. Finding the Length of a List Using len()
favorite_items = ["T-shirt", "Lamp", "Pen"]
size = len(favorite_items)
print(size)


# 14. Checking List Membership Using in
cart = ["T-shirt", "Lamp", "Pen"]

result = "Lamp" in cart
print(result)

result = "Book" in cart
print(result)


# 15. Iterating Through a List
cart_items = ["T-shirt", "Lamp", "Pen"]

for item in cart_items:
    print(item)
