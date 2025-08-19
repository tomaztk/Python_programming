
# **I. What is OOP in Python**


## **1. Object-Oriented Programming (OOP)**

OOP (**Object-Oriented Programming**) is a **way of structuring and organizing code** by grouping **data** and the **functions that work on that data** into single units called **objects**.

Think of **objects** as **real-world things**:

* A **Car** has:

  * **Attributes** → brand, color, speed
  * **Methods** → start(), stop(), accelerate()
* A **Bank Account** has:

  * **Attributes** → account number, balance
  * **Methods** → deposit(), withdraw(), check\_balance()

---

### **Key Definitions**

| Term          | Definition                            | Example              |
| ------------- | ------------------------------------- | -------------------- |
| **Class**     | A **blueprint** for creating objects. | `class Car:`         |
| **Object**    | An **instance** of a class.           | `my_car = Car()`     |
| **Attribute** | A variable that belongs to an object. | `self.color = "red"` |
| **Method**    | A function inside a class.            | `def start(self):`   |

---

### **Why use OOP?**

1. **Organized Code** → Related data and functions are grouped together.
2. **Easier Maintenance** → If something changes, you only update it in one place.
3. **Reusability** → You can reuse classes across projects.
4. **Natural Modeling** → You can represent real-world entities as code objects.
5. **Scalable** → Works well for large projects with many interacting components.

---

### **Difference from Procedural Programming**

So far, you’ve used **procedural programming**:

* Data (**variables**) and behavior (**functions**) are **separate**.
* This works fine for small scripts, but as your program grows, it becomes hard to manage.

**Example: Procedural**

```python
# Procedural style
name = "John"
age = 30

def greet():
    print("Hello", name)

greet()
```

Problems:

* If we had multiple people, we’d need multiple separate variables.
* It’s hard to keep data and behavior tied together.

---

**Example: OOP**

```python
# OOP style
class Person:
    def __init__(self, name, age):
        self.name = name  # attribute
        self.age = age    # attribute
    
    def greet(self):      # method
        print(f"Hello, my name is {self.name}")

person1 = Person("John", 30)
person1.greet()
```

Advantages:

* The **data** (name, age) and **behavior** (greet) are **inside the same object**.
* You can create as many **Person** objects as you want without repeating code.

---

## **2. Names and Objects in Python**

---

In Python, **everything is an object**.

When you create a variable:

```python
x = 10
```

* **x** is a **name** that points to the object `10` (which is of type `int`).
* The **name** and the **object** are **different things**.

---

### **Example**

```python
a = [1, 2, 3]   # name a points to a list object
b = a           # b points to the same list object
b.append(4)

print(a)  # [1, 2, 3, 4] → both a and b point to the same object
```

* `a` and `b` are **names**.
* The list `[1, 2, 3, 4]` is the **object**.
* Changing the object affects all names pointing to it.

---

## **3. Scopes and Namespaces**

---

A **namespace** is a **mapping between names and objects**.
A **scope** is the **region of the code** where a name is visible.

---

### **Types of Scopes** (LEGB Rule):

1. **Local (L)** → Inside the current function
2. **Enclosing (E)** → In enclosing functions (nested functions)
3. **Global (G)** → At the top level of the script
4. **Built-in (B)** → Predefined in Python

---

### **Example**

```python
x = "global"  # Global scope

def outer():
    x = "enclosing"
    
    def inner():
        x = "local"
        print(x)  # Local variable

    inner()

outer()  # Output: local
```

---

### **Namespace Example**

```python
# Global namespace
a = 5
print(globals())  # Shows all global variables

def func():
    # Local namespace
    b = 10
    print(locals())  # Shows all local variables

func()
```

---

## **4. Three New Object Types Introduced with Classes**

When you define a class in Python, three new object types appear:

---

### **1. Class Object**

* Created when you define a class.
* Used to create **instance objects**.

```python
class MyClass:
    pass

print(type(MyClass))  # <class 'type'>
```

---

### **2. Instance Object**

* Created when you call a class.

```python
class Dog:
    pass

dog1 = Dog()  # Instance object
print(type(dog1))  # <class '__main__.Dog'>
```

---

### **3. Method Object**

* A function inside a class that **belongs to an object**.
* When you call it, Python automatically passes the object as the first argument (`self`).

```python
class Dog:
    def bark(self):
        print("Woof!")

dog1 = Dog()
dog1.bark()  # "Woof!"
print(dog1.bark)  # <bound method Dog.bark of <__main__.Dog object>>
```

---

## **5. Putting It All Together**

Example showing:

* **Names and objects**
* **Scopes and namespaces**
* **Three new object types**

```python
class Car:
    # Class attribute (belongs to all instances)
    wheels = 4
    
    def __init__(self, brand):
        # Instance attribute (unique to each object)
        self.brand = brand
    
    def drive(self):
        print(f"{self.brand} is driving.")

# Class object
print(Car)  # <class '__main__.Car'>

# Instance object
my_car = Car("Toyota")
print(my_car)  # <__main__.Car object>

# Method object
print(my_car.drive)  # Bound method
my_car.drive()

# Namespaces
print(my_car.__dict__)  # Instance namespace
print(Car.__dict__)     # Class namespace
```

---
