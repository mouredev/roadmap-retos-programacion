"""
 * EJERCICIO:
 * X) Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
 *   Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
 *   (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
 * x) Utilizando las operaciones con operadores que tú quieras, crea ejemplos
 *   que representen todos los tipos de estructuras de control que existan
 *   en tu lenguaje:
 *   Condicionales, iterativas, excepciones...
 * 3) Debes hacer print por consola del resultado de todos los ejemplos.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
"""

"""Operador aritméticos:"""

# Suma
variable = 1 + 1

# Resta
variable = 1 - 1

# Multiplicación
variable = 1 * 1

# División
variable = 1/1

# División Entera
variable = 1//1

# Resto de la División
variable = 1 % 1

# Potencia
variable = 1**1

"""Operador de asignación:"""

# Asignación
variable = 0

# Asignación con suma
variable += 1

# Asignación con resta
variable -= 1

# Asignación con multiplicación
variable *= 1

# Asignación con división
variable /= 1

# Asignación con división entera
variable //= 1

# Asignación con resto de división
variable %= 1

# Asignación con potencia
variable **= 1

"""Operadores de comparación"""
# Igual que
variable == 1

# No igual que
variable != 1

# Mayor que
variable > 1

# Menor que
variable < 1

# Mayor o igual que
variable >= 1

# Menor o igual que
variable <= 1

"""Operadores lógicos"""
# AND (esto y esto)
variable is 1

# OR (esto o esto)
variable or 1

"""Operadores de identidad"""
# Es
variable is str

# No es
variable is not int

"""Operadores de pertenencia"""
list_variables = []
# Esta en
variable in list_variables

# No esta en
variable not in list_variables

"""Operadores de bits"""
# AND (si ambos bits son 1)
1 & 1

# OR (mientras alguno sea 1)
1 | 1

# XOR (si solo hay 1)
1 ^ 1

# Desplaza bit a la izquierda
1 << 1

# Desplaza bit a la derecha
1 >> 1

"""Estructuras de control"""
a = 1
b = 2
c = 3
d = 4
e = 5
lista = [a, b, c]

# Condicionales
if a < b:
    print(b)
elif a > b:
    print(a)
else:
    print(f"{a} y {b} son iguales")

# Itinerables
for data in lista:
    print(data)

# Bucle condicional
while d not in lista:
    lista.append(d)
    print(f"{d} añadido a lista")

# Control de bucles/condicionales
while a < 10:
    if a == 1:
        a += 1
        pass
    elif e not in lista:
        a *= 2
        lista.append(e)
        print("continua el bucle")
        continue
    else:
        print("cerrando bucle")
        break

# Excepciones
try:
    print("hola" + True)
except TypeError as e:
    print(e)
else:
    print("No hubo fallos")
finally:
    print("Fin de la Gesntion de Excepciones")

"""Ejercicio Extra"""
lista_numeros = [number for number in range(
    1, 56) if number >= 10 and number % 3 != 0 and number % 2 == 0 and number != 16 or number == 55]
print(lista_numeros)
