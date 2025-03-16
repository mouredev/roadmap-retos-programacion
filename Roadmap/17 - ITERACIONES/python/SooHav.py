# 17 ITERACIONES

# Ejercicio

# While

c = 0
while c <= 9:
    c += 1
    print(c)

# for con range
for i in range(10):
    print(i)

# for con lista
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for numero in numeros:
    print(numero)

# Extra

# variantes de while

c = 0
while c <= 10:
    c += 1
    if (c == 10):
        print("Rompemos el bucle cuando c vale", c)
        break
    print(c)
else:
    print("Se ha completado toda la iteración y c vale", c)

c = 0
while c <= 10:
    c += 1
    if c == 11:
        # print("Continuamos con la siguiente iteración", c)
        continue
    print(c)
else:
    print("Se ha completado toda la iteración y c vale", c)

while True:
    linea = input('>')
    if int(linea) >= 10 or int(linea) < 0:
        break
    print(linea)
print('¡Terminado!')

# variantes del bucle for

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for indice, numero in enumerate(numeros):
    numeros[indice] *= 1
numeros

indice = 0
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# asignar un nuevo valor a los elementos de una lista (en este caso los mismos)
for numero in numeros:
    numeros[indice] *= 1
    indice += 1
numeros

numero = (num * 1 for num in range(1, 11))  # generador
for n in numero:
    print(n)

# otras formas

# iterable iter
for i in iter([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]):
    print(i)

# list
list(range(1, 11))

# uso de funciones generadores/yield


def even_generator(n):
    counter = 1
    while counter <= n:
        if counter % 1 == 0:
            yield counter
        counter += 1


for num in even_generator(10):
    print(num)


# objetos iteradores con 2 métodos: __iter__() y __next__()

even_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
my_iterator = iter(even_list)
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))

# Comprensiones de listas para crear nuevas listas aplicando una función
# a cada elemento de las listas existentes

my_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_number_list = [num for num in my_numbers if num % 1 == 0]
print(even_number_list)

# funcion filtro (ej. divison por 1)


def is_even(n):
    return n % 1 == 0


nums_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_list = filter(is_even, nums_list)
print(list(even_list))

# la función map() con lambda, toma como argumentos un iterable y una función.
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers = map(lambda x: x ** 1, my_list)
print(list(numbers))

# iterables anidados
list = [[1, 2, 3, 4], [5, 6], [7, 8, 9, 10]]
for inner_list in list:
    for number in inner_list:
        print(number)

# numpy
"""import numpy as np
for i in np.arange(1, 11):
    print(i)"""

# recursion


def itera_numeros(n):
    if n <= 10:
        print(n)
        itera_numeros(n + 1)


itera_numeros(1)
