"""
OPERATORS
"""

num_one = 15
num_two = 4

# Arithmetic operators
print(f"ADDITION: {num_one} + {num_two} = {num_one + num_two}")
print(f"SUBTRACTION: {num_one} - {num_two} = {num_one - num_two}")
print(f"MULTIPLICATION: {num_one} * {num_two} = {num_one * num_two}")
print(f"DIVISION: {num_one} / {num_two} = {num_one / num_two}")
print(f"FLOOR DIVISION: {num_one} // {num_two} = {num_one // num_two}")
print(f"MODULO: {num_one} % {num_two} = {num_one % num_two}")
print(f"EXPONENT: {num_one} ** {num_two} = {num_one ** num_two}")

# Comparison operators
print(f"EQUAL TO: {num_one} == {num_two} = {num_one == num_two}")
print(f"NOT EQUAL TO: {num_one} != {num_two} = {num_one != num_two}")
print(f"GREATER THAN: {num_one} > {num_two} = {num_one > num_two}")
print(f"LESS THAN: {num_one} < {num_two} = {num_one < num_two}")
print(f"GREATER THAN OR EQUAL TO: {num_one} >= {num_two} = {num_one >= num_two}")
print(f"LESS THAN OR EQUAL TO: {num_one} <= {num_two} = {num_one <= num_two}")

# Logical operators
print(f"AND: {num_one} > 10 and {num_two} < 5 = {num_one > 10 and num_two < 5}")
print(f"OR: {num_one} > 10 or {num_two} < 5 = {num_one > 10 or num_two < 5}")   
print(f"NOT: not {num_one} > 10 = {not num_one > 10}")

# Assignment operators
my_number = 10
print(f"ASSIGNMENT: my_number = {my_number}")
my_number += 5
print(f"ADDITION ASSIGNMENT: my_number += 5 = {my_number}")
my_number -= 3
print(f"SUBTRACTION ASSIGNMENT: my_number -= 3 = {my_number}")
my_number *= 2
print(f"MULTIPLICATION ASSIGNMENT: my_number *= 2 = {my_number}")
my_number /= 4
print(f"DIVISION ASSIGNMENT: my_number /= 4 = {my_number}")
my_number %= 3
print(f"MODULO ASSIGNMENT: my_number %= 3 = {my_number}")
my_number **= 2
print(f"EXPONENT ASSIGNMENT: my_number **= 2 = {my_number}")
my_number //= 2
print(f"FLOOR DIVISION ASSIGNMENT: my_number //= 2 = {my_number}")

# Identity operators
my_new_number = 5
my_new_number = my_number
print(f"IDENTITY: my_number is my_new_number = {my_number is my_new_number}")
print(f"IDENTITY: my_number is not my_new_number = {my_number is not my_new_number}")

# Membership operators
print(f"'o' in 'elhdrond' = {'o' in 'elhdrond'}")
print(f"'d' not in 'elhdrond' = {'d' not in 'elhdrond'}")

# Bitwise operators
a = 10  # 1010
b = 3   # 0011
print(f"BITWISE AND: {a} & {b} = {a & b}")  # 0010
print(f"BITWISE OR: {a} | {b} = {a | b}")   # 1011
print(f"BITWISE XOR: {a} ^ {b} = {a ^ b}")  # 1001
print(f"BITWISE NOT: ~{a} = {~a}")           # 0101
print(f"BITWISE LEFT SHIFT: {a} << 1 = {a << 1}")  # 10100
print(f"BITWISE RIGHT SHIFT: {a} >> 1 = {a >> 1}")  # 0101


"""
CONTROL STRUCTURES
"""

# Conditional statements
my_name = "Elhdrond"
if my_name == "Elhdrond":
    print(f"Hello, {my_name}!")
elif my_name == "MoureDev":
    print(f"Hello, {my_name}!")
else:
    print(f"Hello, stranger!")

# Iteration statements
for i in range(50):
    print(f"Iteration {i}")

i = 0
while i < 50:
    print(f"While loop iteration {i}")
    i += 1 

# Exception handling
try:
    print(23 / 0)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
finally:
    print("Execution completed.")


"""
Extra exercise
"""

for number in range(10, 56):   
    if number % 2 == 0 and number != 16 and number % 3 != 0: 
        print(f"{number} is even, not 16, and not divisible by 3.")