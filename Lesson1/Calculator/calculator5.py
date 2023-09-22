
#Define some constants
SUBTRACT="subtract"
ADD="add"
MULTIPLY="multiply"
DIVIDE="divide"
SUMMATE="summate"
QUIT='quit'

#Functions
def summate(numbers):
    return_sum=0
    for i in numbers:
        return_sum+=i
    return return_sum

def print_menu():
    print("Options:")
    print(f"\tEnter '{ADD}' for addition")
    print(f"\tEnter '{SUBTRACT}' for subtraction")
    print(f"\tEnter '{MULTIPLY}' for multiplication")
    print(f"\tEnter '{DIVIDE}' for division")
    print(f"\tEnter '{SUMMATE}' for summation")
    print(f"\tEnter '{QUIT}' to end the program")
def input_two_floats():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    return (num1,num2) #This returns num1 and num2 together 

#Loop forever
while True:
    #Print the options
    print_menu()

    #Input a variable from the user
    user_input=input("Input: ")

    #If user wants to quit, break the loop, ending the program
    if user_input==QUIT:
        break
    elif user_input == ADD:
        num1,num2=input_two_floats()
        print("Result:", num1+num2)
    elif user_input == SUBTRACT:
        num1,num2=input_two_floats()
        print("Result:", num1-num2)
    elif user_input == MULTIPLY:
        num1,num2=input_two_floats()
        print("Result:", num1*num2)
    elif user_input == DIVIDE:
        # Step 5: Uncomment this section for division
        num1,num2=input_two_floats()
        print("Result:", num1/num2)
    #Anyway that we see to improve this???
    elif user_input==SUMMATE:
        #Initialize list
        numbers_to_sum=[]
        #Initialize input
        num=None
        #Keep inputting numbers 
        while num!=0:
            num=float(input("Enter a number or '0' to stop summing: "))
            numbers_to_sum.append(num)
        #Print our result
        print(summate(numbers_to_sum))
    else:
        print("Unknown input")

    input("Enter anything to continue...\n")