## **IV. Tuple Operators and Operations**

---

### **A. Tuple Operators**

#### **1. Concatenation (`+`)**

* You can join two or more tuples using the `+` operator.
* The result is a new tuple containing the elements of both.

```python
a = (1, 2, 3)
b = (4, 5)
c = a + b
print(c)  # Output: (1, 2, 3, 4, 5)
```

#### **2. Repetition (`*`)**

* You can repeat a tuple multiple times using the `*` operator.

```python
numbers = (0, 1)
result = numbers * 3
print(result)  # Output: (0, 1, 0, 1, 0, 1)
```

#### **3. Membership (`in`, `not in`)**

* Check if an item is in a tuple with `in`, or not in a tuple with `not in`.

```python
colors = ('red', 'green', 'blue')
print('green' in colors)      # True
print('yellow' not in colors) # True
```

#### **4. Comparison Operators**

* Tuples can be compared using `<`, `<=`, `>`, `>=`, `==`, `!=`.
* Python compares element by element (left to right):

```python
a = (1, 2, 3)
b = (1, 2, 4)
print(a < b)   # True, because 3 < 4
```

---

### **B. Tuple Operations (Methods)**

Tuples have only two built-in methods because they are immutable:

#### **1. `count(x)`**

* Returns the number of times `x` appears in the tuple.

```python
t = (1, 2, 2, 3, 2)
print(t.count(2))  # Output: 3
```

#### **2. `index(x)`**

* Returns the first index at which `x` appears.
* Raises a `ValueError` if `x` is not found.

```python
t = ('a', 'b', 'c', 'b')
print(t.index('b'))  # Output: 1
# print(t.index('z'))  # ValueError: tuple.index(x): x not in tuple
```

---

### **C. Built-in Functions Useful with Tuples**

* **`len()`** — Number of elements

  ```python
  tup = (1, 2, 3, 4)
  print(len(tup))  # 4
  ```
* **`min()` / `max()`** — Smallest / largest item

  ```python
  tup = (10, 5, 20)
  print(min(tup))  # 5
  print(max(tup))  # 20
  ```
* **`sum()`** — Sum all elements (only for numbers)

  ```python
  tup = (1, 2, 3)
  print(sum(tup))  # 6
  ```
* **`sorted()`** — Returns a sorted **list** (does not change the tuple!)

  ```python
  tup = (3, 1, 2)
  sorted_tup = sorted(tup)
  print(sorted_tup)  # [1, 2, 3]
  ```
* **`tuple()`** — Converts a list (or any iterable) to a tuple

  ```python
  numbers = [1, 2, 3]
  t = tuple(numbers)
  print(t)  # (1, 2, 3)
  ```

---

### **D. Iterating Over Tuples**

* **For Loop:**

  ```python
  fruits = ('apple', 'banana', 'cherry')
  for fruit in fruits:
      print(fruit)
  ```
* **With Index:**

  ```python
  for i in range(len(fruits)):
      print(f"Index {i}: {fruits[i]}")
  ```
* **Unpacking in Loops (useful for tuples of pairs):**

  ```python
  points = ((1, 2), (3, 4), (5, 6))
  for x, y in points:
      print(f"x={x}, y={y}")
  ```

---

### **E. Tuple Packing and Unpacking**

* **Packing:**
  Grouping values into a tuple, often done implicitly:

  ```python
  t = 1, 2, 3  # Packing
  ```
* **Unpacking:**

  ```python
  a, b, c = t
  print(a, b, c)  # 1 2 3
  ```

---

### **F. Slicing Tuples**

* Just like lists, you can use slicing:

  ```python
  tup = (0, 1, 2, 3, 4, 5)
  print(tup[2:5])  # (2, 3, 4)
  print(tup[:3])   # (0, 1, 2)
  print(tup[-2:])  # (4, 5)
  ```

---

### **G. Practical Demos**

**Demo 1:**
Create two tuples, concatenate and repeat them.

```python
a = ('x', 'y')
b = ('z',)
combo = a + b
print(combo * 2)   # ('x', 'y', 'z', 'x', 'y', 'z')
```

**Demo 2:**
Check for existence of number 2 in tuple: (1, 2, 2, 3, 4, 2) and count occurrences of number 2.

```python
nums = (1, 2, 2, 3, 4, 2)
print(2 in nums)          # True
print(nums.count(2))      # 3
print(nums.index(3))      # 3
```

**Demo 3:**
Create a tuple and sort it (returns a list).

```python
t = (5, 2, 7, 1)
print(sorted(t))          # [1, 2, 5, 7]
```

**Demo 4:**
Tuple unpacking with function return.

```python
def stats(values):
    return (min(values), max(values), sum(values))

min_v, max_v, total = stats((4, 7, 2, 9))
print(min_v, max_v, total)  # 2 9 22
```

---

### **H. Quick Practice Questions**

1. Create a tuple of 5 colors. Print the first three using slicing.
2. Check if 'blue' is in your tuple.
3. Count how many times 'red' appears.
4. Concatenate your color tuple with another tuple of 2 colors.
5. Use unpacking to assign the first two colors to variables and print them.

---

**Keep Coding!**
