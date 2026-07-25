'''
/*
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
 */
'''
# 1º punto del ejercicio
'''
- Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
 *   Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
 *   (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
'''

a, b, resultado = 10, 30, 0

# suma
resultado = a + b
# resta
resultado = a - b
# multiplicacion
resultado = a * b
# division
resultado = a / b
# division entera
resultado = a // b
# resto
resultado = a % b
# exponente
resultado = a ** b

# Comparacion
print(a == b)
# distinto
print(a != b)
# mayor
print(a > b)
# mayor igual
print(a >= b)
# menor
print(a < b)
# menor igual
print(a <= b)
# Operadores lógicos
a = True
b = False
# and
print(a and b)
# Or
print(a or b)
# not
print(not a)
print(not b)
#  Operadores Bit a Bit (Bitwise)
x = 5  # 101 en binario
y = 3  # 011 en binario
print(x & y)  # 001 → 1
print(x | y)  # 111 → 7
print(x ^ y)  # 110 → 6
print(~x)     # Complemento a 2 → -6
print(x << 1)  # Desplazamiento a la izquierda → 1010 → 10
print(x >> 1)  # Desplazamiento a la derecha → 10 → 2
# Operadores de Identidad
x = [1, 2, 3]
y = x
z = [1, 2, 3]
print(x is y)   # True (son el mismo objeto)
print(x is z)   # False (tienen los mismos valores, pero son objetos distintos)
print(x is not z)  # True
# Operadores de Pertenencia
lista = [1, 2, 3, 4]
print(2 in lista)       # True
print(5 not in lista)   # True

# 2º punto del ejercicio
'''
- Utilizando las operaciones con operadores que tú quieras, crea ejemplos
 *   que representen todos los tipos de estructuras de control que existan
 *   en tu lenguaje:
 *   Condicionales, iterativas, excepciones...
 * - Debes hacer print por consola del resultado de todos los ejemplos.
'''
# Comparar
a = 10
b = 30
if a > b:
    print("A es mayor que B")
else:
    print("A es menor que B")

lista = [1, 7, 8, 50, 6, 3]
# buscar número más alto bucle For.
n = lista[0]
for i in lista:
    if i > n:
        n = i
print(f"El número más alta de la lista es: {n}")

# bucle While
r = 1
print("**** Imprimo la tabla del 7 ****")
while r <= 10:
    print(f"7 * {r} = {7*r}")
    r += 1

# Control de excepciones
try:
    texto = int(input("Introduce un texto: "))
    print("Lo que ha introducido No es un caracter. No es Correcto")
except ValueError:
    print("Lo que ha introducido es un caracter. Es correcto")

# 3º punto del ejercicio
'''
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
'''
# Altenativa estandar
print("\nAlternativa estandar:\n")
for i in range(10, 56):
    if i % 2 == 0 and i != 16 and (i % 3 != 0):
        print(i)

# version por compresión
numeros_validos = [i for i in range(
    10, 56) if i % 2 == 0 and i != 16 and i % 3 != 0]
print(f"\nVersión por compresion: {numeros_validos}\n")

# Alternativa usando continue
print("\nAlternativa usando continue:\n")
for i in range(10, 56):
    if i == 16 or i % 2 != 0 or i % 3 == 0:
        continue
    print(i)
