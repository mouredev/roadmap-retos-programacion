"""
 * EJERCICIO:
 * Utilizando tu lenguaje, emplea 3 mecanismos diferentes para imprimir
 * números del 1 al 10 mediante iteración.
"""

for i in range(1, 11):
    print(i)

i = 1
while i <= 10:
    print(i)
    i += 1


[print(i) for i in range(1, 11)]


"""
 * DIFICULTAD EXTRA (opcional):
 * Escribe el mayor número de mecanismos que posea tu lenguaje
 * para iterar valores. ¿Eres capaz de utilizar 5? ¿Y 10?
"""

for i in range(1, 11):
    print(i)

i = 1
while i <= 10:
    print(i)
    i += 1

[print(i) for i in range(1, 11)]

list(map(lambda x: print(x), range(1, 11)))

list(filter(lambda x: print(x) or True, range(1, 11)))

from functools import reduce
reduce(lambda _, x: print(x), range(1, 11), None)

iterator = iter(range(1, 11))
for i in iterator:
    print(i)

for index, value in enumerate(range(1, 11), start=1):
    print(value)

for i, _ in zip(range(1, 11), range(1, 11)):
    print(i)

import itertools
counter = itertools.cycle(range(1, 11))
for _ in range(10):
    print(next(counter))
