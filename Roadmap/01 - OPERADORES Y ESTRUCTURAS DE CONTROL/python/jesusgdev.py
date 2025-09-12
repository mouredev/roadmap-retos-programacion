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

# 1. Tipos de operadores en Python

# Aritméticos
a = 8
b = 5

# operadore suma
suma = a + b
print(suma) # 13

# operadore resta
resta = a - b
print(resta) # 3

# operadore multiplicación
multiplicacion = a * b
print(multiplicacion) # 40

# operadore división
division = a / b
print(division) # 1.6

# operadore división entera
division_entera = a // b
print(division_entera) # 1

# operadore módulo
modulo = a % b
print(modulo) # 3

# operadore potencia
potencia = a ** b
print(potencia) # 32768

# Lógicos
x = True
y = False

print(x and y)  # False
print(x or y)   # True
print(not x)    # False

# Comparación
a = 5
b = 7
print(a == b)  # False
print(a != b)  # True
print(a > b)   # False
print(a < b)   # True
print(a >= b)  # False
print(a <= b)  # True

# Asignación
c = 9
c += 1  # c = c + 1
print(c)  # 10
c -= 2  # c = c - 2
print(c)  # 8
c *= 2  # c = c * 2
print(c)  # 16
c /= 4  # c = c / 4
print(c)  # 4.0
c //= 2  # c = c // 2
print(c)  # 2.0
c %= 2  # c = c % 2
print(c)  # 0.0
c **= 3  # c = c ** 3
print(c)  # 0.0

# Identidad
x = [1, 2, 3]
y = x
z = [1, 2, 3]

print(x is y)  # True, porque y es una referencia al mismo objeto que x
print(x is z)  # False, porque z es un objeto diferente aunque tenga el mismo contenido
print(x is not z)  # True, porque z es un objeto diferente
print(x == z)  # False, porque a y b son diferentes objetos

# Pertenencia
lista = [1, 2, 3, 4, 5]
print(3 in lista)  # True, porque 3 está en la lista
print(6 not in lista)  # True, porque 6 no está en la lista 

# Bits
a = 5  # 0101 en binario
b = 3  # 0011 en binario
print(a & b)  # 1, porque 0101 & 0011 = 0001
print(a | b)  # 7, porque 0101 | 0011 = 0111
print(a ^ b)  # 6, porque 0101 ^ 0011 = 0110
print(~a)     # -6, porque ~0101 = 1010 (en complemento a dos)
print(a << 1)  # 10, porque 0101 << 1 = 1010
print(a >> 1)  # 2, porque 0101 >> 1 = 0010

# 2. Estructuras de control en Python

# Condicionales
edad = 20
if edad < 18:
    print("Eres menor de edad")
elif edad < 65:
    print("Eres adulto")
else:
    print("Eres mayor de edad")
# Iterativas (for y while)
# Bucle for
for i in range(5):
    print(f"Bucle for: {i}")

# Bucle while
contador = 0
while contador < 5:
    print(f"Bucle while: {contador}")
    contador += 1

# Control de flujo: break y continue
for i in range(10):
    if i == 5:
        break  # Sale del bucle cuando i es 5
    print(f"Break ejemplo: {i}")
for i in range(10):
    if i % 2 == 0:
        continue  # Salta a la siguiente iteración si i es par
    print(f"Continue ejemplo: {i}")

# Manejo de excepciones
try:
    resultado = 10 / 0
except ZeroDivisionError:   
    print("Error: División por cero")
else:
    print("División exitosa")
finally:
    print("Bloque finally ejecutado")

# DIFICULTAD EXTRA (opcional)
'''
1. Numeros entre 10 y 55
2. pares excepto el 16
3. Que no sean multiplos de 3
'''
for i in range(10, 56):
    if (i % 2 == 0 and i != 16) and i % 3 != 0:
        print(i)   
