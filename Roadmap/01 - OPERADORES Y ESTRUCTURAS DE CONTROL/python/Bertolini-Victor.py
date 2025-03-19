"""
    EJERCICIO:
    1) Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
        Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
        (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
    2) Utilizando las operaciones con operadores que tú quieras, crea ejemplos
        que representen todos los tipos de estructuras de control que existan
        en tu lenguaje:
        Condicionales, iterativas, excepciones...
    *Debes hacer print por consola del resultado de todos los ejemplos.

    DIFICULTAD EXTRA (opcional):
    3)  Crea un programa que imprima por consola todos los números comprendidos
        entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
"""

# 1) 

# Arithmetic Operators
x = 10
y = 3

print("First we have the arithmetic operators.")
print("")
print(f"Addition: {x} + {y} = {x + y}")
print(f"Subtraction: {x} - {y} = {x - y}")
print(f"Multiplication: {x} * {y} = {x * y}")
print(f"Division: {x} / {y} = {x / y}")
print(f"Modulus: {x} % {y} = {x % y}")
print(f"Exponentiation: {x} ** {y} = {x ** y}")
print(f"Floor division: {x} // {y} = {x // y}")

# Assignment Operators
print("")
print("Second we have the assignment operators.")
print("")
x = 5
print(f"Initial value of x: {x}")
x += 2
print(f"After x += 2, x: {x}")
x -= 2
print(f"After x -= 2, x: {x}")
x *= 2
print(f"After x *= 2, x: {x}")
x /= 2
print(f"After x /= 2, x: {x}")
x %= 3
print(f"After x %= 3, x: {x}")
x //= 2
print(f"After x //= 2, x: {x}")
x **= 2
print(f"After x **= 2, x: {x}")

# Comparison Operators
x = 10
y = 3
print("")
print("In third we have the comparison operators.")
print("")
print(f"Equal: {x} == {y} is {x == y}")
print(f"Not equal: {x} != {y} is {x != y}")
print(f"Greater than: {x} > {y} is {x > y}")
print(f"Less than: {x} < {y} is {x < y}")
print(f"Greater than or equal to: {x} >= {y} is {x >= y}")
print(f"Less than or equal to: {x} <= {y} is {x <= y}")

# Logical Operators
x = True
y = False

print("")
print("In fourth we have the logical operators.")
print("")

print(f"AND: {x} and {y} is {x and y}")
print(f"OR: {x} or {y} is {x or y}")
print(f"NOT: not {x} is {not x}")

# Identity Operators
x = ["star", "wars"]
y = ["star", "wars"]
z = x

print("")
print("In fifth we have the identity operators.")
print("")


print(f"IS: x is z is {x is z}")
print(f"IS NOT: x is not y is {x is not y}")

# Membership Operators
x = ["star", "wars"]

print("")
print("In fifth we have the membership  operators.")
print("")


print(f"IN: 'wars' in x is {'wars' in x}")
print(f"NOT IN: 'pineapple' not in x is {'pineapple' not in x}")

# Bitwise Operators
x = 10  # binary: 1010
y = 4   # binary: 0100

print("")
print("Last but not least we have the bitwise operators.")
print("")


print(f"AND: {x} & {y} = {x & y}")
print(f"OR: {x} | {y} = {x | y}")
print(f"XOR: {x} ^ {y} = {x ^ y}")
print(f"NOT: ~{x} = {~x}")
print(f"Zero fill left shift: {x} << 2 = {x << 2}")
print(f"Signed right shift: {x} >> 2 = {x >> 2}")


# 2)

# Conditionals (if, elif, else)
x = 10
y = 20

print("")
print("Conditionals (if, elif, else)")
print("")

if x < y:
    print("x is less than y")
elif x > y:
    print("x is greater than y")
else:
    print("x is equal to y")


# Loops (For, while, Break, Continue)
p = []
o = []
h = []
t = []

print("")
print("Loops (for, while, Break, Continue)")
print("")

# For loop
for i in range(5):
    p.append(i) 
print(p)

# While loop
i = 0
while i < 5:
    o.append(i)
    i += 1
print(o)

# Break
for i in range(5):
    if i == 3:
        break
    h.append(i)
print(h)

# Continue
for i in range(5):
    if i == 3:
        continue
    t.append(i)
print(t)


# Execeptions.
print("")
print("Exceptions.")
print("")

try:
    print(13)
except NameError:
    print("Variable x is not defined")
finally:
    print("The 'try except' is finished")



# 3) Extra Excercise. 


""" 
    Crea un programa que imprima por consola todos los números comprendidos
    entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3
"""
def printPairNumbersFrom10To55():
    k = []
    for j in range(10, 55):
        if j != 16 and j % 3 != 0 and j % 2 == 0:
            k.append(j)
    print(k)

print(" ")
print("Extra exercise:")
print("")
printPairNumbersFrom10To55()