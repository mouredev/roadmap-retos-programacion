#Una función de orden superior es aquella función que toma otra función como parámetro
def reverse(text:str):
    #vamos a separar los elementos del texto en cada espacio, por palabras
    words = text.split(" ")
    reversed_text = []

    for element in words:
        #agregamos cada elemento al revés en una nueva lista
        reversed_text.append(element[::-1])
    
    #la función devolverá el texto con cada palabra invertida pero en el mismo orden.
    #convertimos la lista a un string, que se una por cada espacio (por palabras)
    return " ".join(reversed_text)

def invert_word(text, fun):
    return fun(text)

print(invert_word("Hola hackermen", reverse))


print("\n ------- EJERCICIO EXTRA -------")
import datetime

#función para especificar que se ordene por el 2º elemento de una lista (edad) en el formato dd/mm/YYYY
def sort_by_date(elem):
    return datetime.datetime.strptime(elem[1], '%d/%m/%Y')

student1 = ["María", "17/2/1998", [9, 7, 3, 8, 5]]
student2 = ["Peque", "3/6/2004", [9, 10, 9, 10, 9]]
student3 = ["Jose", "20/9/1995", [6, 8, 5, 3, 4]]
students = [student1, student2, student3]

def average_marks(student):
    marks = student[2]

    total = 0
    for mark in marks:
        total += mark
    average = total/len(marks)

    return average

def students_marks(students:list):
    for student in students:
        print(f"El alumno {student[0]} tiene una media de {average_marks(student)}")

def best_students(students_list):
    for student in students_list:
        if average_marks(student) > 9:
            print(f"El alumno {student[0]} tiene un promedio de {average_marks(student)}, que es mayor que 9")

def sort_age_students(students:list):
    students.sort(key=sort_by_date, reverse=True)
    student_name = []

    for student in students:
        student_name.append(student[0])
    
    print(" < ".join(student_name), end="\n")

def sorted_marks(students:list):
    best_mark = []
    for student in students:
        marks = student[2]
        marks.sort()
        best_marks = marks[-1]
        best_mark.append(best_marks)

        print(f"La mejor nota de {student[0]} es {best_marks}")
    
    best_mark.sort()
    print(f"La mejor nota es un {best_mark[-1]}")

def interface(students, fun1, fun2, fun3, fun4):
    print("-> DATOS DE ALUMNOS")
    for student in students:
        print(f"{student[0]} nacido el {student[1]}")
    
    print("-- PROMEDIOS --")
    fun1(students)

    print("-- MEJORES ESTUDIANTES --")
    fun2(students)

    print("-- DEL ALUMNO MENOR AL MAYOR --")
    fun3(students)

    print("-- MEJORES NOTAS --")
    fun4(students)
    
interface(students, students_marks, best_students, sort_age_students, sorted_marks)
