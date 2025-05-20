## IV. Python Syntax, Variables, and Data Types 

---

### 1. **Python Syntax: The Basics**

**Case Sensitivity**

* Python distinguishes between uppercase and lowercase letters.

  * `age` and `Age` are two different variables.

**Line Endings**

* Each statement typically ends with a newline (no semicolons needed, but allowed).
* Multiple statements can be placed on one line with `;` (not recommended).

**Comments**

* Single-line comments use `#`.
* Multi-line comments use triple quotes `""" ... """` (also used for docstrings).

**Example:**

```python
# This is a comment
name = "Sam"  # This is also a comment

"""
This is a
multi-line comment or docstring.
"""
```

---

### 2. **Variables in Python**

**Dynamic Typing**

* You don’t need to declare a variable’s type.
* The type is determined by the value assigned, and you can change it at runtime.
* **In theory:** This is called *dynamic typing*. It contrasts with *static typing* in languages like Java or C++.

**Variable Declaration and Assignment**

```python
x = 5         # int
x = "hello"   # Now x is a str!
```

**Variable Naming Rules**

* Must start with a letter or underscore.
* Can include letters, numbers, and underscores.
* Cannot be a Python keyword (like `if`, `for`, `class`, etc.).

**Example:**

```python
_age = 25
user2 = "Alice"
# 2user = "error"  # Invalid!
```

**Why Dynamic Typing?**

* Makes code more flexible and quick to write.
* Encourages prototyping and experimentation.
* **Downside:** Can lead to bugs if you’re not careful (e.g., accidentally treating a string as a number).

---

### 3. **Data Types in Python**

#### **a) Numeric Types**

* **int** – Integer numbers

  ```python
  a = 10
  b = -23
  ```
* **float** – Floating point (decimal) numbers

  ```python
  pi = 3.14159
  price = -2.75
  ```
* **complex** – Complex numbers (less common)

  ```python
  z = 2 + 3j
  ```

#### **b) Text Type**

* **str** – String (sequence of Unicode characters)

  ```python
  message = "Hello, World!"
  char = 'A'
  ```

#### **c) Boolean Type**

* **bool** – Logical values `True` or `False`

  ```python
  is_valid = True
  is_finished = False
  ```

#### **d) Sequence Types**

* **list** – Ordered, mutable sequence

  ```python
  fruits = ["apple", "banana", "cherry"]
  fruits[0] = "grape"  # Lists are mutable!
  ```
* **tuple** – Ordered, immutable sequence

  ```python
  point = (2, 3)
  # point[0] = 5  # Error! Tuples are immutable.
  ```

#### **e) Mapping Type**

* **dict** – Key-value pairs (dictionary)

  ```python
  student = {"name": "Sam", "age": 21}
  print(student["name"])  # "Sam"
  ```

#### **f) Set Types**

* **set** – Unordered, unique elements

  ```python
  colors = {"red", "green", "blue"}
  colors.add("yellow")
  ```

---

### 4. **Type Checking and Conversion**

* Use `type()` to check a variable’s type.

  ```python
  x = 5
  print(type(x))  # <class 'int'>
  ```
* Convert between types:

  ```python
  x = "123"
  y = int(x)     # y is now 123 (int)
  z = float(x)   # z is now 123.0 (float)
  name = str(123)  # name is "123" (str)
  ```

---

### 5. **Differences from Other Languages**

| Feature               | Python                   | Java/C++                  |
| --------------------- | ------------------------ | ------------------------- |
| Type Declaration      | `x = 10`                 | `int x = 10;`             |
| Type Changes Allowed? | Yes                      | No (fixed at declaration) |
| End of Statement      | Newline                  | Semicolon (`;`)           |
| Block Delimiters      | Indentation              | `{ }` braces              |
| Variable Name         | Dynamic (no type prefix) | Static (type required)    |

---

### 6. **Examples for Students**

**Variable Assignments and Types**

```python
age = 18           # int
height = 1.75      # float
name = "Charlie"   # str
is_student = True  # bool
```

**Lists and Dictionaries**

```python
grades = [90, 85, 88, 92]  # list of ints
student_info = {"name": "Sam", "id": 12345}
```

**Type Conversion**

```python
# Input always returns str!
user_age = input("Enter your age: ")
age_num = int(user_age)
```

---

### 7. **Quick Activity / Demo**

* Try assigning different types to the same variable.
* Try using `type()` to print out the types.
* Try making a list, tuple, dict, and set in your IDE.

---

### 8. **Summary Table**

| Type  | Example              | Mutable? | Ordered? | Unique?   |
| ----- | -------------------- | -------- | -------- | --------- |
| int   | `a = 5`              | N/A      | N/A      | N/A       |
| float | `b = 3.14`           | N/A      | N/A      | N/A       |
| str   | `s = "hi"`           | No       | Yes      | N/A       |
| bool  | `is_ready = False`   | N/A      | N/A      | N/A       |
| list  | `l = [1, 2, 3]`      | Yes      | Yes      | No        |
| tuple | `t = (1, 2, 3)`      | No       | Yes      | No        |
| dict  | `d = {"a":1, "b":2}` | Yes      | No       | Keys: Yes |
| set   | `s = {1, 2, 3}`      | Yes      | No       | Yes       |

---

### 9. **Pro Tips**

* Use meaningful variable names.
* Start with lowercase, use underscores for multiple words (`user_name`).
* Avoid using reserved keywords (like `class`, `if`, `def`) as variable names.


