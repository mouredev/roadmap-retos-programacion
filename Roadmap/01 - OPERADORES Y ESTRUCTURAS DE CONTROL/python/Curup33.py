"""
Operadores
"""

# Operadores aritméticos
print(f"Suma: 10 + 3 = {10 + 3}")
print(f"Resta: 10 - 3 = {10 - 3}")
print(f"Multiplicación: 10 * 3 = {10 * 3}")
print(f"División: 10 / 3 = {10 / 3}")
print(f"Módulo: 10 % 3 = {10 % 3}")
print(f"Exponenciación: 10 ** 3 = {10 ** 3}")
print(f"División entera: 10 // 3 = {10 // 3}")

# Operadores de comparación
print(f"Igualdad: 10 == 3 = {10 == 3}")
print(f"Distinto: 10 != 3 = {10 != 3}")
print(f"Mayor que: 10 > 3 = {10 > 3}")
print(f"Menor que: 10 < 3 = {10 < 3}")
print(f"Mayor o igual que: 10 >= 3 = {10 >= 3}")
print(f"Menor o igual que: 10 <= 3 = {10 <= 3}")

# Operadores lógicos
print(f"AND &&: True and False = {True and False}")
print(f"OR ||: True or False = {True or False}")
print(f"NOT !: not True = {not True}")
print(f"NOT !: not False = {not False}")

# Operadores de asignación
my_number = 11
print(f"Mi número es: {my_number}")
my_number += 1 # suma y asigna
print(f"Mi número es: {my_number}")
my_number -= 1 # resta y asigna
print(f"Mi número es: {my_number}")
my_number *= 2 # multiplica y asigna
print(f"Mi número es: {my_number}")
my_number /= 2 # divide y asigna
print(f"Mi número es: {my_number}")
my_number %= 2 # módulo y asigna
print(f"Mi número es: {my_number}")
my_number **= 2 # exponenciación y asigna
print(f"Mi número es: {my_number}")
my_number //= 2 # división entera y asigna
print(f"Mi número es: {my_number}")

# Operadores de identidad
my_mew_number = my_number
print(f"my_number is my_mew_number: {my_number is my_mew_number}")
print(f"my_number is not my_mew_number: {my_number is not my_mew_number}")

# Operadores de pertenencia
print(f"'u' in 'mouredev' = {'u' in 'mouredev'}")
print(f"'b' not in 'mouredev' = {'b' not in 'mouredev'}")

# Operadores de bit
a = 10 # 1010
b = 3 # 0011
print(f"AND: 10 & 3 = {a & b}") # 0010
print(f"OR: 10 | 3 = {a | b}") # 1011
print(f"XOR: 10 ^ 3 = {a ^ b}") # 1001
print(f"NOT: ~10 = {~a}") # 0101
print(f"LEFT SHIFT: 10 << 3 = {a << 3}") # 101000
print(f"RIGHT SHIFT: 10 >> 3 = {a >> 3}") # 0001

"""
Estructura de control
"""

# Condicionales
my_string = "AngelCurup"

if my_string == "AngelCurup":
    print(f"my_string es 'AngelCurup'")
elif my_string == "RafaelCurup":
    print(f"my_string es 'RafaelCurup'")
else:
    print(f"my_string no es 'AngelCurup' ni 'RafaelCurup'")

# Iterativas
for i in range(11):
    print(i)

i = 0

while i < 10:
    print(i)
    i += 1

# Manejo de excepciones
try:
    print(10 / 0)
except ZeroDivisionError:
    print("No se puede dividir por 0")
finally:
    print("Fin del manejo de excepciones")

"""
Extra
"""

for number in range(10, 56):
    if number % 2 == 0 and number != 16 and number % 3 != 0:
        print(number)
