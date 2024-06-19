# -- exercise
def sum(a: int, b: int) -> int:
    return a + b


def subtract(a: int, b: int) -> int:
    return a - b


def multiply(a: int, b: int) -> int:
    return a * b


def fn_sum(fn: callable, a: int, b: int) -> int:
    return fn(a, b)


print(fn_sum(sum, 1, 2))
print(fn_sum(subtract, 1, 2))
print(fn_sum(multiply, 1, 2))
