## II. Errors and exceptions

##  Sample Dataset (for demo programs)

Use this list of diverse values in examples:

```python
sample = ["42", "0", "hello", -1, None, 3.14, [], {}, 7]
```

This dataset contains strings valid for integer conversion, zero, invalid strings, negative values, floats, empty lists/dicts, and a good integer.

---

## 1. How `try…except…else…finally` Works

According to the Python docs:

* **`try` clause** executes code that may raise an exception.
* If **no exception** occurs, any `except` blocks are skipped, and control moves to `else` (if present), then `finally`.
* If an exception **occurs**, the rest of the `try` block is skipped; execution jumps to the **first matching `except` clause**. If none matches, the exception propagates out.
* The **`else` clause** runs only when the `try` succeeds without exceptions.
* The **`finally` clause** always executes, whether or not an exception occurred. Even if `except` or `else` raises an error, `finally` still runs before propagation.
* 
---

## 2. Demo Programs Covering Exception Types

###  A: Integer Conversion and Division Loop

```python
import sys

for item in sample:
    try:
        print(f"Testing: {item} → int:", end=" ")
        n = int(item)
        print(n, "→ divide 100 by it:", end=" ")
        result = 100 / n
    except ValueError as e:
        print("ValueError:", e)
    except ZeroDivisionError as e:
        print("ZeroDivisionError:", e)
    else:
        print("Result =", result)
    finally:
        print("— End of processing for this item\n")
```

**What it shows**:

* Convert items like `"hello"` → raises `ValueError`
* Divide by `"0"` → raises `ZeroDivisionError`
* For valid int and non-zero → runs `else`
* Always runs `finally`

---

###  B: Handling `TypeError`, `KeyError`, `IndexError`

```python
# TypeError demo
a = [1, 2, 3]
try:
    print("Adding int and list:", 1 + a)
except TypeError as e:
    print("TypeError:", e)

# IndexError demo
try:
    print("Accessing index:", a[10])
except IndexError as e:
    print("IndexError:", e)

# KeyError demo
d = {"x": 1}
try:
    print("Access key 'y':", d["y"])
except KeyError as e:
    print("KeyError:", e)
finally:
    print("Completed lookup demos\n")
```

---

### C: FileNotFoundError Clean‑up with `finally`

```python
try:
    f = open("missing_file.txt", "r")
    data = f.read()
except FileNotFoundError as e:
    print("FileNotFoundError:", e)
else:
    print("File length:", len(data))
finally:
    print("Cleaning up: closing file if needed")
    try:
        f.close()
    except NameError:
        print("File was never opened")
```

---

###  D: Custom Raising and Re‑Raising Exceptions

```python
def validate_positive(n):
    if n < 0:
        raise ValueError(f"Negative value not allowed: {n}")
    return n

try:
    x = validate_positive(-5)
except ValueError as e:
    print("Caught custom ValueError:", e)
    raise  # Re‑raises the same exception
finally:
    print("Done validate_positive demo")
```

---

## 3. Summary Table

| Clause    | Runs When?                               | Purpose                                                          |
| --------- | ---------------------------------------- | ---------------------------------------------------------------- |
| `try`     | Always                                   | Put code that might raise exceptions                             |
| `except`  | Only if a matching exception occurs      | Handle specific errors (e.g., `ValueError`, `ZeroDivisionError`) |
| `else`    | Only if `try` succeeds with no exception | Code to run when everything went fine                            |
| `finally` | Always, before block ends                | Cleanup such as closing files or resources                       |

Use specific exception types where possible (e.g. `except ValueError`), not generic `except:`. Use `else` to separate success logic, and `finally` for cleanup ([Python documentation][1], [Stack Overflow][4], [Medium][5], [Wikibooks][3], [Python documentation][6], [Python documentation][7]).

---

## 4. Recap of Covered Built-in Exceptions

From the tutorials and docs:

* **`ValueError`**: right type, wrong value (e.g. `int("hello")`)
* **`ZeroDivisionError`**: dividing by zero
* **`TypeError`**: unsupported operand type(s)
* **`IndexError`**, **`KeyError`**: invalid list/dict access
* **`FileNotFoundError`**: missing file on open
* **`Exception` / re‑raise**: use generic catch with caution; good for logging then re‑raising ([deepnote.com][8])

---

##  Putting It All Together: Full Script Example

```python
import sys

sample = ["42", "0", "hello", -1, None, 3.14, [], {}, 7]

def validate_positive(n):
    if n < 0:
        raise ValueError(f"Negative value not allowed: {n}")
    return n

for item in sample:
    try:
        print("Item:", item)
        n = int(item)
        validate_positive(n)
        result = 100 / n
    except ValueError as e:
        print("ValueError:", e)
    except ZeroDivisionError as e:
        print("ZeroDivisionError:", e)
    except Exception as e:
        print("Unexpected exception:", type(e).__name__, "-", e)
    else:
        print("OK → result =", result)
    finally:
        print("Finished processing this item.")
        print("-" * 40)
```

---

