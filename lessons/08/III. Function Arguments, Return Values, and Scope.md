## **III. Function Arguments, Return Values, and Scope**

---

### **1. Arguments: Required vs Optional Arguments**

#### **Required (Positional) Arguments**

* **Explanation:** Must be provided when the function is called.
* **Example:**

  ```python
  def greet(name):
      print(f"Hello, {name}!")

  greet("Alice")  # Correct
  # greet()      # Error: missing required argument
  ```
* **Good Practice:** Keep functions simple; use required arguments for essential data.

#### **Optional (Default) Arguments**

* **Explanation:** Have default values. If not provided, Python uses the default.
* **Example:**

  ```python
  def greet(name, greeting="Hello"):
      print(f"{greeting}, {name}!")

  greet("Bob")                # Output: Hello, Bob!
  greet("Bob", "Good morning") # Output: Good morning, Bob!
  ```
* **Good Practice:** Place required arguments first, then optional ones.
* **Why Needed:** Makes functions more flexible and easier to use in more situations.

#### **Keyword Arguments**

* **Explanation:** Arguments passed by name. Improves clarity.
* **Example:**

  ```python
  greet(name="Charlie", greeting="Hi")  # Output: Hi, Charlie!
  ```

---

### **2. Return Values: Using `return`, Multiple Return Values**

#### **Using `return`**

* **Explanation:** The `return` statement sends a value back to the caller.
* **Example:**

  ```python
  def add(a, b):
      return a + b

  result = add(2, 3)
  print(result)  # Output: 5
  ```
* **Good Practice:** Always use `return` when your function needs to send data back.

#### **Multiple Return Values**

* **Explanation:** Python can return multiple values as a tuple.
* **Example:**

  ```python
  def get_stats(numbers):
      total = sum(numbers)
      count = len(numbers)
      average = total / count if count > 0 else 0
      return total, count, average

  t, c, avg = get_stats([1, 2, 3])
  print(f"Total: {t}, Count: {c}, Average: {avg}")
  # Output: Total: 6, Count: 3, Average: 2.0
  ```
* **Good Practice:** Use multiple returns when a function naturally produces several results.

#### **No Return (Implicit `None`)**

* **Explanation:** If a function doesn't return anything, Python returns `None`.
* **Example:**

  ```python
  def say_hello():
      print("Hello!")

  result = say_hello()
  print(result)  # Output: None
  ```

---

### **3. Scope: Local vs Global Variables, `global` Keyword, Best Practices**

#### **Local Variables**

* **Explanation:** Variables defined inside a function are *local* to that function.
* **Example:**

  ```python
  def foo():
      x = 5  # x is local to foo()
      print(x)

  foo()
  # print(x)  # Error: x is not defined outside foo()
  ```

#### **Global Variables**

* **Explanation:** Variables defined outside any function are *global* and can be accessed inside functions (but not modified unless declared global).
* **Example:**

  ```python
  y = 10  # global variable

  def bar():
      print(y)  # Can access global y

  bar()
  ```

#### **Modifying Globals with `global` Keyword**

* **Explanation:** To modify a global variable inside a function, use `global`.
* **Example:**

  ```python
  count = 0

  def increment():
      global count
      count += 1

  increment()
  print(count)  # Output: 1
  ```
* **Good Practice:** **Avoid using global variables unless absolutely necessary**—they make code harder to understand and debug. Prefer returning values and passing them as arguments.

#### **Best Practices for Scope**

* Prefer local variables—limit their “reach.”
* Use function arguments and return values to share data between functions.
* Avoid using `global` unless there’s a clear, justifiable reason.

---

### **Summary Table**

| Concept         | What Is It?                      | Example/Practice     | Good Practice               |
| --------------- | -------------------------------- | -------------------- | --------------------------- |
| Required Arg    | Must be provided                 | `def f(x): ...`      | Use for essential info      |
| Optional Arg    | Has default value                | `def f(x, y=0): ...` | Put after required args     |
| Return Value    | Data sent back to caller         | `return x + y`       | Always use if output needed |
| Multiple Return | Return several values as tuple   | `return x, y`        | Use for related data        |
| Local Scope     | Exists only inside the function  | `def f(): x = 1`     | Use for temporary values    |
| Global Scope    | Exists everywhere, use sparingly | `global x`           | Avoid modifying globally    |

---

### **Key Understandings for Beginners**

* Understand which arguments are required and which are optional.
* Use `return` to get data out of your function.
* Know the difference between local and global variables.
* Favor local variables and return values for safer, more modular code.
