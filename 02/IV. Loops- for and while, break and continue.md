
## IV. Loops: for and while, break and continue

---

### **A. For Loops**

#### **What is a `for` loop?**

A `for` loop repeats code for each item in a sequence (such as a list, tuple, string, or range).

#### **Basic Structure:**

```python
for variable in sequence:
    # code block
```

#### **Examples:**

**Iterate over a list:**

```python
fruits = ['apple', 'banana', 'cherry']
for fruit in fruits:
    print(fruit)
# Output:
# apple
# banana
# cherry
```

**Iterate over a string:**

```python
for char in "Python":
    print(char)
# Output:
# P y t h o n (one per line)
```

**Use `range()` for counting:**

```python
for i in range(1, 6):
    print(i)
# Output: 1 2 3 4 5
```

**Iterate with both index and value using `enumerate()`:**

```python
colors = ['red', 'green', 'blue']
for idx, color in enumerate(colors):
    print(idx, color)
```

---

#### **Correct Usage:**

* Looping over any iterable (list, tuple, set, dictionary, string, etc.)

#### **Incorrect Usage:**

* Trying to loop over something that isn’t iterable:

  ```python
  # INCORRECT:
  for x in 5:
      print(x)  # TypeError: 'int' object is not iterable
  ```

* Forgetting the colon or indentation:

  ```python
  # INCORRECT:
  for fruit in fruits
      print(fruit)  # SyntaxError
  ```

* Modifying a list while iterating over it (can lead to skipped items or errors):

  ```python
  mylist = [1, 2, 3]
  for item in mylist:
      if item == 2:
          mylist.remove(item)
  # List modification during iteration is unsafe.
  ```

#### **Other Sequence Types:**

* **Dictionaries:**
  Looping through keys, values, or both:

  ```python
  mydict = {'a': 1, 'b': 2}
  for key in mydict:
      print(key, mydict[key])
  for value in mydict.values():
      print(value)
  for key, value in mydict.items():
      print(key, value)
  ```

---

### **B. While Loops**

#### **What is a `while` loop?**

Repeats code **as long as** a condition is `True`.
Great for situations when you don't know ahead of time how many times to repeat.

#### **Basic Structure:**

```python
while condition:
    # code block
```

#### **Examples:**

**Count up to 5:**

```python
count = 1
while count <= 5:
    print(count)
    count += 1
# Output: 1 2 3 4 5
```

**User input until they guess the correct answer:**

```python
secret = 7
guess = None
while guess != secret:
    guess = int(input("Guess the number: "))
print("You got it!")
```

---

#### **Correct Usage:**

* When the number of iterations isn't known beforehand.

#### **Incorrect Usage:**

* **Forgetting to update the condition variable (infinite loop):**

  ```python
  # INCORRECT:
  i = 0
  while i < 3:
      print(i)
  # This will loop forever because i is never incremented!
  ```

* **Infinite loop without a break:**

  ```python
  while True:
      print("Runs forever")  # Must have a break condition inside!
  ```

---

#### **Common Mistakes with `while`:**

* Using assignment `=` instead of comparison `==`:

  ```python
  # INCORRECT:
  while i = 5:
      print(i)  # SyntaxError
  ```
* Not initializing loop variables.

---

### **C. `break` and `continue`**

#### **break:**

Immediately stops the nearest enclosing loop.

**Example:**

```python
for i in range(10):
    if i == 5:
        break
    print(i)
# Output: 0 1 2 3 4
```

**While Loop Example:**

```python
while True:
    num = int(input("Enter a positive number (or -1 to quit): "))
    if num == -1:
        break
    print("You entered:", num)
```

---

#### **continue:**

Skips the rest of the code **inside the loop for that iteration** and moves to the next loop cycle.

**Example:**

```python
for i in range(1, 6):
    if i % 2 == 0:
        continue  # Skip even numbers
    print(i)
# Output: 1 3 5
```

**While Loop Example:**

```python
count = 0
while count < 5:
    count += 1
    if count == 3:
        continue
    print(count)
# Output: 1 2 4 5 (skips 3)
```

---

#### **Correct Usage:**

* Use `break` to exit a loop early (e.g., searching for an item).
* Use `continue` to skip certain values (e.g., skipping over unwanted data).

#### **Incorrect Usage:**

* Using `break` or `continue` outside a loop:

  ```python
  # INCORRECT:
  if x == 5:
      break   # SyntaxError
  ```

---

### **Similar and Related Cases in Python Loops:**

#### **1. else with Loops**

* Python allows an `else` block **after loops**. The `else` part runs **only if the loop didn’t exit with a `break`**.

**Example:**

```python
for n in range(2, 10):
    if n % 7 == 0:
        print("Found number divisible by 7:", n)
        break
else:
    print("No number divisible by 7 found.")
# If no break, the else runs.
```

#### **2. Nested Loops**

* Loops inside other loops, e.g., to print tables or work with multidimensional data.

```python
for row in range(1, 4):
    for col in range(1, 4):
        print(row, col)
```

#### **3. Looping Over Multiple Sequences (zip):**

```python
names = ["Alice", "Bob"]
scores = [85, 90]
for name, score in zip(names, scores):
    print(name, score)
```

#### **4. List Comprehensions (advanced preview):**

* A more "Pythonic" way to loop and build lists.

```python
squares = [x**2 for x in range(1, 6)]
print(squares)  # [1, 4, 9, 16, 25]
```

---

### **Common Pitfalls and Corrections:**

* **Infinite loops:**

  * Not updating the loop variable or using a `while True:` without a break.
* **Off-by-one errors:**

  * Be careful with `range()`—it’s exclusive at the stop value.
* **Changing a list while iterating over it:**

  * Can result in skipping items or unexpected behavior.
  * Instead, loop over a copy:
    `for item in mylist[:]: ...`

---

### **Let's do some coding:**

1. **For Loop:** Print all even numbers between 1 and 20.
2. **While Loop:** Ask the user to enter numbers until they type 0. Output the sum.
3. **break:** Loop through a list of names, stop if you find "Alice".
4. **continue:** Loop through numbers 1 to 10, print all except multiples of 3.
5. **Nested Loops:** Print a multiplication table (1–5).

---

### **Summary Table**

| Statement    | Usage Example                | Notes/Corrections               |
| ------------ | ---------------------------- | ------------------------------- |
| for          | `for x in [1,2,3]: print(x)` | Loop over any iterable          |
| while        | `while x < 10: x += 1`       | Update loop variable!           |
| break        | `if found: break`            | Exits loop immediately          |
| continue     | `if not ok: continue`        | Skips rest of current iteration |
| else (loops) | `for ... else:`              | Runs if no break occurred       |


