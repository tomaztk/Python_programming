
## **Lesson 09: Python Functions (Solutions)**


#### **1. Basic Function Definition**

```python
def greet_user():
    print("Hello, welcome to Python functions!")

greet_user()
```

---

#### **2. Function with One Parameter**

```python
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")
```

---

#### **3. Function with Return Statement**

```python
def square(num):
    return num * num

result = square(5)
print(result)  # Output: 25
```

---

#### **4. Multiple Parameters**

```python
def add_numbers(a, b):
    return a + b

print(add_numbers(3, 7))  # Output: 10
```

---

#### **5. Default Arguments**

```python
def power(base, exponent=2):
    return base ** exponent

print(power(3))      # Output: 9
print(power(3, 3))   # Output: 27
```

---

#### **6. Keyword Arguments**

```python
def describe_pet(animal_type, pet_name):
    print(f"I have a {animal_type} named {pet_name}.")

describe_pet(animal_type="dog", pet_name="Rex")
describe_pet(pet_name="Whiskers", animal_type="cat")
```

---

#### **7. Positional vs Keyword Arguments**

```python
def describe_pet(animal_type, pet_name):
    print(f"My {animal_type}'s name is {pet_name}.")

# Positional
describe_pet("hamster", "Nibbles")

# Keyword
describe_pet(pet_name="Bubbles", animal_type="fish")
```

---

#### **8. Local vs Global Scope**

```python
x = 5

def show_scope():
    x = 10  # Local variable
    print("Inside function (local x):", x)

show_scope()
print("Outside function (global x):", x)

def modify_global():
    global x
    x = 20

modify_global()
print("After global modification:", x)
```

---

#### **9. Function that Returns Multiple Values**

```python
def split_name(full_name):
    parts = full_name.split()
    return parts[0], parts[1]

first, last = split_name("Ada Lovelace")
print("First:", first)
print("Last:", last)
```

---

#### **10. Nested Functions**

```python
def outer():
    print("Inside outer function.")
    
    def inner():
        print("Inside inner function.")
    
    inner()

outer()
```

---

#### **11. Calculator with Functions**

```python
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero!"
    return a / b

print(add(4, 2))
print(subtract(4, 2))
print(multiply(4, 2))
print(divide(4, 2))
```

---

#### **12. Recursive Function**

```python
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))  # Output: 120
```

---

#### **13. Function with a List Argument**

```python
def print_shopping_list(items):
    for item in items:
        print(f"- {item}")

shopping = ["Milk", "Bread", "Eggs"]
print_shopping_list(shopping)
```

---

#### **14. Function Reusability**

```python
def is_even(number):
    return number % 2 == 0

def filter_evens(numbers):
    evens = []
    for num in numbers:
        if is_even(num):
            evens.append(num)
    return evens

print(filter_evens([1, 2, 3, 4, 5, 6]))  # Output: [2, 4, 6]
```

---

#### **15. Simple Menu using Functions**

```python
def greet():
    print("Hello from the menu!")

def add_numbers():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print("Sum:", a + b)

def main_menu():
    while True:
        print("\nMenu:")
        print("1. Greet")
        print("2. Add two numbers")
        print("3. Quit")
        choice = input("Choose an option: ")

        if choice == '1':
            greet()
        elif choice == '2':
            add_numbers()
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.")

main_menu()
```

