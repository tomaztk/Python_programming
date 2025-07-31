## **Lesson 21: Error Handling and Modules – Exercises**

## **Solutions**

---

**Solution 1**

```python
try:
    num = float(input("Enter a number: "))
    print("Square:", num ** 2)
except ValueError:
    print("Invalid input! Please enter a number.")
    
    
 try:
    #check_age(25)  
    check_age(-5)  
except ValueError as e:
    print("Error:", e)
```

**Solution 2**

```python
try:
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    print("Result:", a / b)
except ValueError:
    print("Invalid input! Enter numbers only.")
except ZeroDivisionError:
    print("Cannot divide by zero!")
```

**Solution 3**

```python
try:
    f = open("sample.txt", "r")
    print(f.read())
except FileNotFoundError:
    print("File not found.")
finally:
    try:
        f.close()
    except:
        pass
```

**Solution 4**

```python
try:
    num = int("abc")
except ValueError:
    print("Cannot convert string to integer.")
```

**Solution 5**

```python
def check_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    print("Valid age")

check_age(25)
# check_age(-5) # Uncomment to test
```

**Solution 6**

```python
def add_numbers(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both arguments must be numbers")
    return a + b

print(add_numbers(5, 3))
```

**Solution 7**

```python
def check_positive(num):
    assert num > 0, "Number must be positive"
    print("Number is positive.")

# check_positive(-5) # Will raise AssertionError
check_positive(10)
```

**Solution 8**

```python
import logging

logging.basicConfig(level=logging.ERROR)

try:
    a = 10 / 0
except ZeroDivisionError as e:
    logging.error("Error occurred: %s", e)
```

**Solution 9**

```python
import logging

logging.basicConfig(filename="errors.log", level=logging.ERROR)

filename = input("Enter filename: ")
try:
    with open(filename, "r") as f:
        print(f.read())
except Exception as e:
    logging.error("Error opening file: %s", e)
```

**Solution 10**

```python
import logging

logging.basicConfig(filename="conversion.log", level=logging.ERROR)

data = ["1", "2", "x", "4"]
for item in data:
    try:
        num = int(item)
    except ValueError as e:
        logging.error("Conversion error for '%s': %s", item, e)
```

**Solution 11**

```python
import math

num = int(input("Enter a number: "))
print("Square root:", math.sqrt(num))
print("Factorial:", math.factorial(num))
```

**Solution 12**

```python
import random

target = random.randint(1, 100)
guess = None
while guess != target:
    guess = int(input("Guess the number (1-100): "))
    if guess < target:
        print("Too low!")
    elif guess > target:
        print("Too high!")
print("Correct!")
```

**Solution 13**

```python
from datetime import datetime, timedelta

now = datetime.now()
print("Now:", now)
print("7 days later:", now + timedelta(days=7))
```

**Solution 14**

```python
import os

print("Current directory:", os.getcwd())
print("Files:", os.listdir())
```

**Solution 15**

```python
import sys

print("Python version:", sys.version)
print("Script name:", sys.argv[0])
```

**Solution 16**

```python
import math

functions = [f for f in dir(math) if not f.startswith("__")]
print(functions)
```

**Solution 17**

```python
import importlib.metadata

print("Numpy version:", importlib.metadata.version("numpy"))
```

**Solution 18**
**my\_utils.py**

```python
def greet(name):
    print(f"Hello, {name}!")
```

**main.py**

```python
import my_utils

my_utils.greet("Alice")
```

**Solution 19**

```python
import statistics

data = [1, 2, 2, 3, 4, 5, 5, 5]
print("Mean:", statistics.mean(data))
print("Median:", statistics.median(data))
print("Mode:", statistics.mode(data))
```

**Solution 20**

```python
import requests

response = requests.get("https://api.github.com")
print("Status code:", response.status_code)
```

