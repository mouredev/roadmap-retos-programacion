""" /*
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
 */ """

#EJERCICIO

#Función de argumento

def apply_func(func, x):
    return func(x)

print(apply_func(len, "David"))

#Retorno de función

def apply_multiplier(n):
    def multiplier(x):
        return x * n
    return multiplier

print(apply_multiplier(2)(3))

#Sistema

numbers = [1, 3, 2, 5, 4]

""" map() """

def apply_double(n):
    return n * 2

print(map(apply_double, numbers))
print(list(map(apply_double, numbers)))

""" filter() """

def is_even(n):
    return n % 2 == 0

print(filter(is_even, numbers))
print(list(filter(is_even, numbers)))

""" sorted() """

print(sorted(numbers))
print(sorted(numbers))
print(sorted(numbers, key=lambda x: -x))

""" reduce() """

from functools import reduce

def sum_(x, y):
    return x + y

print(reduce(sum_, numbers))

#DIFICULTAD EXTRA

students = [
    {"name": "Juan", "birthdate": "10-03-1998", "results": [5, 7, 6, 7]},
    {"name": "José", "birthdate": "02-03-1988", "results": [7, 8, 9, 4]},
    {"name": "Pepe", "birthdate": "02-03-1978", "results": [7, 8, 9, 4]},
    {"name": "Ramiro", "birthdate": "02-11-1990", "results": [9.5, 9, 9, 10]}
]

#Promedio

def average(results):
    return sum(results) / len(results)

print("\nPromedio:")
print(list(map(lambda student: {"name": student["name"], "average": average(student["results"])}, students)))

#Mejores estudiantes

print("\nMejores estudiantes:")
print(list(map(lambda student: student["name"], filter(lambda student: average(student["results"]) >= 9, students))))

#Nacimiento

from datetime import datetime

print("\nOrden de estudiantes por edad:")
print(sorted(students, key=lambda student: datetime.strptime(student["birthdate"], "%d-%m-%Y"), reverse=True))

#Mayor calificación

print("\nMayor calificación:")
print(max(list(map(lambda student: max(student["results"]), students))))