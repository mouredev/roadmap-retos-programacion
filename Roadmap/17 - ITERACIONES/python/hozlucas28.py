# pylint: disable=missing-function-docstring,pointless-string-statement,expression-not-assigned,unnecessary-lambda

"""
    Iterations...
"""

from typing import Literal


print("Iterations...")

START: Literal[1] = 1
END: Literal[10] = 10


def recursive_fn(*, end: int, start: int) -> None:
    print(start)
    if start < end:
        recursive_fn(
            end=end,
            start=start + 1,
        )


print("\nFirst method...\n")
recursive_fn(end=END, start=START)

print("\nSecond method...\n")
for i in range(START, END + 1):
    print(i)


print("\nThird method...\n")
j = START
while j <= END:
    print(j)
    j += 1


print(
    "\n# ---------------------------------------------------------------------------------- #\n"
)

"""
    Additional challenge...
"""

print("Additional challenge...")

print("\nFirst method...\n")
recursive_fn(end=END, start=START)

print("\nSecond method...\n")
for i in range(START, END + 1):
    print(i)


print("\nThird method...\n")
j = START
while j <= END:
    print(j)
    j += 1

print("\nFourth method...\n")
[print(i) for i in range(START, END + 1)]

print("\nFifth method...\n")
list(map(lambda i: print(i), range(START, END + 1)))
