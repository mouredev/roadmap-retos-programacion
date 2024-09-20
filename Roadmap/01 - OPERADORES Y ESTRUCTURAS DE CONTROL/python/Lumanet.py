a = 7
b = 3
# Aritméticos
print(f"Suma: {a} + {b} = {a + b}")
print(f"Resta: {a} - {b} = {a - b}")
print(f"Multiplicación: {a} * {b} = {a * b}")
print(f"División: {a} / {b} = {a / b}")
print(f"Módulo: {a} % {b} = {a % b}")
print(f"Exponente: {a} ** {b} = {a ** b}")
print(f"División entera: {a} // {b} = {a // b}")

# De comparación
print(f"Igualdad: {a} == {b} es {a == b}")
print(f"Desigualdad: {a} != {b} es {a != b}")
print(f"Mayor que: {a} > {b} es {a > b}")
print(f"Menor que: {a} < {b} es {a < b}")
print(f"Mayor o igual que: {a} >= {a} es {a >= a}")
print(f"Menor o igual que: {a} <= {b} es {a <= b}")

# Lógicos
print(f"AND &&: {a} + {b} == {a + b} and 5 - 1 == 4 es {a + b == 10 and 5 - 1 == 4}")
print(f"OR ||: {a} + {b} == {a + b} or 5 - 1 == 4 es {a + b == {a + b} or 5 - 1 == 4}")
print(f"NOT !: not {a} + {b} == 14 es {not a + b == 14}")

# De asignación
mi_numero = 7  # asignación
print(mi_numero)
mi_numero += 1  # suma y asignación
print(mi_numero)
mi_numero -= 1  # resta y asignación
print(mi_numero)
mi_numero *= 3  # multiplicación y asignación
print(mi_numero)
mi_numero /= 3  # división y asignación
print(mi_numero)
mi_numero %= 2  # módulo y asignación
print(mi_numero)
mi_numero **= 1  # exponente y asignación
print(mi_numero)
mi_numero //= 1  # división entera y asignación
print(mi_numero)

# De identidad
otro_numero = mi_numero
print(f"mi_numero is otro_numero es {mi_numero is otro_numero}")
print(f"mi_numero is not otro_numero es {mi_numero is not otro_numero}")

# De pertenencia
print(f"'a' in 'lumanet' = {'a' in 'lumanet'}")
print(f"'s' not in 'lumanet' = {'s' not in 'lumanet'}")

# De bit
a = 7  # 0111
b = 5  # 0101
print(f"AND: {a} & {b} = {a & b}")  # 0101 -> 5
print(f"OR: {a} | {b} = {a | b}")  # 0111 -> 7
print(f"XOR: {a} ^ {b} = {a ^ b}")  # 0010 -> 2
print(f"NOT: ~{a} = {~a}") # 1000 -> -8
print(f"Desplazamiento a la derecha: {a} >> 2 = {a >> 2}")  # 0001 -> 1
print(f"Desplazamiento a la izquierda: {a} << 2 = {a << 2}")  # 11100 -> 28

"""
Estructuras de control
"""

# Condicionales

cadena = "Marcos"

if cadena == "lumanet":
    print("cadena es 'lumanet'")
elif cadena == "Marcos":
    print("cadena es 'Marcos'")
else:
    print("cadena no es 'lumanet' ni 'Marcos'")

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
    print("No se puede dividir por 0.")
finally:
    print("Proceso terminado.")
    
"""
 Crea un programa que imprima por consola todos los números comprendidos
 entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
"""

for i in range(10, 56):
    if i % 2 == 0 and i != 16 and i % 3 != 0:
        print(i)