""" /*
 * EJERCICIO:
 * Utilizando tu lenguaje, emplea 3 mecanismos diferentes para imprimir
 * números del 1 al 10 mediante iteración.
 *
 * DIFICULTAD EXTRA (opcional):
 * Escribe el mayor número de mecanismos que posea tu lenguaje
 * para iterar valores. ¿Eres capaz de utilizar 5? ¿Y 10?
 */ """

from os import sep


for i in range(1, 11):
    print(i)

i = 1
while i <= 10:
    print(i)
    i += 1


def count_recursive(index: int = 1):
    if index <= 10:
        print(index)
        count_recursive(index + 1)


count_recursive()

for e in [1, 2, 3, 4, 5]:
    print(e)

for e in {4, 5, 9, 3}:
    print(e)

for e in {1: "a", 2: "b", 3: "c"}:
    print(e)

print(*[i for i in range(1, 11)], sep="\n")

for ch in "python":
    print(ch)

for ch in reversed("python"):
    print(ch)

for e in sorted("lucas"):
    print(e)

for i, e in enumerate("lucas"):
    print(f"Indice: {i}, valor: {e}")

for e in {1: "a", 2: "b", 3: "c"}.values():
    print(e)
