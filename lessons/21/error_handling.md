# Part 1

### **Assignment 1: Division Calculator**

**Task**: Write a program that takes two numbers from the user and prints their division. Handle division by zero.

```python
try:
    a = int(input("Enter numerator: "))
    b = int(input("Enter denominator: "))
    result = a / b
    print("Result:", result)
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
except ValueError:
    print("Error: Please enter valid integers.")
```

---

### **Assignment 2: File Reader**

**Task**: Ask the user for a filename and print its contents. Handle the case where the file doesn’t exist.

```python
try:
    filename = input("Enter filename: ")
    with open(filename, 'r') as f:
        print(f.read())
except FileNotFoundError:
    print("Error: File not found.")
```

---

### **Assignment 3: List Indexing**

**Task**: Create a list of 5 elements. Ask the user for an index and print the element. Handle index errors.

```python
data = [10, 20, 30, 40, 50]

try:
    idx = int(input("Enter an index (0-4): "))
    print("Element:", data[idx])
except IndexError:
    print("Error: Index out of range.")
except ValueError:
    print("Error: Please enter a valid number.")
```

---

### **Assignment 4: Calculator with Multiple Exception Handling**

**Task**: Build a calculator that takes two numbers and an operation (+, -, \*, /). Handle input and operation errors.

```python
try:
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    op = input("Enter operation (+, -, *, /): ")
    
    if op == '+':
        print(a + b)
    elif op == '-':
        print(a - b)
    elif op == '*':
        print(a * b)
    elif op == '/':
        print(a / b)
    else:
        raise ValueError("Invalid operation.")
except ZeroDivisionError:
    print("Error: Division by zero.")
except ValueError as e:
    print("Error:", e)
```

---

### **Assignment 5: Using `else` and `finally`**

**Task**: Perform a division with `try-except-else-finally` and explain the flow.

```python
try:
    x = int(input("Enter numerator: "))
    y = int(input("Enter denominator: "))
    result = x / y
except ZeroDivisionError:
    print("Cannot divide by zero.")
else:
    print("Result:", result)
finally:
    print("Execution complete.")
```

---

### **Assignment 6: Raising an Exception**

**Task**: Write a function that takes age as input. Raise a `ValueError` if age is negative.

```python
def check_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative.")
    print("Age is valid.")

try:
    age = int(input("Enter your age: "))
    check_age(age)
except ValueError as e:
    print("Error:", e)
```

---

### **Assignment 7: Custom Exception**

**Task**: Create a custom exception `PasswordTooShortError` and use it in a password checker.

```python
class PasswordTooShortError(Exception):
    pass

def check_password(pwd):
    if len(pwd) < 6:
        raise PasswordTooShortError("Password must be at least 6 characters long.")
    print("Password accepted.")

try:
    pwd = input("Enter password: ")
    check_password(pwd)
except PasswordTooShortError as e:
    print("Error:", e)
```

---

### **Assignment 8: Nested Try Blocks**

**Task**: Demonstrate use of nested `try` blocks.

```python
try:
    a = int(input("Enter number: "))
    try:
        b = int(input("Enter divisor: "))
        print("Result:", a / b)
    except ZeroDivisionError:
        print("Inner Error: Division by zero.")
except ValueError:
    print("Outer Error: Invalid input.")
```

---

### **Assignment 9: Exception Logging**

**Task**: Log exceptions to a file.

```python
import logging

logging.basicConfig(filename='errors.log', level=logging.ERROR)

try:
    x = int(input("Enter number: "))
    y = int(input("Enter divisor: "))
    print("Result:", x / y)
except Exception as e:
    logging.error("Exception occurred", exc_info=True)
    print("An error occurred. Check errors.log for details.")
```

---

### **Assignment 10: Retry on Error**

**Task**: Retry taking input until a valid integer is entered.

```python
while True:
    try:
        num = int(input("Enter an integer: "))
        print("You entered:", num)
        break
    except ValueError:
        print("Invalid input. Try again.")
```



# Part 2

## Assignment 1: Using the `math` Module

**Task**: Import the `math` module and perform the following:

* Calculate the square root of 64
* Find the value of π
* Calculate the sine of 90 degrees

```python
import math

print("Square root of 64:", math.sqrt(64))
print("Value of pi:", math.pi)
print("Sine of 90 degrees:", math.sin(math.radians(90)))
```

---

## Assignment 2: Working with `random` Module

**Task**: Use the `random` module to:

* Generate a random integer between 10 and 100
* Shuffle a list
* Pick a random element from a list

```python
import random

numbers = [1, 2, 3, 4, 5]

print("Random integer:", random.randint(10, 100))
random.shuffle(numbers)
print("Shuffled list:", numbers)
print("Random choice:", random.choice(numbers))
```

---

## Assignment 3: Using `datetime` Module

**Task**: Use the `datetime` module to:

* Get the current date and time
* Print only the current year
* Add 7 days to the current date

```python
import datetime

now = datetime.datetime.now()
print("Current date and time:", now)
print("Current year:", now.year)
future = now + datetime.timedelta(days=7)
print("Date after 7 days:", future)
```

---

## Assignment 4: Get Module Information with `dir()` and `help()`

**Task**: Use `dir()` and `help()` on the `math` module. Print the first 5 items returned by `dir()`.

```python
import math

print("First 5 attributes of math module:", dir(math)[:5])
# Uncomment the next line to explore help in an interactive session
# help(math)
```

---

##  Assignment 5: Use the `os` Module to List Files

**Task**: Use the `os` module to:

* Print the current working directory
* List all files in the current directory

```python
import os

print("Current working directory:", os.getcwd())
print("Files in directory:", os.listdir())
```

---

##  Assignment 6: Checking Module Versions

**Task**: Print the version of the `sys` module and check the version of Python being used.

```python
import sys

print("Python version:", sys.version)
print("Version info:", sys.version_info)
```

---

##  Assignment 7: Import Functions Directly from a Module

**Task**: Import only `sqrt` and `pi` from the `math` module and use them.

```python
from math import sqrt, pi

print("Square root of 49:", sqrt(49))
print("Value of pi:", pi)
```

---

##  Assignment 8: Creating a Custom Module

**Task**:

1. Create a file named `mymath.py` with a function `square(x)` that returns `x * x`.
2. Then import it in another script and use the function.

🔹 **mymath.py**

```python
def square(x):
    return x * x
```

🔹 **main.py**

```python
import mymath

print("Square of 8 is:", mymath.square(8))
```

---

##  Assignment 9: Module with Multiple Functions

**Task**:

1. Create a module named `geometry.py` with functions `area_circle(r)` and `perimeter_circle(r)`
2. Import and test both functions

🔹 **geometry.py**

```python
import math

def area_circle(r):
    return math.pi * r * r

def perimeter_circle(r):
    return 2 * math.pi * r
```

🔹 **main.py**

```python
import geometry

radius = 5
print("Area:", geometry.area_circle(radius))
print("Perimeter:", geometry.perimeter_circle(radius))
```

---

##  Assignment 10: `if __name__ == "__main__"` in a Module

**Task**: Create a module with some test code that only runs when the module is executed directly.

🔹 **testmodule.py**

```python
def greet(name):
    return f"Hello, {name}!"

if __name__ == "__main__":
    print(greet("Tester"))
```

🔹 **main.py**

```python
import testmodule

print(testmodule.greet("Alice"))
```

