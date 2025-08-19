# TODO: build a simple CLI calculator that supports + - * /

    # TODO: add a function to add two numbers
def add(a, b):
        return a + b

    # TODO: add a function to subtract two numbers
def subtract(a, b):
        return a - b

    # TODO: add a function to multiply two numbers
def multiply(a, b):
        return a * b

    # TODO: add a function to divide two numbers
def divide(a, b):
        return a / b

    # TODO: add main function to run the calculator in CLI
def main():
        print("Welcome to the calculator!")
        print("Enter two numbers and an operator to perform the operation")
        a = float(input("Enter the first number: "))
        b = float(input("Enter the second number: "))
        operator = input("Enter the operator: ")
        if operator == "+":
            print(add(a, b))
        elif operator == "-":
            print(subtract(a, b))
        elif operator == "*":
            print(multiply(a, b))
        elif operator == "/":
            print(divide(a, b))
        else:
            print("Invalid operator")

if __name__ == "__main__":
        main()