
# 1. Iterating Through a List
a = ["Geeks", "for", "Geeks"]
for i in a:
    print(i)


# 2. Iterating Through a String
s = "Geeks"
for i in s:
    print(i)


# 3. Using range() with a Step Size
for i in range(0, 10, 2):
    print(i)


# 4. Using continue to Skip Characters
for i in 'geeksforgeeks':
    if i == 'e' or i == 's':
        continue
    print(i)


# 5. Using break to Stop a Loop
for i in 'geeksforgeeks':
    if i == 'e' or i == 's':
        break
print(i)


# 6. Using pass as a Placeholder
for i in 'geeksforgeeks':
    pass


# 7. Using else with a For Loop
for i in range(1, 4):
    print(i)
else:
    print("No Break\n")


# 8. Using enumerate() to Get Index and Value
b = ["eat", "sleep", "repeat"]
for i, j in enumerate(b):
    print(i, j)


# 9. Using Nested For Loops
for i in range(1, 4):
    for j in range(1, 4):
        print(i, j)
