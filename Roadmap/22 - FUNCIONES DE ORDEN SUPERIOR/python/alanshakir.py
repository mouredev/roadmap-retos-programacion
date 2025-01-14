"""
 * EJERCICIO:
 * Explora el concepto de funciones de orden superior en tu lenguaje 
 * creando ejemplos simples (a tu elección) que muestren su funcionamiento.
 *
 * DIFICULTAD EXTRA (opcional):
 * Dada una lista de estudiantes (con sus nombres, fecha de nacimiento y 
 * lista de calificaciones), utiliza funciones de orden superior para 
 * realizar las siguientes operaciones de procesamiento y análisis:
 * - Promedio calificaciones: Obtiene una lista de estudiantes por nombre
 *   y promedio de sus calificaciones.
 * - Mejores estudiantes: Obtiene una lista con el nombre de los estudiantes
 *   que tienen calificaciones con un 9 o más de promedio.
 * - Nacimiento: Obtiene una lista de estudiantes ordenada desde el más joven.
 * - Mayor calificación: Obtiene la calificación más alta de entre todas las
 *   de los alumnos.
 * - Una calificación debe estar comprendida entre 0 y 10 (admite decimales).
 */
"""
from functools import reduce
from datetime import datetime
numbers = [2 , 5, 10, 21, 3, 30]
numbers_str = ['1', '2', '3', '4', '5']  # iterable

#Map -- devuelve un iterable

numbers_int = map(int, numbers_str)
print(list(numbers_int))    # [1, 2, 3, 4, 5]


def multiply_two(value):
    return value*2
print(list(map(multiply_two, numbers)))

#filter -- devuelve un iterable

def is_odd(num):
    if num % 2 != 0:
        return True
    return False

odd_numbers = filter(is_odd, numbers)
print(list(odd_numbers))

def filter_greater_than_ten(number):
    if number > 10:
        return True
    return False
print(list(filter(filter_greater_than_ten, numbers)))

#Reduce -- devuelve un unico valor

def add_two_nums(x, y):
    return int(x) + int(y)

total = reduce(add_two_nums, numbers_str)
print(total)

def sum_two_values_and_one(first_value, second_value):
    return first_value + second_value

print(reduce(sum_two_values_and_one, numbers))

#Extra
lista_estudiantes = [{"name":"Alan", "birthdate":"20-01-1985", "grades": [9,8,7.3]},
                     {"name":"Nico", "birthdate":"05-04-2014", "grades":[10,9.9,8]}, 
                     {"name":"Matheo",  "birthdate":"03-01-2024", "grades": [10,10,10]}]

# Promedio calificaciones
def averages(notes):
    return sum(notes) / len(notes)

print(list(map(lambda estudiante: 
               {"name": estudiante["name"],
                "average": averages(estudiante["grades"])}, lista_estudiantes)))

# Mejores estudiantes
print(list(map(lambda estudiante: 
               estudiante["name"],
               filter(lambda estudiante: averages(estudiante["grades"]) >= 9, lista_estudiantes) )))

#Nacimiento
print(sorted(lista_estudiantes, key=lambda estudiante: datetime.strptime(estudiante["birthdate"], "%d-%m-%Y"), reverse=True))

#Mayor calificación
print(max(map(lambda estudiante: max(estudiante["grades"]), lista_estudiantes)))
