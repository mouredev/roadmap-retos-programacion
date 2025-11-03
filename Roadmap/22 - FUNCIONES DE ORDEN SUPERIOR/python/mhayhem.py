# @Author Daniel Grande (Mhayhem)

from datetime import date, datetime

# EJERCICIO:
# Explora el concepto de funciones de orden superior en tu lenguaje 
# creando ejemplos simples (a tu elección) que muestren su funcionamiento.

def greet(name):
    return f"Hola {name}"

def process_greeting(text: str, function):
    return function(text)

print(process_greeting("Dany", greet))
    
# DIFICULTAD EXTRA (opcional):
# Dada una lista de estudiantes (con sus nombres, fecha de nacimiento y 
# lista de calificaciones), utiliza funciones de orden superior para 
# realizar las siguientes operaciones de procesamiento y análisis:
# - Promedio calificaciones: Obtiene una lista de estudiantes por nombre
#   y promedio de sus calificaciones.
# - Mejores estudiantes: Obtiene una lista con el nombre de los estudiantes
#   que tienen calificaciones con un 9 o más de promedio.
# - Nacimiento: Obtiene una lista de estudiantes ordenada desde el más joven.
# - Mayor calificación: Obtiene la calificación más alta de entre todas las
#   de los alumnos.
# - Una calificación debe estar comprendida entre 0 y 10 (admite decimales).

students = [
    {
    "name": "Dany",
    "birth_day": date(1999, 7, 15),
    "grades": [6, 7.5, 9, 9, 10, 9]
    },
    {
    "name": "Carlos",
    "birth_day": date(1999, 2, 13),
    "grades": [9, 9, 10, 9, 9, 10]
    },
    {
    "name": "Sandra",
    "birth_day": date(2000, 12, 31),
    "grades": [9, 8.5, 9, 9, 9, 9.5]
    }
]
def students_info(func1, func2, func3, func4, array):
    print("Promedios:")
    print(func1(array))
    print("Promedios mas altos:")
    print(func2(array))
    print("Estudiantes ordenados de menor a mayor:")
    print(func3(array))
    print("Mejor promedio:")
    print(func4(array))

def average_grades(array: list):
    return [
        f"{student['name']}; Promedio: {sum(student['grades']) / len(student['grades']):.1f}" for student in array
    ]

def highest_average(array: list):
    return [
        student['name']
        for student in array
        if (sum(student['grades']) / len(student['grades'])) >= 9
    ]
def youngest(array: list):
    today = date.today()
    sorted_list = sorted(array, key=lambda s: s["birth_day"], reverse=True)
    return [
        f"{item['name']} {today.year - (item['birth_day'].year) - ((today.month, today.day) < (item["birth_day"].month, item["birth_day"].day))} años"
        for item in sorted_list
    ]

def the_best(array: list):
    return max(array, key=lambda s: sum(s["grades"]) / len(s["grades"]))["name"]

students_info(average_grades, highest_average, youngest, the_best, students)