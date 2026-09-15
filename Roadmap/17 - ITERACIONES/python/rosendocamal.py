"""
 * EJERCICIO:
 * Utilizando tu lenguaje, emplea 3 mecanismos diferentes para imprimir
 * números del 1 al 10 mediante iteración.
 *
 * DIFICULTAD EXTRA (opcional):
 * Escribe el mayor número de mecanismos que posea tu lenguaje
 * para iterar valores. ¿Eres capaz de utilizar 5? ¿Y 10?
"""

for i in range(0, 11):
    print(i)
else:
    print()


contador = 0

while contador != 10:
    contador += 1
    print(contador)
print()

def count(num: int):

    if num <= 10:
        print(num)
        count(num + 1)

count(1)
print()

n_stack = [1 for _ in range(0, 10)]
def stack(list, num):
    if list:
        result = list.pop() + num
        print(result)
        stack(list=list, num=result)

stack(num=0, list=n_stack)

print('\n', *[i for i in range(1, 11)], "\n", sep="\n")

for i in [i for i in range(1, 11)]:
    print(i)
else:
    print()


for i in {1, 2, 3, 4}:
    print(i)
else: 
    print()

for i in "Python"[::-1]:
    print(i)
else:
    print()