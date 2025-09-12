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

# Suma
a = 5
b = 3
suma = a + b
print("Suma:", suma)  # Resultado: 8

# Resta
resta = a - b
print("Resta:", resta)  # Resultado: 2

# Multiplicación
multiplicacion = a * b
print("Multiplicación:", multiplicacion)  # Resultado: 15

# División
division = a / b
print("División:", division)  # Resultado: 1.6666666666666667

# División entera
division_entera = a // b
print("División entera:", division_entera)  # Resultado: 1

# Módulo (resto de la división)
modulo = a % b
print("Módulo:", modulo)  # Resultado: 2

# Exponenciación
exponenciacion = a ** b
print("Exponenciación:", exponenciacion)  # Resultado: 125

# AND lógico
x = True
y = False
and_logico = x and y
print("AND lógico:", and_logico)  # Resultado: False

# OR lógico
or_logico = x or y
print("OR lógico:", or_logico)  # Resultado: True

# NOT lógico
not_logico = not x
print("NOT lógico:", not_logico)  # Resultado: False

# Igualdad
a = 5
b = 3
igualdad = a == b
print("Igualdad:", igualdad)  # Resultado: False

# Desigualdad
desigualdad = a != b
print("Desigualdad:", desigualdad)  # Resultado: True

# Mayor que
mayor_que = a > b
print("Mayor que:", mayor_que)  # Resultado: True

# Menor que
menor_que = a < b
print("Menor que:", menor_que)  # Resultado: False

# Mayor o igual que
mayor_igual_que = a >= b
print("Mayor o igual que:", mayor_igual_que)  # Resultado: True

# Menor o igual que
menor_igual_que = a <= b
print("Menor o igual que:", menor_igual_que)  # Resultado: False

x = 5
# Asignación
x += 2  # Equivalente a: x = x + 2
print("Asignación:", x)  # Resultado: 7

x = [1, 2, 3]
y = [1, 2, 3]
z = x

# Identidad (comparando referencias de objetos)
identidad1 = x is y
print("Identidad 1:", identidad1)  # Resultado: False

identidad2 = x is z
print("Identidad 2:", identidad2)  # Resultado: True

# No Identidad
no_identidad = x is not y
print("No Identidad:", no_identidad)  # Resultado: True

# Pertenencia (comprobando si un valor está presente en una secuencia)
lista = [1, 2, 3, 4, 5]
pertenencia = 3 in lista
print("Pertenencia:", pertenencia)  # Resultado: True

# No Pertenencia
no_pertenencia = 6 not in lista
print("No Pertenencia:", no_pertenencia)  # Resultado: True

a = 10  # Representación binaria: 1010
b = 4   # Representación binaria: 0100

# AND a nivel de bits
and_bits = a & b
print("AND a nivel de bits:", and_bits)  # Resultado: 0 (binario: 0000)

# OR a nivel de bits
or_bits = a | b
print("OR a nivel de bits:", or_bits)    # Resultado: 14 (binario: 1110)

# XOR a nivel de bits
xor_bits = a ^ b
print("XOR a nivel de bits:", xor_bits)  # Resultado: 14 (binario: 1110)

# Desplazamiento a la izquierda
despl_izquierda = a << 2
print("Desplazamiento a la izquierda:", despl_izquierda)  # Resultado: 40 (binario: 101000)

# Desplazamiento a la derecha
despl_derecha = a >> 1
print("Desplazamiento a la derecha:", despl_derecha)  # Resultado: 5 (binario: 101)

