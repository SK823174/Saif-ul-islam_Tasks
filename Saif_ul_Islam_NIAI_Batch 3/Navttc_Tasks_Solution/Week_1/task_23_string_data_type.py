# 1. Python Multiline Strings

# Multiline string
message = """To avoid pain, they avoid pleasure.
To avoid death, they avoid life."""

print(message)


# 2. Access String Characters

model = 'ChatGPT'

# Access the first character
print(model[0])  # Output: C

# Access the fifth character
print(model[4])  # Output: G


# 3. Negative Indexing

model = 'ChatGPT'

# Access the last character
print(model[-1])  # Output: T

# Access the fourth last character
print(model[-4])  # Output: t


# 4. String Index Out of Range

model = 'ChatGPT'

# This raises IndexError because index 8 is out of range
# print(model[8])


# 5. String Slicing

model = 'ChatGPT'

# Access characters from index 0 up to (but not including) 4
print(model[0:4])  # Output: Chat


# 6. Strings are Immutable

model = 'ChatGPT'

# Strings cannot be modified by assigning to an index
# model[0] = 'W'  # TypeError: 'str' object does not support item assignment

# Create a modified string by concatenation
model = 'Opus'
version = '5'

model = model + " " + version
print(model)  # Opus 5


# 7. Python String Methods

text = "ChatGPT is great."

# Replace "ChatGPT" with "Claude"
new_text = text.replace("ChatGPT", "Claude")

print(new_text)  # Output: Claude is great.


# 8. String Membership Test

print('Chat' in 'ChatGPT')        # True
print('Claude' not in 'ChatGPT')  # True


# 9. Iterate Through a String

model = 'Opus'

for c in model:
    print(c)


# 10. Python String Length

model = 'Opus'

# Count the number of characters
print(len(model))  # Output: 4


# 11. Escape Sequences

# Escape double quotes
example = "He said, \"What's there?\""

# Escape single quotes
example2 = 'He said, "What\'s there?"'

print(example)
print(example2)

# 12. String Formatting (f-Strings)

company = 'Google'
field = 'AI'

message = f'{company} is an {field} company.'
print(message)

