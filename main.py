#First project - 'Python Calculator'
print("\n--- Python Calculator ---\n")
num1 = float(input("Enter first number: "))

while True:
    operation = input("Enter operator (+, -, *, /, **, %, q): ").lower()
    
    if operation == "q":
        print("Calculator closed.")
        break
    elif operation not in ["+", "-", "*", "/", "**", "%"]:
        print("Invalid operator. Please enter a valid operator (+, -, *, /, **, %, q).")
        continue

    num2 = float(input("Enter second number: "))

    result = None

    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        if num2 != 0:
            result = num1 / num2
        else:
            print("Error: Division by zero is not allowed.")
    elif operation == "**":
        result = num1 ** num2
    elif operation == "%":
        if num2 != 0:
            result = num1 % num2
        else:
            print("Error: Division by zero is not allowed.")
    print("________________________________")
    print(f"Result: {result}\n")

    continue_operation = input("Do you want to continue, restart or quit this operation? (c/ r/ q): ").lower()

    if continue_operation == 'c':
        num1 = result
    elif continue_operation == 'r':
        num1 = float(input("Enter first number: "))
    elif continue_operation == 'q':
        print(f"\nFinal Result: {result}\n")
        break