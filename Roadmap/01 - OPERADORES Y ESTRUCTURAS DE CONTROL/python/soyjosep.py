
# Operadores Aritméticos
print("=== Operadores Aritméticos ===")
a, b = 10, 3
print(f"Suma: {a} + {b} = {a + b}")
print(f"Resta: {a} - {b} = {a - b}")
print(f"Multiplicación: {a} * {b} = {a * b}")
print(f"División: {a} / {b} = {a / b:.2f}")
print(f"Módulo: {a} % {b} = {a % b}")
print(f"Exponente: {a} ** {b} = {a ** b}")
print(f"División Entera: {a} // {b} = {a // b}")

# Operadores de Comparación
print("\n=== Operadores de Comparación ===")
print(f"Igualdad: {a} == {b} -> {a == b}")
print(f"Desigualdad: {a} != {b} -> {a != b}")
print(f"Mayor que: {a} > {b} -> {a > b}")
print(f"Menor que: {a} < {b} -> {a < b}")
print(f"Mayor o igual que: {a} >= {b} -> {a >= b}")
print(f"Menor o igual que: {a} <= {b} -> {a <= b}")

# Operadores Lógicos
print("\n=== Operadores Lógicos ===")
x, y = True, False
print(f"AND: {x} and {y} -> {x and y}")
print(f"OR: {x} or {y} -> {x or y}")
print(f"NOT: not {x} -> {not x}")

# Operadores de Asignación
print("\n=== Operadores de Asignación ===")
number = 5
print(f"Asignación inicial: number = {number}")
number += 2
print(f"Suma y asignación: number += 2 -> {number}")
number *= 3
print(f"Multiplicación y asignación: number *= 3 -> {number}")
number /= 2
print(f"División y asignación: number /= 2 -> {number:.2f}")
number //= 1
print(f"División entera y asignación: number //= 1 -> {number}")

# Operadores de Identidad
print("\n=== Operadores de Identidad ===")
x = 10
y = x
print(f"x is y: {x is y}")
print(f"x is not y: {x is not y}")

# Operadores de Pertenencia
print("\n=== Operadores de Pertenencia ===")
sequence = "Python"
print(f"'P' in '{sequence}' -> {'P' in sequence}")
print(f"'z' not in '{sequence}' -> {'z' not in sequence}")

# Operadores de Bits
print("\n=== Operadores de Bits ===")
a, b = 10, 3  # 1010 y 0011 en binario
print(f"AND: {a} & {b} = {a & b}")
print(f"OR: {a} | {b} = {a | b}")
print(f"XOR: {a} ^ {b} = {a ^ b}")
print(f"NOT: ~{a} = {~a}")
print(f"Desplazamiento a la derecha: {a} >> 1 = {a >> 1}")
print(f"Desplazamiento a la izquierda: {a} << 2 = {a << 2}")

"""
Estructuras de Control en Python
"""

# Condicionales
print("\n=== Condicionales ===")
name = "Joseph"
if name == "MoureDev":
    print(f"Hola {name}, bienvenido!")
elif name == "Joseph":
    print(f"Hola {name}, has sido identificado.")
else:
    print(f"Nombre no reconocido: {name}")

# Bucle For
print("\n=== Bucle For ===")
for i in range(5):
    print(f"Iteración {i+1}: i = {i}")

# Bucle While
print("\n=== Bucle While ===")
counter = 0
while counter < 3:
    print(f"Contador: {counter}")
    counter += 1

# Manejo de Excepciones
print("\n=== Manejo de Excepciones ===")
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"Error: {e}")
finally:
    print("Finalizó el manejo de la excepción.")

"""
Desafío Extra:
Números entre 10 y 55, pares, excluyendo 16 y múltiplos de 3.
"""
print("\n=== Desafío Extra ===")
for number in range(10, 56):
    if number % 2 == 0 and number != 16 and number % 3 != 0:
        print(f"Número válido: {number}")