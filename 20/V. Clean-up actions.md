## **V. Clean-up actions**

### What is a Clean-up Action?

A **clean-up action** ensures that certain code (like closing files or releasing resources) **always runs**, even if an exception is raised.

---

##  Use Case: Resource Management

Resources like files, sockets, or database connections **must be released** even if an error occurs. Failing to do this can lead to:

* Resource leaks
* File locks
* Incomplete transactions

---

##  Methods for Clean-up:

### 1. Using `finally` Clause

The `finally` block **always executes**, whether an exception was raised or not.

---

###  Demo 1: File Handling with `finally`

```python
try:
    file = open("example.txt", "r")
    # Simulate error or normal read
    content = file.read()
    print(content)
except FileNotFoundError:
    print("File not found.")
finally:
    print("Closing file...")
    try:
        file.close()
    except NameError:
        print("File was never opened.")
```

###  Explanation:

* `file.close()` is guaranteed to run.
* Prevents leaving a file open even when an error is raised.

---

###  2. Using `with` Statement (Context Manager)

The `with` statement is a cleaner and safer way to manage resources. It **automatically handles clean-up** by calling special methods like `__enter__()` and `__exit__()`.

---

###  Demo 2: File Handling with `with`

```python
try:
    with open("example.txt", "r") as f:
        content = f.read()
        print(content)
except FileNotFoundError:
    print("File not found.")
```

###  Explanation:

* `with` automatically closes the file after the block.
* No need for `finally`.

---

##  Demo 3: `finally` Always Executes

```python
try:
    print("Starting calculation...")
    result = 10 / 0
except ZeroDivisionError:
    print("Caught divide by zero.")
finally:
    print("Clean-up: Shutting down safely.")
```

Output:

```
Starting calculation...
Caught divide by zero.
Clean-up: Shutting down safely.
```

---

##  Summary Table

| Approach         | Description                                         | Example Use Cases                          |
| ---------------- | --------------------------------------------------- | ------------------------------------------ |
| `finally` block  | Always runs. Useful for manual cleanup              | File closing, DB disconnect, logging       |
| `with` statement | Automatically handles clean-up via context managers | File I/O, network sockets, temporary files |

---

## Demo 4: Cleaning Up a Network Connection (Simulated)

```python
class DummyConnection:
    def __enter__(self):
        print("Opening connection...")
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Closing connection...")

with DummyConnection() as conn:
    print("Using connection...")
    raise RuntimeError("Connection error!")
```

Output:

```
Opening connection...
Using connection...
Closing connection...
```

Even though an exception is raised, the clean-up runs!

---

##  Best Practices

* **Use `with` when possible** – it’s concise, clean, and less error-prone.
* **Use `finally`** for manual or conditional resource release.
* **Never rely on garbage collection** to clean up important resources.

 
