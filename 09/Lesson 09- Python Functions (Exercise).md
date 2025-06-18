
## **Lesson 09: Python Functions (Exercise)**

Each assignment is designed to reinforce the core concepts covered in **Lesson 8: Python Functions**, which typically include:

* Function definition and calling
* Parameters and arguments
* Return statements
* Scope (local/global)
* Default and keyword arguments
* Nested functions
* Recursion (if applicable)

#### **1. Basic Function Definition**

**Assignment**: Write a function called `greet_user()` that prints "Hello, welcome to Python functions!"
**What we want**: Ensure the learner can define and call a simple function with no parameters.

---

#### **2. Function with One Parameter**

**Assignment**: Define a function `greet(name)` that prints a personalized greeting like "Hello, Alice!"
**What we want**: Practice using parameters and string formatting.

---

#### **3. Function with Return Statement**

**Assignment**: Create a function `square(num)` that returns the square of the number provided.
**What we want**: Understand how return statements work and how to use returned values.

---

#### **4. Multiple Parameters**

**Assignment**: Write a function `add_numbers(a, b)` that returns the sum of two numbers.
**What we want**: Use multiple parameters and arithmetic operations.

---

#### **5. Default Arguments**

**Assignment**: Define a function `power(base, exponent=2)` that returns base raised to the exponent. Test it with and without the second argument.
**What we want**: Practice using default values in function parameters.

---

#### **6. Keyword Arguments**

**Assignment**: Call a function `describe_pet(animal_type, pet_name)` using keyword arguments in different orders.
**What we want**: Reinforce understanding of how keyword arguments work.

---

#### **7. Positional vs Keyword Arguments**

**Assignment**: Modify `describe_pet()` to demonstrate the difference between positional and keyword arguments.
**What we want**: Show learners how argument order and naming affect function behavior.

---

#### **8. Local vs Global Scope**

**Assignment**: Write a function `show_scope()` that tries to modify a global variable. Then use `global` keyword to actually modify it.
**What we want**: Illustrate the difference between local and global variables.

---

#### **9. Function that Returns Multiple Values**

**Assignment**: Write a function `split_name(full_name)` that returns first and last name separately.
**What we want**: Demonstrate returning multiple values using tuples.

---

#### **10. Nested Functions**

**Assignment**: Define a function `outer()` with an inner function `inner()` inside it. The outer function should call the inner one.
**What we want**: Understand function nesting and scope implications.

---

#### **11. Calculator with Functions**

**Assignment**: Create a simple calculator with functions: `add`, `subtract`, `multiply`, and `divide`. Each should take two numbers.
**What we want**: Combine multiple concepts (functions, parameters, return) into one task.

---

#### **12. Recursive Function**

**Assignment**: Write a recursive function `factorial(n)` that returns the factorial of `n`.
**What we want**: Introduce the concept of recursion and base cases.

---

#### **13. Function with a List Argument**

**Assignment**: Write a function `print_shopping_list(items)` that takes a list and prints each item.
**What we want**: Practice passing collections (like lists) to functions.

---

#### **14. Function Reusability**

**Assignment**: Write a function `is_even(number)` that returns True if a number is even, else False. Then use it inside another function `filter_evens(numbers)` that returns only even numbers from a list.
**What we want**: Show how functions can call and reuse other functions.

---

#### **15. Simple Menu using Functions**

**Assignment**: Create a text menu with three options (e.g., greet, add two numbers, quit). Implement each option using a function and use a loop to keep the program running.
**What we want**: Integrate functions into a user-interactive program and demonstrate modular design.





Arbitrary number of arguments
varying number of arguments can be passed to a function using *args and **kwargs

 *args = allows passing a variable number of positional arguments (non-keyword arguments)
 
 **kwargs = allows passing a variable number of keyword arguments (key-value pairs)
 
 * unpacking operator (can be used to unpack a list or tuple into positional arguments)

```python
def sum_123(a,b,):
    return a +b 
```

```python
print(sum_123(1,23))
print(sum_123(1,2,3,4)) # error: sum_123() takes 2 positional arguments but 4 were given
```

```python
def sum_all(*args) -> int:
    """Return the sum of all arguments."""
    return sum(args)
```

convention is to use *args for positional arguments but you can use any name, but *args is a common convention

```python
def sum_all2(*nums) -> int:
    """Return the sum of all arguments."""
    return sum(nums)

print(sum_all(1, 2, 3))  
print(sum_all(1, 2, 3, 4, 5,43,43,34,3,423,423,423423))  


print(sum_all2(1, 2, 3))  
print(sum_all2(1, 2, 3, 4, 5,43,43,34,3,423,423,423))  
```


 **kwargs allows passing a variable number of keyword arguments (key-value pairs)

```python
def print_address(**kwargs) -> None:
    """Print the address."""
    for key, value in kwargs.items():
        print(f"{key}: {value}")
    print(type(kwargs))  # <class 'dict'>, kwargs is a dictionary

print_address(street="Dol 42", city="LJubljana", zip="1000", country="Slovenia")
```


order of arguments in function definition is crucial:
* 1. positional arguments
* 2. *args (variable number of positional arguments)
* 3. keyword arguments (default arguments)

```python
def shipping_label(*args, **kwargs):
    pass

print(shipping_label("Alex", "Castro", 
                     street="Dol 42", 
                     city="LJubljana", 
                     zip="1000", 
                     country="Slovenia"))
```