"""EJERCICIO:
Utilizando tu lenguaje, emplea 3 mecanismos diferentes para imprimir
números del 1 al 10 mediante iteración."""


def print_to_10_using_for():
    print('Using "For" loop:')
    for i in range(1, 11):
        print(i, end=' ')


def print_to_10_using_while():
    print('\nUsing "While" loop:')
    n = 1
    while n < 11:
        print(n, end=' ')
        n += 1


def print_to_10_using_recursive(num):
    if num < 11:
        print(num, end=' ')
        num += 1
        print_to_10_using_recursive(num)
    else:
        return


def print_to_5_using_list_comprehension():
    print('\nIteration using list comprehension')
    numbers = [num for num in range(1, 6)]
    print(numbers)


def print_to_5_using_iterators():
    print('Iteration using iterators')
    numbers = [num for num in range(1, 6)]
    iter_number = iter(numbers)
    while True:
        try:
            value = next(iter_number)
            print(value, end=' ')
        except StopIteration:
            break


def print_to_5_using_enumerate_method():
    print('\nIteration using enumerate method')
    numbers = [num for num in range(1, 6)]
    for _, number in enumerate(numbers):
        print(number, end=' ')


def print_to_5_using_zip_function():
    print('\nIteration using zip function')
    for _, number in zip(range(1, 6), range(1, 6)):
        print(number, end=' ')


def print_to_5_using_keys_in_dictionary():
    print('\nIteration using keys of a dictionary')
    numbers_dict = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5}
    for key in numbers_dict:
        print(key, end=' ')


def print_to_5_using_map_function():
    def print_number(n):
        print(n, end=' ')

    print('\nIteration using map function')
    numbers_map = map(print_number, range(1, 6))
    list(numbers_map)


"""DIFICULTAD EXTRA (opcional):
Escribe el mayor número de mecanismos que posea tu lenguaje
para iterar valores. ¿Eres capaz de utilizar 5? ¿Y 10?"""

print_to_10_using_for()
print_to_10_using_while()
print('\nUsing "Recursive" loop:')
print_to_10_using_recursive(1)

print_to_5_using_list_comprehension()
print_to_5_using_iterators()
print_to_5_using_enumerate_method()
print_to_5_using_zip_function()
print_to_5_using_keys_in_dictionary()
print_to_5_using_map_function()
