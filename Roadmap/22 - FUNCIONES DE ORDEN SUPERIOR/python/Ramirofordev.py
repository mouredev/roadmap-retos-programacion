'''
Ejercicio:
Explora el concepto de funciones de orden superior en tu lenguaje creando ejemplos simples (a tu eleccion) que muestren su funcionamiento.

Las funciones de orden superior, son aquellas funciones que toman otra funcion como parametro o que retornar una funcion por ejemplo:
'''

#! Funcion superior que retorna una funcion

# Creamos la funcion de orden superior
def get_numbers(n1: int, n2: int):

    # Creamos la funcion que desamos retornar
    def multiplicar():
        return f"{n1 * n2}" # Retornamos el resultado de esa funcion
    
    return multiplicar # Retornamos la funcion

print(get_numbers(5, 7)()) # Le entregamos los valores a la funcion de orden superior y ejecutamos la funcion que tiene adentro

#! Funcion superior usando como parametro otra funcion

# Creamos la funcion que usaremos como parametro
def get_name():
    name = input("Inserte su nombre por favor: ")

    if len(name) != 0:
        return name # Retornamos solo cuando el usuario haya escrito algo
    
def say_hi_to(func_name):
    name = func_name() # Obtenemos el valor de la funcion
    print(f"Hi, {name}") # Imprimimos su valor

say_hi_to(get_name) # Llamamos a la funcion de orden superior, con la funcion como su parametro

'''
Dificultad extra:
Dada una lista de estudiantes (con sus nombres, fecha de nacimiento y lista de calificaciones), utiliza funciones de orden superior para realizar las siguientes operaciones de procesamiento y analisis:
    * Promedio de calificaciones: Obtiene una lista de estudiantes por nombre y promedio de sus calificaciones.
    * Mejores estudiantes: Obtiene una lista con el nombre de los estudiantes que tienen calificaciones con un 9 o mas de promedio
    * Nacimiento: Obtiene una lista de estudiantes ordenada desde el mas joven.
    * Mayor calificaciones: Obtiene la calificacion mas alta de entre todas las de los alumnos
    * Una calificaciones debe estar comprendida entre 0 y 10 (admite decimales).
'''
# Para la fecha de nacimiento importaremos el modulo datetime
from datetime import datetime


students = [{
    "nombre": "Nacho",
    "nacimiento": "2006-12-22",
    "calificaciones": [9.5, 9.2 , 8.5]
}]

def estudiantes():
    mejores = mejores_estudiantes(students, promedios)
    edades = orden_edades(students)
    mayor = mayor_cal(students)

    # Imprimimos los resultados de las funciones
    print("Promedios: ", promedios(students))
    print("Mejores estudiantes: ", mejores)
    print("Orden por edad: ", edades)
    print("Mayor calificaciones: ", mayor)

    add = input("Quieres agregar un nuevo estudiante(y/n): ").lower()
    if add == "y":
        agregar_estudiante(students)
    else:
        print("Gracias por usarme!")    

def agregar_estudiante(students):
    # Creamos un diccionario vacio para almacenar los datos 

    student = {}

    # Creamos una lista vacia para añadir las calificaciones.
    califications = []

    # Pedimos los datos del estudiante
    student_name = input("Por favor inserte el nombre del estudiante: ")
    birth_date = input("Por favor inserte la fecha de nacimiento del estudiante (a/m/d): ")

    i = 0
    while i < 7:
        calification = float(input("Inserte sus calificaciones por favor: "))
        if 0 <= calification <= 10:
            califications.append(calification)
        else:
            print("Error: las calificaciones deben estar entre 0 y 10")
        i += 1
    
    # Agregamos los datos al diccionario
    try:
        student["nombre"] = student_name
        student["nacimiento"] = birth_date
        student["calificaciones"] = califications
        print("Estudiante almacenado con exito!")
    except Exception as e:
        print(f"Ha ocurrido un error: {e}")

    # Agregamos el diccionario a la lista de estudiantes
    students.append(student)

def promedios(students):
    return list(map(lambda s: (s["nombre"], sum(s["calificaciones"]) / len(s["calificaciones"])), students))

def mejores_estudiantes(students, func_prom):
    return list(filter(lambda s: s[1] >= 9, func_prom(students)))

def orden_edades(students): 
    return sorted(
        students,
        key = lambda s: datetime.strptime(s["nacimiento"], "%Y-%m-%d")
    )

def mayor_cal(students):
    return max(map(lambda s: max(s["calificaciones"]), students))

estudiantes()