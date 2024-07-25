###############################################################################
### EJERCIOCIO
###############################################################################
def high_order_function(function, name:str):
    """
    Una funcion que recibe otra funcion como argumento
    """
    #Llama a la funcion con el nombre proporcionado
    function(name)

def greeting(name:str):
    """
    Simplemente devuelve un saludo
    """
    print(f'Hola {name}, ¿Como estas?')

#Ejemplo de uso: le pasamos la funcion y mi nombre.
high_order_function(greeting, 'Dani')



###############################################################################
### DIFICULTAD EXTRA
###############################################################################

# DATOS:
names = ['Dani', 'Moure', 'Juanito', 'Conchita']
birthdates = [1989, 1986, 1990, 1970]
grades = [9,10,4,7]
students_list = list(zip(names, birthdates, grades))


def main(function, student_list:list):
    """
    Llama a la funcion y le pasa el listado de alumnos
    """
    function(students_list)


def sort_by_grades(students_list):
    """
    Ordena a los estudiantes por calificaicon mas alta a la mas baja
    """
    students_list = sorted(students_list, key = lambda x: x[2])
    print('\nLista de estudiantes ordenada por notas:')
    show_list(students_list)

 
def best_student(students_list):
    """
    Muestra a los estudiantes con mas de 8 de calificacion
    """
    students_list = list(filter(lambda x: x[2]>8, students_list))
    print('\nLos mejores estudiantes son:')
    show_list(students_list)


def sort_by_age(students_list):
    """
    Ordena a los estudiantes por edad de menor a mayor
    """
    students_list = sorted(students_list, key=lambda x: x[1], reverse=True)
    print('\nLista Estudiantes ordenados por edad de menor a mayor: ')
    show_list(students_list)


def best_grade(students_list):
    """
    Muestra la calificacion mas alta
    """
    students_list = max(students_list, key=lambda x: x[2])
    print('\nEl mejor estudiante es: ')
    print(students_list)


def show_list(students_list):
    """
    Muestra el resultado por pantalla
    """
    for student in students_list:
        print(student)

     
main(sort_by_grades, students_list)
main(best_student, students_list)
main(sort_by_age, students_list)
main(best_grade, students_list)

            
 
 
    