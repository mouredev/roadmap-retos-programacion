###############################################################################
## EJERCICIO
###############################################################################
print("\n1# Bucle for")
for numero in range(10):
    print(numero+1)


print("\n2# Bucle While")
number = 1
while number <= 10:
    print(number)
    number += 1


print("\n3#Funcion Recursiva")
def counter(number=1):
    if number == 10:
        print(10)
        return
    else:
        print(number)
        counter(number+1)
counter()


###############################################################################
## DIFICULTAD EXTRA
###############################################################################
print("\n4# En una linea")
[print(number) for number in range(1, 11)]

print("\n5# While + break")
number = 1
while True:
    if number <= 10:
        print(number)
        number += 1
    else:
        break

print("\n6# While + break")
number = 1
while True:
    print(number)
    number += 1
    if number == 11:
        break

print("\n7# Bucle for con lista predefinida")
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for numero in numeros:
    print(numero)

print("\n8# Función Map:")
list(map(lambda x: print(x), range(1, 11)))

print("\n9# Usando la Función reduce():")
from functools import reduce
reduce(lambda _, numero: print(numero), range(1, 11), None)

print("\nUsando NumPy arange():")
import numpy as np
for numero in np.arange(1, 11):
    print(numero)

