#Define some constants
SUBTRACT="subtract"
ADD="add"
MULTIPLY="multiply"
DIVIDE="divide"


#Print the options
#The f before the "" allows us to put a variable in the string, so what do we think these will print?
print("Options:")
print(f"Enter '{ADD}' for addition")
print(f"Enter '{SUBTRACT}' for subtraction")
print(f"Enter '{MULTIPLY}' for multiplication")
print(f"Enter '{DIVIDE}' for division")

#Input a variable from the user
user_input=input()

#If user input equals add, add and so forth
if user_input == ADD:
    num1 = float(input("Enter first number: "))#float() makes the input into a float, instead of a string
    num2 = float(input("Enter second number: "))
    print("Result:", num1+num2)
elif user_input == SUBTRACT:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    print("Result:", num1-num2)
elif user_input == MULTIPLY:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    print("Result:", num1*num2)
elif user_input == DIVIDE:
    # Step 5: Uncomment this section for division
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    print("Result:", num1/num2)
#This means the user didn't enter any of the options 
else:
    print("Unknown input")