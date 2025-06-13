def add(a, b):
    """Return the sum of a and b."""
    return a + b

def subtract(a, b):
    """Return the difference of a and b."""
    return a - b

def multiply(a, b):
    """Return the product of a and b."""
    return a * b

def divide(a, b):
    """Return the division of a by b. Handles division by zero."""
    try:
        return a / b
    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")
        return None

def get_numbers():
    """Get two numbers from the user, handling invalid input."""
    while True:
        try:
            a = float(input("Enter the first number: "))
            b = float(input("Enter the second number: "))
            return a, b
        except ValueError:
            print("Invalid input. Please enter valid numbers.")

def main():
    print("Simple Calculator")
    print("Select operation: +, -, *, /")
    operations = {'+': add, '-': subtract, '*': multiply, '/': divide}

    while True:
        op = input("Enter operation (+, -, *, /) or 'q' to quit: ")
        if op == 'q':
            print("Goodbye!")
            break
        if op not in operations:
            print("Invalid operation. Try again.")
            continue

        a, b = get_numbers()
        result = operations[op](a, b)
        if result is not None:
            print(f"Result: {result}")


''' for now, ignore the following line
if __name__ == "__main__":
    main()
'''
main()