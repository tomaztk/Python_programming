
## V. Input/Output Functions, Print Statements, and Console Communication (20 minutes)

---

### 1. **Printing Output with `print()`**

**Purpose:**

* The `print()` function displays information on the console (standard output).

**Basic Usage:**

```python
print("Hello, World!")
```

*Output:*

```
Hello, World!
```

**Printing Multiple Items:**

* You can print several values separated by commas. Python will add a space by default.

```python
name = "Alice"
age = 23
print("Name:", name, "Age:", age)
```

*Output:*

```
Name: Alice Age: 23
```

**String Concatenation:**

* You can use `+` to join strings.

```python
print("Hello, " + name + "!")
```

*Output:*

```
Hello, Alice!
```

> Note: All arguments must be strings when using `+`. If not, you need to convert them with `str()`.

---

**Advanced Printing: Formatting Strings**

* **f-strings** (Python 3.6+): Easy way to insert variable values.

```python
print(f"My name is {name} and I am {age} years old.")
```

*Output:*

```
My name is Alice and I am 23 years old.
```

* **`format()` method:**

```python
print("My name is {} and I am {} years old.".format(name, age))
```

---

**Custom Endings and Separators:**

* **`end` argument:** Change what is printed at the end (default is newline `\n`).

```python
print("Hello,", end=" ")
print("World!")
```

*Output:*

```
Hello, World!
```

* **`sep` argument:** Change how multiple arguments are separated (default is space).

```python
print("2025", "05", "19", sep="-")
```

*Output:*

```
2025-05-19
```

---

### 2. **Receiving Input with `input()`**

**Purpose:**

* `input()` lets you get user input from the console.
* It always returns a string.

**Basic Usage:**

```python
name = input("What is your name? ")
print("Hello,", name)
```

*Sample Run:*

```
What is your name? Sam
Hello, Sam
```

---

**Converting Input to Other Types**

* Since `input()` always returns a string, you need to **convert** it for numbers:

```python
age = input("How old are you? ")
print(type(age))  # <class 'str'>

# Convert to int
age = int(age)
print(type(age))  # <class 'int'>
```

**Example: Adding Two Numbers from User Input**

```python
num1 = input("Enter a number: ")
num2 = input("Enter another number: ")

# Convert to numbers
num1 = float(num1)
num2 = float(num2)

print("The sum is:", num1 + num2)
```

*Sample Run:*

```
Enter a number: 3
Enter another number: 4.5
The sum is: 7.5
```

---

**Error to Watch For:**
If you try to convert something that’s not a number:

```python
num = int("abc")  # This will cause a ValueError!
```

---

### 3. **Console Communication – Tips and Best Practices**

* **Prompt clearly:** Always give the user instructions on what to enter.

  * Good: `input("Enter your age: ")`
  * Bad:  `input()`
* **Use print() to make output user-friendly and informative.**
* **Always convert user input** when a number is needed (`int()` or `float()`).

---

### 4. **Demo Activities for Students**

**Activity 1:** Greet the user

```python
name = input("What's your name? ")
print("Welcome,", name, "!")
```

**Activity 2:** Simple calculator

```python
a = float(input("First number: "))
b = float(input("Second number: "))
print(f"Sum: {a + b}")
print(f"Product: {a * b}")
```

**Activity 3:** Personalized output

```python
color = input("What is your favorite color? ")
animal = input("What is your favorite animal? ")
print(f"Your favorite color is {color} and your favorite animal is {animal}.")
```

---

### 5. **Summary Table**

| Function  | Purpose             | Example Usage            | Returns |
| --------- | ------------------- | ------------------------ | ------- |
| `print()` | Output to console   | `print("Hello")`         | None    |
| `input()` | Get input from user | `name = input("Name: ")` | `str`   |

---

### 6. **Pro Tip**

* If you want to print a blank line, just use:

  ```python
  print()
  ```
* For complex inputs, you can split and process:

  ```python
  data = input("Enter two numbers separated by space: ")
  x, y = data.split()
  x = int(x)
  y = int(y)
  print(x, y)
  ```

---

Let me know if you want exercises, a handout, or an interactive Jupyter notebook for this section!
