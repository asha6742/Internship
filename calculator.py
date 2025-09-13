def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Division by zero error."
    return x / y

def calculator():
    print("Command-Line Calculator")
    print("Operations available: +  -  *  /")
    print("Type 'q' to quit.")

    while True:
        try:
            num1 = float(input("\nEnter first number: "))
            output= input("Enter operator (+, -, *, / or q to quit): ")

            if output.lower() == 'q':
                print("Exiting calculator")
                break

            num2 = float(input("Enter second number: "))

            if output == '+':
                print("Result:", add(num1, num2))
            elif output == '-':
                print("Result:", subtract(num1, num2))
            elif output == '*':
                print("Result:", multiply(num1, num2))
            elif output == '/':
                print("Result:", divide(num1, num2))
            else:
                print("Invalid operator. Try again.")
        except ValueError:
            print("Invalid input! Please enter numbers only.")

if __name__ == "__main__":
    calculator()
