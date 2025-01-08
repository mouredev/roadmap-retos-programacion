"""
1. Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
(Ten en cuenta que cada lenguaje puede poseer unos diferentes) 
"""
# Operadores aritmeticos
print(suma=15 + 5)
print(resta=39 - 12)
print(multiplicacion=12 * 3)
print(division=12 / 4)
print(resto=12 % 5)
print(potencia=3**2)
print(division_resultado_entero=15 // 4)

# Operadores Relacionales
print(igualdad=15 == 15)
print(distinto=15 != 15)
print(mayor=15 > 15)
print(menor=15 < 15)
print(mayorIgual=15 >= 15)
print(menorIgual=15 <= 15)

# Operadores bit a bit
print(and_=2 & 1)
print(or_=2 | 1)
print(xor=2 ^ 1)
print(not_=~2)
print(shift_left=2 << 1)
print(shift_right=2 >> 1)

# Operadores asignacion
a = 100
print(a=10)
a += 1
print(a)
a -= 1
print(a)
a /= 3
print(a)
a *= 3
print(a)
a %= 3
print(a)
a **= 3
print(a)
a //= 3
print(a)
a &= 3
print(a)
a ^= 3
print(a)
a <<= 3
print(a)
a >>= 3
print(a)

# Operadores lógicos
print(and_=True and True)
print(or_=True or False)
print(not_=not True)

# Operadores de pertinencia
print(a=[1, 2, 3])
print(x=3 in a)
print(y=4 not in a)

# Operadores de identidad
print(x=4 is 4)
print(z=4 is not 4)

#
"""
2. Utilizando las operaciones con operadores que tú quieras, crea ejemplos
que representen todos los tipos de estructuras de control que existan
en tu lenguaje:
Condicionales, iterativas, excepciones...
"""
# if-elif-else
x = 10
z = 3
if x > z:
    print("x es mayor que z")
elif x < z:
    print("x es menor que z")
else:
    print("x es igual a z")

# for
for i in range(10):
    print(i)

# while
while i < 10:
    print(i)

# exception
try:
    1 / 0
except NameError:
    print("No se puede dividir entre cero")
    print("Cambiar numero divisor")
finally:
    print("Cambiar numero divisor")

#
""" 
3. Debes hacer print por consola del resultado de todos los ejemplos.
"""
"""
4. Crea un programa que imprima por consola todos los números comprendidos
entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
"""
for i in range(10, 56):
    if i % 2 == 0 and i != 16 and i % 3 != 0:
        print(i)
