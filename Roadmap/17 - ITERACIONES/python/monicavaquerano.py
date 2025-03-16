# 17 ITERACIONES
# Monica Vaquerano
# https://monicavaquerano.dev

"""
/*
 * EJERCICIO:
 * Utilizando tu lenguaje, emplea 3 mecanismos diferentes para imprimir
 * números del 1 al 10 mediante iteración.
 *
 * DIFICULTAD EXTRA (opcional):
 * Escribe el mayor número de mecanismos que posea tu lenguaje
 * para iterar valores. ¿Eres capaz de utilizar 5? ¿Y 10?
 */
"""

print("\nFor Range Loop")
for i in range(1, 11):
    print(i, end=" ")

print("\nWhile Loop")
x = 0
while x < 10:
    x += 1
    print(x, end=" ")

print("\nMap() Function")


def impresion(x):
    print(x, end=" ")


list(map(impresion, range(1, 11)))

print("\n\n# Extra")

print("For Loop")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for number in numbers:
    print(number, end=" ")

print("\nRecursividad")


def printToTen(x):
    if x >= 10:
        print(10)
        return
    print(x, end=" ")
    printToTen(x + 1)


printToTen(1)

print("\nEnumerate() Function")
for i, number in enumerate(numbers, start=1):
    print(f"{i}.{number}", end=" ")

print("\nZip() Function")
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
for number, letter in zip(numbers, letters):
    print(f"{number}.{letter}", end=" ")

print("\nIterators")
# Un iterador es un objeto que implementa los métodos __iter__() y __next__().
# Se utiliza para recorrer una secuencia de elementos.

my_list = [1, 2, 3]
my_iter = iter(my_list)
print(next(my_iter))  # 1
print(next(my_iter))  # 2
print(next(my_iter))  # 3

print("\nGenerators")
# Los generadores son una forma especial de crear iteradores utilizando la palabra clave yield.


def count_up_to(max):
    count = 1
    while count <= max:
        yield count
        count += 1


counter = count_up_to(5)
for num in counter:
    print(num, end=" ")


print("\nComprensiones")
# Las comprensiones en Python proporcionan una forma concisa de crear listas, conjuntos y diccionarios.

# Lista de comprensiones
squares = [x**2 for x in range(10)]
print(squares)

# Conjunto de comprensión
unique_squares = {x**2 for x in range(10)}
print(unique_squares)

# Diccionario de comprensiones
squares_dict = {x: x**2 for x in range(10)}
print(squares_dict)
