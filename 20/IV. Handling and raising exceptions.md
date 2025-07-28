## **IV. Handling and raising exceptions**


###  What Is Exception Handling?

Exception handling allows you to **gracefully respond** to errors without crashing your program. This is done using:

* `try`: code that might raise an exception
* `except`: code to handle the exception
* `else`: code to run if no exceptions were raised
* `finally`: code that runs no matter what (for cleanup)

---

##  Basic Structure

```python
try:
    # risky code
except SomeException:
    # handle error
else:
    # run if no error
finally:
    # always runs
```

---

##  **Demo 1: Handling a Specific Exception**

```python
try:
    number = int(input("Enter a number: "))
    print("100 divided by your number is:", 100 / number)
except ValueError:
    print("Oops! That was not a valid number.")
except ZeroDivisionError:
    print("Cannot divide by zero.")
```

###  Explanation:

* **`ValueError`**: occurs if input is non-numeric (e.g., "abc")
* **`ZeroDivisionError`**: occurs if user enters `0`

---

##  **Demo 2: Handling Multiple Exceptions in One Line**

```python
try:
    num = int(input("Enter a number: "))
    print("Reciprocal is", 1 / num)
except (ValueError, ZeroDivisionError) as e:
    print("Handled error:", e)
```

###  Explanation:

You can group multiple exceptions using parentheses.

---

##  **Demo 3: Using `else` and `finally`**

```python
try:
    value = int(input("Enter an integer: "))
except ValueError:
    print("That’s not an integer.")
else:
    print("Success! You entered:", value)
finally:
    print("Finished input processing.")
```

###  Explanation:

* `else`: runs only if no exception occurs.
* `finally`: runs **regardless** of whether an error was raised.

---

##  **Demo 4: Handling Unknown Exceptions**

```python
try:
    risky = [1, 2, 3][5]  # IndexError
except Exception as e:
    print("An unexpected error occurred:", type(e).__name__, "-", e)
```

###  Tip:

* Using `except Exception` is good for logging or debugging.
* Avoid using it in place of specific exception handling.

---

##  **Re-raising Exceptions**

Sometimes you want to handle an error but still let it bubble up:

```python
try:
    raise ValueError("Something went wrong.")
except ValueError as e:
    print("Logging error:", e)
    raise  # Re-raise the same exception
```

---

##  **Best Practices**

| Practice                           | Why It Matters                                      |
| ---------------------------------- | --------------------------------------------------- |
| Use specific exception types       | Easier to debug, avoids catching unexpected errors  |
| Use `finally` for cleanup          | Guarantees resources (like files) are released      |
| Log or raise meaningful exceptions | Helps with debugging and production error reporting |
| Avoid bare `except:` clauses       | They hide real bugs and make issues harder to trace |

---

##  **Challenge Demo: Full Exception Handling Flow**

```python
def get_number():
    try:
        num = int(input("Enter an integer: "))
        if num == 0:
            raise ZeroDivisionError("Manual raise: zero not allowed.")
        print("Result is", 100 / num)
    except ValueError:
        print("Please enter a numeric value.")
    except ZeroDivisionError as e:
        print("Math error:", e)
    else:
        print("Everything worked fine!")
    finally:
        print("Cleanup complete.\n")

# Run the function
get_number()
```

