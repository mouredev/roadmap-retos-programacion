"""EJERCICIO"""

""""Tipos simples: Se pasan por valor, se crea una copia independiente al modificar.
    Tipos compuestos: Se pasan por referencia, se modifica la variable original al cambiar la copia."""

# Asignación por valor con enteros

my_number = 50
my_two_number = my_number
# Modifica y no afecta a la original
my_two_number = 34

print(f"My first number is: {my_number}")
print(f"My second number is: {my_two_number}")

# Asignación por valor con flotantes

my_float = 3.14
my_two_float = my_float
# Modifica y no afecta a la original
my_two_float = 2.71

print(f"My first float is: {my_float}")
print(f"My second float is: {my_two_float}")

# Asignación por valor con cadenas

my_string = "Sistema"
my_two_string = my_string
# Modifica y no afecta a la original
my_two_string = "Operativo"

print(f"My first string is: {my_string}")
print(f"My second string is: {my_two_string}")

# Asignación por referencia con listas

my_list = [1, 1, 2, 3, 5, 8, 13]
copy_list = my_list
# Modificar y sí afecta a la original
copy_list.append(4)

print(f"My list is: {my_list}")
print(f"My copy list is: {copy_list}")

# Asignación por referencia con diccionarios

my_diccionario = {"name": "María", "age": 17}
copy_diccionario = my_diccionario
# Modificar y sí afecta a la original
copy_diccionario["age"] = "25"

print(f"My dictionary is: {my_diccionario}")
print(f"My copy dictionary is: {copy_diccionario}")

""""Variables por valor: Se crea una copia independiente al pasarlas a una función. Modificar la copia no afecta a la variable original.
    Variables por referencia: Se modifica la variable original al pasarla a una función y modificarla dentro de la misma."""

# Asignación por valor en funciones


def multiply_number(number: int):
    number *= 2


n = 10
multiply_number(n)
print(f"My multiply_number is: {n}")

# Asignación por referencia en funciones


def multiply_numbers(numbers: list):
    for i, n in enumerate(numbers):
        numbers[i] *= 2


ns = [1, 5, 10]
multiply_numbers(ns)
print(f"My multiply_numbers is: {ns}")

"""DIFICULTAD EXTRA"""
# Por valor


def exchange_value(value_a: int, value_b: int):
    temp = value_a
    value_a = value_b
    value_b = temp
    return value_a, value_b


my_number_a = 10
my_number_b = 20

new_a, new_b = exchange_value(my_number_a, my_number_b)

print(f"Original value a: {my_number_a}")
print(f"Original value b: {my_number_b}")

print(f"New a: {new_a}")
print(f"New b: {new_b}")

# Por referencia


def exchange_reference(value_a: list, value_b: list) -> tuple:
    temp = value_a
    value_a = value_b
    value_b = temp
    return value_a, value_b


my_number_c = [10, 20]
my_number_d = [30, 40]

new_c, new_d = exchange_reference(my_number_c, my_number_d)

print(f"Original value c: {my_number_c}")
print(f"Original value d: {my_number_d}")

print(f"New c: {new_c}")
print(f"New d: {new_d}")
