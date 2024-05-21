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

# Listado de operadores
print('--------------------------------')
print('Operadores aritméticos')
print('--------------------------------')
resultado = 10 + 5
print(resultado)

# Operador resta
resultado = 15 - 10
print(resultado)

# Operador división
resultado = 15 / 10
print(resultado)

# Operador división descartando el resto
resultado = 15 / 10
print(resultado)

print('--------------------------------')
print('Operadores lógicos')
print('--------------------------------')

resultado = True and True
print(resultado)

resultado = True or False
print(resultado)

resultado = not True
print(resultado)

print('--------------------------------')
print('Operadores de identidad')
print('--------------------------------')

resultado = 'Hello' is 'Hi'
print(resultado)

resultado = 'Hello' is 'Hello'
print(resultado)

resultado = 'Hello' is not 'Hi'
print(resultado)

print('--------------------------------')
print('Operadores de asignación')
print('--------------------------------')

resultado = 100
resultado += 1
print(resultado)

resultado = 100
resultado -= 1
print(resultado)

resultado = 100
resultado *= 3
print(resultado)

resultado = 100
resultado /= 3
print(resultado)

print('--------------------------------')
print('Operadores de pertenencia')
print('--------------------------------')

resultado = 'a' in ['a', 'b', 'c']
print(resultado)

resultado = 'z' in ['a', 'b', 'c']
print(resultado)

print('--------------------------------')
print('Operadores de bit')
print('--------------------------------')

resultado = 'a' in ['a', 'b', 'c']
print(resultado)

print('--------------------------------')
print('Estructuras de control')
print('--------------------------------')

print('--- If-elif-else ---')
a = 10
b = 100
if a == b:
    print('a es igual a b')
elif a > b:
    print('a es mayor a b')
else:
    print('a es menor a b')

print('--- for ---')
list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
for x in list:
    print(x)

print('--- try-except-finally ---')
a = 100
b = 'cien'

if str(a) == b:
    print('a es igual a b')
    
try:
    if a == int(b):
        print('a es igual a b')
except:
    print('Error: a y b no se pueden comparar')
finally:
    print('try-except ejecutado')

"""
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
"""
for x in range(10, 56):
    if x%2 == 0 and x != 16 and x%3 != 0:
        print(x)