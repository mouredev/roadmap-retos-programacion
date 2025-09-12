"""
    Exceptions...
"""

print("Exceptions...")

print(
    """\n# Invalid operation
try:
    operation: float = 10 / 0 # <-- Invalid operation.
    print(f"\\nOperation --> {operation}")
except ZeroDivisionError as error:
    print(f"\\nError --> {error}")"""
)

# Invalid operation
try:
    operation: float = 10 / 0  # <-- Invalid operation.
    print(f"\nOperation --> {operation}")
except ZeroDivisionError as error:
    print(f"\nError --> {error}")


print(
    """\n# Invalid index
try:
    my_list: list[int] = [1, 2, 3]
    element: int = my_list[3]  # <-- Index three doesn't exist.
    print(f"\\nElement --> {element}")
except IndexError as error:
    print(f"\\nError --> {error}")"""
)


# Invalid index
try:
    my_list: list[int] = [1, 2, 3]
    element: int = my_list[3]  # <-- Index three doesn't exist.
    print(f"\nElement --> {element}")
except IndexError as error:
    print(f"\nError --> {error}")

print(
    "\n# ---------------------------------------------------------------------------------- #\n"
)

"""
    Additional challenge...
"""


print("Additional challenge...")


def fn(param: float | int | str | list[int]) -> float | int | str | list[int]:
    """Function to test error exceptions."""
    if isinstance(param, int):
        return param.upper()  # type: ignore

    if isinstance(param, str):
        return param / 2  # type: ignore

    if isinstance(param, list):
        raise TypeError("My custom error")

    return param


# No error
try:
    result: float | int | str | list[int] = fn(param=1.25)
    print(f"\nResult --> {result}")
except Exception as error:  # pylint: disable=[broad-exception-caught]
    print(f"\nError --> {error}")

# Attribute error
try:
    result: float | int | str | list[int] = fn(param=12)
    print(f"\nResult --> {result}")
except AttributeError as error:
    print(f"\nError --> {error}")

# Custom error
try:
    result: float | int | str | list[int] = fn(param=[22, 21, 20])
    print(f"\nResult --> {result}")
except TypeError as error:
    print(f"\nError --> {error}")

# Type error
try:
    result: float | int | str | list[int] = fn(param="Lucas Hoz")
    print(f"\nResult --> {result}")
except TypeError as error:
    print(f"\nError --> {error}")


print("\nAdditional challenge finished!")
