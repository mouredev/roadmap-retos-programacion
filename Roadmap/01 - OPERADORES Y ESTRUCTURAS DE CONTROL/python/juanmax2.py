""" 
Ejemplos de operadores
"""
# Operadores lógicos

# Ejemplo and:
my_num1 = 1
my_num2 = 10
if my_num1 == 1 and my_num2 == 10:
    print("Las dos condiciones se cumplen")
else:
    print("No se cumplen las condiciones")
# Ejemplo or:
if my_num1 == 1 or my_num2 == 10:
    print("Una de las condiciones se cumple")
else:
    print("Ninguna de las condiciones se cumple")

# Ejemplo not:
if not my_num1 == 2:
    print("El numero 1 no es igual a 2")

# Operadores aritméticos
print(f"Suma: 9 + 3 = {9 + 3}")
print(f"Resta: 9 - 3 = {9 - 3}")
print(f"Multiplicación: 9 * 3 = {9 * 3}")
print(f"División: 9 / 3 = {9 / 3}")
print(f"Módulo: 9 % 3 = {9 % 3}")
print(f"Poténcia: 9 ** 3 = {9 ** 3}")
print(f"División entera: 9 // 3 = {9 // 3}")

# Operadores de comparación
print(f"Operador igualdad: 9 == 3 es {9 == 3}")
print(f"Operador desigualdad: 9 != 3 es {9 != 3}")
print(f"Operador mayor que: 9 > 3 es {9 > 3}")
print(f"Operador menor que: 9 < 3 es {9 < 3}")
print(f"Operador mayor o igual que: 9 >= 3 es {9 >= 3}")
print(f"Operador menor o igual que: 9 <= 3 es {9 <= 3}")

# Operadores de asignación
numero = 1 # Asignación
print(numero)
numero += 1 # Asignación y suma
print(numero)
numero -= 1 # Asignación y resta
print(numero)
numero *= 2 # Asignación y multiplicación
print(numero)
numero /= 2 # Asignación y división
print(numero)
numero **= 2 # Asignación y potencia
print(numero)
numero %= 2 # Asignación y módulo
print(numero)
numero //= 2 # Asignación y división entera
print(numero)

# Operadores de identidad
nuevo_numero = numero
print(f"numero is nuevo_numero es {numero is nuevo_numero}")
print(f"numero is not nuevo_numero es {numero is not nuevo_numero}")

# Operadores de pertenencia

print(f"'a' in 'juanma' = {'a' in 'juanma'}")
print(f"'d' not in 'juanma' = {'d' not in 'juanma'}")

# Operadores de bit
x = 9
y = 3
print(f"AND: 9 & 3 = {9 & 3}")
print(f"OR: 9 | 3 = {9 | 3}")
print(f"XOR: 9 ^ 3 = {9 ^ 3}")
print(f"NOT: ~9 = {~9}")
print(f"Desplazamiento a la derecha: 9 >> 3 = {9 >> 3}")
print(f"Desplazamiento a la izquierda: 9 << 3 = {9 << 3}")

"""
Estructuras de control
"""
# IF:
if my_num1 == 1 and my_num2 == 10:
    print("Las dos condiciones se cumplen")
elif my_num == 1 or my_num2 == 10:
    print("Una de las condiciones se cumple")
else:
    print("No se cumplen las condiciones")
    
# FOR:
for i in range(0,11):
    print(i)

# WHILE:
while i < 10:
    print(i)
    i += 1

# Manejo de excepciones:
try: 
    print(10 / 0)
except:
    print("Se ha producido un error")
finally:
    print("Ha finalizado el manejo de excepciones")


"""Ejercicio extra:
Crea un programa que imprima por consola todos los números comprendidos
entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3."""

for i in range(10,56):
    if (i % 2 == 0) and (not i == 16) and (i % 3 != 0):
        print(i)