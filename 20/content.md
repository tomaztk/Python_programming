
## **LESSON 20: ERROR HANDLING AND MODULES**


* Handling exceptions in Python using `try`, `except`, `finally`
* Importing and using Python modules (`math`, `random`, etc.)
* Working with variables and objects
* Hands-on exercises

---

### **1. Handling Exceptions in Python**

####  Example: Division with Exception Handling

```python
try:
    num = int(input("Enter a number: "))
    result = 10 / num
    print("Result:", result)
except ValueError:
    print("Invalid input. Please enter an integer.")
except ZeroDivisionError:
    print("Cannot divide by zero.")
finally:
    print("Operation complete.")
```

####  Explanation:

* `try`: runs code that may raise an error.
* `except ValueError`: handles non-integer inputs.
* `except ZeroDivisionError`: handles divide-by-zero errors.
* `finally`: always runs, whether there’s an error or not.

####  Practical Use Case:

User input validation in a calculator or online form to prevent crashes and give helpful feedback.

---

###  **2. Importing and Using Modules**

####  Example: Using `math` and `random` Modules

```python
import math
import random

num = random.randint(1, 100)
square_root = math.sqrt(num)

print(f"The square root of {num} is {square_root:.2f}")
```

####  Explanation:

* `random.randint(1, 100)`: picks a random number between 1 and 100.
* `math.sqrt(num)`: calculates the square root of the number.

#### 💡 Practical Use Case:

Games, simulations, statistical tools, or quiz apps that need randomness and math operations.

---

###  **3. Working with Variables and Objects**

####  Example: Object-Oriented Error Handling

```python
class Calculator:
    def __init__(self, value):
        self.value = value

    def inverse(self):
        try:
            return 1 / self.value
        except ZeroDivisionError:
            return "Cannot take inverse of zero."

calc = Calculator(0)
print(calc.inverse())
```

####  Explanation:

* Shows working with object properties (`self.value`).
* `Calculator` is a custom object with methods that include error handling.

####  Practical Use Case:

Encapsulate logic in classes (e.g., scientific calculator, finance apps) with robust error handling.

---

###  **Hands-On Practice Exercise**

```python
# Ask the user for a number and compute its square root
import math

try:
    user_input = input("Enter a number to find the square root: ")
    number = float(user_input)
    if number < 0:
        raise ValueError("Cannot compute square root of a negative number.")
    result = math.sqrt(number)
    print(f"Square root of {number} is {result:.2f}")
except ValueError as ve:
    print("Error:", ve)
finally:
    print("Thank you for using the calculator.")
```

####  Explanation:

* Demonstrates full use of exception handling and module import.
* Validates user input and handles math domain errors.


