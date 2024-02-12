#01 Roadmap

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


# Aritméticos
a = 10
b = 3

suma = a + b        # Suma
resta = a - b       # Resta
multiplicacion = a * b  # Multiplicación
division = a / b    # División
division_entera = a // b  # División entera
resto = a % b       # Resto
potencia = a ** b   # Potencia


# Comparación
x = 5
y = 10

igual = x == y     # Igual a
diferente = x != y  # Diferente de
mayor = x > y       # Mayor que
menor = x < y       # Menor que
mayor_igual = x >= y   # Mayor o igual que
menor_igual = x <= y   # Menor o igual que


# Asignación
a = 5
b = 10

a += b     # a = a + b
a -= b     # a = a - b
a *= b     # a = a * b
a /= b     # a = a / b
a %= b     # a = a % b
a **= b    # a = a ** b
a //= b    # a = a // b


# Identidad
lista1 = [1, 2, 3]
lista2 = [1, 2, 3]

identidad = lista1 is lista2     # Compara identidad de objetos
no_identidad = lista1 is not lista2  # Compara no identidad de objetos

# Pertenencia
elemento_en_lista = 1 in lista1      # Comprueba si un elemento está en la lista
elemento_no_en_lista = 4 not in lista1  # Comprueba si un elemento no está en la lista


# Bits
bitwise_and = 5 & 3     # AND a nivel de bits
bitwise_or = 5 | 3      # OR a nivel de bits
bitwise_xor = 5 ^ 3     # XOR a nivel de bits
bitwise_not = ~5        # NOT a nivel de bits
left_shift = 5 << 1     # Desplazamiento a la izquierda
right_shift = 5 >> 1    # Desplazamiento a la derecha



# Estructura de control if
numero = 10

if numero > 0:
    print("El número es positivo.")
elif numero < 0:
    print("El número es negativo.")
else:
    print("El número es cero.")


# Estructura de control for
for i in range(5):
    print("Iteración:", i)


# Estructura de control try-except
try:
    resultado = 10 / 2
except ZeroDivisionError:
    resultado = "Error: División por cero."
finally:
    print("Resultado:", resultado)