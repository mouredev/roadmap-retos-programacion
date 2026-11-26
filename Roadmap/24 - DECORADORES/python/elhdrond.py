import functools

"""
DECORATORS
"""


def print_call(function):
    def print_function():
        print(f"The function '{function.__name__}' has been called.")
        return function

    return print_function


@print_call
def example_function():
    pass


@print_call
def example_function_2():
    pass


@print_call
def example_function_3():
    pass


example_function()
example_function_2()
example_function_3()


"""
    EXTRA EXERCISE
"""

def call_counter(function):
    # functools.wraps preserves the original function's __name__ and __doc__
    @functools.wraps(function)
    def wrapper(*args, **kwargs):
        wrapper.call_count += 1
        print(
            f"'{function.__name__}' has been called {wrapper.call_count} time(s)."
        )
        return function(*args, **kwargs)

    wrapper.call_count = 0
    return wrapper


@call_counter
def greet(name: str):
    print(f"Hello, {name}!")


@call_counter
def add(a: int, b: int) -> int:
    return a + b


greet("Luke")
greet("Leia")
greet("Han")

result = add(3, 4)
print(f"Result: {result}")
result = add(10, 20)
print(f"Result: {result}")
