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

# Map function
# La función map() es una función incorporada que toma una función y es iterable como parámetros.

languages = ["Java", "Python", "JavaScript", "Go", "Bash"]

def change_lower(name):
    return name.lower()

languages_changed= map(change_lower, languages)
languages_changed_lambda = map(lambda lan: lan.lower(), languages)
print(list(languages_changed))
print(list(languages_changed_lambda))

# Filter function
# La función filter() llama a la función especificada que devuelve un valor booleano para cada elemento 
# del iterable (lista) especificado. Filtra los elementos que satisfacen los criterios de filtrado.

def is_name_long(name):
    if len(name) > 6:
        return True
    return False

long_names = filter(is_name_long, languages)
print(list(long_names))


numbers = [1, 2, 3, 4, 5]

def is_odd(num):
    return num % 2 != 0

odd_numbers = filter(is_odd, numbers)
print(list(odd_numbers))

# Reduce function
# Aplica una función de manera acumulativa a los elementos de una lista, reduciéndolos a un solo valor. 
# Esta función está en el módulo functools.

from functools import reduce

list_num = ['1', '2', '3', '4', '5']

def sum_two_nums(x, y):
    return int(x) + int(y)

total = reduce(sum_two_nums, list_num)
print(total)

#########  ------------------------------ EXTRA ------------------------------------ ###########

from datetime import datetime

students = [
    {"name": "Carlos", "date_birth": "15-05-2001", "grades": [8.5, 9, 9.5]},
    {"name": "Juan", "date_birth": "08-11-2000", "grades": [10, 9, 9.5]},
    {"name": "Pedro", "date_birth": "17-01-2002", "grades": [7, 8, 7.6]},
    {"name": "Jose", "date_birth": "22-10-2000", "grades": [9.5, 7.5, 8.5]},
    {"name": "Mau","date_birth": "30-09-2000", "grades": [6.5, 9, 10]},
    {"name": "Chris", "date_birth": "10-04-2001","grades": [8.5, 10, 9.5]},
    {"name": "Marcelo", "date_birth": "15-12-2000", "grades": [7.5, 10, 5]},
    {"name": "Edward", "date_birth": "04-01-2001", "grades": [5.5, 8.8, 9.6]},
    {"name": "Rodrigo", "date_birth": "01-06-2002", "grades": [9.4, 5.6, 9.3]}
]

def calculate_average(grades):
    valid_grades = [grade for grade in grades if 0 <= grade <= 10]
    return sum(valid_grades) / len(valid_grades) if valid_grades else 0

def get_average_student(student):
    return {
        "name": student["name"],
        "average_grade": calculate_average(student["grades"])
    }

def best_student(student):
    return student["average_grade"] >= 9

def parse_date(dob):
    return datetime.strptime(dob, "%d-%m-%Y")

def get_date_birth(student):
    return parse_date(student["date_birth"])

students_with_averages = list(map(get_average_student, students))

best_students = list(filter(best_student, students_with_averages))

students_by_age = sorted(students, key=get_date_birth)

highest_grade = 0
student_with_highest_grade = None

for student in students:
    for grade in student["grades"]:
        if grade > highest_grade:
            highest_grade = grade
            student_with_highest_grade = student["name"]

print("Estudiantes con sus promedios de calificaciones:")
for student in students_with_averages:
    print(f"{student['name']}: {student['average_grade']:.2f}")

print("\nMejores Estudiantes(promedio >= 9):")
for student in best_students:
    print(student["name"])

print("\nEstudiantes ordenados desde el mas joven:")
for student in students_by_age:
    print(f"{student['name']}: {student['date_birth']}")

print(f"La calificacion mas alta es {highest_grade} de {student_with_highest_grade}")