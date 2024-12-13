# Decorators

def my_decorator(func):
    print("inside my_decorator")

    def wrapper(*args, **kwargs):
        print("inside wrapper - before func")
        result = func(*args, **kwargs)
        print("inside wrapper - after func")
        return result

    return wrapper


@my_decorator
def my_func(*args, **kwargs):
    print("inside my_func")
    print(args, kwargs)

my_func(1, 2, three=3)

# EXTRA

def call_count(func):
    def wrapper(*args, **kwargs):
        wrapper.calls += 1
        print(f"Function {func.__name__} called {wrapper.calls} times.")
        return func(*args, **kwargs)

    wrapper.calls = 0
    return wrapper

@call_count
def sum(num1, num2):
    return num1 + num2

@call_count
def mult(num1, num2):
    return num1 * num2

sum(1,2)
sum(2,3)
sum(3,4)
mult(5,6)
sum(8,9)
sum(1,5)
mult(2,6)