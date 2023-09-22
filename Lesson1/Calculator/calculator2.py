#Define some constants to print
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

#Say what was chosen
print("You chose",user_input)