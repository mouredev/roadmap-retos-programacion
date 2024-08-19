from functools import reduce
from datetime import datetime
"""
EJERCICIO:
Explora el concepto de funciones de orden superior en tu lenguaje 
creando ejemplos simples (a tu elección) que muestren su funcionamiento.

DIFICULTAD EXTRA(opcional):
Dada una lista de estudiantes (con sus nombres, feca de nacimiento y 
lista de calificaciones), utiliza funciones de orden superior para 
realizar las siguientes operaciones de procesamiento y análisis:
- Promedio calificaciones: Obtiene una lista de estudiantes por nombre 
y promedio de sus calificaciones.
- MEJORES ESTUDIANTES: Obtiene una lista con el nombre de los estudiantes
que tienen calificaciones con un 9 o más de promeido.
- Nacimiento: Obtiene una lista de estudiantes ordenada desde el más joven.
- Mayor calificación: Obtiene la calificación más alta de entre todas las
de los alumnos.
- Una calificación debe estar comprendida entre 0 y 10 (admite decimales).

by adra-dev
"""

"""
Funciones de orden superior: Una función se denomina Función de orden
superior si esta contiene otras funciones como parámetros de entrada 
o si devuelve una función como salida, es decir, las funciones que 
operan con otra función se conocen como Funciones de orden superior 
en Python.
"""

# Función como argumento

def high_order_function(fun):
  fun()

def greeting():
  print("Hello World")

high_order_function(greeting) 
# Retorno de función


def apply_multiplier(n):
    def multiplier(x):
        return x * n
    return multiplier


multiplier = apply_multiplier(2)
print(multiplier(5))
print(apply_multiplier(3)(2))

#  Sistema

numbers = [1, 3, 4, 2, 5]

# map()


def apply_double(n):
    return n * 2


print(list(map(apply_double, numbers)))

# filter()


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
Extra
"""

students = [
    {"name": "Adrian", "birthdate": "29-04-1987", "grades": [5, 8.5, 3, 10]},
    {"name": "Luis", "birthdate": "04-08-1995", "grades": [1, 9.5, 2, 4]},
    {"name": "Pepe", "birthdate": "15-12-2000", "grades": [4, 6.5, 5, 2]},
    {"name": "supermouredev", "birthdate": "25-01-1980",
        "grades": [10, 9, 9.7, 9.9]}
]


def average(grades):
   return sum(grades) / len(grades)

# Promedio

print(
   list(map(lambda student: {
   "name": student["name"], "average": average(student["grades"])}, students)
   )   
)

# Mejores

print(
    list(
        map(lambda student:
            student["name"],
            filter(lambda student: average(student["grades"]) >= 9, students)
            )
    )
)

# Fecha de nacimiento ordenada

print(sorted(students, key=lambda student: datetime.strptime(
    student["birthdate"], "%d-%m-%Y"), reverse=True))

# Califiación más alta

print(max(map(lambda student: max(student["grades"]), students)))