# operadores aritméticos
print(f"Suma: 10 + 3 = {10 + 3}")
print(f"Resta: 10 - 3 = {10 - 3}")
print(f"Multiplicación: 10 * 3 = {10 * 3}")
print(f"División: 10 / 3 = {10 / 3}")
print(f"Módulo: 10 % 3 = {10 % 3}")
print(f"Exponente: 10 ** 3 = {10 ** 3}")
print(f"División entera: 10 // 3 = {10 // 3}")

# operadores de comparación
print(f"Igualdad: 10 == 3 es {10 == 3}")
print(f"Desigualdad: 10 != 3 es {10 != 3}")
print(f"Mayor que: 10 > 10 es {10 > 10}")
print(f"Menor que: 10 < 3 es {10 < 3}")
print(f"Mayor o igual que: 10 >= 10 es {10 >= 10}")
print(f"Menor o igual que: 10 <= 3 es {10 <= 3}")

# operadores lógicos
print(f"AND: 10 + 3 == 13 and 5 - 1 == 4 es {10 + 3 == 13 and 5 - 1 == 4}")
print(f"OR: 10 + 3 == 14 or 5 - 1 == 4 es {10 + 3 == 14 or 5 - 1 == 4}")
print(f"NOT: 10 + 3 == 14 es {not 10 + 3 == 14}")

# operadores de asignación
my_number = 11 # asgnación
print(my_number)
my_number += 2 # suma y asignación
print(my_number)
my_number -= 2 # resta y asignación
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

# operadores de identidad
my_new_number = 1.0
print(f"my_number is my_new_number es {my_number is my_new_number}")
my_new_number = my_number
print(f"my_number is my_new_number es {my_number is my_new_number}")
print(f"my_number is not my_new_number es {my_number is not my_new_number}")

# operadores de pertenencia
print(f"'v' in 'fishellVvv' = {'v' in 'fishellVvv'}")
print(f"'v' not in 'fishellVvv' = {'v' not in 'fishellVvv'}")

# operadores de bit
a = 10 # 00001010
b = 3  # 00000011
print(f"AND: 10 & 3 = {10 & 3}") # 00000010
print(f"OR: 10 | 3 = {10 | 3}")  # 00001011
print(f"XOR: 10 ^ 3 = {10 ^ 3}") # 00001001
print(f"NOT: ~10 = {~10}")       # 11110101
print(f"Despalzamiento a la derecha: 10 >> 2 = {10 >> 2}") # 00000010
print(f"Despalzamiento a la izquierda: 10 << 2 = {10 << 2}") # 00101000

# estructuras de control condicionales
if a == b:
    print("a es igual a b")
elif a > b:
    print("a es mayor que b")
else:
    print("a no es igual ni mayor que b")

# estructuras de control iterativas
for i in range(a):
    print(i, end="")
while b < a:
    print(b, end="")
    b += 1

# estructuras de control para manejo de excepciones
try:
    print(a/0)
except:
    print("\nSe ha producido un error")
finally:
    print("Ha finalizado el manejo de excepciones")

# EXTRA

for i in range(10, 56, 2):
    if i != 16 and i % 3 != 0:
        print(i, end=", ")