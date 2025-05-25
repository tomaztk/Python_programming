--outline

## **LESSON 6: PYTHON DATA STRUCTURES - PART 2 (DICTIONARIES AND SETS)**

**Duration:** 2 hours

### **A. Recap: Previous Lesson (5-10 min)**

* **Brief review of lists and tuples:**

  * **Lists**: Mutable, ordered collections of items (`[1, 2, 3]`).
  * **Tuples**: Immutable, ordered collections (`(1, 2, 3)`).
* **Common operations**: Indexing, slicing, adding/removing items, iterating.

---

### **B. Introduction to Dictionaries and Sets (10 min)**

#### **What is a Dictionary?**

* A **dictionary** is an unordered, mutable collection of key-value pairs.
* **Syntax:**

  ```python
  my_dict = {'name': 'Alice', 'age': 25}
  ```

#### **What is a Set?**

* A **set** is an unordered collection of unique elements.
* **Syntax:**

  ```python
  my_set = {1, 2, 3}
  ```

**Why use them?**

* **Dictionaries**: Great for storing data with a unique identifier (like names, IDs).
* **Sets**: Useful for membership tests, removing duplicates.

---

### **C. Dictionary Operations (40 min)**

#### **1. Creating a Dictionary**

```python
student = {'name': 'John', 'age': 20, 'courses': ['Math', 'CompSci']}
```

#### **2. Accessing Values**

```python
print(student['name'])      # Output: John
print(student.get('age'))   # Output: 20
print(student.get('grade')) # Output: None (no error)
```

#### **3. Adding/Updating Values**

```python
student['phone'] = '555-1234'   # Adds a new key-value pair
student['age'] = 21             # Updates existing value
print(student)
```

#### **4. Removing Items**

```python
del student['age']
phone = student.pop('phone')
print(student)
```

#### **5. Dictionary Methods**

* **Keys:** `student.keys()`
* **Values:** `student.values()`
* **Items:** `student.items()`
* **Iterate:**

  ```python
  for key, value in student.items():
      print(key, value)
  ```

#### **6. Example: Counting Words**

```python
sentence = "this is a test this is only a test"
word_count = {}
for word in sentence.split():
    word_count[word] = word_count.get(word, 0) + 1
print(word_count)
```

---

### **D. Introduction to Sets (20 min)**

#### **1. Creating Sets**

```python
nums = {1, 2, 3, 4}
nums2 = set([3, 4, 5, 6])
print(nums, nums2)
```

#### **2. Adding/Removing Elements**

```python
nums.add(5)
nums.remove(1)
print(nums)
```

#### **3. Set Operations**

* **Union:** `nums | nums2` or `nums.union(nums2)`
* **Intersection:** `nums & nums2` or `nums.intersection(nums2)`
* **Difference:** `nums - nums2` or `nums.difference(nums2)`
* **Membership test:** `3 in nums` returns `True` if 3 is in the set.

#### **4. Example: Removing Duplicates**

```python
items = [1, 2, 2, 3, 4, 4, 5]
unique_items = set(items)
print(unique_items)  # Output: {1, 2, 3, 4, 5}
```

---

### **E. Hands-on Practice (30 min)**

#### **Exercise 1: Store and Retrieve Data Using a Dictionary**

```python
person = {}
person['name'] = input("Enter your name: ")
person['age'] = input("Enter your age: ")
print(f"Hello {person['name']}, you are {person['age']} years old.")
```

#### **Exercise 2: Use a Set to Check for Duplicates**

```python
nums = [int(x) for x in input("Enter numbers separated by space: ").split()]
if len(nums) != len(set(nums)):
    print("There are duplicates!")
else:
    print("All numbers are unique.")
```

#### **Exercise 3: Iterating Over a Dictionary**

```python
grades = {'Alice': 85, 'Bob': 90, 'Charlie': 78}
for name, grade in grades.items():
    print(f"{name}: {grade}")
```

---

### **F. Homework Assignment (End of Class)**

**Build a Contact Book using dictionaries.**

* Users can add, update, or search for contacts.
* **Sample requirements:**

  * Store each contact’s name as the key, value as another dictionary with phone/email.
  * Provide options to add, update, or search for a contact.

**Example Starter Code:**

```python
contacts = {}

while True:
    print("\nContact Book")
    print("1. Add Contact")
    print("2. Update Contact")
    print("3. Search Contact")
    print("4. Exit")
    choice = input("Choose an option: ")
    
    if choice == '1':
        name = input("Enter name: ")
        phone = input("Enter phone: ")
        email = input("Enter email: ")
        contacts[name] = {'phone': phone, 'email': email}
        print("Contact added.")
    elif choice == '2':
        name = input("Enter name to update: ")
        if name in contacts:
            phone = input("Enter new phone: ")
            email = input("Enter new email: ")
            contacts[name] = {'phone': phone, 'email': email}
            print("Contact updated.")
        else:
            print("Contact not found.")
    elif choice == '3':
        name = input("Enter name to search: ")
        if name in contacts:
            print(f"Name: {name}")
            print(f"Phone: {contacts[name]['phone']}")
            print(f"Email: {contacts[name]['email']}")
        else:
            print("Contact not found.")
    elif choice == '4':
        break
    else:
        print("Invalid option.")
```


