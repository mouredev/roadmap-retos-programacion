# Operadores en Python
print("Operadores en Python:")

# Aritméticos
print("\nOperadores aritméticos:")
print("5 + 2 =", 5 + 2)
print("5 - 2 =", 5 - 2)
print("5 * 2 =", 5 * 2)
print("5 / 2 =", 5 / 2)
print("5 % 2 =", 5 % 2)
print("5 ** 2 =", 5 ** 2)
print("5 // 2 =", 5 // 2)

# Lógicos
print("\nOperadores lógicos:")
print("True and False =", True and False)
print("True or False =", True or False)
print("not True =", not True)

# Comparación
print("\nOperadores de comparación:")
print("5 == 2 =", 5 == 2)
print("5 != 2 =", 5 != 2)
print("5 > 2 =", 5 > 2)
print("5 < 2 =", 5 < 2)
print("5 >= 2 =", 5 >= 2)
print("5 <= 2 =", 5 <= 2)

# Asignación
print("\nOperadores de asignación:")
a = 5
print("a = 5 -> a =", a)
a += 2
print("a += 2 -> a =", a)
a -= 2
print("a -= 2 -> a =", a)
a *= 2
print("a *= 2 -> a =", a)
a /= 2
print("a /= 2 -> a =", a)
a %= 2
print("a %= 2 -> a =", a)
a **= 2
print("a **= 2 -> a =", a)
a //= 2
print("a //= 2 -> a =", a)

# Identidad
print("\nOperadores de identidad:")
print("5 is 2 =", 5 is 2)
print("5 is not 2 =", 5 is not 2)

# Pertenencia
print("\nOperadores de pertenencia:")
print("5 in [1, 2, 3] =", 5 in [1, 2, 3])
print("2 not in [1, 2, 3] =", 2 not in [1, 2, 3])

# Bits
print("\nOperadores de bits:")
print("5 & 2 =", 5 & 2)
print("5 | 2 =", 5 | 2)
print("5 ^ 2 =", 5 ^ 2)
print("~5 =", ~5)
print("5 << 2 =", 5 << 2)
print("5 >> 2 =", 5 >> 2)

# Estructuras de control en Python
print("\nEstructuras de control en Python:")

# Condicionales
print("\nCondicionales:")
if 5 > 2:
    print("5 es mayor que 2")
else:
    print("5 no es mayor que 2")

# Iterativas
print("\nIterativas:")
for i in range(5):
    print(i)

# Excepciones
print("\nExcepciones:")
try:
    print(5 / 0)
except ZeroDivisionError:
    print("No se puede dividir por cero")

# Programa que imprime por consola todos los números comprendidos entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3
print("\nPrograma que imprime por consola todos los números comprendidos entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3:")
for i in range(10, 56):
    if i % 2 == 0 and i != 16 and i % 3 != 0:
        print(i)