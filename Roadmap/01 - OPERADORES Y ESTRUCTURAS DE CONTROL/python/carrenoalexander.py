"""
 * Operadores
"""

# Aritméticos 

print(f"Addition: 18 + 8 = {18 + 8}")
print(f"Subtraction: 18 - 8 = {18 - 8}")
print(f"Multiplication: 18 * 8 = {18 * 8}")
print(f"Division: 18 / 8 = {18 / 8}")
print(f"Modulus: 18 % 8 = {18 % 8}")
print(f"Floor division: 18 // 8 = {18 // 8}")
print(f"Exponentiation: 18 ** 8 = {18 ** 8}")

# Lógicos

print(True == True and False == False)
print(False == True or False == False)
print(not True)

# Comparación

print(f"Greater than: 24 > 24: {24 > 24}")
print(f"Less than: 24 < 24: {24 < 24}")
print(f"Greater than or equal to: 24 >= 24: {24 >= 24}")
print(f"Less than or equal to: 24 <= 24: {24 <= 24}")
print(f"Equal: 24 == 24: {24 == 24}")
print(f"Not equal: 24 != 24: {24 != 24}")

# Asignación

number = 12

number += 2
print(number)
number -= 2
print(number)
number *= 2
print(number)
number /= 2
print(number)
number %= 2
print(number)
number //= 2
print(number)
number **= 2
print(number)

# Identidad

variable = None

print(f"My variable is None: {variable is None}")
print(f"My variable is not None: {variable is not None}")

# Pertenencia

print(f"'E' in word: {"E" in "word"}")
print(f"'E' not in word: {"E" not in "word"}")

# Bits

a = 8  # 1000
b = 10  # 1010

print(f"AND: 8 & 10 = {8 & 10}")  # 0001 <
print(f"OR: 8 | 10 = {8 | 10}")   # 0101 <
print(f"XOR: 8 ^ 10 = {8 ^ 10}")  # 0100 <
print(f"NOT: ~8 = {~8}")
print(f"Right shift: 8 >> 10: {8 >> 2}")  # 0010
print(f"Left shift: 8 << 10: {8 << 2}")   # 100000

"""
 * Estructuras de control
"""

# Condicionales

language = "Python"

if language == "JavaScript":
    print("The language is JavaScript")
elif language == "Python":
    print("The language is Python")
else:
    print("It could be another language")

# Iterativas

for number in range(1, 9):
    print(number)

age = 0

while age <= 8:
    print(age)
    age += 2

# Excepciones

try:
    print(18 / 0)
except:
    print("Cannot divide by zero")  # ZeroDivisionError
finally:
    print("Try again")

"""
 * Extra
"""

for extra_number in range(10, 56):
    if extra_number %2 == 0 and extra_number != 16 and extra_number %3 != 0:
        print(extra_number)