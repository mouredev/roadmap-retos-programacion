
from functools import reduce
from datetime import date, datetime
"""
* EJERCICIO:
 * Explora el concepto de funciones de orden superior en tu lenguaje 
 * creando ejemplos simples (a tu elección) que muestren su funcionamiento.

"""
# Función como argumento 

def saluda(name, saluda_callback):
    saluda_callback(name)

def texto(name):
    print(f"Hola {name}, como estás?")

saluda("Brais", texto)

# Función como retorno 

def concatena_strings(name):
    def get_last_name(last_name):
        return name + " " + last_name
    return get_last_name
name = concatena_strings("Borja") # devuelve función
print(name("Lv")) #utlizamos función
print(concatena_strings("Brais")("Moure")) # pasamos todos los argumentos


# Sistema: map(), filter(), sorted(), reduce

my_list = ["Brais", "Borja", "María", "Sonia"]


# map

def to_lower(name):
    return name.lower()

print(list(map(to_lower, my_list))) # aplica la función a todos los elementos de un iterable


# filter: 

def filter_by_name(name):
    return name[0] == "B"

print(list(filter(filter_by_name, my_list)))


# sorted

print(sorted(my_list))
print(sorted(my_list, reverse=True))
print(sorted(my_list, key=lambda x: x))

# reduce

def reduce_one_line(x, y):
    return x + " " + y

print(reduce(reduce_one_line, my_list))

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

student_list = [
    {"nombre": "Brais", "fecha_nacimiento": "29-04-1987", "calificaciones": [10, 3, 5, 8]},
    {"nombre": "Borja", "fecha_nacimiento": "29-04-1992", "calificaciones": [7, 6, 5, 9]},
    {"nombre": "Sonia", "fecha_nacimiento": "30-05-1999", "calificaciones": [2, 10, 10, 4]},
    {"nombre": "María", "fecha_nacimiento": "13-01-1985", "calificaciones": [4, 3, 4, 6]},
]

def calcular_promedio_calificaciones(calificaciones):
    return(sum(calificaciones)/len(calificaciones))


print("Promedio de calificaciones")
print(list(map(lambda student: {"name": student["nombre"], "grades": calcular_promedio_calificaciones(student["calificaciones"])}, student_list)))

print("Mejores estudiantes")

print(
    list(
        map(lambda student: 
        student["nombre"], 
        filter(lambda student: calcular_promedio_calificaciones(student["calificaciones"]) >=5, student_list)
        )
    )
)

print("Nacimientos")

def formatear_fechas(dates):
    return datetime.strptime(dates, "%d-%m-%Y").date()

print(list(map(lambda student:
                    student["nombre"], 
                    sorted(student_list, key= lambda student: formatear_fechas(student["fecha_nacimiento"]), reverse=True)
                    )))

print("Mayor calificación")

print(max(map(lambda student: max(student["calificaciones"]), student_list)))