"""
 * EJERCICIO:
 * - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
 *   Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
 *   (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
 * - Utilizando las operaciones con operadores que tú quieras, crea ejemplos
 *   que representen todos los tipos de estructuras de control que existan
 *   en tu lenguaje:
 *   Condicionales, iterativas, excepciones...
 * - Debes hacer print por consola del resultado de todos los ejemplos.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
 *
 * Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.
"""


# OPERADORES
print("OPERADORES")

# Aritméticos
print("\nAritméticos")
print("Suma: 2 + 3 =", 2 + 3)
print("Resta: 2 - 3 =", 2 - 3)
print("Multiplicación: 2 * 3 =", 2 * 3)
print("División: 2 / 3 =", 2 / 3)
print("División entera: 2 // 3 =", 2 // 3)
print("Módulo: 2 % 3 =", 2 % 3)
print("Potencia: 2 ** 3 =", 2 ** 3)

# Lógicos
print("\nLógicos")
print("And: True and False =", True and False)
print("Or: True or False =", True or False)
print("Not: not True =", not True)
print("Xor: True ^ False =", True ^ False)

# De comparación
print("\nDe comparación")
print("Equal: 2 == 3 =", 2 == 3)
print("Not equal: 2 != 3 =", 2 != 3)
print("Less than: 2 < 3 =", 2 < 3)
print("Less than or equal: 2 <= 3 =", 2 <= 3)
print("Greater than: 2 > 3 =", 2 > 3)
print("Greater than or equal: 2 >= 3 =", 2 >= 3)

# Asignación
print("\nAsignación")
a = 5
print("a = 5, a =", a)
a += 2
print("a += 2, a =", a)
a -= 2
print("a -= 2, a =", a)
a *= 2
print("a *= 2, a =", a)
a /= 2
print("a /= 2, a =", a)
a %= 2
print("a %= 2, a =", a)

# Identidad
print("\nIdentidad")
a = 1000
b = 1000
print("Is: a is b =", a is b)
print("Is: a is not b =", a is not b)

# Pertenencia
print("\nPertenencia")
print("In: 2 in [1, 2, 3] =", 2 in [1, 2, 3])
print("Not in: 2 not in [1, 2, 3] =", 2 not in [1, 2, 3])

# Bits
print("\nBits")
print("Bitwise And: 2 & 3 =", 2 & 3)
print("Bitwise Or: 2 | 3 =", 2 | 3)
print("Bitwise Xor: 2 ^ 3 =", 2 ^ 3)
print("Bitwise Not: ~2 =", ~2)
print("Left shift: 2 << 3 =", 2 << 3)
print("Right shift: 2 >> 3 =", 2 >> 3)

# ESTRUCTURAS DE CONTROL
print("\nESTRUCTURAS DE CONTROL")

# Condicionales
print("\nCondicionales")
if 100 < 1000:
    print("100 < 1000")
else:
    print('100 >= 1000')

# Condicionales en una sola línea
print("\nEn una sola línea")
print("2 < 3") if 2 < 3 else print("2 >= 3")

# Iterativas
print("\nIterativas")
for i in range(3):
    print(i)
i = 0
while i < 3:
    print(i)
    i += 1

# Excepciones
print("\nExcepciones")
try:
    print(2 / 0)
except ZeroDivisionError:
    print("Cannot divide by zero")
finally:
    print("Ended the exception handling")

# DIFICULTAD EXTRA
print("\nDIFICULTAD EXTRA")
for i in range(10, 56):
    print(i) if i % 2 == 0 and i != 16 and i % 3 != 0 else None
