"""
    Ejercicio:
    Utilizando tu lenguaje, emplea 3 mecanismos diferentes para imprimir
    números del 1 al 10 mediante iteración.
"""

# For
for i in range(i, 11):
    print(i)


# While
i = 1
while i <= 10:
    print(i)
    i += 1

# Recursión


def recursivo(i=1):
    if i <= 10:
        print(i)
        recursivo(i+1)


recursivo()


"""
    Dificultad Extra
    Escribe el mayor número de mecanismos que posea tu lenguaje
    para iterar valores
"""

for e in [1, 2, 3, 4]:
    print(e)

for e in {1, 2, 3, 4}:
    print(e)

for e in (1, 2, 3, 4):
    print(e)

print(*[i for i in range(1, 11)], sep="\n")

for c in "Python":
    print(c)

for e in reversed([1, 2, 3, 4]):
    print(e)
