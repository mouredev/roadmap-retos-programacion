"""
    Variable assignment by value...
"""

print("Variable assignment by value...")

A: int = 3
B: int = A

print("\nA: int = 3\nB: int = A")
print(f"\nValue of 'A' = {A}\nValue of 'B' = {B}")

A = A * 3

print("\nA = A * 3")
print(f"\nValue of 'A' = {A}\nValue of 'B' = {B}")

print(
    "\n# ---------------------------------------------------------------------------------- #"
)

"""
    Variable assignment by reference...
"""

print("\nVariable assignment by reference...")

C: list[int] = [1, 2, 3, 4]
D: list[int] = C

print("\nC: list[int] = [1, 2, 3, 4]\nD: list[int] = C")
print(f"\nValue of 'C' = {C}\nValue of 'D' = {D}")

C.append(5)

print("\nC.append(5)")
print(f"\nValue of 'C' = {C}\nValue of 'D' = {D}")

print(
    "\n# ---------------------------------------------------------------------------------- #"
)

"""
    Function with an argument passed by value...
"""

print("\nFunction with an argument passed by value...")

VALUE: str = 13

print("\nVALUE: str = 13")


def fn_with_paramenter_by_value(x: int):
    """Example function which receives a parameter as a value"""
    x += x


print(
    "def fn_with_paramenter_by_value(x: int):\n" + "    x += x",
)

fn_with_paramenter_by_value(VALUE)

print("\nfn_with_paramenter_by_value(VALUE)")

print(f"\nValue of 'VALUE' = {VALUE}")

print(
    "\n# ---------------------------------------------------------------------------------- #"
)

"""
    Function with an argument passed by reference...
"""

print("\nFunction with an argument passed by reference...")

REFERENCE: list[int] = [10, 11, 12, 13, 14]

print("\nREFERENCE: list[int] = [10, 11, 12, 13, 14]")


def fn_with_paramenter_by_reference(param: list[int]):
    """Example function which receives a parameter as a reference"""
    param.append(15)


print(
    "def fn_with_paramenter_by_reference(param: list[int]):\n" + "    param.append(15)"
)

fn_with_paramenter_by_reference(REFERENCE)

print("\nfn_with_paramenter_by_reference(REFERENCE)")

print(f"\nValue of 'REFERENCE' = {REFERENCE}")

print(
    "\n# ---------------------------------------------------------------------------------- #"
)

"""
    Additional challenge...
"""


def first_program(a: int, b: int) -> list[int]:
    """Function which receives value parameters"""
    a, b = b, a

    return [a, b]


def second_program(a: list[int], b: list[int]) -> list[list[int]]:
    """Function which receives reference parameters"""
    aux: list[int] = a.copy()
    a.extend(b)
    b.extend(aux)

    return [a, b]


ARG_01: int = 5
ARG_02: int = 12
ARG_03: list[int] = [1, 2, 3, 4, 5]
ARG_04: list[int] = [6, 7, 8, 9, 10]

[NEW_ARG_01, NEW_ARG_02] = first_program(ARG_01, ARG_02)
[NEW_ARG_03, NEW_ARG_04] = second_program(ARG_03, ARG_04)

print(f"\noriginal:\n    ARG_01: {ARG_01}\n    ARG_02: {ARG_02}")
print(f"new:\n    ARG_01: {NEW_ARG_01}\n    ARG_02: {NEW_ARG_02}")

print(f"\noriginal:\n    ARG_03: {ARG_03}\n    ARG_04: {ARG_04}")
print(f"new:\n    ARG_03: {NEW_ARG_03}\n    ARG_04: {NEW_ARG_04}")
