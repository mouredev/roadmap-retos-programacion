"""
    Type of operators...
"""

# Arithmetic
ADDITION = 1 + 1
print(f"Add: 1 + 1 --> {ADDITION}")

SUBTRACTION = 1 - 1
print(f"Subtraction: 1 - 1 --> {SUBTRACTION}")

MULTIPLICATION = 2 * 5
print(f"Multiplication: 2 * 5 --> {MULTIPLICATION}")

DIVISION = 10 / 3
print(f"Division: 10 / 3 --> {DIVISION}")

MODULE = 24 % 2
print(f"Module: 24 % 2 --> {MODULE}")

EXPONENT = 2**3
print(f"Exponent: 2 ** 3 --> {EXPONENT}")

QUOTIENT = 10 // 3
print(f"Quotient: 10 // 3 --> {QUOTIENT}")


# Comparison
EQUAL = 1 == 1
print(f"\nEqual: 1 == 1 --> {EQUAL}")

NOT_EQUAL = 1 != 2
print(f"Not Equal: 1 != 2 --> {NOT_EQUAL}")

GREATER_THAN = 1 > 1
print(f"Greater than: 1 > 1 --> {GREATER_THAN}")

LESS_THAN = -1 < 0
print(f"Less than: -1 < 0 --> {LESS_THAN}")

GREATER_THAN_OR_EQUAL_TO = 1 >= 1
print(f"Greater than or equal to: 1 >= 1 --> {GREATER_THAN_OR_EQUAL_TO}")

LESS_THAN_OR_EQUAL_TO = 2 <= 2
print(f"Less than or equal to: 2 <= 2 --> {LESS_THAN_OR_EQUAL_TO}")

LETTER_A_01 = 1
LETTER_A_02 = LETTER_A_01
print(f"Is: {LETTER_A_01} is {LETTER_A_02} --> {LETTER_A_01 is LETTER_A_02}")

LETTER_A_03 = 1
LETTER_A_04 = LETTER_A_01
print(
    f"Is not: {LETTER_A_03} is not {LETTER_A_04} --> {LETTER_A_03 is not LETTER_A_04}"
)

ARRAY_01 = ["Hello", "World"]
print(f"In: 'World' in {ARRAY_01} --> {'World' in ARRAY_01}")

ARRAY_02 = ["Hello", "World"]
print(f"Not in: 'World' not in {ARRAY_02} --> {'World' not in ARRAY_02}")


# Logical
print(f"\nAnd: True and False --> {True and False}")

print(f"Or: False or True --> {False or True}")

print(f"Not: not False --> {not False}")


"""
    Control structures...
"""

# < if > and < if else >
if True:
    print("\nIf: True statement")

if False:
    print("If else: False --> True statement")
else:
    print("If else: False --> False statement")

# < if elif else >
LETTER = "A"
if LETTER == "D":
    print(f"If elif else: {LETTER} --> First statement")
elif LETTER == "C":
    print(f"If elif else: {LETTER} --> Second statement")
elif LETTER == "B":
    print(f"If elif else: {LETTER} --> Third statement")
else:
    print(f"If elif else: {LETTER} --> Default statement")

# < while >
i = 5
while i > 0:
    print(f"While (condition i > 0): loop {i}")

    if i == 3:
        break

    i = i - 1

# < for >
for char in "banana":
    if char == "n":
        continue
    print(f"{char}")


"""
    Additional challenge...
"""

print("")
for n in range(10, 56):
    if n != 16 and n % 2 == 0 and n % 3 != 0:
        print(f"{n}")
