'''
 EJERCICIO:
* Explora el concepto de funciones de orden superior en tu lenguaje 
* creando ejemplos simples (a tu elección) que muestren su funcionamiento.
'''

from functools import reduce
from datetime import datetime

def dobla():
    def multiplica(n):
        return n * 2
    return multiplica

multiplica = dobla()
print(multiplica(9))
print(dobla()(4))

cadena = "Ricardo"
def contar(func, texto):
    return func(texto)
print(contar(len,cadena))

#Sistema map, filter, sorted y reduce

#map aplica una función a cada elemento aprámetro

Lista = [1, 2, 3, 4, 5, 6]
Tupla = ("e", "c", "a", "d", "b")
Conjunto = {7, 6, 5}

print(list(map(lambda x: -x, Lista)))

#filter aplica una función al parametro y devuelve los casos que la verifican

print(list(filter(lambda x: x % 2 == 0, Lista)))

#sort ordena los elementos del parámetro

print(sorted(Lista))
print(sorted(Tupla, reverse=True))
print(sorted(Conjunto))

#reduce aplica una operación en bucle acumulando el resultado

def mul(a,b):
    return a * b

print(reduce(lambda a, b: a + b, (sorted(Tupla))))
print(f"Factorial de 7: {reduce(mul,  Lista)}")


'''
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
'''

students = [
    {"name": "Elna", "birthdate": "01-09-1975", "grades": [10, 8.5, 9, 10]},
    {"name": "moure", "birthdate": "04-08-1995", "grades": [1, 9.5, 2, 4]},
    {"name": "mouredev", "birthdate": "15-12-2000", "grades": [4, 6.5, 5, 2]},
    {"name": "supermouredev", "birthdate": "25-01-1980",
        "grades": [10, 9, 9.7, 9.9]}
]

def media (Lista:list)->float:
    return sum(Lista)/len(Lista)

print("Media " * 10)

print(list(map(lambda student: {
        "Nombre": student["name"],
        "Media": media(student["grades"])
    }, students ))
)

print("-" * 60)
print("Calificaciones con un 9 o más de promedio.")
print(list(map(lambda student: 
        student["name"],
        filter(lambda student: media(student["grades"]) >= 9, students )))
)

print("-" * 60)
print("Estudiantes ordenados desde el más joven.")

print(list(map(lambda student: {
        "Nombre": student["name"],
        "Nacimiento": student["birthdate"]
    }, sorted(students, key=lambda student: datetime.strptime(student["birthdate"], "%d-%m-%Y"), reverse=True))))           

print("-" * 60)
print("La calificación más alta de entre todas las de los alumnos.")

print(max(list(map(lambda student: max(student["grades"])
                                 , students))))


        