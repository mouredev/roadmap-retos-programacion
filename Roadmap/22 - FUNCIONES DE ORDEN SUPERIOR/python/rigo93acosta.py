'''
## 22 FUNCIONES DE ORDEN SUPERIOR
/*
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
'''

from functools import reduce
from datetime import datetime

"""
Ejercicio
"""

# Funcion con argumento
def apply_func(func, x):
    return func(x)

print(apply_func(len, "Hola mundo"))

# Retorno de funcion

def apply_multiplier(n):
    def multiplier(x):
        return x * n
    return multiplier

x = apply_multiplier(2)
print(x(5))

# Sistema
numbers = [3, 4, 1, 5, 2]

# map()
def applay_double(n):
    return n*2

print(list(map(applay_double, numbers)))

# filter()
def is_even(n):
    return n % 2 == 0

print(list(filter(is_even, numbers)))

# sorted()
print(sorted(numbers))
print(sorted(numbers, reverse=True))
print(sorted(numbers, key=lambda x: -x))

# reduce 

def sum(x, y):
    return x + y

print(reduce(sum, numbers))

"""
Extra
"""

students = [
    {"name": "Rigo", "birthdate": "25-05-1993", "grades": [10, 9, 10, 7, 10]},
    {"name": "Mary", "birthdate": "24-08-1988", "grades": [9, 9, 5, 7, 6]},
    {"name": "Robe", "birthdate": "06-05-1986", "grades": [8, 8, 8, 7, 6]}
]

def average(grades):
    return sum(grades)/len(grades)

# Promedio calificaciones
print(
    list(map(lambda student: 
             {"name": student["name"], 
              "average": average(student["grades"])}, students))
)

# Mejores estudiantes
print(
    list(
        map(lambda student: 
             student["name"], 
              filter(lambda student: average(student["grades"]) >= 9, students))
    )
)

# Nacimiento
print(
    list(
        sorted(students, key=lambda student: datetime.strptime(student["birthdate"], "%d-%m-%Y"), reverse=True)
    )
)

# Mayor calificacion

print(max(map(lambda student: max(student["grades"]), students)))