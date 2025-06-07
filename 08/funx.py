# Types hinting and type checking

def add(a: int, b: int) -> int:
    return a + b

print(add(2, 3))  # 5

from typing import List, Callable
def apply_transform(numbers: List[int], transform: Callable[[int], int]) -> List[int]:
    def is_valid(n: int) -> bool:
        return n >= 0
    return [transform(n) for n in numbers if is_valid(n)]

result = apply_transform([1, -2, 3], lambda x: x * x)
print(result)  # Output: [1, 9]




#####
# Simple decorator
####

def debug(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@debug
def say_hello():
    print("Hello!")

say_hello()


def my_decorator(func):
    def wrapper():
        print("Before call")
        func()
        print("After call")
    return wrapper

@my_decorator
def say_hi():
    print("Hi!")

say_hi()
 

##
## Nested functions
##
def outer(x):
    def inner(y):
        return x + y
    return inner

add_five = outer(5)
print(add_five(3))  # 8



## Recursive function


def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

print(factorial(5))  # 120



## Lambda

def apply_func(lst, func):
    return [func(x) for x in lst]

squared = apply_func([1, 2, 3], lambda x: x ** 2)
print(squared)  # [1, 4, 9]

print(apply_func([1, 2, 3], lambda x: x ** 2))

#######
###### ARGUMENTS IN FUNCTION
#######


# POSITIONAL argumetns

def net_price(price,tax):
    """Calculate net price after tax."""
    return price * (1 + tax)

print(net_price(499, 0.2)) 
print(net_price(0.2, 499)) 



# DEFAULT arguments in functions

def net_price(price: float, tax: float = 0.2, discount: float = 0) -> float:
    """Calculate net price after tax."""
    return price * (1- discount) * (1 + tax)


print(net_price(499, 0))

print(net_price(499, discount=0.1))  

print(net_price(499, tax=0.0, discount=0.1)) 


# KEYWORD arguments
# order not matter, helps with readability but must be after positional arguments

def aloha(greets, name, surname) -> str:
    """Return a greeting message."""
    return f"{greets}, {name}, {surname}!"

print(aloha("Aloha", "John", "Doe"))  
print(aloha("Aloha", surname="John", name="Doe"))  

# Arbitrary number of arguments
# varying number of arguments can be passed to a function using *args and **kwargs
# *args = allows passing a variable number of positional arguments (non-keyword arguments)
# **kwargs = allows passing a variable number of keyword arguments (key-value pairs)
# * unpacking operator (can be used to unpack a list or tuple into positional arguments)


def sum_123(a,b,):
    return a +b 

print(sum_123(1,23))
# print(sum_123(1,2,3,4)) # error: sum_123() takes 2 positional arguments but 4 were given


def sum_all(*args) -> int:
    """Return the sum of all arguments."""
    return sum(args)

# convention is to use *args for positional arguments but you can use any name, but *args is a common convention

def sum_all2(*nums) -> int:
    """Return the sum of all arguments."""
    return sum(nums)

print(sum_all(1, 2, 3))  
print(sum_all(1, 2, 3, 4, 5,43,43,34,3,423,423,423423))  


print(sum_all2(1, 2, 3))  
print(sum_all2(1, 2, 3, 4, 5,43,43,34,3,423,423,423))  


### **kwargs allows passing a variable number of keyword arguments (key-value pairs)

def print_address(**kwargs) -> None:
    """Print the address."""
    for key, value in kwargs.items():
        print(f"{key}: {value}")
    print(type(kwargs))  # <class 'dict'>, kwargs is a dictionary

print_address(street="Dol 42", city="LJubljana", zip="1000", country="Slovenia")


# order of arguments in function definition is crucial:
# 1. positional arguments
# 2. *args (variable number of positional arguments)
# 3. keyword arguments (default arguments)
def shipping_label(*args, **kwargs):
    pass

print(shipping_label("Alex", "Castro", 
                     street="Dol 42", 
                     city="LJubljana", 
                     zip="1000", 
                     country="Slovenia"))