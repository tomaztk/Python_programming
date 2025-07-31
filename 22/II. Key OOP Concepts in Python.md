## **II. Key OOP Concepts in Python**

---

### **A. Class**

A **class** is a **blueprint** or **template** for creating objects.
It defines:

* **What data** the objects will have (attributes)
* **What actions** the objects can perform (methods)

Think of a **class** like an **architect’s blueprint** for a house:

* It describes the structure (rooms, walls, doors).
* But the blueprint itself is **not** a house — you must **create instances** (real houses) from it.

**Example:**

```python
class Dog:
    pass  # Empty class for now

print(type(Dog))  # <class 'type'>
```

Here:

* `Dog` is a **class**.
* No attributes or methods are defined yet.

---

### **B. Object**

An **object** is an **instance** of a class.
It is **created** from the class blueprint and has **its own copy of the attributes** defined by the class.

**Example:**

```python
class Dog:
    pass

dog1 = Dog()  # Create first object
dog2 = Dog()  # Create second object

print(dog1)  # <__main__.Dog object>
print(dog2)  # <__main__.Dog object>
```

* `dog1` and `dog2` are **different objects** created from the same `Dog` class.
* They are independent — changing one doesn’t affect the other.

---

### **C. Attributes**

**Attributes** are **variables that belong to an object**.
They store **information** about that specific object.

We define attributes inside the **constructor** (`__init__` method).

**Example:**

```python
class Dog:
    def __init__(self, name, age):
        self.name = name  # Instance attribute
        self.age = age

dog1 = Dog("Buddy", 3)
dog2 = Dog("Max", 5)

print(dog1.name)  # Buddy
print(dog2.age)   # 5
```

Here:

* `self.name` and `self.age` are **attributes**.
* `dog1` and `dog2` have **their own values** for these attributes.

---

### **D. Methods**

**Methods** are **functions inside a class** that describe **what the object can do**.
They always take **`self`** as the first parameter (which refers to the **current object**).

**Example:**

```python
class Dog:
    def __init__(self, name):
        self.name = name
    
    def bark(self):  # Method
        print(f"{self.name} says Woof!")

dog1 = Dog("Buddy")
dog2 = Dog("Max")

dog1.bark()  # Buddy says Woof!
dog2.bark()  # Max says Woof!
```

* `bark()` is a **method**.
* It works differently for each dog because it uses that object's `self.name`.

---

### **E. Constructor (`__init__` Method)**

The **constructor** is a **special method** named `__init__` that runs **automatically** when you create an object.

It’s used to:

* Initialize the object’s attributes
* Set up default values if none are provided

**Example:**

```python
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

car1 = Car("Toyota", "Corolla")
car2 = Car("Honda", "Civic")

print(car1.brand)  # Toyota
print(car2.model)  # Civic
```

* Every time you create a `Car` object, Python automatically calls `__init__`.

---

### **F. Using `*args` and `**kwargs`**

Sometimes, you don’t know how many arguments will be passed when creating an object.
Python lets you handle this with:

* `*args` → captures **multiple positional arguments**
* `**kwargs` → captures **multiple keyword arguments**

---

#### **Example with `*args`**

```python
class NumberList:
    def __init__(self, *args):
        self.numbers = list(args)

num_list = NumberList(1, 2, 3, 4, 5)
print(num_list.numbers)  # [1, 2, 3, 4, 5]
```

Here:

* `*args` takes all numbers and stores them in `self.numbers`.

---

#### **Example with `**kwargs`**

```python
class Person:
    def __init__(self, **kwargs):
        self.name = kwargs.get("name", "Unknown")
        self.age = kwargs.get("age", 0)
        self.city = kwargs.get("city", "Not specified")

p1 = Person(name="Alice", age=25, city="New York")
p2 = Person(name="Bob")

print(p1.name, p1.city)  # Alice New York
print(p2.name, p2.city)  # Bob Not specified
```

Here:

* `**kwargs` stores all keyword arguments in a dictionary.
* `.get()` is used to provide **default values** if the key is missing.

---

### **Best Practices Recap**

1. **Classes** → Blueprints for objects
2. **Objects** → Actual things created from classes
3. **Attributes** → Variables inside objects
4. **Methods** → Functions inside objects
5. **Constructor (`__init__`)** → Automatically runs when creating an object
6. **`*args` & `**kwargs`** → Handle variable arguments flexibly

---

