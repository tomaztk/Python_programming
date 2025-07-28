## **VI. Modules**


### What is a Module?

A **module** is a file containing Python code — variables, functions, classes — that you can **import and reuse** in other Python programs.

* File name: `mymodule.py`
* Allows code to be organized logically and reused across multiple files.

---

##  1. **Creating a Module**

###  Example: `calculator.py`

```python
# calculator.py
def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

pi = 3.14159
```

---

##  2. **Importing Modules**

###  A. Basic Import

```python
import calculator

print(calculator.add(2, 3))        # 5
print(calculator.pi)              # 3.14159
```

###  B. Import with Alias

```python
import calculator as calc

print(calc.multiply(3, 4))         # 12
```

###  C. Import Specific Functions or Variables

```python
from calculator import add, pi

print(add(5, 6))                   # 11
print(pi)                          # 3.14159
```

###  D. Import All Symbols (*not recommended*)

```python
from calculator import *

print(multiply(2, 8))              # 16
```

** Warning:** This can **clutter your namespace** and lead to conflicts.

---

## 3. **Module Search Path**

Python searches for modules in these locations:

1. The current directory
2. Built-in modules (like `math`, `random`, etc.)
3. Directories listed in `sys.path`

You can inspect the module search path:

```python
import sys
print(sys.path)
```

---

##  4. **The `__name__ == "__main__"` Trick**

Used to make a Python file work both as a **script** and a **module**.

###  Example: `greeter.py`

```python
def greet(name):
    print(f"Hello, {name}!")

if __name__ == "__main__":
    greet("Alice")  # Runs only when executed directly
```

When you run:

```bash
python greeter.py
```

➡️ Output: `Hello, Alice!`

But if you import it:

```python
import greeter
# greet() doesn’t run automatically
```

---

##  5. **Standard Modules**

Python comes with a large library of **built-in modules**:

| Module     | Purpose                            | Example Usage             |
| ---------- | ---------------------------------- | ------------------------- |
| `math`     | Mathematical functions             | `math.sqrt(25)`           |
| `random`   | Random number generation           | `random.randint(1, 10)`   |
| `os`       | File system, environment variables | `os.getcwd()`             |
| `sys`      | Interpreter info                   | `sys.version`, `sys.path` |
| `datetime` | Dates and times                    | `datetime.datetime.now()` |

---

##  6. **Packages (Brief Overview)**

A **package** is a folder containing modules and a special `__init__.py` file (can be empty) to mark it as importable.

### Folder Structure:

```
myapp/
│
├── __init__.py
├── math_utils.py
└── string_utils.py
```

Then import like this:

```python
from myapp import math_utils
```

---

##  Practical Demo: Using Standard Modules

### Using `math` and `random`

```python
import math
import random

angle = random.uniform(0, math.pi)
print(f"sin({angle:.2f}) = {math.sin(angle):.4f}")
```

###  Using `datetime`

```python
from datetime import datetime

now = datetime.now()
print("Current time:", now.strftime("%Y-%m-%d %H:%M:%S"))
```

---

##  Summary Table

| Action                        | Syntax                       |
| ----------------------------- | ---------------------------- |
| Import entire module          | `import module`              |
| Import with alias             | `import module as alias`     |
| Import specific items         | `from module import item`    |
| Import everything (not ideal) | `from module import *`       |
| Check if script is main       | `if __name__ == "__main__":` |

---

##  Best Practices

*  Use specific imports for clarity (`from module import item`)
*  Use `as` to shorten long module names
*  Avoid wildcard imports (`from module import *`)
*  Use `__name__ == "__main__"` to separate testing from import behavior


##  **Python Modules and Packages, Requisites, and Environments**

---

##  1. What Are Python Modules and Packages?

* A **module** is a `.py` file containing Python code (functions, classes, variables).
* A **package** is a **directory** with an `__init__.py` file that can contain multiple modules or sub-packages.

###  Example Folder Structure:

```
my_project/
│
├── calculator.py
├── greeter.py
├── main.py
└── utils/
    ├── __init__.py
    └── text_tools.py
```

You can import like:

```python
from utils.text_tools import capitalize_words
```

---

##  2. What Are Requisites?

**Requisites** are **external packages** your code depends on (e.g., `numpy`, `requests`, `pandas`). These are not built into Python and must be installed using **pip**.

You track them using a `requirements.txt` file.

---

##  Example: `requirements.txt`

```
requests==2.31.0
pandas>=1.5
numpy
```

---

##  Code Using Requisites (`http_demo.py`)

```python
import requests

def fetch_python_org():
    response = requests.get("https://www.python.org")
    if response.status_code == 200:
        print("Python.org fetched successfully!")
    else:
        print("Failed to reach Python.org")

fetch_python_org()
```

### To run this:

1. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```
2. Run the script:

   ```bash
   python http_demo.py
   ```

---

## How to Generate `requirements.txt`

From a working environment:

```bash
pip freeze > requirements.txt
```

This captures the current package versions you're using.

---

## Example: Reading and Installing

**Reading** `requirements.txt`:

```bash
cat requirements.txt
```

**Installing everything**:

```bash
pip install -r requirements.txt
```

---

## Virtual Environments (Isolated Python Spaces)

A **virtual environment** is a self-contained directory with its own Python binaries and packages. It helps you:

* Avoid version conflicts
* Reproduce environments across machines
* Keep project dependencies isolated

---

### Creating a Virtual Environment

```bash
python -m venv venv
```

Activate it:

* **Windows**:

  ```bash
  venv\Scripts\activate
  ```

* **Mac/Linux**:

  ```bash
  source venv/bin/activate
  ```

---

### After Activation:

```bash
pip install -r requirements.txt
```

Then run your program safely in an isolated space!

---

## Recap Summary

| Tool               | Purpose                              | Command                         |
| ------------------ | ------------------------------------ | ------------------------------- |
| `requirements.txt` | Track package dependencies           | `pip freeze > requirements.txt` |
| `pip`              | Install packages                     | `pip install package_name`      |
| `venv`             | Create isolated Python environments  | `python -m venv venv`           |
| `__init__.py`      | Mark a directory as a Python package | Empty or with init logic        |
| `import`           | Use functions from modules           | `from module import name`       |

---

## Best Practices

* Always use a **virtual environment** per project.
* Use **specific versions** in `requirements.txt` for reproducibility.
* Keep related functionality in **separate modules** or packages.


