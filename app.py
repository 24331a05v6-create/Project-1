import math

def get_real_number(prompt):
    while True:
        try:
            value = input(prompt).strip().lower()

            if value == "inf":
                return float("inf")
            elif value == "-inf":
                return float("-inf")
            elif value == "nan":
                return float("nan")

            return float(value)

        except ValueError:
            print("Invalid number. Try again.")

def safe_operation(name, func):
    try:
        result = func()
        return result
    except Exception as e:
        return f"Error: {e}"

def display_result(name, result):
    print(f"{name:<25}: {result}")

def main():
    print("=" * 70)
    print("UNIVERSAL REAL NUMBER CALCULATOR")
    print("Supports decimals, negatives, scientific notation, inf, -inf, nan")
    print("=" * 70)

    a = get_real_number("Enter first real number: ")
    b = get_real_number("Enter second real number: ")

    operations = {
        "Addition": lambda: a + b,
        "Subtraction": lambda: a - b,
        "Multiplication": lambda: a * b,
        "Division": lambda: a / b,
        "Modulo": lambda: a%b,
    }

    print("\nRESULTS")
    print("-" * 70)

    for name, operation in operations.items():
        result = safe_operation(name, operation)
        display_result(name, result)

if __name__ == "__main__":
    main()