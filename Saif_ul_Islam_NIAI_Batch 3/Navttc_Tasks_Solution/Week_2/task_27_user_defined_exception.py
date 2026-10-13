# Defining a Custom Exception
class CustomError(Exception):
    pass


try:
    raise CustomError
except CustomError:
    print("Custom error occurred.")


# Example: User-Defined Exception
class InvalidAgeException(Exception):
    pass


number = 18

try:
    input_num = int(input("Enter a number: "))
    if input_num < number:
        raise InvalidAgeException
    else:
        print("Eligible to Vote")

except InvalidAgeException:
    print("Exception occurred: Invalid Age")


# Customizing Exception Classes
class SalaryNotInRangeError(Exception):
    def __init__(self, salary, message="Salary is not in (5000, 15000) range"):
        self.salary = salary
        self.message = message
        super().__init__(self.message)


salary = int(input("Enter salary amount: "))

if not 5000 < salary < 15000:
    raise SalaryNotInRangeError(salary)
