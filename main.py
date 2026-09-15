from calculator import add, subtract, multiply, divide


def calculator():
    print("Welcome to the calculator! Type 'exit' to quit.")

    while True:
        user_input = input(
            "Enter an operation (add, subtract, multiply, divide) "
            "and two numbers, or 'exit' to quit: "
        )

        if user_input.lower() == "exit":
            print("Exiting calculator...")
            break

        try:
            operation, num1, num2 = user_input.split()
            num1, num2 = float(num1), float(num2)
        except ValueError:
            print("Invalid input. Please follow the format: <operation> <num1> <num2>")
            continue

        if operation == "add":
            result = add(num1, num2)
        elif operation == "subtract":
            result = subtract(num1, num2)
        elif operation == "multiply":
            result = multiply(num1, num2)
        elif operation == "divide":
            try:
                result = divide(num1, num2)
            except ValueError as e:
                print(e)
                continue
        else:
            print("Unknown operation. Use add, subtract, multiply, or divide.")
            continue

        print(f"Result: {result}")


if __name__ == "__main__":
    calculator()