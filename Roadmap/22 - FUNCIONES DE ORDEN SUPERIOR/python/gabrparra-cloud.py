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
"""

from functools import reduce
from datetime import datetime


def apply_func(func,x):
    return print(func(x))

apply_func(len,"Hola mundo")

# Retorno de función

def apply_multiplier(n):
    def multiplier(x):
        return x * n
    return multiplier

multiplier = apply_multiplier(2)
print(multiplier(5))
print(apply_multiplier(3)(3))

# Sistema

numbers = [2,5,6,9,19]

# map()

def apply_double(n):
    return n * 2

print(list(map(apply_double,numbers)))

# filter

def is_even(n):
    return n % 2 == 0

print(list(filter(is_even,numbers)))

# Sorted

print(sorted(numbers))
print(sorted(numbers,reverse=True))
print(sorted(numbers,key=lambda x: -x))

# reduce
def sum02(x,y):
    return x + y

print(reduce(sum02,numbers))

"""
Extra
"""

students = [
    {"name": "Juan01", "birthdate": "01-04-1999", "grades":[5,8,9.1,7.5,6]},
    {"name": "Juan02", "birthdate": "02-01-1990", "grades":[6,7,3,4,5]},
    {"name": "Juan03", "birthdate": "03-04-1998", "grades":[9.2,9,3,7,5]}
]

def average(grades):
    return sum(grades) / len(grades)

print(list(map(lambda student: {"name": student["name"], "average": average(student["grades"])}, students)))

print(
    list(map(lambda student:
        student["name"],
        filter(lambda student: average(student["grades"]) >= 6, students)
            )
        )
    )

print(sorted(students, key=lambda student: datetime.strptime(
    student["birthdate"],"%d-%m-%Y"),reverse=True))

print(
    max(map(lambda student: 
    max(student["grades"]),students)))