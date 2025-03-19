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


def count_ten(i=1):
    if i <= 10:
        print(i)
        count_ten(i + 1)


count_ten()
