# Funciones de Orden superior #

# Son funciones que reciben como parametros otras funcion y devuelven otra funcion

# Ejemplos
# 1. Recibe una función como parametro

from datetime import datetime 
from functools import reduce

def do_operation(a, b, operation):
    return operation(a,b)

def suma_2_mumeros(a,b):
    return a + b

print(do_operation(5,8,suma_2_mumeros))

# 2. Devuelve una función

def multiplicator_maker(factor):
    def multiplicator(num):
        return num * factor
    return multiplicator

tri = multiplicator_maker(3)
print(tri(5))

# 3. Sistema

numbers = [1, 3, 4, 2, 5]

# map()

def apply_double(n):
    return n*2

print(list(map(apply_double,numbers)))

# filter()

def is_two(n):
    return n % 2 == 0

print(list(filter(is_two,numbers)))

# Sorted()

print(sorted(numbers))
print(sorted(numbers, reverse=True))
print(sorted(numbers, key= lambda x: -x))

# Reduce()

def sum_two(x, y):
    return x + y

print(reduce(sum_two, numbers))

###########################################################################################################################
"Dificultad extra"
###########################################################################################################################

######################### OPCION 1 ################################

students_list = [
    {"name": "Gustavo", 
    "birthdate": datetime.strptime("01/02/2015","%d/%m/%Y"),
    "scores":
    {"math": 6 ,"english": 8,"science": 5}
},
{"name": "Maria", 
    "birthdate": datetime.strptime("05/05/2014","%d/%m/%Y"),
    "scores":
    {"math": 5 ,"english": 10,"science": 7}
},
{"name": "John", 
    "birthdate": datetime.strptime("20/10/2016","%d/%m/%Y"),
    "scores":
    {"math": 10 ,"english": 8,"science": 10}
}
]

# Toma un diccionario de materias y notas, para sacar un promedio total
def score_prom(scores: dict):
    total_sum = 0
    flag = 0
    for key, value in scores.items():
        total_sum += value
        flag += 1 
    return total_sum/flag 

# Toma un diccionario que tiene el nombre, y le aplica una función al valor del key (name) dado.
def student_duo(student: dict, function2, name):
    return student["name"], function2(student[name])

# print(student_prom(students_list[0],score_prom))

# Forma una lista, a partir de un diccionario mas grande con muchas dependencias, y le apica 2 funciones.
def student_form_list(student_list: list, function1,function2, item):
    list_of_student = []
    for i in student_list:
        list_of_student.append(function1(i,function2, item)) 
    return list_of_student

# Toma la lista de estudiantes con su promedio y elige los que tienen mayor promedio que 9
def student_best_list(student_form_list):
    student_list_of_best = []    
    for i in student_form_list:
        if i[1]>9:
            student_list_of_best.append(i)
    return student_list_of_best

# def student_date(student: dict):
#     return student["name"], student["birthdate"]

def identidad(name):
    return name

def age(date_given):
    return date_given.strftime("%d/%m/%Y")

print(student_form_list(students_list,student_duo,score_prom,"scores"))
print(student_best_list(student_form_list(students_list,student_duo,score_prom, "scores")))

print(student_duo(students_list[0],identidad,"birthdate"))

print(sorted(student_form_list(students_list,student_duo,identidad,"birthdate"),key=lambda x: x[1]))

def max_score(scores: dict):
    score_data = list(scores.items())
    # for key, value in scores.items():
    return max(score_data, key=lambda x : x[1])

print(max_score(students_list[0]["scores"]))

print(max(student_form_list(students_list,student_duo,max_score,"scores")))



######################### OPCION 2 ################################

students = [
    {"name": "Brais", "birthdate" : "29-04-1987", "grades": [5, 8.5, 3, 10]},
    {"name": "moure", "birthdate" : "04-08-1995", "grades": [1, 9.5, 2, 4]},
    {"name": "mouredev", "birthdate" : "15-12-2000", "grades": [4, 6.5, 5, 2]},
    {"name": "supermouredev", "birthdate" : "25-01-1980", "grades": [10, 9, 9.7, 9.9]}
]

def average(grades):
    return sum(grades) / len(grades)


# Promedio

print(
    list(map(lambda student: {
        "name": student["name"], 
        "average": average(student["grades"])},students)
    )
)


# Mejores

print(
    list(map(lambda student: 
        student["name"], 
        filter(lambda student: average(student["grades"]) >= 9 ,students)
        )
    )
)

# Fecha de nacimiento ordenada

print(sorted(students, key= lambda student: datetime.strptime(
    student["birthdate"], "%d-%m-%Y"), reverse= True))


# Calificación mas alta

print(max(list(map(lambda student: max(student["grades"]), students))))