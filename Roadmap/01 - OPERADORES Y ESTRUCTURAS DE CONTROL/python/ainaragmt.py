# Operadores aritméticos
print("\nOperadores aritméticos")
print(f"Suma: 2 + 3 = {2 + 3}")
print(f"Resta: 2 - 3 = {2 - 3}")
print(f"Multiplicación: 2 * 3 = {2 * 3}")
print(f"División: 2 / 3 = {2 / 3}")
print(f"Módulo: 2 % 3 = {2 % 3}") # Resto de la división
print(f"Exponente: 2 ** 3 = {2 ** 3}")
print(f"División entera: 2 // 3 = {2 // 3}") # División truncada

# Operadores lógicos
print("\nOperadores lógicos")
print(f"AND: 2 + 3 == 4 & 2 + 3 == 5 es {2 + 3 == 4 & 2 + 3 == 5}") # & o and
print(f"OR: 2 + 3 == 4 | 2 + 3 == 5 es {2 + 3 == 4 | 2 + 3 == 5}") # | o or
print(f"NOT: 2 + 3 == 4 es {not 2 + 3 == 4}")

# Operadores de comparación
print("\nOperadores de comparación")
print(f"Igualdad: 2 == 3 es {2 == 3}")
print(f"Desigualdad: 2 != 3 es {2 != 3}")
print(f"Mayor que: 2 > 3 es {2 > 3}")
print(f"Menor que: 2 < 3 es {2 < 3}")
print(f"Mayor igual que: 2 >= 3 es {2 >= 3}")
print(f"Menor igual que: 2 <= 3 es {2 <= 3}")

# Operadores de asignación
print("\nOperadores de asignación")
my_int = 17 # asignación
print(my_int)
my_int += 1 # suma y asignación
print(my_int)
my_int -= 1 # resta y asignación
print(my_int)
my_int *= 2 # multiplicación y asignación
print(my_int)
my_int /= 2 # división y asignación
print(my_int)
my_int %= 2 # módulo y asignación
print(my_int)
my_int **= 1 # exponente y asignación
print(my_int)
my_int //= 1 # división entera y asignación
print(my_int)

# Operadores de identidad (comparan la posición de memoria)
print("\nOperadores de identidad")
my_new_int = 1.0
print(f"my_int es my_new_int? {my_int is my_new_int}")
my_int = my_new_int
print(f"my_int es my_new_int? {my_int is my_new_int}")

# Operadores de pertenecia
print("\nOperadores de pertenencia")
print(f"'a' está en 'ainara'? {'a' in 'ainara'}")
print(f"'a' está en 'ainara'? {'a' not in 'ainara'}")

# Operadores de bits
print("\nOperadores de bits")
a = 10 # 1010
b = 3 # 0011
print(f"AND: 10 & 3 = {a & b}")
print(f"OR: 10 | 3 = {a | b}")
print(f"XOR: 10 ^ 3 = {a ^ b}")
print(f"NOT: ~ 10 = {~ a}")
print(f"Shift right: 10 >> 1 = {10 >> 1}")
print(f"Shift left: 10 << 1 = {10 << 1}")

# Estructuras condicionales
print("\nEstructuras condicionales")
a = 10
b = 3
if (a == b):
    print("a == b")
elif (a == 10):
    print("a == 10")
else:
    print("a != b")

# Estructuras iterativas
print("\nEstructuras iterativas")
for i in range (5):
    print("i: ", i) # hace el i++ por defecto

j = 5
while j > 2:
    j -= 1
    print("j: ", j)

# Excepciones
print("\nExcepciones")
try:
    print(3 / 1)
    print(5 / 0)
    print(2 / 1) # no se llega a ejecutar porque salta la excepción
except:
    print("No se puede dividir entre 0")
finally:
    print("Ha finalizado el manejo de excepciones") # se ejecuta tanto si se produce algún error como si no

'''
Crea un programa que imprima por consola todos los números comprendidos
entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
'''
print("\nEjercicio de dificultad extra")
a = 10
while a <= 55:
    if (a != 16 and (a % 3) != 0):
        if (a % 2) == 0:
            print(a)
    a+=1