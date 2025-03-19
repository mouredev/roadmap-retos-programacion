'''
EJERCICIO 1 -> Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje de programación.
'''

# Operadores aritméticos (Un operador aritmético toma dos operandos como entrada y devuelve el resultado)

# Suma
print(f"Suma 12 + 3 = {12 + 3}")

# Resta
print(f"Resta 12 - 3 = {12 - 3}")

# Multiplicación
print(f"Multiplicación 12 * 3 = {12 * 3}")

# División
print(f"División 12 / 3 = {12 / 3}")

# División entera
print(f"División entera 12 // 3 = {12 // 3}")

# Módulo
print(f"Módulo 12 % 3 = {12 % 3}")

# Potencia
print(f"Potencia 12 ** 3 = {12 ** 3}")


# Operadores de asignación (Se utilizan para asignar valores a las variables)
x = 5 # Asigna el valor 5 a la variable x
print(x)
x += 3 # Equivale a x = x + 3
print(x)
x -= 3 # Equivale a x = x - 3
print(x)
x *= 3 # Equivale a x = x * 3
print(x)
x /= 3 # Equivale a x = x / 3
print(x)
x //= 3 # Equivale a x = x // 3
print(x)
x %= 3 # Equivale a x = x % 3
print(x)
x **= 3 # Equivale a x = x ** 3
print(x)
x &= 3 # Equivale a x = x & 3
print(x)
x |= 3 # Equivale a x = x | 3
print(x)
x ^= 3 # Equivale a x = x ^ 3
print(x)
x >>= 3 # Equivale a x = x >> 3
print(x)
x <<= 3 # Equivale a x = x << 3
print(x)


# Operadores relacionales (Se utilizan para comparar dos valores)
print(f"Igualdad 12 == 3 es {12 == 3}")
print(f"Desigualdad 12 != 3 es {12 != 3}")
print(f"Mayor que 12 > 3 es {12 > 3}")
print(f"Menor que 12 < 3 es {12 < 3}")
print(f"Mayor o igual que 12 >= 3 es {12 >= 3}")
print(f"Menor o igual que 12 <= 3 es {12 <= 3}")


# Operadores lógicos (Se utilizan para combinar expresiones condicionales)
print(f"AND 12 > 3 and 5 < 2 es {12 > 3 and 5 < 2}")
print(f"OR 12 > 3 or 5 < 2 es {12 > 3 or 5 < 2}")
print(f"NOT not 12 > 3 es {not 12 > 3}")

# Operadores de identidad (Se utilizan para comparar objetos, no si son iguales, sino si son realmente el mismo objeto, con la misma ubicación de memoria)
print(f"12 is 3 es {12 is 3}")
print(f"12 is not 3 es {12 is not 3}")

# Operadores de pertenencia (Se utilizan para comprobar si un valor está presente en una secuencia, como una cadena, una lista, una tupla, un conjunto, o un diccionario)
print(f"12 in [1, 2, 3] es {12 in [1, 2, 3]}")
print(f"12 not in [1, 2, 3] es {12 not in [1, 2, 3]}")


# Operadores de bits (Se utilizan para comparar números (binarios))
print(f"AND 12 & 3 = {12 & 3}")
print(f"OR 12 | 3 = {12 | 3}")
print(f"XOR 12 ^ 3 = {12 ^ 3}")
print(f"NOT ~12 = {~12}")
print(f"Desplazamiento a la derecha 12 >> 3 = {12 >> 3}")
print(f"Desplazamiento a la izquierda 12 << 3 = {12 << 3}")

'''
EJERCICIO 2 -> Crea ejemplos utilizando todas las estructuras de control de tu lenguaje de programación.
'''

# Condicionales
# IF
if 12 > 3:
    print("12 es mayor que 3")

# IF-ELSE
if 12 < 3:
    print("12 es menor que 3")
else:
    print("12 no es menor que 3")

# IF-ELIF-ELSE
if 12 < 3:
    print("12 es menor que 3")  
elif 12 == 3:
    print("12 es igual a 3")
else:
    print("12 no es menor que 3 ni igual a 3")

# Iterativas

# WHILE
i = 1
while i < 6:
    print(i)
    i += 1

# FOR
for i in range(1, 6):
    print(i)


'''
 DIFFICULTAD EXTRA
'''

for i in range(1, 56):
    if i % 2 == 0 and i != 16 and i % 3 != 0:
        print(i)