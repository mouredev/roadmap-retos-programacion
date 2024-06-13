'''
 * EJERCICIO:
 * Utilizando tu lenguaje, emplea 3 mecanismos diferentes para imprimir
 * números del 1 al 10 mediante iteración.
 *
 * DIFICULTAD EXTRA (opcional):
 * Escribe el mayor número de mecanismos que posea tu lenguaje
 * para iterar valores. ¿Eres capaz de utilizar 5? ¿Y 10?
 */
'''

'''
Ejercicio
'''
# 1. For
for i in range(1, 11):
    print(i)

# 2. While
i = 1
while i <= 10:
    print(i)
    i += 1

# 3. Recursividad
def count(n=1):
    if n <= 10:
        print(n)
        count(n + 1)

count()

'''
Dificultad extra
'''

for e in [1, 2, 3, 4]:
    print(e)

for e in {1, 2, 3, 4}:
    print(e)

for e in (1, 2, 3, 4):
    print(e)

for e in {1: "a", 2: "b", 3:"c", 4:"d"}:
    print(e)

for e in {1: "a", 2: "b", 3:"c", 4:"d"}.values():
    print(e)

print(*[i for i in range(1, 11)], sep="\n")

for c in "Python":
    print(c)

for e in reversed([1, 2, 3, 4]):
    print(e)

for e in sorted(["c", "a", "b"]):
    print(e)

for index, value in enumerate(["a", "b", "c"]):
    print(f'Index: {index}, value: {value}')