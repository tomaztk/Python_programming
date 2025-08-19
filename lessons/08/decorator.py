def log_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Calling function '{func.__name__}' with arguments {args} {kwargs}")
        result = func(*args, **kwargs)
        print(f"Function '{func.__name__}' returned {result}")
        return result
    return wrapper


@log_decorator
def add(a, b):
    return a + b


@log_decorator
def divide(a, b):
    return a / b

@log_decorator
def sum_total(numbers):
    total = 0
    for number in numbers:
        total += number
    return total



add(311, 432)

divide(110,21)

sum_total([5133,2213, 44, 6346456535])