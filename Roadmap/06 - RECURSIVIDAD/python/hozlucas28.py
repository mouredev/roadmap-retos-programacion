"""
    Recursive function...
"""

print("\nRecursive function...")


def recursive_fn(start: int, end: int, rtn: list[int]) -> list[int]:
    """Recursive function"""
    if start < end:
        return rtn

    rtn.append(start)
    recursive_fn(start - 1, end, rtn)


print(
    """\ndef recursive_fn(start: int, end: int, rtn: list[int]) -> list[int]:
    if start < end:
        return rtn

    rtn.append(start)
    recursive_fn(start - 1, end, rtn)"""
)

recursive_rtn: list[int] = []
recursive_fn(100, 0, recursive_rtn)

print("\nrecursive_rtn: list[int] = []")
print("recursive_fn(100, 0, recursive_rtn)")

print(f"\nrecursive_rtn --> {recursive_rtn}")

print(
    "\n# ---------------------------------------------------------------------------------- #\n"
)

"""
    Additional challenge...
"""

print("Get factorial...")


def get_factorial(number: int) -> int:
    """Get factorial of a number"""
    if number == 1:
        return 1

    return number * get_factorial(number - 1)


print(
    """\ndef get_factorial(number: int) -> int:
    if number == 1:
        return 1

    return number * get_factorial(number - 1)"""
)

print(f"\nget_factorial(5) --> {get_factorial(5)}")

print(
    "\n# ---------------------------------------------------------------------------------- #\n"
)

print("Get Fibonacci value by position...")


def get_fibonacci_value_by_pos(pos: int) -> int:
    """Get Fibonacci value by position"""
    if pos in [1, 2]:
        return 1

    return get_fibonacci_value_by_pos(pos - 1) + get_fibonacci_value_by_pos(pos - 2)


print(
    """\ndef get_fibonacci_value_by_pos(pos: int)->int: 
    if pos in [1, 2]: 
        return 1

    return get_fibonacci_value_by_pos(pos - 1) + get_fibonacci_value_by_pos(pos - 2)"""
)

print(f"\nget_fibonacci_value_by_pos(8) --> {get_fibonacci_value_by_pos(8)}")
