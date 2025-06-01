## **LESSON 6: PYTHON DATA STRUCTURES - PART 2 (DICTIONARIES AND SETS)**

## II. Introduction to Dictionaries and Sets

### What is a Dictionary?

A **dictionary** in Python is an **unordered**, **mutable** collection of key-value pairs. Each key in a dictionary must be unique and immutable (like strings, numbers, or tuples), and is used to store and retrieve values efficiently.

#### Syntax:

```python
my_dict = {'name': 'Alice', 'age': 25}
```

* Here, `'name'` and `'age'` are **keys**.
* `'Alice'` and `25` are their corresponding **values**.

#### Accessing Values:

You can access a value by referencing its key:

```python
print(my_dict['name'])   # Output: Alice
```

#### Adding or Updating Entries:

```python
my_dict['email'] = 'alice@example.com'  # Adds a new key-value pair
my_dict['age'] = 26                     # Updates existing key
```

#### Removing Entries:

```python
del my_dict['age']                      # Removes the key 'age'
```

#### Useful Methods:

* `my_dict.keys()` returns all keys.
* `my_dict.values()` returns all values.
* `my_dict.items()` returns all key-value pairs.

#### Example Scenario:

* **Student Grades:** Store student names as keys and their grades as values.

  ```python
  grades = {'Alice': 95, 'Bob': 88, 'Charlie': 72}
  print(grades['Bob'])  # Output: 88
  ```
* **Phone Book:** Map names to phone numbers.

  ```python
  phone_book = {'John': '555-1234', 'Jane': '555-5678'}
  ```
* **Counting Occurrences:** Count how many times each word appears in a sentence.

---

### What is a Set?

A **set** is an **unordered** collection of **unique** elements. Sets are mutable, but elements must be immutable.

#### Syntax:

```python
my_set = {1, 2, 3}
```

* Duplicates are automatically removed.

  ```python
  s = {1, 2, 2, 3}
  print(s)  # Output: {1, 2, 3}
  ```

#### Adding Elements:

```python
my_set.add(4)    # Adds 4 to the set
```

#### Removing Elements:

```python
my_set.remove(2) # Removes 2 from the set (raises error if 2 not present)
my_set.discard(5) # Removes 5 if present, does nothing if not
```

#### Useful Methods:

* `my_set.union(other_set)` combines two sets.
* `my_set.intersection(other_set)` finds common elements.
* `my_set.difference(other_set)` finds elements in one set but not the other.

#### Example Scenario:

* **Removing Duplicates:** Turn a list into a set to remove duplicates.

  ```python
  numbers = [1, 2, 2, 3, 4, 4]
  unique_numbers = set(numbers)
  print(unique_numbers)  # Output: {1, 2, 3, 4}
  ```
* **Membership Testing:** Quickly check if an item exists.

  ```python
  vowels = {'a', 'e', 'i', 'o', 'u'}
  print('e' in vowels)  # Output: True
  ```
* **Finding Shared Items:** Find common students in two classes.

  ```python
  class1 = {'Alice', 'Bob', 'Charlie'}
  class2 = {'Bob', 'David', 'Ella'}
  print(class1.intersection(class2))  # Output: {'Bob'}
  ```

---

### Why use them?

* **Dictionaries:**
  Use dictionaries when you want to associate keys with values, such as mapping student names to their grades, usernames to passwords, or product IDs to product details. They allow for very fast lookups, additions, and deletions based on the key.

* **Sets:**
  Use sets for tasks that involve uniqueness and membership tests, such as removing duplicates from a list, checking if a value exists, or finding common or unique items between two groups.

---

**Summary Table:**

| Structure  | Order     | Mutable | Unique Elements | Key-Value Pair | Main Use Case                    |
| ---------- | --------- | ------- | --------------- | -------------- | -------------------------------- |
| Dictionary | Unordered | Yes     | Keys are unique | Yes            | Fast lookup by key, data mapping |
| Set        | Unordered | Yes     | Yes             | No             | Uniqueness, membership tests     |

---

**Quick Challenge:**

* Create a dictionary of three countries and their capitals.
* Create a set of five numbers, with at least two repeated, and print the set.

