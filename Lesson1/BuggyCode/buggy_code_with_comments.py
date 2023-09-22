# Syntax Error: Missing closing parenthesis for the print function.
print("Hello, world"

# Syntax Error: Missing colon at the end of the if statement.
if True
    print("This will never be printed")

# Runtime Error: Trying to divide by zero, which results in a ZeroDivisionError.
result = 10 / 0

# Syntax Error: Invalid character "@" in the variable name.
@variable_name = 42

# Logical Error: The loop should print numbers from 1 to 5, but it prints 0 to 4.
for i in range(5):
    print(i)

# Runtime Error: Attempting to access an index that is out of range.
my_list = [1, 2, 3]
print(my_list[5])

# Logical Error: The function should return the sum of two numbers, but it returns their product.
def add_numbers(a, b):
    return a * b

# Runtime Error: Using an undefined variable.
print(undefined_variable)

# Logical Error: The condition in the if statement is always True, so "Good morning!" will always be printed.
time = "night"
if time == "night":
    print("Good morning!")

# Syntax Error: Invalid indentation; inconsistent use of spaces and tabs.
def inconsistent_indentation():
    print("This function has inconsistent indentation.")
      print("This line has more spaces than the previous one.")

# Runtime Error: Calling a function with too few arguments.
def divide(a, b):
    return a / b

result = divide(10)

# Logical Error: The function should check if a number is even, but it checks if it's odd.
def is_even(number):
    if number % 2 != 0:
        return True
    else:
        return False

# Runtime Error: Using an incorrect escape sequence in a string.
print("This is a string with an invalid escape sequence: \g")

# Logical Error: The function should find the maximum of two numbers, but it returns the minimum.
def find_maximum(a, b):
    if a < b:
        return a
    else:
        return b
