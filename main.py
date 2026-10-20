#First project - 'Python Calculator'
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

    operation = input("Enter operator (+, -, *, /, **, %, q): ").lower()
    
    if operation == "q":
        print("Calculator closed.")
        break
    elif operation not in ["+", "-", "*", "/", "**", "%"]:
        print("Invalid operator. Please enter a valid operator (+, -, *, /, **, %, q): ")
        continue
    
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
            recalculation = True
    elif operation == "**":
        result = num1 ** num2
    elif operation == "%":
        if num2 != 0:
            result = num1 % num2
        else:
            print("Error: Division by zero is not allowed.")
            recalculation = True

    if result is None:
        if past_result:
            continue
        
        while True:
            try:
                num1 = float(input("Enter first number: "))
                break
            except ValueError:
                print("Invalid input. Please enter a valid number.")
                continue
        continue

    print("________________________________")
    print(f"Result: {result}\n")

    continue_operation = input("Do you want to continue, restart or quit this operation? (c/ r/ q): ").lower()

    if continue_operation == 'c':
        num1 = result
        past_result = True

    elif continue_operation == 'r':
        past_result = False
        
        while True:
            try:
                num1 = float(input("Enter first number: "))
                break
            except ValueError:
                print("Invalid input. Please enter a valid number.")
                continue
    elif continue_operation == 'q':
        print(f"\nFinal Result: {result}\n")
        break