## VI. Hands-on Coding: Simple Python Programs (20 minutes - work)

---

### **Program 1: Greet the User**

**Objective:**

* Practice input/output, variables, and string formatting.

**Step-by-Step:**

1. **Prompt the user** for their name using `input()`.
2. **Store** the name in a variable.
3. **Print** a personalized greeting using `print()`.

**Example Code:**

```python
# Ask for the user's name
name = input("What is your name? ")

# Greet the user
print("Hello,", name + "! Welcome to Python programming.")
```

**Explanation:**

* The `input()` function displays the prompt and waits for the user to type their name.
* The entered name is stored in the variable `name`.
* The greeting uses string concatenation and the `print()` function to display a message.

---

### **Program 2: Add Two Numbers Entered by the User**

**Objective:**

* Practice input, type conversion, variables, arithmetic operations, and output formatting.

**Step-by-Step:**

1. **Prompt the user** to enter two numbers.
2. **Store** both inputs in variables.
3. **Convert** the inputs from strings to floats or ints.
4. **Add** the two numbers.
5. **Print** the result.

**Example Code:**

```python
# Ask the user for two numbers
num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")

# Convert the inputs to float (to allow decimals)
num1 = float(num1)
num2 = float(num2)

# Add the numbers
result = num1 + num2

# Print the result using an f-string
print(f"The sum of {num1} and {num2} is {result}.")
```

**Explanation:**

* `input()` collects user input as strings.
* `float()` converts input to numbers (for whole numbers, `int()` can also be used).
* The sum is stored in `result`.
* The output is displayed using an **f-string** for clarity and readability.

---

### **Bonus Program: Mini Calculator (Combines Both Examples and More)**

**Objective:**

* Reinforce input, output, data types, variables, and arithmetic.
* Demonstrate user-friendly interaction.

**Example Code:**

```python
# Welcome message
print("Welcome to the Python Mini Calculator!")

# Get user's name
name = input("What's your name? ")
print(f"Hi, {name}! Let's do some math.")

# Get two numbers from user
a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))

# Perform calculations
print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")
if b != 0:
    print(f"{a} / {b} = {a / b}")
else:
    print("Cannot divide by zero.")
```

**Explanation:**

* This example brings together everything from today: input/output, variables, data types, arithmetic, conditionals (for division by zero), and string formatting.

---

### **Activity Instructions for Students**

* Type each example into your IDE or Jupyter notebook.
* Modify the programs (change variable names, messages, or add new features).
* Experiment with both `int` and `float` conversions.
* Try to break the program—what happens if you type a word instead of a number?

---

### **Summary of Skills Practiced**

* Declaring and using variables
* Getting user input (`input()`)
* Printing output (`print()`)
* Using data types (`str`, `int`, `float`)
* Performing arithmetic operations
* String formatting (`+` and f-strings)
* Handling basic errors (like dividing by zero)

