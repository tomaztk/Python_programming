## III. Conditional Statements

Conditional statements let your program make decisions and perform actions depending on different conditions.

---

### **A. The `if` Statement**

#### **Basic Structure:**

```python
if condition:
    # code to execute if condition is True
```

#### **Example:**

```python
x = 10
if x > 5:
    print("x is greater than 5")
```

*Output:*

```
x is greater than 5
```

#### **How it Works:**

* The code inside the `if` block (indented) runs only if the `condition` evaluates to `True`.
* Indentation (typically 4 spaces) is crucial in Python to define code blocks.

#### **Correct Usage:**

```python
temperature = 30
if temperature > 25:
    print("It's a hot day.")
```

#### **Incorrect Usage:**

```python
# INCORRECT: No colon
if temperature > 25
    print("It's a hot day.")  # SyntaxError

# INCORRECT: No indentation
if temperature > 25:
print("It's a hot day.")      # IndentationError

# INCORRECT: Assignment instead of comparison
x = 10
if x = 5:
    print("x is 5")           # SyntaxError, should be == for comparison
```

#### **Other Valid Conditions:**

* Any expression that evaluates to `True` or `False`, including:

  * Comparisons (`>`, `<`, `==`)
  * Checking membership: `if "a" in "apple":`
  * Boolean variables

---

### **B. The `else` Statement**

`else` defines what to do if the `if` condition is not met.

#### **Structure:**

```python
if condition:
    # code if condition is True
else:
    # code if condition is False
```

#### **Example:**

```python
age = 16
if age >= 18:
    print("You can vote.")
else:
    print("You are too young to vote.")
```

*Output:*

```
You are too young to vote.
```

#### **Correct Usage:**

* `else` must always follow an `if` (and any `elif`).
* No condition after `else`.

#### **Incorrect Usage:**

```python
# INCORRECT: Adding a condition to else
if age >= 18:
    print("Adult")
else age < 18:
    print("Minor")   # SyntaxError

# CORRECT:
if age >= 18:
    print("Adult")
else:
    print("Minor")
```

---

### **C. The `elif` Statement**

`elif` stands for "else if", allowing multiple exclusive conditions.

#### **Structure:**

```python
if condition1:
    # code if condition1 is True
elif condition2:
    # code if condition2 is True
elif condition3:
    # code if condition3 is True
else:
    # code if none above are True
```

#### **Example:**

```python
score = 72
if score >= 90:
    print("Grade A")
elif score >= 80:
    print("Grade B")
elif score >= 70:
    print("Grade C")
else:
    print("Grade D")
```

*Output:*

```
Grade C
```

#### **Multiple Conditions:**

* Python checks conditions **top-down**. The first `True` one runs, the rest are skipped.

#### **Correct Usage:**

* Only one branch is ever executed in an `if`-`elif`-`else` block.

#### **Incorrect Usage:**

```python
# INCORRECT: More than one block can run (NOT in if/elif/else)
if score > 70:
    print("Pass")
if score > 90:
    print("Excellent")  # Both can run if score > 90

# CORRECT: Use elif/else for mutually exclusive
if score > 90:
    print("Excellent")
elif score > 70:
    print("Pass")
else:
    print("Try again")
```

#### **Omitting `else`:**

* `else` is optional; if omitted and no condition is met, nothing happens.

---

### **Edge Cases & Truthy/Falsy Values**

* Any value in Python can be tested in a condition.

  * Zero, empty string/list/tuple/dict, and `None` are considered **False**.
  * Non-empty, non-zero values are **True**.

**Examples:**

```python
if []:
    print("Non-empty")   # Will NOT print

if [1, 2, 3]:
    print("Non-empty list")  # Will print

if 0:
    print("Zero")   # Will NOT print

if "Hello":
    print("Has text")  # Will print
```

---

### **Similar Cases / Alternatives to Conditional Statements**

#### **1. Nested `if` Statements**

```python
num = 5
if num > 0:
    if num < 10:
        print("Number is between 1 and 9")
```

#### **2. Multiple Separate `if` Statements**

(Not mutually exclusive; all can run)

```python
num = 7
if num > 5:
    print("Greater than 5")
if num % 2 == 1:
    print("Odd number")
```

#### **3. Ternary Conditional Expression ("one-line if")**

```python
status = "Adult" if age >= 18 else "Minor"
print(status)
```

#### **4. No `switch/case` in Basic Python**

* Python doesn’t have a built-in `switch/case` like some languages (Java, C). Use `if`/`elif`/`else` or dictionaries for similar logic.

##### **Example of switch-case alternative:**

```python
choice = 2
if choice == 1:
    print("Option 1 selected")
elif choice == 2:
    print("Option 2 selected")
elif choice == 3:
    print("Option 3 selected")
else:
    print("Invalid option")

# Or, with dictionary mapping:
def option_one():
    print("Option 1 selected")
def option_two():
    print("Option 2 selected")
def option_three():
    print("Option 3 selected")

options = {1: option_one, 2: option_two, 3: option_three}
options.get(choice, lambda: print("Invalid option"))()
```

---

### **D. Example Program: Check if a Number is Positive, Negative, or Zero**

```python
num = float(input("Enter a number: "))

if num > 0:
    print("The number is positive.")
elif num < 0:
    print("The number is negative.")
else:
    print("The number is zero.")
```

---

### **Common Pitfalls and Corrections:**

* **Not using `elif`, causing redundant checks:**

  ```python
  if num > 0:
      print("Positive")
  if num == 0:
      print("Zero")
  if num < 0:
      print("Negative")
  # More than one could run if logic is off!
  ```

* **Using `else` without `if`:**

  ```python
  # INCORRECT
  else:
      print("Error")  # SyntaxError
  ```

* **Missing indentation:**

  ```python
  if num > 0:
  print("Positive")  # IndentationError
  ```

---

### **Practice and check our knowledge:**

1. Write a program to print if a person is a "teenager", "adult", or "child" based on their age.
2. Check if a given year is a leap year.
3. Use a ternary expression to print "Even" or "Odd" for a given number.

---

### **Summary Table**

| Statement | Usage Example                       | Notes/Corrections                      |
| --------- | ----------------------------------- | -------------------------------------- |
| `if`      | `if a > b:`                         | Condition must return `True`/`False`   |
| `else`    | `else:`                             | No condition after else                |
| `elif`    | `elif score >= 70:`                 | Use for multiple, exclusive options    |
| Ternary   | `x = "yes" if flag else "no"`       | One-line assignment based on condition |
| No switch | Use if/elif/else or dict for switch | No native switch/case in Python        |

---

