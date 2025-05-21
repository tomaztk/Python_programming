
## II. Operators, Counting, Flow Control, Enumerators

---

### **A. Operators in Python**

Operators are symbols that perform operations on variables and values. In Python, the main types are:

#### **1. Arithmetic Operators**

| Operator | Name           | Example   | Result      |
| -------- | -------------- | --------- | ----------- |
| +        | Addition       | `3 + 2`   | 5           |
| -        | Subtraction    | `7 - 4`   | 3           |
| \*       | Multiplication | `5 * 2`   | 10          |
| /        | Division       | `10 / 4`  | 2.5 (float) |
| //       | Floor Division | `10 // 4` | 2 (integer) |
| %        | Modulo         | `10 % 3`  | 1           |
| \*\*     | Exponentiation | `2 ** 3`  | 8           |

#### **Examples:**

```python
print(5 + 3)       # 8
print(7 / 2)       # 3.5
print(7 // 2)      # 3
print(10 % 4)      # 2
print(2 ** 4)      # 16
```

**Common Mistake:**
Using `/` when you want integer division:

```python
print(9 / 2)   # 4.5 (float) CORRECT
print(9 // 2)  # 4 (integer division) CORRECT

# INCORRECT:
result = 9 // 2.0   # Result is float 4.0, not integer, as one operand is float
```

#### **2. Comparison Operators**

Used to compare values. Always returns `True` or `False`.

| Operator | Description           | Example  | Result |
| -------- | --------------------- | -------- | ------ |
| ==       | Equal                 | `3 == 4` | False  |
| !=       | Not Equal             | `5 != 3` | True   |
| <, >     | Less, Greater         | `2 < 5`  | True   |
| <=, >=   | Less/Greater or Equal | `5 >= 5` | True   |

#### **Examples:**

```python
a = 5
b = 7
print(a < b)       # True
print(a == b)      # False
print(a != b)      # True
```

**Common Mistake:**
Assigning (`=`) instead of comparing (`==`):

```python
# INCORRECT:
if a = b:
    print("Equal")  # SyntaxError

# CORRECT:
if a == b:
    print("Equal")
```

#### **3. Logical Operators**

Combine multiple conditions.

* `and` – True if both are True
* `or` – True if at least one is True
* `not` – Inverts the condition

#### **Examples:**

```python
x = 10
print(x > 5 and x < 20)   # True
print(x < 5 or x > 5)     # True
print(not (x == 10))      # False
```

---

### **B. Counting with `range()`**

#### **What is `range()`?**

* `range(start, stop, step)` generates a sequence of numbers.
* Often used with `for` loops.

#### **Common Usages:**

```python
# Count from 0 to 4 (default start is 0)
for i in range(5):
    print(i)   # 0, 1, 2, 3, 4

# Count from 1 to 5
for i in range(1, 6):
    print(i)   # 1, 2, 3, 4, 5

# Count from 2 to 10, stepping by 2
for i in range(2, 11, 2):
    print(i)   # 2, 4, 6, 8, 10
```

#### **Counting Downwards:**

```python
for i in range(10, 0, -2):
    print(i)  # 10, 8, 6, 4, 2
```

#### **Common Mistakes:**

* Forgetting that the `stop` value is **exclusive** (not included).

  ```python
  for i in range(1, 5):
      print(i)   # 1, 2, 3, 4 (not 5)
  ```
* Using a negative step without adjusting start/stop.

  ```python
  for i in range(5, 0, -1):
      print(i)  # 5, 4, 3, 2, 1
  ```

#### **Other Useful Counting:**

* **Sum all numbers from 1 to N:**

  ```python
  total = 0
  for i in range(1, 11):
      total += i
  print(total)  # 55
  ```

* **Generate a list of numbers:**

  ```python
  numbers = list(range(5))
  print(numbers)  # [0, 1, 2, 3, 4]
  ```

---

### **C. Enumerators (`enumerate()`)**

#### **What is `enumerate()`?**

* Lets you loop over a sequence **and** get the index and value at the same time.

#### **Example:**

```python
colors = ['red', 'green', 'blue']
for index, color in enumerate(colors):
    print(f"Index: {index}, Color: {color}")
```

*Output:*

```
Index: 0, Color: red
Index: 1, Color: green
Index: 2, Color: blue
```

#### **Correct Usage:**

* Using both index and value for display, calculations, or logic:

  ```python
  for idx, val in enumerate(['a', 'b', 'c']):
      print(idx, val)
  ```

#### **Customizing Start Index:**

```python
for idx, val in enumerate(['apple', 'banana'], start=1):
    print(idx, val)
# Output: 1 apple 2 banana
```

#### **Incorrect Usage:**

* Using `enumerate()` on something not iterable (e.g., a number):

  ```python
  # INCORRECT:
  for idx, val in enumerate(100):
      print(idx, val)  # TypeError: 'int' object is not iterable
  ```

* Forgetting to unpack both index and value:

  ```python
  # INCORRECT:
  for item in enumerate(['a', 'b']):
      print(item)  # Prints tuples: (0, 'a'), (1, 'b')
  # CORRECT:
  for idx, val in enumerate(['a', 'b']):
      print(idx, val)
  ```

#### **Similar/Related Cases:**

* **Looping with range(len(list)):**
  (Not recommended unless you need the index specifically)

  ```python
  mylist = ['x', 'y', 'z']
  for i in range(len(mylist)):
      print(i, mylist[i])
  ```
* **Using zip() for two lists:**

  ```python
  names = ['Alice', 'Bob']
  scores = [85, 90]
  for name, score in zip(names, scores):
      print(name, score)
  ```

---

## **Summary Table**

| Feature    | Usage Example                           | Notes/Corrections             |
| ---------- | --------------------------------------- | ----------------------------- |
| Arithmetic | `a + b`, `a // b`                       | Use `//` for int division     |
| Comparison | `a == b`, `a < b`                       | Use `==`, not `=` for compare |
| Logical    | `x > 2 and x < 10`                      | Combine multiple conditions   |
| Range      | `for i in range(3, 8, 2): ...`          | Step can be negative          |
| Enumerate  | `for idx, item in enumerate(list): ...` | Unpack both index and value   |

---

## **Let us check play with:**

1. **Arithmetic & Comparison:**

   * Write a program that asks for two numbers and prints their sum, difference, and whether they are equal.

2. **Counting:**

   * Print all even numbers between 20 and 30.
   * Sum all numbers from 50 down to 10 (inclusive), stepping by -5.

3. **Enumerate:**

   * Print a shopping list with item numbers starting at 1.


