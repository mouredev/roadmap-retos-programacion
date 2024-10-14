import os
os.system('cls')
from datetime import datetime as DT

"""* EJERCICIO:
 * Explora el concepto de funciones de orden superior en tu lenguaje 
 * creando ejemplos simples (a tu elección) que muestren su funcionamiento.
 *
"""

def operator(fun:str):#Función de orden superior
    def sum(num1:int,num2:int)->int:#Función secundaria
        return num1+num2
    def multiplication(num1:int,num2:int)->int:#Función secundaria
        return num1*num2
    def substraction(num1:int,num2:int)->int:#Función secundaria
        return num1-num2
    def division (num1:int,num2:int)->int:#Función secundaria
        try:                                            
           return num1/num2
        except ZeroDivisionError as zde:
            print("ERROR:",zde) 
    def pow (num1:int,num2:int)->int:#Función secundaria
        return num1**num2
    if fun == '+':#Condicional para función de orden superior
        return sum #Retorno de resultado de función secundaria
    elif fun == '-':#Condicional para función de orden superior
        return substraction#Retorno de resultado de función secundaria
    elif fun == '*':#Condicional para función de orden superior
        return multiplication#Retorno de resultado de función secundaria
    elif fun == "**":#Condicional para función de orden superior
        return pow#Retorno de resultado de función secundaria
    elif fun == '/':#Condicional para función de orden superior
        return division#Retorno de resultado de función secundaria
    else:
        print("Operador incorrecto")
    
print(operator('+')(6,5))#Llamada a función de orden superior asignando en los primeros paréntesis
# su argumento y dentro del paréntesis siguiente los argumentos de la función secundaria a la que llama la primera
resta = operator('-')#También se puede almacenar en una variable la llamada a la función de orden superior
print(resta(456,89.5))# con su argumento y pasarle a esta variable después los argumentos de la secundaria 
suma = operator('+')
multiplicacion = operator('*')
division = operator('/')
potencia = operator("**")
print (suma(485,896),"",division(4,0),"",potencia(2,8),"",multiplicacion(14,24))
print('\n\n\n\n')

""" * DIFICULTAD EXTRA (opcional):
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
 * - Una calificación debe estar comprendida entre 0 y 10 (admite decimales)."""

students_list = [
                 ["Ana", DT.strptime('31/1/1997', '%d/%m/%Y'), [10, 9.9, 8.8, 9.6, 8.7, 9.5, 9.2, 8.9, 9.9, 10]],
                 ["Carlos", DT.strptime('21/3/1986', '%d/%m/%Y'), [8, 9.9, 8, 9.9, 8.7, 9.8, 9, 8.8, 9, 10, 6.9]],
                 ["Jesus", DT.strptime('26/12/1974', '%d/%m/%Y'), [9.8, 8.3, 7.8, 9.9, 10, 9.7, 9.6, 9.7, 9.3]],
                 ["Leire", DT.strptime('2/11/1991', '%d/%m/%Y'), [9.5, 9.7, 9.8, 9.3, 7.7, 9, 9, 8.7, 9.9, 8.9]],
                 ["Pablo", DT.strptime('14/8/1982', '%d/%m/%Y'), [6.5, 7.3, 8, 9.6, 5, 8.5, 9, 9.8, 8, 9.6, 9]],
                 ["Sandra", DT.strptime('24/3/1989', '%d/%m/%Y'), [6.2, 9.6, 7.9, 8, 7.8, 8.4, 9, 7.8, 9.8, 8.6]],
                 ["Sara", DT.strptime('11/6/1991', '%d/%m/%Y'), [9.7, 9.7, 7.8, 9.9, 7.8, 9.5, 9.3, 9.7, 9.9, 10]],
                 ["Steven", DT.strptime('10/2/1994', '%d/%m/%Y'), [9.7, 9.1, 8.8, 7.3, 7.9, 9.8, 9, 6.7, 10, 9]]
                 ]

def students(option:int):

    def avg_grade(students_list:list)->dict:
        grade_list = []
        names_list = []
        acc = 0
        for student in students_list:
            names_list.append(student[0])
            for grade in student[2]:
                acc = grade + acc
                grade = 0
            grade_list.append(round(acc/len(student[2]),1))
            acc = 0
        if option == 1:
            print("Nota media de los alumnos: \n")
            for name, avg in zip(names_list,grade_list) :
                print('{:<10}'.format(name)," Nota media:", avg)
        name_grades_dict = {name:avg for name, avg in zip(names_list,grade_list)}     
        return name_grades_dict


    def best(students_list:list):
      best_students = avg_grade(students_list)
      print("Estudiantes con un 9 o más de nota media: \n")
      for name,grade_over_nine in best_students.items():                                                                
          if grade_over_nine >= 9:
              print ('{:<10}'.format(name), "-  Nota media:", grade_over_nine)


    def sorted_age(students_list:list):
        print("Lista de estudiantes ordenados desde el más joven:\n")
        sorted_age_list = sorted(students_list, key=lambda student: student[1], reverse=True)
        for student in sorted_age_list:
            birth_date = student[1].strftime('%d/%m/%Y')
            print('{:<10}'.format(student[0]), "-  Fecha de nacimiento:", birth_date)
    

    def hight_grade(students_list:list):
        print("Lista de estudiantes con su nota más alta: \n")
        for student in students_list:
            hightest = 0
            name = student[0]
            for grade in student[2]:
                if grade > hightest:
                    hightest = grade
            print ('{:<10}'.format(name), "-  Calificación más alta: ",hightest)

    if option == 1:
        return avg_grade
    if option == 2:
        return best
    if option == 3:
        return sorted_age
    if option == 4:
        return hight_grade
    
while True:
    option = input("""\nElija una opción:\n1-Mostrar la nota media de todos los alumnos\n2-Mostrar los alumnos con nota media igual o superior a 9
3-Mostrar todos los alumnos ordenados por fecha de nacimiento desde el más joven\n4-Mostrar todos los alumnos con su nota más alta\n5-Salir\n---> """)
    if option == "5":
        break
    elif option.isdigit():
        if int(option) > 4 or int(option) < 1:
            print("Solo se pueden introducir números del 1 al 5, intente de nuevo o pulse 5 para salir\n") 
            print()       
        else:
            students(int(option))(students_list)
            break
    else:
        print("Solo se pueden introducir números del 1 al 5, intente de nuevo o pulse enter para salir") 





