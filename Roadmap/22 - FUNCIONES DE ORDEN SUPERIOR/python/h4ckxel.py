"""Explora el concepto de funciones de orden superior en tu lenguaje
creando ejemplos simples (a tu elección) que muestren su funcionamiento"""
from math import sqrt, pow
from datetime import datetime


def right_triangle(func, triangle: dict):
    return func(triangle)


def triangle_area(triangle: dict) -> float:
    adjacent = triangle.get('adjacent')
    opposite = triangle.get('opposite')
    area = (adjacent * opposite) / 2
    return area


def triangle_hypotenuse(triangle: dict) -> float:
    adjacent = triangle.get('adjacent')
    opposite = triangle.get('opposite')
    hypotenuse = sqrt(pow(adjacent, 2) + pow(opposite, 2))
    return hypotenuse


triangle_definition = {'adjacent': 3, 'opposite': 4}
print(f'Triangle definition\n'
      f'Adjacent side: {triangle_definition["adjacent"]}\n'
      f'Opposite side: {triangle_definition["opposite"]}')

# Found the area of a triangle
example_area = right_triangle(triangle_area, triangle_definition)
print(f'The area of the right triangle is {example_area}')

# Found the hypotenuse of a triangle
example_hypotenuse = right_triangle(triangle_hypotenuse, triangle_definition)
print(f'The hypotenuse of the right triangle is {example_hypotenuse}')


"""DIFICULTAD EXTRA (opcional):
Dada una lista de estudiantes (con sus nombres, fecha de nacimiento y 
lista de calificaciones), utiliza funciones de orden superior para 
realizar las siguientes operaciones de procesamiento y análisis:
- Promedio calificaciones: Obtiene una lista de estudiantes por nombre y promedio de sus calificaciones.
- Mejores estudiantes: Obtiene una lista con el nombre de los estudiantes 
que tienen calificaciones con un 9 o más de promedio.
- Nacimiento: Obtiene una lista de estudiantes ordenada desde el más joven.
- Mayor calificación: Obtiene la calificación más alta de entre todas las de los alumnos.
- Una calificación debe estar comprendida entre 0 y 10 (admite decimales)."""


students = [
    {"name": "Andres", "dob": "2000-01-01", "grades": [5.0, 7.0, 3.5]},
    {"name": "Brandon", "dob": "2002-02-02", "grades": [10, 9.8, 9.0]},
    {"name": "Ash", "dob": "2001-05-05", "grades": [8.5, 9.0, 7.5]},
    {"name": "Seiya", "dob": "2001-10-10", "grades": [9.4, 9.0, 8.6]},
    {"name": "Alpha", "dob": "2000-12-25", "grades": [7.0, 6.5, 6.0]},
]


def students_gpa(students_list: list) -> list:
    students_gpa_list = list()

    for student in students_list:
        student_grades = student['grades']
        gpa = round((sum(student_grades) / len(student_grades)), 2)

        students_gpa_list.append({'name': student['name'], 'gpa': gpa})

    return students_gpa_list


def best_gpa(student_gpa: list) -> list:
    bets_students_list = list()

    for student in student_gpa:
        gpa = student['gpa']
        if gpa >= 9.0:
            bets_students_list.append({'name': student['name'], 'gpa': gpa})

    return bets_students_list


def best_student(best_students_list: list) -> list:
    highest_gpa = max(student['gpa'] for student in best_students_list)
    best_students = [{'name': student['name'], 'gpa': student['gpa']} for student in best_students_list if
                     student['gpa'] == highest_gpa]
    return best_students


def sort_list_by_age(students_list: list) -> list:
    def get_dob(student):
        return datetime.strptime(student['dob'], '%Y-%m-%d')

    sorted_students = sorted(students_list, key=get_dob, reverse=True)
    return sorted_students


def students_grades_functions(get_gpa, get_best_gpa, get_best_student, get_sorted_student_list, students_list: list):
    # Get a list of students with their gpa
    student_gpa_list = get_gpa(students_list)

    # Get a list of the best gpas
    best_gpa_list = get_best_gpa(student_gpa_list)

    # Get a list of the best student
    best_student = get_best_student(best_gpa_list)

    # Get a list of students sorted by age
    sorted_student_list = get_sorted_student_list(students_list)

    return student_gpa_list, best_gpa_list, best_student, sorted_student_list


gpa_list, best_gpa, higher_gpa, sorted_list = students_grades_functions(students_gpa, best_gpa, best_student, sort_list_by_age, students)
print('**** List of students with their gpa ****')
print(gpa_list)
print('**** List of best gpa ****')
print(best_gpa)
print('**** Best gpa ****')
print(higher_gpa)
print('**** Sorted list ****')
print(sorted_list)
