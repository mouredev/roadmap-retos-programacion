# Operadores Aritméticos
print(f"Suma: 10 + 3 = {10 + 3}")
print(f"Resta: 10 - 3 = {10 - 3}")
print(f"Multiplicación: 10 x 3 = {10 * 3}")
print(f"División: 10 / 3 = {10 / 3}")
print(f"Módulo: 10 % 3 = {10 % 3}") # El módulo es lo que resta de una división
print(f"Exponente: 10 ** 3 = {10 ** 3}")
print(f"División Entera: 10 // 3 = {10 // 3}")

# Operadores de Comparación
print(f"Igualdad: 10 == 3 es {10 == 3}")
print(f"Desigualdad: 10 != 3 es {10 != 3}")
print(f"Mayor que: 10 > 3 es {10 > 3}")
print(f"Menor que: 10 < 3 es {10 < 3}")
print(f"Mayor o igual que: 10 >= 3 es {10 >= 3}")
print(f"Menor o igual que: 10 <= 3 es {10 <= 3}")

# Operadores Lógicos 
print(f"AND &&: 10 + 3 == 13 and 5 - 1 == 4 es {10 + 3 == 13 and 5 - 1 == 4}")
print(f"OR ||: 10 + 3 == 13 or 5 - 1 == 4 es {10 + 3 == 14 or 5 - 1 == 4}")
print(f"NOT !: not 10 + 3 == 14 es {not 10 + 3 == 14}")

# Operadores de asignación
my_number = 11  # asignación
print(my_number)
my_number += 1  # suma y asignación
print(my_number)
my_number -= 1  # resta y asignación
print(my_number)
my_number *= 2  # multiplicación y asignación
print(my_number)
my_number /= 2  # división y asignación
print(my_number)
my_number %= 2  # módulo y asignación
print(my_number)
my_number **= 1  # exponente y asignación
print(my_number)
my_number //= 1  # división entera y asignación
print(my_number)

# Operadores de identidad, comparan la posición en memoria
my_new_number = my_number
print(f"my_number is my_new_number es {my_number is my_new_number}")
print(f"my_number is not my_new_number es {my_number is not my_new_number}")

# Operadores de pertenencia
print(f"'u' in 'mouredev' = {'u' in 'mouredev'}")
print(f"'b' not in 'mouredev' = {'b' not in 'mouredev'}")

# Operadores de bit
a = 10  # 1010
b = 3  # 0011
print(f"AND: 10 & 3 = {10 & 3}")  # 0010
print(f"OR: 10 | 3 = {10 | 3}")  # 1011
print(f"XOR: 10 ^ 3 = {10 ^ 3}")  # 1001
print(f"NOT: ~10 = {~10}")
print(f"Desplazamiento a la derecha: 10 >> 2 = {10 >> 2}")  # 0010
print(f"Desplazamiento a la izquierda: 10 << 2 = {10 << 2}")  # 101000

"""
=======================
Estructuras de control
=======================
"""

# Condicionales

my_string = "Brais"

if my_string == "MoureDev":
    print("my_string es 'MoureDev'")
elif my_string == "Brais":
    print("my_string es 'Brais'")
else:
    print("my_string no es 'MoureDev' ni 'Brais'")

# Iterativas

for i in range(11):
    print(i)

i = 0

while i <= 10:
    print(i)
    i += 1

# Manejo de excepciones
try:
    print(10 / 0)
except:
    print("Se ha producido un error")
finally:
    print("Ha finalizado el manejo de excepciones")

"""
==========================
Extra
==========================
"""

for number in range(10, 56):
    if number % 2 == 0 and number != 16 and number % 3 != 0:
        print(number)