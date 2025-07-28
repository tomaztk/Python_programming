## **VI. Hands-on**

1. Create a folder structure for hands-on examples (simulated here in code)
1. Simulate the creation of multiple Python files as string examples



### calculator.py (Module)

calculator_code: 

```python
def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

pi = 3.14159
```

###  greeter.py (Script/Module with __name__ check)

greeter_code:

```python
def greet(name):
    print(f"Hello, {name}!")

if __name__ == "__main__":
    greet("Alice")
```

###  hands_on_demo.py (Main script using modules and exception handling)


hands_on_demo_code:

```python
import calculator
import greeter
import math
import random
from datetime import datetime

def main():
    print("=== Calculator Demo ===")
    print("Add 5 + 3:", calculator.add(5, 3))
    print("Multiply 4 * 6:", calculator.multiply(4, 6))
    print("Value of pi:", calculator.pi)

    print("\\n=== Random and Math Demo ===")
    num = random.randint(1, 100)
    print("Random number:", num)
    print("Square root:", math.sqrt(num))

    print("\\n=== DateTime Demo ===")
    now = datetime.now()
    print("Current time:", now.strftime("%Y-%m-%d %H:%M:%S"))

    print("\\n=== Exception Handling Demo ===")
    sample = ["42", "0", "abc", None]
    for item in sample:
        try:
            print(f"Processing: {item}")
            n = int(item)
            print("Reciprocal:", 1 / n)
        except ValueError:
            print("ValueError: Cannot convert to int.")
        except ZeroDivisionError:
            print("ZeroDivisionError: Cannot divide by zero.")
        except Exception as e:
            print("Unexpected error:", type(e).__name__, "-", e)
        finally:
            print("Done.\\n")

if __name__ == "__main__":
    main()
```


### Main file

```python
import pandas as pd
import ace_tools as tools

  
examples_df = pd.DataFrame([
    {"File": "calculator.py", "Purpose": "Module with math functions", "Code": calculator_code.strip()},
    {"File": "greeter.py", "Purpose": "Greets user; demonstrates __name__ check", "Code": greeter_code.strip()},
    {"File": "hands_on_demo.py", "Purpose": "Main hands-on script for demo", "Code": hands_on_demo_code.strip()}
])

tools.display_dataframe_to_user(name="Hands-On Python Modules and Exception Examples", dataframe=examples_df)
```