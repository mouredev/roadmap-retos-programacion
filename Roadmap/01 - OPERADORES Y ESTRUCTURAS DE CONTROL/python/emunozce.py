"""
    Operators and control structures
"""

# OPERATORS
# Arithmetic operators
print(5 + 3)  # 8 (Addition)
print(5 - 3)  # 2 (Subtraction)
print(5 * 3)  # 15 (Multiplication)
print(5 / 3)  # 1.6666666666666667 (Division)
print(5 % 3)  # 2 (Modulus)
print(5**3)  # 125 (Exponentiation)
print(5 // 3)  # 1 (Floor division)
print("#######################################")
#######################################

# Assignment operators
x = 5
print(x)  # 5
x += 3
print(x)  # 8
x -= 3
print(x)  # 5
x *= 3
print(x)  # 15
x /= 3
print(x)  # 5.0
x %= 3
print(x)  # 2.0
x **= 3
print(x)  # 8.0
x //= 3
print(x)  # 2.0
print("#######################################")
#######################################

# Comparison operators
print(5 == 3)  # False (Equal)
print(5 != 3)  # True (Not equal)
print(5 > 3)  # True (Greater than)
print(5 < 3)  # False (Less than)
print(5 >= 3)  # True (Greater than or equal to)
print(5 <= 3)  # False (Less than or equal to)
print("#######################################")
#######################################

# Logical operators
print(True and False)  # False (AND)
print(True or False)  # True (OR)
print(not True)  # False (NOT)
print("#######################################")
#######################################

# Identity operators
# Check if two objects are the same object in memory location
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x
print(x is y)  # False (IS)
print(x is not z)  # False (IS NOT)
print(x is z)  # True (IS)
print("#######################################")
#######################################

# Membership operators
# Check if a sequence is present in an object
x = ["apple", "banana"]
print("banana" in x)  # True (IN)
print("orange" not in x)  # True (NOT IN)
print("#######################################")
#######################################

# Bitwise operators
print(5 & 3)  # 1 (AND)
print(5 | 3)  # 7 (OR)
print(5 ^ 3)  # 6 (XOR)
print(~5)  # -6 (NOT)
print(5 << 3)  # 40 (Zero fill left shift)
print(5 >> 3)  # 0 (Signed right shift)
print("#######################################")
#######################################

##############################################################################


# CONTROL STRUCTURES

# IF-ELSE statement example

if 5 > 3:
    print("5 es mayor que 3")  # This line will be printed
else:
    print("5 no es mayor que 3")  # This line will not be printed
print("#######################################")

# IF-ELIF statement example
if 5 > 3:
    print("5 es mayor que 3")  # This line will be printed
elif 5 == 3:
    print("5 es igual a 3")  # This line will not be printed
else:
    print("5 no es mayor que 3")
print("#######################################")
#######################################

# FOR loop example
for i in range(1, 5):  # The second parameter is exclusive and optional
    print(i)  # This will print numbers from 1 to 4
print("#######################################")
#######################################

# WHILE loop example
i = 1
while i < 5:
    print(i)  # This will print numbers from 1 to 4
    i += 1  # Increment i by 1
print("#######################################")
#######################################

# BREAK statement example
i = 1
while i < 5:
    print(i)  # This will print numbers from 1 to 2
    if i == 2:
        break  # Exit the loop
    i += 1
print("#######################################")
#######################################

# CONTINUE statement example
for i in range(1, 5):
    if i == 2:
        continue  # Skip the rest of the code inside the loop
    print(i)  # This will print numbers 1, 3 and 4
print("#######################################")
#######################################

# PASS statement example
for i in range(1, 5):
    pass  # Do nothing
print("#######################################")
#######################################

##############################################################################


# DESAFIO EXTRA
for i in range(10, 56):
    if i != 16 and not i % 3 == 0:  # If i is not 16 and i is not divisible by 3
        print(i)  # Print i
