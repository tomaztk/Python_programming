## **LESSON 4: PYTHON DATA STRUCTURES - PART 1 (LISTS AND TUPLES)**



## **II. Introduction to Lists and Tuples (15–20 min)**

---

### **A. Why Do We Need Collections?**

* In many programs, we need to store multiple values—not just one.

  * Example: A list of student names, the temperatures for each day of a week, all items in a shopping cart.
* Instead of using many variables (`name1`, `name2`, `name3`...), we use a **collection**.
* Python provides several types of collections; today, we focus on **lists** and **tuples**.

---

### **B. What is a List?**

* **Definition**:
  A list is a collection of values/items stored in a single variable. Lists can hold items of any type—integers, strings, floats, even other lists.
* **Properties**:

  * **Ordered**: Items have a defined order. Each item has an index (starting from 0).
  * **Mutable (changeable)**: You can change, add, or remove items after the list is created.
  * **Allows duplicates**: The same value can appear more than once.
  * **Syntax**: Square brackets `[ ]`.

#### **Example:**

```python
# Creating a list of numbers
numbers = [10, 20, 30, 40]

# Creating a list of strings
fruits = ['apple', 'banana', 'cherry']

# A list can have mixed types
mixed = [1, "hello", 3.14, True]
```

* **Use cases**:

  * A student's test scores throughout the semester.
  * All user inputs in a game.
  * Shopping cart items in an online store.

---

### **C. What is a Tuple?**

* **Definition**:
  A tuple is a collection **very similar to a list**, but **immutable**—once created, its items cannot be changed, added, or removed.
* **Properties**:

  * **Ordered**: Like lists, each item has a fixed position (index).
  * **Immutable (unchangeable)**: You cannot modify the tuple after it is created.
  * **Allows duplicates**: Repeating values are fine.
  * **Syntax**: Parentheses `( )`.

#### **Declaring Tuples:**

```python
# Creating a tuple of numbers
coordinates = (3, 5)

# Tuple of strings
colors = ('red', 'green', 'blue')

# Single-value tuple (note the comma!)
one_value = (42,)

# Tuple without parentheses (not recommended, but possible)
data = 1, 2, 3  # This is a tuple!
```

#### **Immutability Example:**

```python
person = ('Alice', 30)
# person[0] = 'Bob'  # This will cause an error!
```

---

### **D. When to Use Lists vs Tuples?**

| Feature   | List                     | Tuple                          |
| --------- | ------------------------ | ------------------------------ |
| Syntax    | `[1, 2, 3]`              | `(1, 2, 3)`                    |
| Mutable   | Yes (can change items)   | No (cannot change items)       |
| Use Cases | Data that changes (cart) | Fixed data (coordinates, days) |
| Speed     | Slightly slower          | Slightly faster (read-only)    |
| Methods   | Many (append, remove, …) | Few (mainly count, index)      |

#### **Examples:**

* **Use a List when:**

  * You need to add/remove/change items
  * Example: Keeping track of scores as a game progresses
* **Use a Tuple when:**

  * The data must not change (protect it by making it immutable)
  * Example: (x, y) coordinates of a point, dates, RGB color values

---

### **E. Practical Examples and Why Tuples are Useful**

1. **Coordinates Example (Tuples):**

   * Coordinates in 2D/3D space should not change after they’re set.

   ```python
   point = (10, 20)
   # x, y = point  # tuple unpacking
   ```
2. **Function Returning Multiple Values (Tuple Packing/Unpacking):**

   ```python
   def min_max(nums):
       return (min(nums), max(nums))

   result = min_max([2, 8, 3, 5])
   print("Min:", result[0], "Max:", result[1])

   # Tuple unpacking
   min_val, max_val = min_max([2, 8, 3, 5])
   print("Min:", min_val, "Max:", max_val)
   ```
3. **Days of the Week (Tuple):**

   * Days never change, so we use a tuple.

   ```python
   days = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
   ```
4. **List Example (Changeable Data):**

   * Adding items to a shopping cart:

   ```python
   cart = ['apple', 'banana']
   cart.append('orange')
   cart[0] = 'grape'
   ```

---

### **F. Summary Table**

| Property | List        | Tuple       |
| -------- | ----------- | ----------- |
| Syntax   | `[ ]`       | `( )`       |
| Ordered  | Yes         | Yes         |
| Mutable  | Yes         | No          |
| Methods  | Many        | Few         |
| Use case | Changeable  | Fixed       |
| Example  | Scores list | Coordinates |

---

### **G. Discussion:**

* Why do you think Python has both lists and tuples?
* What would happen if you tried to change a tuple?

---

#### **Recap** 

> Use **lists** when you need to work with changeable sequences of items.
> Use **tuples** when you want to *protect* data from changes, or when returning multiple values from a function.

