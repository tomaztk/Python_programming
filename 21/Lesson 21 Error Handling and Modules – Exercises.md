## **Lesson 21: Error Handling and Modules – Exercises**

---

### **Part 1: Error Handling**

**Exercise 1 – Basic `try-except`**
Write a program that asks the user for a number and prints its square. Handle any errors if the input is not a valid number.

**Exercise 2 – Multiple `except` Blocks**
Write a program that:

* Divides two numbers entered by the user
* Catches both `ValueError` (invalid input) and `ZeroDivisionError` separately

**Exercise 3 – `try-except-finally`**
Write a program that opens a file and reads its content. Make sure the file is always closed, even if an error occurs.

**Exercise 4 – Catching Specific Exceptions**
Write a program that tries to convert a string `"abc"` to an integer and catches the error.

**Exercise 5 – Raising a `ValueError`**
Write a function `check_age(age)` that:

* Raises a `ValueError` if age is negative
* Prints "Valid age" otherwise

**Exercise 6 – Raising a `TypeError`**
Write a function `add_numbers(a, b)` that:

* Raises a `TypeError` if either `a` or `b` is not a number
* Returns their sum otherwise

**Exercise 7 – Using `assert`**
Write a function that asserts the given number is positive. Test it with a negative number.

**Exercise 8 – Logging Errors (Console)**
Write a program that:

* Tries to divide two numbers
* Logs the error to the console using the `logging` module

**Exercise 9 – Logging Errors (File)**
Write a program that:

* Reads a file name from the user
* Tries to open the file
* Logs any errors to a file `errors.log`

**Exercise 10 – Combining `try-except` with Logging**
Write a program that:

* Tries to convert a list of strings to integers
* Logs all errors into a file `conversion.log`

---

### **Part 2: Working with Modules**

**Exercise 11 – Using the `math` Module**
Write a program that:

* Asks the user for a number
* Prints its square root and factorial using the `math` module

**Exercise 12 – Using the `random` Module**
Write a program that:

* Generates a random number between 1 and 100
* Lets the user guess until they get it right

**Exercise 13 – Using the `datetime` Module**
Write a program that:

* Prints the current date and time
* Prints the date 7 days from now

**Exercise 14 – Using the `os` Module**
Write a program that:

* Prints the current working directory
* Lists all files in it

**Exercise 15 – Using the `sys` Module**
Write a program that:

* Prints the Python version
* Prints the script name

**Exercise 16 – Listing Functions in a Module**
Write a program that:

* Lists all available functions in the `math` module (excluding special methods)

**Exercise 17 – Getting a Package Version**
Write a program that:

* Prints the version of the `numpy` package (if installed)

**Exercise 18 – Creating and Importing a Custom Module**
Create a module `my_utils.py` with a function `greet(name)` that prints `"Hello, <name>!"`. Import and use it in another script.

**Exercise 19 – Using the `statistics` Module**
Write a program that:

* Calculates the mean, median, and mode of a given list of numbers

**Exercise 20 – Using a Third-Party Module**
Install the `requests` module and write a program that fetches data from `https://api.github.com` and prints the status code.

---
