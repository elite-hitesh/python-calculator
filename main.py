#First project - 'Python Calculator'


def square(num1):
    return num1 ** 2


def square_root(num1):
    if num1 < 0:
        return "Error: Cannot calculate square root of a negative number."
    else:
        return num1 ** 0.5


print("\n--- Python Calculator ---\n")

past_result = False

while True:
    try:
        num1 = float(input("Enter first number: "))
        break
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        continue
    
while True:

    operation = input("Enter operator (+, -, *, /, **, %, sq, sqrt, q): ").lower()
    
    if operation == "q":
        print("Calculator closed.")
        break
    elif operation not in ["+", "-", "*", "/", "**", "%", "sq", "sqrt"]:
        print("Invalid operator. Please enter a valid operator (+, -, *, /, **, %, q): ")
        continue

    if operation == "sq":
        result = square(num1)
        print("________________________________")
        print(f"Result: {result}\n")
        break
    elif operation == "sqrt":
        result = square_root(num1)
        print("________________________________")
        print(f"Result: {result}\n")
        break
    else:
        break
    
    while True:
        try:
            num2 = float(input("Enter second number: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue

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

    if result is None:
        if past_result:
            continue
        
        while True:
            try:
                num1 = float(input("\nEnter first number: "))
                break
            except ValueError:
                print("Invalid input. Please enter a valid number.")
                continue
        continue

    print("________________________________")
    print(f"Result: {result}\n")

    continue_operation = input("Do you want to continue, restart or quit this operation? (c/ r/ q): ").lower()

    while continue_operation not in ['c', 'r', 'q']:
        print("Invalid input. Please enter: \n'c' to continue, \n'r' to restart, or \n'q' to quit.")
        continue_operation = input("Do you want to continue, restart or quit this operation? (c/ r/ q): ").lower()

    if continue_operation == 'c':
        num1 = result
        past_result = True

    elif continue_operation == 'r':
        past_result = False

        while True:
            try:
                num1 = float(input("\nEnter first number: "))
                break
            except ValueError:
                print("Invalid input. Please enter a valid number.")
                continue
    elif continue_operation == 'q':
        print(f"\nFinal Result: {result}\n")
        break