### **III. Dictionary Operations**

#### **1. Creating a Dictionary**

A dictionary can be created using curly braces `{}` or the `dict()` constructor.

```python
# Using curly braces
student = {'name': 'John', 'age': 20, 'courses': ['Math', 'CompSci']}
print(student)

# Using dict() constructor
employee = dict(name='Jane', department='HR', salary=50000)
print(employee)
```

#### **2. Accessing Values**

Retrieve values using keys. If the key doesn’t exist, using `[]` raises an error, but `.get()` returns `None` (or a default value if provided).

```python
print(student['name'])      # Output: John
print(student.get('age'))   # Output: 20
print(student.get('grade')) # Output: None (no error)
print(student.get('grade', 'Not Assigned')) # Output: Not Assigned
```

##### **Tip:**

Use `.get()` to avoid errors when a key might not exist.

#### **3. Adding/Updating Values**

Add a new key-value pair or update an existing key by assignment.

```python
student['phone'] = '555-1234'   # Adds a new key-value pair
student['age'] = 21             # Updates the value for 'age'
print(student)
```

**Bulk update:**
You can update multiple values at once with `.update()`:

```python
student.update({'name': 'Jonathan', 'age': 22, 'email': 'jon@example.com'})
print(student)
```

#### **4. Removing Items**

Remove a key-value pair using `del`, `.pop()`, or `.popitem()`:

```python
del student['age']                     # Removes 'age'
phone = student.pop('phone')           # Removes 'phone' and returns its value
print(student)

# Remove and return the last inserted key-value pair (Python 3.7+)
last_item = student.popitem()
print(last_item)
```

**Clear all items:**

```python
student.clear()
print(student)  # Output: {}
```

#### **5. Dictionary Methods**

Some useful dictionary methods and ways to work with them:

* **Keys:** Get a view of all keys

  ```python
  print(student.keys())     # dict_keys(['name', 'courses'])
  ```
* **Values:** Get a view of all values

  ```python
  print(student.values())   # dict_values(['John', ['Math', 'CompSci']])
  ```
* **Items:** Get a view of key-value pairs (tuples)

  ```python
  print(student.items())    # dict_items([('name', 'John'), ('courses', ['Math', 'CompSci'])])
  ```

**Iterating through a dictionary:**

```python
for key in student:
    print(key, student[key])

for key, value in student.items():
    print(key, value)
```

**Checking if a key exists:**

```python
if 'name' in student:
    print('Name found!')
```

#### **6. Example: Counting Words**

A common use case for dictionaries is to count occurrences:

```python
sentence = "this is a test this is only a test"
word_count = {}
for word in sentence.split():
    word_count[word] = word_count.get(word, 0) + 1
print(word_count)
# Output: {'this': 2, 'is': 2, 'a': 2, 'test': 2, 'only': 1}
```

#### **7. More Examples and Useful Functions**

**a. Dictionary Comprehensions**

Quickly create a dictionary from a sequence:

```python
# Squares of numbers 1-5
squares = {x: x*x for x in range(1, 6)}
print(squares)  # Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
```

**b. Merging Dictionaries**

Combine two dictionaries (Python 3.5+):

```python
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
merged = {**dict1, **dict2}
print(merged)  # Output: {'a': 1, 'b': 3, 'c': 4}
```

**c. Using Default Values with defaultdict**

The `collections` module has a helpful `defaultdict` for auto-initializing values:

```python
from collections import defaultdict

word_count = defaultdict(int)
for word in sentence.split():
    word_count[word] += 1
print(dict(word_count))
```

---

### **Real World Examples**

* **Contacts/Phone Book:**
  Store contact names as keys, and phone numbers or info as values.

  ```python
  contacts = {
      'Alice': {'phone': '123-4567', 'email': 'alice@mail.com'},
      'Bob': {'phone': '987-6543'}
  }
  ```

* **Inventory Management:**
  Keep track of product names/IDs and their stock.

  ```python
  inventory = {'apples': 30, 'bananas': 12, 'oranges': 7}
  ```

* **Student Grades:**
  Map students to their list of grades.

  ```python
  grades = {'Alice': [90, 85], 'Bob': [78, 80]}
  ```

* **Configuration Settings:**
  Store application settings, such as theme, language, etc.

  ```python
  settings = {'theme': 'dark', 'language': 'en'}
  ```

* **Counting Occurrences:**
  Like the word count example above, this can be used for counting anything—votes, reactions, etc.

---

### **Summary Table: Useful Dictionary Methods**

| Method              | Description                                            | Example                        |
| ------------------- | ------------------------------------------------------ | ------------------------------ |
| `dict.get(key)`     | Returns value for key or None/default                  | `my_dict.get('a', 0)`          |
| `dict.update(...)`  | Updates dictionary with another dict or key-values     | `my_dict.update({'a': 10})`    |
| `dict.pop(key)`     | Removes specified key and returns value                | `my_dict.pop('a')`             |
| `dict.clear()`      | Removes all items                                      | `my_dict.clear()`              |
| `dict.keys()`       | Returns view of all keys                               | `my_dict.keys()`               |
| `dict.values()`     | Returns view of all values                             | `my_dict.values()`             |
| `dict.items()`      | Returns view of all key-value pairs                    | `my_dict.items()`              |
| `dict.setdefault()` | Returns value if key exists, else sets and returns new | `my_dict.setdefault('a', 100)` |
| `dict.fromkeys()`   | Creates dict from sequence of keys with given value    | `dict.fromkeys(['a', 'b'], 0)` |

---

**Quick Challenges:**

1. Create a dictionary of three movies and their release years. Print all the movie names.
2. Write a program to count the number of times each letter appears in a word (hint: use a dictionary).
3. Given two dictionaries of student marks, merge them so that the second dictionary’s data overwrites any duplicates.

