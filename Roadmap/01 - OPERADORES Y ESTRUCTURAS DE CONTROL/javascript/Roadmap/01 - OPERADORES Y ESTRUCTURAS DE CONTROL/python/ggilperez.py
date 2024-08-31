"""
Operators
"""

# Arithmetic
print("Arithmetic")
print(f"Sum {1+2 = }")
print(f"Sub {2-3 = }")
print(f"Mul {3*4 = }")
print(f"Div {4/5 = }")
print(f"Div int {5//6 = }")
print(f"Exp {6**7 = }")
print(f"Mod {7%8 = }")
print()

# Comparison
print("Comparison")
print(f"Equality {1 == 2 = }")
print(f"Inequality {2 != 3 = }")
print(f"Greater than {3 > 4 = }")
print(f"Less than {4 < 5 = }")
print(f"Greater or equal {5 >= 6 = }")
print(f"Less or equal {6 <= 7 = }")
print()

# Logical
print("Logical")
print(f"AND {1 + 2 == 3 and 4 - 5 == -1 = }")
print(f"OR {1 + 2 == 3 or 4 - 5 == 6 = }")
print(f"NOT {not 1 + 2 == 3 = }")
print()

# Assignment
print("Assignment")
my_int = 0
print(f"my_int = 0 => {my_int}")
my_int += 1
print(f"my_int += 1 => {my_int}")
my_int -= 2
print(f"my_int -= 2 => {my_int}")
my_int *= 3
print(f"my_int *= 3 => {my_int}")
my_int /= 4
print(f"my_int /= 4 => {my_int}")
my_int //= 5
print(f"my_int //= 5 => {my_int}")
my_int **= 6
print(f"my_int **= 6 => {my_int}")
my_int %= 7
print(f"my_int %= 7 => {my_int}")
print()

# Identity
print("Identity")
aux_int = my_int
print(f"{my_int is aux_int = }")
print(f"{my_int is not aux_int = }")
print()

# Containment
print("Containment")
print(f"{'y' in 'python' = }")
print(f"{'a' in 'python' = }")
print(f"{'y' not in 'python' = }")
print(f"{'a' not in 'python' = }")
print()

# Bitwise
print("Bitwise")
a = 10  # 1010
b = 3  # 0011
print(f"AND {10 & 3 = }")
print(f"OR {10 | 3 = }")
print(f"XOR {10 ^ 3 = }")
print(f"NOT {~10 = }")
print(f"Right Shift {10 >> 2 = }")  # 0010
print(f"Left Shift {10 << 2 = }")  # 101000
print()

"""
Compound statements
"""

# Conditional
print("Conditional")
my_int = 3

if my_int % 2 == 0:
    print("my_int is even")
elif my_int == 0:
    print("can't check, 0 given")
else:
    print("my_int is odd")
print()

# Iterative
print("Iterative")
for i in range(5):
    print(i)

i = 0
while i <= 5:
    print(i)
    i += 1
print()

# Exceptions management
print("Exceptions")
try:
    print(10 / 0)
except ZeroDivisionError:
    print("Division by 0")
else:
    print("All OK")
finally:
    print("Finishing")
print()

# Extra
print("Extra")
print([number for number in range(10, 56) if number % 2 == 0 and number != 16 and number % 3 != 0])
print()
