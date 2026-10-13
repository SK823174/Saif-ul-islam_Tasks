# 1. Defining a Function
def fun():
    print("Welcome to GFG")


# 2. Calling a Function
def fun():
    print("Welcome to GFG")

fun()


# 3. Function Arguments: Checking Even or Odd
def evenOdd(x):
    if (x % 2 == 0):
        return "Even"
    else:
        return "Odd"

print(evenOdd(16))
print(evenOdd(7))


# 4. Default Arguments
def myFun(x, y=50):
    print("x: ", x)
    print("y: ", y)

myFun(10)


# 5. Keyword Arguments
def student(fname, lname):
    print(fname, lname)

student(fname='Geeks', lname='Practice')
student(lname='Practice', fname='Geeks')


# 6. Positional Arguments
def nameAge(name, age):
    print("Hi, I am", name)
    print("My age is ", age)

print("Case-1:")
nameAge("Olivia", 27)

print("Case-2:")
nameAge(27, "Olivia")


# 7. Arbitrary Arguments (*args and **kwargs)
def myFun(*args, **kwargs):
    print("Non-Keyword Arguments (*args):")
    for arg in args:
        print(arg)

    print("Keyword Arguments (**kwargs):")
    for key, value in kwargs.items():
        print(f"{key} == {value}")

myFun('Hey', 'Welcome', first='Geeks', mid='for', last='Geeks')


# 8. Function Within a Function
def f1():
    s = 'I love GeeksforGeeks'

    def f2():
        print(s)

    f2()

f1()


# 9. Return Statement
def sq_value(num):
    return num**2

print(sq_value(2))
print(sq_value(-4))


# 10. Pass by Reference and Pass by Value
def myFun(x):
    x[0] = 20

b = [10, 11, 12, 13]
myFun(b)
print(b)


def myFun2(x):
    x = 20

a = 10
myFun2(a)
print(a)
