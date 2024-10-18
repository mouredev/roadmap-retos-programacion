"""
EJERCICIO:
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



#Operadores aritméticos
x,y = 4,5

#Suma
print(f"Suma: {x + y = }")

#Resta
print(f"Resta: {x - y = }")

#Producto
print(f"Producto: {x * y = }")

#Division flotante
print(f"Divison flotante: {x / y = }")

#Division entera
print(f"Divison entera: {x // y = }")

#Division residual
print(f"Mod: {x%y = }")



#Operadores de comparacion

print(f"{x > y = }")
print(f"{x < y = }")
print(f"{x == y = }")
print(f"{x != y = }")
print(f"{x >= y = }")
print(f"{x <= y = }")


#Asignacion
x = 5  # Asignación simple
print(x)  # 5

x += 3  # Equivalente a x = x + 3
print(x)  # 8

x -= 2  # Equivalente a x = x - 2
print(x)  # 6

x *= 4  # Equivalente a x = x * 4
print(x)  # 24

x /= 2  # Equivalente a x = x / 2
print(x)  # 12.0

x //= 3  # Equivalente a x = x // 3 (división entera)
print(x)  # 4.0

x %= 3  # Equivalente a x = x % 3
print(x)  # 1.0

x **= 2  # Equivalente a x = x ** 2
print(x)  # 1.0


#Operadores Logicos
x = True
y = False

# AND lógico
print(x and y)  # False

# OR lógico
print(x or y)  # True

# NOT lógico
print(not x)  # False

#Identidad
a = [1, 2, 3]
b = [1, 2, 3]
c = a

# "is" verifica si son el mismo objeto
print(a is b)  # False (porque son listas diferentes en la memoria)

print(a is c)  # True (porque c es una referencia a a)

# "is not" verifica si no son el mismo objeto
print(a is not b)  # True

#Pertenencia
lista = [1, 2, 3, 4]

# "in" verifica si un valor está presente
print(3 in lista)  # True

# "not in" verifica si un valor no está presente
print(5 not in lista)  # True


#Operadores a nivel de bit
a = 10  # 1010 en binario
b = 4   # 0100 en binario

# AND bit a bit
print(a & b)  # 0 (0000)

# OR bit a bit
print(a | b)  # 14 (1110)

# XOR bit a bit
print(a ^ b)  # 14 (1110)

# Desplazamiento a la derecha
print(a >> 2)  # 2 (0010)

# Desplazamiento a la izquierda
print(a << 2)  # 40 (101000)


x = 8  # 1000 en binario

x &= 5  # x = x & 5 -> 1000 & 0101 = 0000
print(x)  # 0

x |= 3  # x = x | 3 -> 0000 | 0011 = 0011
print(x)  # 3

x ^= 2  # x = x ^ 2 -> 0011 ^ 0010 = 0001
print(x)  # 1

x <<= 1  # x = x << 1 -> 0001 << 1 = 0010
print(x)  # 2

x >>= 1  # x = x >> 1 -> 0010 >> 1 = 0001
print(x)  # 1


"""
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
 *
 * Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.
"""

print("*** Difiultad extra ***")
for n in range(10,56):
    if n%2 == 0 and n!=16 and n%3!=0:
        print(n)













