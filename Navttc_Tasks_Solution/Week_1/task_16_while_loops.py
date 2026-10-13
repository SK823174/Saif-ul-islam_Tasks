# 1. Basic While Loop
count = 0
while count < 3:
    count = count + 1
    print("Hello Geek")


# 2. Infinite While Loop
age = 28
while age > 19:
    print('Infinite Loop')


# 3. Using Continue Statement in While Loop
i = 0
a = 'geeksforgeeks'

while i < len(a):
    if a[i] == 'e' or a[i] == 's':
        i += 1
        continue
    print(a[i])
    i += 1


# 4. Using Break Statement in While Loop
i = 0
a = 'geeksforgeeks'

while i < len(a):
    if a[i] == 'e' or a[i] == 's':
        i += 1
        break
    print(a[i])
    i += 1


# 5. Using Pass Statement in While Loop
a = 'geeksforgeeks'
i = 0
while i < len(a):
    i += 1
    pass

print('Value of i :', i)


# 6. Using Else with While Loop
i = 0
while i < 4:
    i += 1
    print(i)
else:
    print("No Break\n")


# 7. Using Break with While Loop and Else
i = 0
while i < 4:
    i += 1
    print(i)
    break
else:
    print("No Break")


# 8. Print Numbers in Decreasing Order
def printInDecreasing(x):
    while x >= 0:
        print(x, end=" ")
        x -= 1

printInDecreasing(3)

