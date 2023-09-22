#Pip install numpy if you dont have it
import numpy as np

# Define some constants
SUBTRACT = "subtract"
ADD = "add"
MULTIPLY = "multiply"
DIVIDE = "divide"
SUMMATE = "summate"
SQUARE_ROOT = "sqrt"
SQUARE = "square"
SINE = "sine"
COSINE = "cosine"
TANGENT = "tangent"
QUIT = 'quit'

class Calculator:
    def __init__(self):
        pass

    def print_menu(self):
        print("Options:")
        print(f"\tEnter '{ADD}' for addition")
        print(f"\tEnter '{SUBTRACT}' for subtraction")
        print(f"\tEnter '{MULTIPLY}' for multiplication")
        print(f"\tEnter '{DIVIDE}' for division")
        print(f"\tEnter '{SUMMATE}' for summation")
        print(f"\tEnter '{SQUARE_ROOT}' for square root")
        print(f"\tEnter '{SQUARE}' for squaring")
        print(f"\tEnter '{SINE}' for sine")
        print(f"\tEnter '{COSINE}' for cosine")
        print(f"\tEnter '{TANGENT}' for tangent")
        print(f"\tEnter '{QUIT}' to end the program")

    def input_two_floats(self):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        return num1, num2  # This returns num1 and num2 together

    def run(self):
        while True:
            # Print the options
            self.print_menu()

            # Input a variable from the user
            user_input = input("Input: ")

            # If user wants to quit, break the loop, ending the program
            if user_input == QUIT:
                break
            elif user_input == ADD:
                num1, num2 = self.input_two_floats()
                print("Result:", num1 + num2)
            elif user_input == SUBTRACT:
                num1, num2 = self.input_two_floats()
                print("Result:", num1 - num2)
            elif user_input == MULTIPLY:
                num1, num2 = self.input_two_floats()
                print("Result:", num1 * num2)
            elif user_input == DIVIDE:
                num1, num2 = self.input_two_floats()
                if num2 != 0:
                    print("Result:", num1 / num2)
                else:
                    print("Division by zero is not allowed.")
            elif user_input == SUMMATE:
                # Initialize list
                numbers_to_sum = []
                # Initialize input
                num = None
                # Keep inputting numbers
                while num != 0:
                    num = float(input("Enter a number or '0' to stop summing: "))
                    numbers_to_sum.append(num)
                # Print our result
                print("Sum:", sum(numbers_to_sum))
            elif user_input == SQUARE_ROOT:
                num = float(input("Enter a number: "))
                print("Square Root:", np.sqrt(num))
            elif user_input == SQUARE:
                num = float(input("Enter a number: "))
                print("Squared:", np.square(num))
            elif user_input == SINE:
                num = float(input("Enter an angle in degrees: "))
                print("Sine:", np.sin(np.radians(num)))
            elif user_input == COSINE:
                num = float(input("Enter an angle in degrees: "))
                print("Cosine:", np.cos(np.radians(num)))
            elif user_input == TANGENT:
                num = float(input("Enter an angle in degrees: "))
                print("Tangent:", np.tan(np.radians(num)))
            else:
                print("Unknown input")

            input("Enter anything to continue...\n")
