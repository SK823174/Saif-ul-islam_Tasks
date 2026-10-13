# 1. Using continue to Skip a Number
for i in range(1, 11):
    if i == 6:
        continue
    print(i, end=" ")


# 2. Skipping Specific Characters in a String
for char in "GeeksforGeeks":
    if char == "e":
        continue
    print(char, end=" ")


# 3. Using continue in Nested Loops
a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for row in a:
    for num in row:
        if num == 3:
            continue
        print(num, end=" ")


# 4. Using continue with a while Loop
i = 0

while i < 10:
    if i == 5:
        i += 1  # Ensure the loop variable is incremented to avoid an infinite loop
        continue
    print(i)
    i += 1
