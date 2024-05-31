"""
EJERCICIO:
 * Explora el concepto de funciones de orden superior en tu lenguaje 
 * creando ejemplos simples (a tu elección) que muestren su funcionamiento.
"""
def multiply_for_five(value:int):
    return value*5

def multiply_for_two(value:int):
    return value*2

def multiply_value(value,func):
    return func(value)

print(multiply_value(5,multiply_for_five))
print(multiply_value(5,multiply_for_two)) #desde la misma función puedo llamar a otra
print(multiply_value(5,lambda x:x*3)) #o incluso crear una lambda

#BUILT-IN HIGH ORDER LEVEL FUNCTIONS
numbers = [1,2,3,4,5,6]
print(list(map(lambda x:x*2,numbers)))
print(list(filter(lambda x:x>3,numbers)))

#CLOSURES
def sum_five(): #una función que retorna una función
    def add(value:int):
        return value + 5
    return add

print(sum_five()(7))

"""
DIFICULTAD EXTRA (opcional):
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

students = [
    {
        "name":"Alex",
        "birthdate" : "19/12/1984",
        "qualifications": [8.0,7.5,6.7,7.2]
    },
    {
        "name":"Sole",
        "birthdate" : "12/01/1983",
        "qualifications": [9.1,6.8,7.3,8.7]
    },
    {
        "name":"Martín",
        "birthdate" : "12/11/2015",
        "qualifications": [9.4,8.9,9.9,9.4]
    },
    {
        "name":"Valeria",
        "birthdate" : "17/04/2018",
        "qualifications": [9.0,8.9,9.7,9.1]
    }
]

from functools import reduce
from datetime import datetime
from operator import itemgetter

def average(students:list): #BUILT-IN FUNCTION: REDUCE + LAMBDA
    result = []
    for student in students:
        qualifications_average = reduce(lambda x,y:x+y,student["qualifications"])/len(student["qualifications"])
        result.append({"name":student["name"],"average":round(qualifications_average,2)})
    return result

print(f"PROMEDIO DE CALIFICACIONES:\n{average(students)}")


def best_students(students:list): #BUILT-IN FUNCTION: FILTER + LAMBDA
    students_with_average = average(students)
    bests = list(filter(lambda students_with_average: students_with_average["average"]>9,students_with_average))
    for student in bests:
        del(student["average"])
    return bests

print(f"\nMEJORES ALUMNOS:\n{best_students(students)}")

def sort_youngest(students:list): #CLOSURE
    def youngest ():
        sorted_students = list()
        for student in students:
            student["birthdate"] = datetime(day=int(student["birthdate"][0:2]),month=int(student["birthdate"][3:5]),year=int(student["birthdate"][6:])).timestamp()
        sorted_students = sorted(students,key=itemgetter("birthdate"),reverse=True)
        for student in sorted_students:
            student["birthdate"] = datetime.fromtimestamp(student["birthdate"]).strftime("%d/%m/%Y")
        return sorted_students
    return youngest


print(f"\nALUMNOS ORDENADOS DESDE EL MÁS JOVEN:\n{sort_youngest(students)()}")

def find_best_student(students:list): #CLOSURE
    def best_qualifications():
        students_best_qualifications = list()
        for student in students:
            student["qualifications"] = sorted(student["qualifications"],reverse=True)
            students_best_qualifications.extend(student["qualifications"])
        return sorted(students_best_qualifications,reverse=True)[0]
    return best_qualifications

print(f"\nLA MEJOR NOTA:\n{find_best_student(students)()}")
