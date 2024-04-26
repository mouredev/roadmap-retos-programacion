""" En este ejercicio crearemos los operadores aritméticos, de comparación,
lógicos y más"""

# Operadores aritméticos
print(f"Sumar 13 + 3 = {13 + 10}, es mi número favorito")
print(f"Restar 16 - 3 = {16 - 3}, es mi número de la suerte")
print(f"Multiplicar 9 * 6 = {9 * 6}")
print(f"Dividir 9 / 6 = {9 / 6}")
print(f"Módulo 17 % 7 = {17 % 7}")
print(f"Exponente 3 ** 6 = {3 ** 6}")
print(f"División entera 9 // 6 = {9 // 6}")

# Operadores de comparación
print(f"Igualdad: 12 == 6 es {12 == 6}")
print(f"Desigualdad: 12 != 6 es {12 != 6}")
print(f"Mayor: 12 > 6 es {12 > 6}")
print(f"Menor: 12 < 6 es {12 < 6}")
print(f"Mayor o igual que: 12 >= 6 es {12 >= 6}")
print(f"Menor o igual que: 12 <= 6 es {12 <= 6}")

# Operadores lógicos
print(f"AND &&: 13 + 3 == 16 and 7 - 3 == 4 es {13 + 3 == 16 and 7 - 3 == 4}")
print(f"OR ||: 13 + 3 == 16 or 7 - 5 == 4 es {13 + 3 == 16 or 7 - 5 == 4}")
print(f"NOT !: not 13 + 2 == 16 {not 13 + 2 == 16}")

# Operadores de asignación
my_number = 8 # asignación
print(my_number)
my_number += 1 # suma y asignación
print(my_number)
my_number -= 1 # resta y asignación
print(my_number)
my_number *= 2 # multiplicación y asignación
print(my_number)
my_number /= 2 # división y asignación
print(my_number)
my_number %= 2 # módulo y asignación
print(my_number)
my_number **= 2 # exponente y asignación
print(my_number)
my_number //= 2 # división entera y asignación
print(my_number)

# Operadores de identidad
my_new_number = 1.0
print(f"my_number is my_new_number es {my_number is my_new_number}")
print(f"my_number is not my_new_number es {my_number is not my_new_number}")

# Operadores de pertenencia
print(f"'o' in 'Fernando'{'o' in 'Fernando'}")
print(f"'j' not in 'Fernando'{'j' not in 'Fernando'}")

# Operadores de bit
a = 10 #1010
b = 3 # 0011
print(f"AND: 10 & 3 = {10 & 3}") # 0010
print(f"OR: 10 | 3 = {10 | 3}") # 1011
print(f"XOR: 10 ^ 3 = {10 ^ 3}") # 1001
print(f"NOT: ~10  = {~10}")
print(f"Desplazamiento a la derecha: 10 >> 2 = {10 >> 2}") # 0010 
print(f"Desplazamiento a la izquierda: 10 << 2 = {10 << 2}") # 101000

"""
Estructuras de control
"""

# Condicionales

my_name = "Fernando"

if my_name == "Tello":
    print("my_name es 'Tello'")
elif my_name == "Fernando":
    print("my_name es 'Fernando'")
else:
    print("my_name no es 'Tello' ni 'Fernando'")

# Iterativas

for i in range(11):
    print(i)

i = 0

while i <= 10:
    print(i)
    i += 1

# Manejo de excepciones

try:
    print(10/0)
except:
    print("Se ha producido un error")
finally:
    print("Ha finalizado el manejo de excepciones")

"""
Crea un programa que imprima por consola todos los números comprendidos
entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
"""

for (i) in range (10, 55, 2):
    if i != 16 and i % 3 !=0:
        print(i)
