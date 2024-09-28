def call_counter(func):
    count = 0

    def wrapper(*args, **kwargs):
        nonlocal count
        count += 1
        print(f"Function '{func.__name__}' has been called {count} times.")
        return func(*args, **kwargs)

    return wrapper


@call_counter
def add(a, b):
    return a + b


@call_counter
def subtract(a, b):
    return a - b


print(add(3, 5))
print(subtract(10, 2))
print(add(4, 4))
print(subtract(8, 3))
