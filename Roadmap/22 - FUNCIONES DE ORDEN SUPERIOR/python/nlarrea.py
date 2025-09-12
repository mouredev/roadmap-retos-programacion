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

# Funciones de orden superior -> funciones que toman una función como argumento
# o que devuelven una función como resultado

# map


def cube(x: int) -> int:
    return x**3


numbers = [1, 2, 3, 4, 5]
cube_numbers = list(map(cube, numbers))
print(cube_numbers)


# filter


def even(x: int) -> bool:
    return x % 2 == 0


even_numbers = list(filter(even, numbers))
print(even_numbers)


# sorted

numbers = [1, 4, 2, 6, 9]
print(sorted(numbers))
print(sorted(numbers, reverse=True))

fruits = ["banana", "apple", "melon", "pineapple"]
print(sorted(fruits, key=len))  # sorts fruits based on the length of strings
# ['apple', 'melon', 'banana', 'pineapple']
print(sorted(fruits, reverse=True, key=len))
# ['pineapple', 'banana', 'apple', 'melon']


# reduce

from functools import reduce


numbers = [1, 2, 3, 4, 5]
sum_of_values = reduce(lambda a, b: a + b, numbers)
print(sum_of_values)  # 15


"""
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

students_data: list[dict] = [
    {
        "first_name": "Brennan",
        "last_name": "Wiza",
        "birth_date": "2004, 2, 11",
        "marks": [5, 6.7, 8, 9.2, 3],
    },
    {
        "first_name": "Hilton",
        "last_name": "Schimmel",
        "birth_date": "1998, 7, 7",
        "marks": [8, 7.6, 7.8, 5.5, 9],
    },
    {
        "first_name": "Aditya",
        "last_name": "Rowe",
        "birth_date": "1999, 5, 2",
        "marks": [7.6, 8.9, 9.3, 10, 7.8],
    },
    {
        "first_name": "Estella",
        "last_name": "King",
        "birth_date": "1997, 6, 29",
        "marks": [9.6, 8.9, 9.3, 10, 7.8],
    },
]


# Average


def average(grades: list):
    return round(sum(grades) / len(grades), 2)


print(
    list(
        map(
            lambda student: {
                "name": student["first_name"],
                "average": average(student["marks"]),
            },
            students_data,
        )
    )
)


# Best students

print(
    list(
        map(
            lambda student: student["first_name"],
            filter(
                lambda student: average(student["marks"]) >= 9, students_data
            ),
        )
    )
)


# Birth Day

from datetime import datetime

print(
    sorted(
        students_data,
        reverse=True,
        key=lambda student: datetime.strptime(
            student["birth_date"], "%Y, %m, %d"
        ),
    )
)


# Highest score

print(max(map(lambda student: max(student["marks"]), students_data)))
