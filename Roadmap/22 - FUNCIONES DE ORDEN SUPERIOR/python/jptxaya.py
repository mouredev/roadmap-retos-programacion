# #22 FUNCIONES DE ORDEN SUPERIOR


# ```
# /*
#  * EJERCICIO:
#  * Explora el concepto de funciones de orden superior en tu lenguaje 
#  * creando ejemplos simples (a tu elección) que muestren su funcionamiento.
#  *
#  * DIFICULTAD EXTRA (opcional):
#  * Dada una lista de estudiantes (con sus nombres, fecha de nacimiento y 
#  * lista de calificaciones), utiliza funciones de orden superior para 
#  * realizar las siguientes operaciones de procesamiento y análisis:
#  * - Promedio calificaciones: Obtiene una lista de estudiantes por nombre
#  *   y promedio de sus calificaciones.
#  * - Mejores estudiantes: Obtiene una lista con el nombre de los estudiantes
#  *   que tienen calificaciones con un 9 o más de promedio.
#  * - Nacimiento: Obtiene una lista de estudiantes ordenada desde el más joven.
#  * - Mayor calificación: Obtiene la calificación más alta de entre todas las
#  *   de los alumnos.
#  * - Una calificación debe estar comprendida entre 0 y 10 (admite decimales).
#  */


def suma(a,b):
    return a + b

def resta(a,b):
    return a - b

multiplicar = lambda a,b: a*b

def operacion(action,a,b):
    print(action(a,b,))

operacion(suma,4,5)
operacion(resta,5,4)
operacion(multiplicar,5,4)

lista = [1,2,3,4]
print(lista)
print("filter")
filtered = list(filter(lambda a: a % 2 == 0,lista))
print(filtered)

print("map")
mapped = list(map(lambda a: a * 3,lista))
print(mapped)

from functools import reduce
print("reduce")
reduced = reduce(lambda a, b: a+b, lista)
print(reduced)

lista_estudiantes = [{"name": "jptx1","age": 30, "califications":[5,6,8,8.7,4.5]},
                     {"name": "jptx2","age": 20, "califications":[9.2,6,8,9.3,9.5]},
                     {"name": "jptx3","age": 35, "califications":[4,5.5,8,9.7,4.5]},
                     {"name": "jptx4","age": 18, "califications":[9,9.3,8.5,9.9]}]




print(lista_estudiantes)
print("Promedio calificaciones")
def promedio_calif(calif):
    return reduce(lambda a,b: a+b,list(filter(lambda a: a >= 0 and a <= 10,calif))) / len(calif)


promedio_calificaciones = list(map(lambda estudiante: dict(name = estudiante.get("name"),
                                                  califications = promedio_calif(estudiante.get("califications"))),
                                   lista_estudiantes))

print(promedio_calificaciones)

print("Mejores estudiantes")
print(list(filter(lambda estudiante: estudiante["califications"] >= 9,promedio_calificaciones)))

print("Ordenacion Estudiantes Nacimiento")
print(sorted(lista_estudiantes,key= lambda estudiante: estudiante["age"]))

print("Mayor Calificacion")
print(max(map(lambda estudiante: max(estudiante["califications"]),lista_estudiantes)))

