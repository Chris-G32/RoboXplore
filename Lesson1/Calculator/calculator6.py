# Define some constants
SUBTRACT = "subtract"
ADD = "add"
MULTIPLY = "multiply"
DIVIDE = "divide"
SUMMATE = "summate"
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
        print(f"\tEnter '{QUIT}' to end the program")

    def input_two_floats(self):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        return num1, num2  # This returns num1 and num2 together
    
    @staticmethod
    def summate(numbers):
        return_sum=0
        for i in numbers:
            return_sum+=i
        return return_sum
    
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
                print("Sum:", Calculator.summate(numbers_to_sum))
            else:
                print("Unknown input")

            input("Enter anything to continue...\n")

if __name__ == "__main__":
    calculator = Calculator()
    calculator.run()
    print("Calculator finished...")
