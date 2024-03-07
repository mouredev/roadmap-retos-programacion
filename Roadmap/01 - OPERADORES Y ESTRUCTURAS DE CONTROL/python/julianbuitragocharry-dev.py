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

# Aritmetic Operators
x = 10
y = 5.1
addition = x + y
print(addition)
subtraction = x - y
print(subtraction)
multiplication = x * y
print(multiplication)
division = x / y
print(division)
modulus = x % y
print(modulus)
exponential = x ** y
print(exponential)
floor_division = x // y
print(floor_division)

# Asygment Operators
x = 5
print(x)
x += 3
print(x)
x -= 3
print(x)
x *= 3
print(x)
x /= 3
print(x)
x %= 3
print(x)
x //= 3
print(x)
x **= 3
print(x)
x &= 3
print(x)
x |= 3
print(x)
x ^= 3 
print(x)
x >>= 3
print(x)
x <<= 3 
print(x)

# Comparision Operators
x = True
y = False
equal = x == y
print(equal)
not_equal = x != y
print(not_equal)
greater_than = x > y
print(greater_than)
less_than = x < y
print(less_than)
greater_than_or_equal_to = x >= y
print(greater_than_or_equal_to)
less_than_or_equal_to = x <= y
print(less_than_or_equal_to)

# Logical Operators
"""
or --> returns True if one of the statements is true
and --> returns True if both of the statements is true
not --> reverse the result
"""

# Identity
"""
is --> returns true if both variables are the same object
is not --> return true if both variables are not the same object
"""

# Membership
"""
in --> returns true if a sequence with the specified value is present in object
not in --> returns true if a sequence with the specified value is not present in object
"""

# Condictionals
year = 18
if year == 18:
    print('You can follow')
else:
    print('You can\'t follow')

# Iteratives
i = 0
while(i <= 10):
    print(i)
    i += 1

for i in range(0, 11):
    print(i)

# Exceptions
try:
    print(not_define)
except:
    print("An exception occurred")

def challenge():
    for numb in range(10, 56, 2):
        if numb == 16 or numb % 3 == 0:
            pass
        else:
            print(numb)

challenge()