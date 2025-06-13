## **VIII. Homework Assignment**

### **Task**

**Create a Python program with multiple functions that simulate a simple calculator.**

**Requirements:**

* Use separate functions for addition, subtraction, multiplication, and division.
* Include user input handling.
* Implement error handling (such as dividing by zero or invalid input).
* Use a main function to organize the workflow.
* Display results to the user.

---

### **Example Solution**

#### **Program Structure**

1. **add(a, b)** – returns sum
2. **subtract(a, b)** – returns difference
3. **multiply(a, b)** – returns product
4. **divide(a, b)** – returns quotient (handle division by zero)
5. **get\_numbers()** – gets two numbers from the user, handles invalid input
6. **main()** – controls the calculator loop and user interaction

#### **Example Code**

```python
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

if __name__ == "__main__":
    main()
```

---

### **Explanation**

* **Separation of Concerns:** Each operation is handled by its own function, making code organized and reusable.
* **Error Handling:**

  * `get_numbers()` checks for valid number input.
  * `divide()` handles division by zero.
* **User Interaction:** The user can repeatedly perform calculations or quit.
* **Scalability:** More operations or features (like exponentiation) can be added easily by defining new functions.

---

### **Good Practices Illustrated**

* Each function has a single responsibility.
* Functions use docstrings for documentation.
* Errors are handled gracefully.
* User input is validated.
* Code is modular and easy to read.