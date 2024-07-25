'''```
/*
 * EJERCICIO:
 * Explora el concepto de funciones de orden superior en tu lenguaje 
 * creando ejemplos simples (a tu elección) que muestren su funcionamiento.
 *
 * DIFICULTAD EXTRA (opcional):
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
 */
```'''
estudiantes = [
    {
        "nombre": "Juan",
        "fecha_nacimiento": "1999-05-10",
        "calificaciones": [9, 8,9, 10, 9]
    },
    {
        "nombre": "María",
        "fecha_nacimiento": "2000-03-15",
        "calificaciones": [4, 7, 6, 5, 8]
    },
    {
        "nombre": "Pedro",
        "fecha_nacimiento": "1998-11-20",
        "calificaciones": [6, 9, 4, 5, 7]
    },
    {
        "nombre": "Ana",
        "fecha_nacimiento": "2001-07-05",
        "calificaciones": [7, 10, 8, 6, 9]
    }
]
# Promedio calificaciones: Obtiene una lista de estudiantes por nombre y promedio de sus calificaciones.
def obtener_promedio(calificaciones):
    return sum(calificaciones)/ len(calificaciones)
print(f"Los promedios son", list(map(lambda estudiante: {"nombre":estudiante['nombre'], "promedio": obtener_promedio(estudiante['calificaciones'])}, estudiantes)))
# Mejores estudiantes: Obtiene una lista con el nombre de los estudiantes que tienen calificaciones con un 9 o más de promedio.
mejores_estudiantes= list(filter(lambda estudiante: obtener_promedio(estudiante['calificaciones'])>=9,estudiantes))
print(f"Los mejores estudiantes son")
for i in mejores_estudiantes:
    print(i['nombre'])

# Nacimiento: Obtiene una lista de estudiantes ordenada desde el más joven.
print("Lista ordenada por el mas joven: ", sorted(estudiantes, key=lambda estudiante: estudiante['fecha_nacimiento'], reverse=True))

#Mayor calificación: Obtiene la calificación más alta de entre todas las de los alumnos.
calificaciones = [calificacion for estudiante in estudiantes for calificacion in estudiante['calificaciones']]
print("La calificación mas alta es: ", max(calificaciones))
