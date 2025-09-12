# 01 OPERADORES Y ESTRUCTURAS DE CONTROL

"""
 * EJERCICIO:
 * - Crea e...
 
 * - Utilizando las operaciones con operadores que tú quieras, crea ejemplos
 *   que representen todos los tipos de estructuras de control que existan
 *   en tu lenguaje:
 *   Condicionales, iterativas, excepciones...
 """

# Ejemplos utilizando todos los tipos de operadores aritméticos de Python:

from tkinter import Y
from numpy import true_divide


suma = 1 + 1
resta = 2 - 1
division = 4 / 2
multiplicacion = 2 * 2
modulo = 4 % 3
potencia = 2 ** 2
division_entera = 5 // 2

# creo lista para facilitar el print
operadores_aritmeticos = ["suma", "resta", "division", "multiplicacion", "modulo", "potencia", "division_entera"]

# mostramos los resultados
for operador in operadores_aritmeticos:
    print(operador, ":", eval(operador))

print("-"*48)

# Operadores Lógicos - and or, not
a = True
b = False

# operador and para agregar dos condiciones
if a and b:
    print("a y b son True")

# operador or para agregar dos condiciones de las que se cumple 1
if a or b:
    print("a o b es True")

# operador not para negar una condición
if not b:
    print("b es False")

print("-"*48)

# Operadores de comparación - ==, !=, >, <, >=, <=
x = 420
y = 69

print(f"Tenemos los valores: \n x = {x} \n y = {y} \nVamos a realizar unas comprobaciones de comparación:")

# operador == para comparar si dos valores son iguales
if x == y:
    print("x es igual a y")
else:
    print("x no es igual a y")

# operador != para comparar si dos valores son diferentes
if x != y:
    print("x es diferente a y")
else:
    print("x no es diferente a y")

# operador > para comparar si un valor es mayor
if x > y:
    print("x es mayor que y")
else:
    print("x no es mayor que y")

# operador < para comparar si un valor es menor
if x < y:
    print("x es menor que y")
else:
    print("x no es menor que y")

# operador >= para comparar si un valor es mayor o igual
if x >= y:
    print("x es mayor o igual que y")
else:
    print("x no es mayor o igual que y")

# operador <= para comprobar si un valor es menor o igual
if x <= y:
    print("x es menor o igual que y")
else:
    print("x no es menor o igual que y")

print("-"*48)

""" * DIFICULTAD EXTRA (opcional):
 * Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3."""

for i in range(10, 56):
    # imprimir pares, y que no son ni el 16 ni múltiplos de 3.
    if i % 2 == 0 and i != 16 and not i % 3 == 0:
        print(i)