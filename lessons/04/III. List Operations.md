## **III. List Operations**

---

### **1. Indexing & Slicing**

#### **A. Indexing**

* **What is Indexing?**

  * Each item in a list has a position, called an *index*. Indexes start at 0 (zero-based).
  * You can use positive or negative numbers.

    * **Positive:** Start from left (`0, 1, 2, ...`)
    * **Negative:** Start from right (`-1, -2, ...`)

**Example:**

```python
fruits = ['apple', 'banana', 'cherry', 'date']

print(fruits[0])    # 'apple'  (first element)
print(fruits[2])    # 'cherry' (third element)
print(fruits[-1])   # 'date'   (last element)
print(fruits[-2])   # 'cherry' (second last)
```

* **Usage Demo:**

  * Ask students to create a list of their favorite colors, then print the first and last color.

---

#### **B. Slicing**

* **What is Slicing?**

  * Slicing lets you extract a *portion* (sublist) from a list using `list[start:stop]`.
  * The slice includes the `start` index, but **not** the `stop` index (`stop` is excluded).

**Syntax:**

```python
list[start:stop]
```

**Examples:**

```python
numbers = [0, 1, 2, 3, 4, 5, 6]

print(numbers[1:4])   # [1, 2, 3]
print(numbers[:3])    # [0, 1, 2]
print(numbers[3:])    # [3, 4, 5, 6]
print(numbers[-3:])   # [4, 5, 6] (last three items)
```

* **Usage Demo:**

  * Given a list of 7 days, print the weekdays only (slice out the first 5 days).

---

### **2. Modifying Lists**

#### **A. Changing Values**

* **Modify an existing element by index:**

```python
fruits = ['apple', 'banana', 'cherry']
fruits[1] = 'blueberry'
print(fruits)   # ['apple', 'blueberry', 'cherry']
```

* **Demo:**

  * Students change their favorite animal in a list from "cat" to "lion".

---

#### **B. Adding Elements**

* **append():** Adds to the end.
* **insert():** Adds at a specific position.

```python
fruits = ['apple', 'banana']
fruits.append('orange')
print(fruits)   # ['apple', 'banana', 'orange']

fruits.insert(1, 'kiwi')  # Insert at index 1
print(fruits)   # ['apple', 'kiwi', 'banana', 'orange']
```

* **Demo:**

  * Students add a new favorite movie to their list.

---

#### **C. Removing Elements**

* **remove(value):** Removes first occurrence of value.
* **del list\[index]:** Deletes by index.
* **pop():** Removes and returns the last item (can take an index).

```python
fruits = ['apple', 'banana', 'cherry', 'banana']

fruits.remove('banana')  # Removes the first 'banana'
print(fruits)   # ['apple', 'cherry', 'banana']

del fruits[1]   # Deletes at index 1 ('cherry')
print(fruits)   # ['apple', 'banana']

last = fruits.pop()  # Removes last element and returns it
print(last)     # 'banana'
print(fruits)   # ['apple']
```

* **Demo:**

  * Students remove a disliked subject from their list of subjects.

---

#### **D. Other Useful Operations**

* **Length of a list:**

```python
colors = ['red', 'blue', 'green']
print(len(colors))   # 3
```

* **Check if an item exists:**

```python
if 'blue' in colors:
    print('Blue is in the list!')
```

* **Concatenate two lists:**

```python
list1 = [1, 2, 3]
list2 = [4, 5]
combined = list1 + list2
print(combined)      # [1, 2, 3, 4, 5]
```

* **Repeat a list:**

```python
repeat = [0] * 5
print(repeat)        # [0, 0, 0, 0, 0]
```

---

### **3. Iterating Over Lists**

#### **A. For Loop (Most Common Way)**

* **Go through each element:**

```python
fruits = ['apple', 'banana', 'cherry']
for fruit in fruits:
    print(fruit)
```

* **Demo:**

  * Ask students to print every item in their "to-do" list.

#### **B. While Loop (Alternative)**

* **Using indexes to loop:**

```python
i = 0
while i < len(fruits):
    print(fruits[i])
    i += 1
```

* **When to use?**

  * When you need access to the index, or want more control over the loop.

#### **C. Looping with Indexes (Enumerate)**

* **Get both index and value:**

```python
for i, fruit in enumerate(fruits):
    print(f"Index {i}: {fruit}")
```

---

### **Student Demos & Mini-Exercises**

**Try these in class:**

1. Create a list of 5 countries. Print the third one.
2. Add a new country, then remove the first one.
3. Slice and print the last two countries.
4. Loop through your list and print each country in uppercase.
5. Concatenate your list with a friend's list.

---

### **Summary Table**

| Operation     | Example Code               | Output / Explanation          |
| ------------- | -------------------------- | ----------------------------- |
| Indexing      | `fruits[1]`                | 'banana' (second item)        |
| Slicing       | `fruits[1:3]`              | \['banana', 'cherry']         |
| Change value  | `fruits[1] = 'kiwi'`       | Replaces 'banana' with 'kiwi' |
| Append        | `fruits.append('orange')`  | Adds 'orange' at the end      |
| Insert        | `fruits.insert(0, 'pear')` | Adds 'pear' at start          |
| Remove value  | `fruits.remove('apple')`   | Removes first 'apple'         |
| Delete index  | `del fruits[0]`            | Removes item at index 0       |
| Pop           | `fruits.pop()`             | Removes & returns last item   |
| Check in list | `'apple' in fruits`        | True if 'apple' exists        |
| Length        | `len(fruits)`              | Number of items in list       |
| Concatenate   | `list1 + list2`            | Joins two lists               |


