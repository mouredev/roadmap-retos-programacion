# Suma
print(f"2 + 2 = {2 + 2}")

# Resta
print(f"2 - 2 = {2 - 2}")

# Multiplicación
print(f"2 * 2 = {2 * 2}")

# División
print(f"2 / 2 = {2 / 2}")

# División entera
print(f"2 // 2 = {2 // 2}")

# Módulo
print(f"2 % 2 = {2 % 2}")

# Potencia
print(f"2 ** 2 = {2 ** 2}")

# Operadores de comparación

# Igualdad
print(f"2 == 2: {2 == 2}")

# Desigualdad
print(f"2 != 2: {2 != 2}")

# Mayor que
print(f"2 > 2: {2 > 2}")

# Menor que
print(f"2 < 2: {2 < 2}")

# Mayor o igual que
print(f"2 >= 2: {2 >= 2}")

# Menor o igual que
print(f"2 <= 2: {2 <= 2}")

# Operadores lógicos

# AND
print(f"True and False = {True and False}")

# OR
print(f"True or False = {True or False}")

# NOT
print(f"not True = {not True}")

# Operadores de asignación

# Asignación
a = 2
print(f"a = 2")

# Asignación con suma
print(f"a += 2: {a + 2}")

# Asignación con resta
print(f"a -= 2: {a - 2}")

# Asignación con multiplicación
print(f"a *= 2: {a * 2}")

# Asignación con división
print(f"a /= 2: {a / 2}")

# Asignación con división entera
print(f"a //= 2: {a // 2}")

# Asignación con módulo
print(f"a %= 2: {a % 2}")

# Asignación con potencia
print(f"a **= 2: {a ** 2}")

# Operadores de identidad

# is
b = None
print(f"b is None: {b is None}")
b = 1
print("b = 1")
print(f"b is None: {b is None}")

# is not
print(f"b is not None: {b is not None}")

# Operadores de pertenencia

# in
print(f"2 in [1, 2, 3]: {2 in [1, 2, 3]}")

# not in
print(f"2 not in [1, 2, 3]: {2 not in [1, 2, 3]}")

# Operadores de bits

# AND
print(f"2 & 2 = {2 & 2}")

# OR
print(f"2 | 2 = {2 | 2}")

# XOR
print(f"2 ^ 2 = {2 ^ 2}")

# NOT
print(f"~2 = {~2}")

# Desplazamiento a la izquierda
print(f"2 << 2 = {2 << 2}")

# Desplazamiento a la derecha
print(f"2 >> 2 = {2 >> 2}")

# Estructuras de control

# Condicionales

# if
if (2 + 2 == 4):
    print("2 + 2 = 4")

# if else
if (2 + 2 == 3):
    print("2 + 2 = 3")
else:
    print("2 + 2 != 3")

# if elif else
if (isinstance(2, str)):
    print("2 es un string")
elif (isinstance(2, int)):
    print("2 es un entero")
else:
    print("2 no es un string ni un entero")

# Iterativas

# for
for number in range(1, 6):
    print(number)

# while
number = 1
while number < 6:
    print(number)
    number += 1

# Excepciones

# try except
try:
    print(2 / 0)
except ZeroDivisionError:
    print("No se puede dividir entre 0")

# try except else
try:
    print(2 / 2)
except ZeroDivisionError:
    print("No se puede dividir entre 0")
else:
    print("No se ha producido ninguna excepción")

# try except finally
try:
    print(2 / 0)
except ZeroDivisionError:
    print("No se puede dividir entre 0")
finally:
    print("Se ejecuta siempre")

# try except else finally
try:
    print(2 / 2)
except ZeroDivisionError:
    print("No se puede dividir entre 0")
else:
    print("No se ha producido ninguna excepción")
finally:
    print("Se ejecuta siempre")

# Dificultad extra

# Lista de números prohibidos (múltiplos de 3, número 16 y pares)
prohibited_numbers = [x for x in range(10, 56) if (
    x % 3 == 0 or x == 16 or x % 2 != 0)]

for number in range(10, 56):
    if number in prohibited_numbers:
        continue
    print(number)
