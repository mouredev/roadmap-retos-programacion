# #22 FUNCIONES DE ORDEN SUPERIOR
"""
 * EJERCICIO:
 * Explora el concepto de funciones de orden superior en tu lenguaje 
 * creando ejemplos simples (a tu elección) que muestren su funcionamiento.
"""

from functools import reduce
# Función como argumento

def saludo (func):
    func()
    
def saludar():
    print (f"Hola Mundo")

saludo(saludar)

# Función como retorno

def saludo_2(x):
    def saludar_2(x):
        print(x)
    return saludar_2(x)

saludo_2("Hello world")

# Funciones de orden superior del sistema

numeros = [1,3,5,2,4]

# Filter

resultado = filter (lambda x: x%2==1,numeros) # Filtra y etorna números impares
print (list(resultado))

# Map

print (list(map(lambda x: x*2,numeros))) # Realiza el recoorido de la lista operando en cada elemento

# Reduce

print (reduce(lambda x,y:x*y, numeros)) # Realiza las operaciones en todos los números de la lista de manera acumulativa

# Sorted

print (sorted(numeros)) # Ordena los elementos de la lista
print (sorted(numeros,reverse=True))



"""
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
"""

estudiantes = [
    {"nombre": "Juan", "nacimiento":25/4/1980,"calificaciones": [3,8,9,5,6]},
    {"nombre": "Pedro", "nacimiento":20/3/1990,"calificaciones": [3,9,7,5,2]},
    {"nombre": "María", "nacimiento":11/7/19850,"calificaciones": [10,9,9,9,9]}
]
def main():
    print ("-"*60)
    print ("Promedio de calificaciones por alumno")
    promedio(estudiantes)
    print ("-"*60)
    print ("Estudiantes con promedio mayor a 9")
    mayor_nueve(estudiantes)
    print ("-"*60)
    print ("La calificación más alta entre todos")
    mas_alta(estudiantes)
    print ("-"*60)
    
    
    
def promedio(estudiante):
    for elem in estudiante:
        prom = ((reduce(lambda x,y: x+y,elem["calificaciones"]))/len(elem["calificaciones"]))
        nombre = elem["nombre"]
        print (f"El estudiante {nombre} tiene un promedio de {prom}")

def mayor_nueve(estudiante):
    print (list(
        map(lambda estudiante: estudiante["nombre"],
        filter(lambda estudiante: (sum(estudiante["calificaciones"])/len(estudiante["calificaciones"]))>=9,estudiante))))

def mas_alta(estudiante):
    print (max(map(lambda estudiante: max(estudiante["calificaciones"]),estudiante)))

if __name__ == "__main__":
    main()
    
