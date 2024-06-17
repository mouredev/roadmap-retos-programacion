from functools import reduce
from datetime import datetime

"""
    Explora el concepto de funciones de orden superior en tu lenguaje 
    creando ejemplos simples (a tu elección) que muestren su funcionamiento.
"""
# funcion como argumento


def apply_func(func, x):
    return func(x)


x = apply_func(len, "Aldroide")
print(x)

# retorno de funcion


def apply_mult(n):
    def mult(x):
        return x*n
    return (mult)


x = apply_mult(2)

mult = apply_mult(2)
print(mult(5))

# Sistema
numbers = [1, 3, 4, 2, 5]

# map


def apply_double(n):
    return n*2


print(list(map(apply_double, numbers)))


# filter
def is_even(n):
    return n % 2 == 0


print(list(filter(is_even, numbers)))

# sorted()
print(sorted(numbers))
print(sorted(numbers, reverse=True))
print(sorted(numbers, key=lambda x: -x))

# reduce()


def sum_values(x, y):
    return x + y


print(reduce(sum_values, numbers))


"""
DIFICULTAD EXTRA (opcional):
    Dada una lista de estudiantes (con sus nombres, fecha de nacimiento y 
        lista de calificaciones), utiliza funciones de orden superior para 
        realizar las siguientes operaciones de procesamiento y análisis:
        Promedio calificaciones: Obtiene una lista de estudiantes por nombre
            promedio de sus calificaciones.
        Mejores estudiantes: Obtiene una lista con el nombre de los estudiantes
            que tienen calificaciones con un 9 o más de promedio.
        Nacimiento: Obtiene una lista de estudiantes ordenada desde el más joven.
        Mayor calificación: Obtiene la calificación más alta de entre todas las
            de los alumnos.
        Una calificación debe estar comprendida entre 0 y 10 (admite decimales).
"""

students = [
    {"name": "Aldroide", "birthdate": "29-04-1983",
        "grades": [9.5, 8.5, 9.9, 10]},
    {"name": "Richard", "birthdate": "04-08-1983", "grades": [7.5, 9.5, 7, 6]},
    {"name": "Emmanuel", "birthdate": "15-12-2000",
        "grades": [6, 8.5, 9.5, 8.2]},
    {"name": "Samira", "birthdate": "25-01-1980", "grades": [10, 9, 9.7, 9.9]}
]


def average(grades):
    return sum(grades)/len(grades)


# Promedio
print(
    list(map(lambda student: {
        "name": student["name"],
        "average": average(student["grades"])}, students)
    )
)


# Mejores
print(
    list(map(lambda student:
            student["name"],
            filter(lambda student: average(student["grades"]) >= 9, students)
            )
        )
)

# Fecha de naciemiento ordenada
print(sorted(students, key=lambda student: datetime.strptime(
    student["birthdate"], "%d-%m-%Y"), reverse=True))


# Califiación más alta

print(max(map(lambda student: max(student["grades"]), students)))
