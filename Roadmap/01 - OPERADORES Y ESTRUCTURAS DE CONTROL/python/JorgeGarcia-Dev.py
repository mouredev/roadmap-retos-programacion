# * EJERCICIO:
#  * - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
#  *   Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
#  *   (Ten en cuenta que cada lenguaje puede poseer unos diferentes)

print("****ARITMÉTICOS****")

a = 10
b = 5

sum = a + b
print(sum)

sub = a - b
print(sub)

mult = a * b
print(mult)

div = a / b
print(div)

residuo = a % b == 0
print(residuo)

potencia = a**b
print(potencia)

div_int = a // b
print(div_int)

print("****LÓGICOS****")

print(f"and: True and True = {True and True}")
print(f"or: True or False = {True or False}")
print(f"not: not True = {not True}")

print("****DE COMPARACIÓN****")

print(f"Mayor: {a} > {b} = {a > b}")
print(f"Mayor o igual: {a} >= {b} = {a >= b}")
print(f"Menor: {a} < {b} = {a < b}")
print(f"Menor o igual: {a} <= {b} = {a <= b}")
print(f"Igual: {a} == {b} = {a == b}")
print(f"Distinto: {a} != {b} = {a != b}")

print("****ASIGNACIÓN****")

a = 10
b = 5

a += b
print(a)

a -= b
print(a)

a *= b
print(a)

a /= b
print(a)

a %= b
print(a)

a //= b
print(a)

a **= b
print(a)

print("****IDENTIDAD****")

print(f"Is: {a} is {b} = {a is b}")
print(f"Is not: {a} is not {b} = {a is not b}")

print("****PERTENENCIA****")

print(f"In: {a} in [1, 2, 3] = {a in [1, 2, 3]}")
print(f"Not in: {a} not in [1, 2, 3] = {a not in [1, 2, 3]}")

print("****BITS****")

a = 0b1010
b = 0b1101

print(f"Bitwise and: {bin(a)} & {bin(b)} = {bin(a & b)}")
print(f"Bitwise or: {bin(a)} | {bin(b)} = {bin(a | b)}")
print(f"Bitwise xor: {bin(a)} ^ {bin(b)} = {bin(a ^ b)}")
print(f"Bitwise not: ~{bin(a)} = {bin(~a)}")
print(f"Bitwise left shift: {bin(a)} << {bin(b)} = {bin(a << b)}")
print(f"Bitwise right shift: {bin(a)} >> {bin(b)} = {bin(a >> b)}")

#  * - Utilizando las operaciones con operadores que tú quieras, crea ejemplos
#  *   que representen todos los tipos de estructuras de control que existan
#  *   en tu lenguaje:
#  *   Condicionales, iterativas, excepciones...
#  * - Debes hacer print por consola del resultado de todos los ejemplos.

print("****CONDICIONALES****")

if a < b:
    print(f"{a} es menor que {b}")
elif a > b:
    print(f"{a} es mayor que {b}")
else:
    print(f"{a} es igual que {b}")

print("****ITERATIVAS****")

for i in "Exercises":
    print(i)

for i in range(11):
    print(i)

num = 1
while num <= 5:
    print(num)
    num += 1

print("****EXCEPCIONES****")

num1 = 5
num2 = 0

try:
    num3 = num1 / num2
except Exception:
    print("Ha habido una excepción")

#  * DIFICULTAD EXTRA (opcional):
#  * Crea un programa que imprima por consola todos los números comprendidos
#  * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.

print("****DIFICULTAD EXTRA****")


def pares():
    for i in range(10, 56):
        if i % 2 == 0 and i % 3 != 0 or i == 16:
            print(i)


pares()

#  * Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.
