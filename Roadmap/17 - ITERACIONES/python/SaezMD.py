#17 - ITERACIONES
"""
 * EJERCICIO:
 * Utilizando tu lenguaje, emplea 3 mecanismos diferentes para imprimir números del 1 al 10 mediante iteración.
 *
 * DIFICULTAD EXTRA (opcional):
 * Escribe el mayor número de mecanismos que posea tu lenguaje para iterar valores. ¿Eres capaz de utilizar 5? ¿Y 10?
"""

#Iteration from 1 to 10
#Option1:

for i in range(0,11):
    print(1,i)

#Option2:

counter = 0
while counter <= 9:
    counter += 1
    print(2,counter)

#Option3:

number_list = [1,2,3,4,5,6,7,8,9,10]
iterator = iter(number_list)

for element in iterator:
    print(3, element)

#EXTRA:


for e in [1, 2, 3, 4]:
    print(e)

for e in {1, 2, 3, 4}:
    print(e)

for e in (1, 2, 3, 4):
    print(e)

for e in {1: "a", 2: "b", 3: "c", 4: "d"}:
    print(e)

for e in {1: "a", 2: "b", 3: "c", 4: "d"}.values():
    print(e)

print(*[i for i in range(1, 11)], sep="\n")

for c in "Python":
    print(c)

for e in reversed([1, 2, 3, 4]):
    print(e)

for e in sorted(["m", "o", "u", "r", "e"]):
    print(e)

for i, e in enumerate(sorted(["m", "o", "u", "r", "e"])):
    print(f"Índice: {i}, valor: {e}")

