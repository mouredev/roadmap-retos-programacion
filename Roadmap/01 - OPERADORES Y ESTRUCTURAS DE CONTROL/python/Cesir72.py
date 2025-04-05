# EJERCICIO RETO 01

# - Crea un comentario en el código y coloca la URL del sitio web oficial del lenguaje de programación que has seleccionado.

# https://www.python.org
"""
EJERCICIO:
- Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
  Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
  (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
  

- Utilizando las operaciones con operadores que tú quieras, crea ejemplos
  que representen todos los tipos de estructuras de control que existan
  en tu lenguaje:
  Condicionales, iterativas, excepciones...
- Debes hacer print por consola del resultado de todos los ejemplos.
"""

# OPERADORES ARITMÉTICOS
# Suma
print(5 + 5)
# Resta
print(10 - 5)
# Multiplicación
print(5 * 5)
# División
print(10 / 2)
# Módulo
print(10 % 3)
# Potencia
print(2 ** 3)
# División entera
print(10 // 3)      


# OPERADORES DE COMPARACIÓN
# Igual
print(5 == 5)
# Distinto
print(5 != 5)
# Mayor que
print(10 > 5)
# Menor que
print(5 < 10)
# Mayor o igual que
print(10 >= 10)
# Menor o igual que
print(5 <= 10)  

# OPERADORES LÓGICOS
# AND
print(True and True)
# OR
print(True or False)
# NOT
print(not True) 
# XOR
print(True != True)

# OPERADORES DE ASIGNACIÓN
# Igual
a = 5
print(a)
# Suma
a += 5
print(a)
# Resta
a -= 5
print(a)
# Multiplicación
a *= 5
print(a)
# División
a /= 5
print(a)
# Módulo
a %= 3
print(a)
# Potencia
a **= 3
print(a)
# División entera
a //= 3
print(a)

# OPERADORES DE IDENTIDAD
# is
print(5 is 5)
# is not
print(5 is not 5)       

# OPERADORES DE PERTENENCIA
# in
print(5 in [1, 2, 3, 4, 5])
# not in
print(5 not in [1, 2, 3, 4, 5])     

# OPERADORES DE BITS
# AND
print(5 & 3)
# OR
print(5 | 3)
# XOR
print(5 ^ 3)
# NOT
print(~5)
# Desplazamiento a la izquierda
print(5 << 1)
# Desplazamiento a la derecha
print(5 >> 1)   


# ESTRUCTURAS DE CONTROL
# CONDICIONALES
# IF
if 5 == 5:
    print("5 es igual a 5")
# IF ELSE
if 5 != 5:
    print("5 es distinto de 5")


# ITERATIVAS
# FOR
for i in range(5):
    print(i)
# WHILE
i = 0
while i < 5:
    print(i)
    i += 1      

# EXCEPCIONES
try:
    print(5 / 0)
except ZeroDivisionError:
    print("No se puede dividir por cero")   


"""
DIFICULTAD EXTRA (opcional):
Crea un programa que imprima por consola todos los números comprendidos
entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.

Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.
"""
# EJERCICIO RETO 02
# Crea un programa que imprima por consola todos los números comprendidos entre 10 y 55 (incluidos).
for i in range(10, 56):
    if i % 2 == 0 and i != 16 and i % 3 != 0:
        print(i)            # Imprime los números del 10 al 55






