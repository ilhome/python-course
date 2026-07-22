def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def calculate(a, operator, b):
    if operator == "+":
        return add(a, b)
    if operator == "-":
        return subtract(a, b)
    if operator == "*":
        return multiply(a, b)
    if operator == "/":
        return divide(a, b)
    raise ValueError("Unsupported operator")


def main():
    print("Simple Calculator")
    print("Enter expressions like: 5 + 3")

    while True:
        expression = input("Enter calculation (or 'q' to quit): ").strip()

        if expression.lower() in {"q", "quit", "exit"}:
            print("Goodbye!")
            break

        parts = expression.split()
        if len(parts) != 3:
            print("Please use this format: number operator number")
            continue

        try:
            left = float(parts[0])
            operator = parts[1]
            right = float(parts[2])
            result = calculate(left, operator, right)
            print(f"Result: {result}")
        except ValueError as error:
            print(f"Error: {error}")


if __name__ == "__main__":
    main()
