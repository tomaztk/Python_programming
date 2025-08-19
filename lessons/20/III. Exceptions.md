## **III. Exceptions**


###  What is an Exception?

An **exception** is an error that **interrupts normal program flow**. Instead of crashing the program, Python allows you to handle exceptions using `try`, `except`, and related keywords.

---

###  Common Built-in Exceptions

| Exception           | Description                                                                        |
| ------------------- | ---------------------------------------------------------------------------------- |
| `ZeroDivisionError` | Raised when dividing by zero                                                       |
| `ValueError`        | Raised when a function gets an argument of correct type but invalid value          |
| `TypeError`         | Raised when an operation or function is applied to an object of inappropriate type |
| `IndexError`        | Raised when a sequence index is out of range                                       |
| `KeyError`          | Raised when a dictionary key is not found                                          |
| `FileNotFoundError` | Raised when trying to open a file that doesn't exist                               |
| `ImportError`       | Raised when an import fails                                                        |
| `AttributeError`    | Raised when an object does not have a requested attribute                          |

---

##  Demo 1: Catching Multiple Exception Types

```python
data = ["10", "0", "abc", None]

for item in data:
    try:
        print(f"Processing: {item}")
        number = int(item)
        result = 100 / number
    except ValueError:
        print("ValueError: Cannot convert to integer.")
    except ZeroDivisionError:
        print("ZeroDivisionError: Cannot divide by zero.")
    except Exception as e:
        print(f"Unhandled Exception: {type(e).__name__} - {e}")
    finally:
        print("Done.\n")
```

---

##  Demo 2: Catching Unknown Exceptions

```python
try:
    x = 5
    y = "10"
    z = x + y  # Will raise TypeError
except Exception as e:
    print(f"Exception caught: {type(e).__name__} - {e}")
```

** Tip:** Using `except Exception as e` is helpful for debugging unknown issues, but not recommended for production error handling unless logging and re-raising.

---

##  Demo 3: Using `else` and `finally`

```python
try:
    num = int(input("Enter a number: "))
    result = 10 / num
except (ValueError, ZeroDivisionError) as e:
    print("Caught an error:", e)
else:
    print("Everything worked! Result is:", result)
finally:
    print("This runs no matter what.")
```

---

###  Best Practices for Exceptions

* Catch **only expected exceptions**.
* Use **specific exception types** instead of a generic `except:`.
* Always use `finally` when a resource needs to be cleaned up (e.g., file closing).
* `raise` can be used to throw an exception manually.
* You can also define your own **custom exception classes** if needed.

---

##  Demo 4: Custom Exception

```python
class NegativeNumberError(Exception):
    pass

def check_positive(n):
    if n < 0:
        raise NegativeNumberError("Negative number not allowed.")
    return n

try:
    check_positive(-5)
except NegativeNumberError as e:
    print("Custom exception caught:", e)
```



