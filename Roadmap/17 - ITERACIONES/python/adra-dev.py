"""
EJERCICIO:
Utilizando tu lenguaje, emplea 3 mecanismos diferentes para imprimir
números del 1 al 10 mediante iteración.

DIFICULTAD EXTRA (opcional):
Escribe el mayor número de mecanismos que posea tu lenuaje para 
iterar valores. ¿Eres capaz de utilizar 5? ¿Y 10?

by adra-dev
"""

# For 
for i in range(1,11):
    print(i)

# While
i = 1 
while i <= 10:
    print(i)
    i +=1

# Recursividad 

def count_ten(i=1):
    if i <= 10:
        print(i)
        count_ten(i + 1)

count_ten()


"""
Extra
"""

for e in [1, 2, 3, 4]:
    print(e)

for e in {1, 2, 3, 4}:
    print(e)

for e in (1, 2, 3, 4):
    print(e)

for e in {1:"a", 2:"b", 3:"c", 4:"d"}:
    print(e)

for e in {1: "a", 2: "b", 3: "c", 4: "d"}.values():
    print(e)

print(*[i for i in range(1, 11)], sep="\n")

for c in "Python":
    print(c)

for e in reversed([1, 2, 3, 4]):
    print(e)

for e in sorted(["a", "d", "r", "i"]):
    print(e)

for i, e in enumerate(sorted(["a", "d", "r", "i"])):
    print(f"Índice: {i}, valor: {e}")