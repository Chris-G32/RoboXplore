#Define some constants
SUBTRACT="subtract"
ADD="add"
MULTIPLY="multiply"
DIVIDE="divide"
QUIT='quit'

#Loop forever
while True:
    #Print the options
    #The f before the "" allows us to put a variable in the string, so what do we think these will print?
    print("Options:")
    print(f"Enter '{ADD}' for addition")
    print(f"Enter '{SUBTRACT}' for subtraction")
    print(f"Enter '{MULTIPLY}' for multiplication")
    print(f"Enter '{DIVIDE}' for division")
    print(f"Enter '{QUIT}' to end the program")

    #Input a variable from the user
    user_input=input()

    #If user wants to quit, break the loop, ending the program
    if user_input==QUIT:
        break
    elif user_input == ADD:
        num1 = float(input("Enter first number: "))
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
    else:
        print("Unknown input")
        
    input("Enter anything to continue...\n")