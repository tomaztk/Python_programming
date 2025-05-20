## III. Python Basics: Language, History, PEP Standards, and Indentation

---

### 1. **Python: A Quick Overview**

* **Python** is a high-level, interpreted programming language.
* Known for **readability**, **simplicity**, and a huge supportive community.
* Widely used for web development, automation, data science, AI, education, scripting, and more.

---

### 2. **A Brief History of Python**

* **Creator:** Guido van Rossum, Netherlands.
* **First released:** 1991 (Python 0.9.0).
* **Name origin:** Named after the TV show “Monty Python’s Flying Circus,” not the snake!
* **Philosophy:** "There should be one—and preferably only one—obvious way to do it."

**Major Versions:**

* **Python 2:** Introduced in 2000, legacy now.
* **Python 3:** Launched in 2008, is the standard (not backward-compatible with Python 2).
* **Current versions:** Always recommend using the latest Python 3.x.

**Fun fact:** Python is now maintained by the Python Software Foundation.

---

### 3. **Python’s Design Principles**

* Emphasizes **clarity and readability** ("beautiful is better than ugly").
* Code is meant to be easy for humans to read, not just computers.
* Encourages using whitespace and indentation for structure, unlike many other languages.

**Zen of Python (Easter Egg!):**
Type `import this` in Python interpreter to see guiding aphorisms.

**Example Output:**

```
>>> import this
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
```

---

### 4. **PEP: Python Enhancement Proposals**

* **PEP** stands for **Python Enhancement Proposal**.
* Documents that propose features, design, style guidelines, and improvements.
* **PEP 8:** The official style guide for writing Python code.
* **PEP 20:** The Zen of Python (see above).

**Why follow PEP 8?**

* Keeps code consistent, readable, and maintainable.
* Encourages good habits from the start.

**Key PEP 8 Rules (with examples):**

| Bad Practice        | Good Practice              |
| ------------------- | -------------------------- |
| `x=10`              | `x = 10`                   |
| `def myFunction():` | `def my_function():`       |
| `if(x>0): print(x)` | `if x > 0:\n    print(x)`  |
| 80+ character lines | Wrap lines before 80 chars |

**Example:**

```python
# PEP 8 compliant
def calculate_sum(a, b):
    return a + b
```

---

### 5. **Indentation: Python’s Structure**

* **Indentation replaces curly braces or keywords (like “end”)** used in other languages.
* Blocks of code are defined by **consistent indentation** (default: 4 spaces).
* **Mixing spaces and tabs is discouraged** (use spaces).

**Why is this important?**

* Python will throw an `IndentationError` if code is not properly indented.

**Example:**

```python
# Correct
if 10 > 2:
    print("10 is greater than 2")
    print("This is inside the if block.")

print("This is outside the if block.")

# Incorrect (will raise error)
if 10 > 2:
print("10 is greater than 2")  # IndentationError!
```

**Best Practice:**

* Use **4 spaces** for each level of indentation (can be set in your IDE settings).

---

### 6. **Quick Comparison: Indentation vs. Other Languages**

**JavaScript Example:**

```javascript
if (x > 0) {
    console.log(x);
}
```

**Python Example:**

```python
if x > 0:
    print(x)
```

**Notice:** No `{}` in Python—just indentation.

---

### 7. **Quick Activity for Students**

* **Try in your IDE:**

  1. Remove the indentation in a code block and observe the error.
  2. Re-indent and see it work.

---

### 8. **Summary Table**

| Concept       | Python Example                     | Notes                       |
| ------------- | ---------------------------------- | --------------------------- |
| Variable Name | `snake_case` (e.g., `my_variable`) | Lowercase with underscores  |
| Indentation   | `if x > 0:\n    print(x)`          | 4 spaces per block          |
| Line Length   | `# Keep lines < 80 chars`          | Improves readability        |
| Comments      | `# This is a comment`              | Use `#` for inline comments |

---


## **Python’s Global Community**

* Python is open source and globally supported.
* **Official docs:** [docs.python.org](https://docs.python.org/3/)
* Many conferences: PyCon, EuroPython, etc.

---


