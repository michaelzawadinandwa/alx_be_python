def perform_operation(num1, num2, operation):
    if operation == "+" or operation == "add":
        return num1 + num2

    elif operation == "-" or operation == "subtract":
        return num1 - num2

    elif operation == "*" or operation == "multiply":
        return num1 * num2

    elif operation == "/" or operation == "divide":
        if num2 == 0:
            return "Error: Division by zero"
        return num1 / num2

    else:
        return "Error: Invalid operation"

if __name__ == "__main__":
    number1 = float(input("Enter first number: "))
    number2 = float(input("Enter second number: "))
    operation = input("Enter any one of the operations (+, -, *, /): ").strip().lower()

    result = perform_operation(number1, number2, operation)
    print(f"Result: {result}")
