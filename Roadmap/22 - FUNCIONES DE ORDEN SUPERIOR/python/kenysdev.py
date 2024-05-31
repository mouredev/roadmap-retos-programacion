# ╔═════════════════════════════════════╗
# ║ Autor:  Kenys Alvarado              ║
# ║ GitHub: https://github.com/Kenysdev ║
# ║ 2024 -  Python                      ║
# ╚═════════════════════════════════════╝

# -----------------------------------
# * FUNCIONES DE ORDEN SUPERIOR
# -----------------------------------

"""
* EJERCICIO #1:
* Explora el concepto de funciones de orden superior en tu lenguaje 
* creando ejemplos simples (a tu elección) que muestren su funcionamiento.
"""

def arithmetic_op(func: object):
    def wrapper(x: int, y: int):
        return func(x, y)
    return wrapper

def add(x: int, y: int):
    return x + y

def subtract(x: int, y: int):
    return x - y

def multiply(x: int, y: int):
    return x * y

addition = arithmetic_op(add)
subtraction = arithmetic_op(subtract)
multiplication = arithmetic_op(multiply)

r_addition = addition(2, 3)
r_subtraction = subtraction(10, 5)
r_multip = multiplication(2, 5)


print(f"""EJERCICIO #1
Resultado de la suma:    {r_addition}
Resultado de la resta:   {r_subtraction}
Resultado de la multip.: {r_multip}
""")

# ______________________________________
"""
* EJERCICIO #2:
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

students_list = [
    {"name": "Ken", "dob": "2012-04-21", "grades": [9.5, 9.4, 9.3, 9.2]},
    {"name": "Ben", "dob": "2012-03-20", "grades": [8.5, 8.4, 8.3, 8.2]},
    {"name": "Ada", "dob": "2012-02-19", "grades": [7.5, 7.4, 7.3, 7.2]},
    {"name": "zoe", "dob": "2012-01-18", "grades": [9.0, 9.1, 9.0, 9.1]},
]

def higher_order_fun(msg: str, print_fn: object) -> object:
    def wrapper(students: list):
        print(f"\n----\n{msg}")
        for student in students:
            print_fn(student)

    return wrapper

def print_gpa(student: dict):
    grades: list = student["grades"]
    average_grade: float = sum(grades) / len(grades)
    print(student["name"], average_grade)

def print_top(student: dict):
    grades: list = student["grades"]
    average: float = sum(grades) / len(grades)
    if average >= 9: 
        print(student["name"])

def print_bth(student: dict):
    print(student["name"], student["dob"])

def print_hgg(student: dict):
    max_grade: float = max(student["grades"])
    name: str = student["name"]
    print(name, max_grade)

grade_point_average = higher_order_fun("Promedio calificaciones", print_gpa)
top_students = higher_order_fun("Mejores estudiantes:", print_top)
birth_order = higher_order_fun("Por nacimiento:", print_bth)
highest_grade = higher_order_fun("Mayor calificación:", print_hgg)

print("EJERCICIO #2")

grade_point_average(students_list)
top_students(students_list)
birth_order(sorted(students_list, key=lambda student: student["dob"]))
highest_grade(students_list)

