## **IV. Advanced Functions: Decorators, Anonymous, and Lambda Functions**

---

### **1. Decorators**

#### **What Are Decorators?**

* **Explanation:**
  Decorators are special functions in Python that "wrap" or modify the behavior of other functions without changing their actual code.
* **Why Use Them?**
  They help you add common functionality—like logging, access control, or timing—easily and cleanly.
* **Beginner Analogy:**
  Think of a decorator like a phone case: the phone works the same, but the case adds extra features (like protection or color) without changing the phone itself.

#### **Basic Syntax**

* A decorator is applied to a function using the `@decorator_name` syntax, just above the function definition.
* **Example:**

  ```python
  def simple_decorator(func):
      def wrapper():
          print("Before function runs")
          func()
          print("After function runs")
      return wrapper

  @simple_decorator
  def say_hello():
      print("Hello!")

  say_hello()
  # Output:
  # Before function runs
  # Hello!
  # After function runs
  ```

#### **Common Use-Cases**

* **Logging:** Recording when a function runs.
* **Timing:** Measuring how long a function takes to run.
* **Access Control:** Checking permissions before running a function.

#### **Good Practices**

* Use decorators to avoid repeating code (DRY principle).
* Always use `functools.wraps` if you want to preserve the decorated function’s name and docstring (more advanced, but good to mention).
* Don’t overuse decorators—keep code readable.

---

### **2. Anonymous/Lambda Functions**

#### **What Are Lambda Functions?**

* **Explanation:**
  A lambda function is a small, anonymous function (i.e., it has no name). Used for short, simple operations, often passed as arguments to other functions.
* **Syntax:**

  ```python
  lambda arguments: expression
  ```

#### **Where to Use Them**

* When you need a short function for a short period—usually as an argument to functions like `map()`, `filter()`, or `sorted()`.

#### **Examples**

**A. Simple Lambda Example**

```python
add = lambda x, y: x + y
print(add(2, 3))  # Output: 5
```

**B. Using Lambda with `sorted()`**

```python
names = ['Anna', 'John', 'Mike']
# Sort by the last letter
sorted_names = sorted(names, key=lambda name: name[-1])
print(sorted_names)  # Output: ['Anna', 'Mike', 'John']
```

**C. Using Lambda with `filter()`**

```python
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # Output: [2, 4, 6]
```

#### **Good Practices**

* Use lambda functions for simple, one-line tasks.
* If the function gets complex, use a `def` instead for readability.
* Name lambda functions only if you must reuse them; otherwise, use them inline.

---

### **Summary Table**

| Concept   | What Is It?                         | Example         | Good Practice                          |
| --------- | ----------------------------------- | --------------- | -------------------------------------- |
| Decorator | Wraps/modifies another function     | `@my_decorator` | Use for code reuse, keep them readable |
| Lambda    | Small, anonymous, one-line function | `lambda x: x*2` | Use for simple, short-lived operations |

---

### **Key Takeaways for Beginners**

* **Decorators:** Allow you to add extra features to your functions with clean syntax.
* **Lambda Functions:** Handy for quick, throwaway functions, especially as arguments.
* **Best Practice:** Use both features to write more modular, concise, and readable code—but don’t sacrifice clarity for cleverness!
