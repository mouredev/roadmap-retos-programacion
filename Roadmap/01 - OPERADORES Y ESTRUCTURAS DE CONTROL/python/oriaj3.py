"""
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

### Operadores aritméticos 
a = 2
b = 3 

# Suma
print(f"La suma de {a} + {b} es: {a+b}")

# Resta
print(f"La resta de {a} - {b} es: {a-b}")

# Multiplicación
print(f"La multiplicación de {a} * {b} es: {a*b}")

# División
print(f"La división de {a} / {b} es: {a/b}")

# Módulo
print(f"El módulo de {a} % {b} es: {a%b}")

# Exponente
print(f"El exponente de {a} ** {b} es: {a**b}")

# División entera o Resto
print(f"La división entera de {a} // {b} es: {a//b}")

### Operadores de comparación
a = 2
b = 3

# Igualdad
print(f"¿{a} es igual a {b}?: {a==b}")

# Desigualdad
print(f"¿{a} es desigual a {b}?: {a!=b}")

# Mayor que
print(f"¿{a} es mayor que {b}?: {a>b}")

# Menor que 
print(f"¿{a} es menor que {b}?: {a<b}")

# Mayor o igual que
print(f"¿{a} es mayor o igual que {b}?: {a>=b}")

# Menor o igual que
print(f"¿{a} es menor o igual que {b}?: {a<=b}")

### Operadores lógicos
a = True
b = False

# AND
print(f"¿{a} AND {b}?: {a and b}")

# OR
print(f"¿{a} OR {b}?: {a or b}")

# NOT
print(f"¿NOT {a}?: {not a}")

### Operadores de asignación
a = 2
b = 3

# Asignación
print(f"¿a es igual a {a}?: {a}")

# Suma
a += b
print(f"¿a += {b}?: {a}")

# Resta
a -= b
print(f"¿a -= {b}?: {a}")

# Multiplicación
a *= b
print(f"¿a *= {b}?: {a}")

# División
a /= b
print(f"¿a /= {b}?: {a}")

# Módulo
a %= b
print(f"¿a %= {b}?: {a}")

# Exponente
a **= b
print(f"¿a **= {b}?: {a}")

# División entera
a //= b
print(f"¿a //= {b}?: {a}")

### Operadores de identidad
# Compara si una dirección de memoria es la misma
a = 2
b = 2.0

# is
print(f"¿{a} is {b}?: {a is b}")

# is not
print(f"¿{a} is not {b}?: {a is not b}")

### Operadores de pertenencia
a = 2
b = 3
c = [1, 2, 3, 4, 5]

# in
print(f"¿{a} in {c}?: {a in c}")

# not in
print(f"¿{a} not in {c}?: {a not in c}")

### Operadores de bits
a = 10
b = 11

# AND
print(f"¿{a} & {b}?: {a & b}")

# OR
print(f"¿{a} | {b}?: {a | b}")

# XOR
print(f"¿{a} ^ {b}?: {a ^ b}")

# NOT
print(f"¿~{a}?: {~a}")


b = 2

# Desplazamiento a la izquierda dos bits
print(f"¿{a} << {b}?: {a << b}")

# Desplazamiento a la derecha dos bits 
print(f"¿{a} >> {b}?: {a >> b}")

### Estructuras de control condicionales
a = 2
b = 3

# if
if a == b:
    print(f"¿{a} == {b}?: {a == b}")

# if-else
if a == b:
    print(f"¿{a} == {b}?: {a == b}")
else:
    print(f"¿{a} != {b}?: {a != b}")

# if-elif-else
if a == b:
    print(f"¿{a} == {b}?: {a == b}")
elif a > b:
    print(f"¿{a} > {b}?: {a > b}")
else:
    print(f"¿{a} < {b}?: {a < b}")

### Estructuras de control iterativas
a = 2
b = 3

# while
while a < b:
    print(f"¿{a} < {b}?: {a < b}")
    a += 1

# for
for i in range(a, b):
    print(f"¿{i} < {b}?: {i < b}")

### Estructuras de control de excepciones
a = 2
b = 0

# try-except
try:
    print(f"¿{a} / {b}?: {a / b}")
except ZeroDivisionError:
    print("No se puede dividir entre 0")

# try-except-else
b = 3
try:
    print(f"¿{a} / {b}?: {a / b}")
except ZeroDivisionError:
    print("No se puede dividir entre 0")
else:
    print(f"¿{a} / {b}?: {a / b}")
finally:
    print("Fin del manejo de excepciones")
    

    
### Ejercicio extra
# * DIFICULTAD EXTRA (opcional):
# Crea un programa que imprima por consola todos los números comprendidos
# entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
#
# Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.

# Solución 1
for i in range(10, 56):
    if i % 2 == 0 and i != 16 and i % 3 != 0:
        print(i)

# Solución 2
for i in range(10, 56, 2):
    if i != 16 and i % 3 != 0:
        print(i)

# Solución 3
for i in range(10, 56, 2):
    if i == 16 or i % 3 == 0:
        continue
    print(i)

# Solución 4
for i in range(10, 56, 2):
    if i == 16 or i % 3 == 0:
        break
    print(i)

# Solución 5
i = 10
while i < 56:
    if i % 2 == 0 and i != 16 and i % 3 != 0:
        print(i)
    i += 1

# Solución 6
i = 10
while i < 56:
    if i == 16 or i % 3 == 0:
        i += 1
        continue
    print(i)
    i += 1

# Solución 7
i = 10
while i < 56:
    if i == 16 or i % 3 == 0:
        break
    print(i)
    i += 1

# Solución 8
i = 10
while i < 56:
    if i % 2 == 0 and i != 16 and i % 3 != 0:
        print(i)
    i += 2

# Solución 9
i = 10
while i < 56:
    if i == 16 or i % 3 == 0:
        i += 2
        continue
    print(i)
    i += 2

# Solución 10
i = 10
while i < 56:
    if i == 16 or i % 3 == 0:
        break
    print(i)
    i += 2

# Solución 11
i = 10
while i < 56:
    if i % 2 != 0 or i == 16 or i % 3 == 0:
        i += 1
        continue
    print(i)
    i += 1