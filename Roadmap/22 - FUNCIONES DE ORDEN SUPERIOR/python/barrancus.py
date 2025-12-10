# 22 - Python
# 
# EJERCICIO:
# Explora el concepto de funciones de orden superior en tu lenguaje 
# creando ejemplos simples (a tu elección) que muestren su funcionamiento.
# 
# DIFICULTAD EXTRA (opcional):
# Dada una lista de estudiantes (con sus nombres, fecha de nacimiento y 
# lista de calificaciones), utiliza funciones de orden superior para
# realizar las siguientes operaciones de procesamiento y análisis:
# - Promedio calificaciones: Obtiene una lista de estudiantes por nombre
#   y promedio de sus calificaciones.
# - Mejores estudiantes: Obtiene una lista con el nombre de los estudiantes
#   que tienen calificaciones con un 9 o más de promedio.
# - Nacimiento: Obtiene una lista de estudiantes ordenada desde el más joven.
# - Mayor calificación: Obtiene la calificación más alta de entre todas las
#   de los alumnos.
# - Una calificación debe estar comprendida entre 0 y 10 (admite decimales).
# 
from random import randint, choice
from functools import reduce, partial

class Counter:
    def __iter__(self):
        self.a = 1
        return self
    
    def __next__(self):
        x = self.a
        self.a += 1
        return x

def serparacion(cadena) -> str:
    global contador
    print(f'\nEjercicio {next(contador)}. {cadena * 20}')

contador = iter(Counter())

students = [
    {
        "nombre": "Sofía Martínez",
        "fecha_nacimiento": "2005-03-14",
        "calificaciones": [8.5, 9.0, 9.5, 8.8]
    },
    {
        "nombre": "Alejandro López",
        "fecha_nacimiento": "2004-11-22",
        "calificaciones": [7.0, 6.5, 7.8, 6.0]
    },
    {
        "nombre": "Valeria González",
        "fecha_nacimiento": "2005-01-10",
        "calificaciones": [9.8, 10.0, 9.9, 9.5]
    },
    {
        "nombre": "Diego Rodríguez",
        "fecha_nacimiento": "2004-07-05",
        "calificaciones": [5.5, 6.0, 5.0, 6.2]
    },
    {
        "nombre": "Camila Fernández",
        "fecha_nacimiento": "2005-09-30",
        "calificaciones": [8.0, 8.5, 7.5, 8.2]
    },
    {
        "nombre": "Mateo Sánchez",
        "fecha_nacimiento": "2004-05-18",
        "calificaciones": [6.5, 7.0, 6.8, 7.2]
    },
    {
        "nombre": "Isabella Pérez",
        "fecha_nacimiento": "2005-12-03",
        "calificaciones": [9.0, 9.2, 8.8, 9.5]
    },
    {
        "nombre": "Santiago Gómez",
        "fecha_nacimiento": "2004-02-14",
        "calificaciones": [7.5, 7.0, 8.0, 7.8]
    },
    {
        "nombre": "Valentina Ruiz",
        "fecha_nacimiento": "2005-06-21",
        "calificaciones": [8.8, 8.5, 9.0, 8.2]
    },
    {
        "nombre": "Daniel Díaz",
        "fecha_nacimiento": "2004-08-09",
        "calificaciones": [6.0, 5.8, 6.5, 6.2]
    },
    {
        "nombre": "Lucía Hernández",
        "fecha_nacimiento": "2005-04-17",
        "calificaciones": [9.5, 9.8, 9.2, 9.7]
    },
    {
        "nombre": "Nicolás Álvarez",
        "fecha_nacimiento": "2004-10-25",
        "calificaciones": [7.2, 7.5, 7.0, 7.8]
    },
    {
        "nombre": "Mariana Torres",
        "fecha_nacimiento": "2005-02-05",
        "calificaciones": [8.2, 8.0, 8.5, 8.1]
    },
    {
        "nombre": "Samuel Flores",
        "fecha_nacimiento": "2004-12-12",
        "calificaciones": [5.0, 5.5, 6.0, 5.2]
    },
    {
        "nombre": "Gabriela Romero",
        "fecha_nacimiento": "2005-08-28",
        "calificaciones": [9.0, 8.8, 9.2, 9.5]
    },
    {
        "nombre": "Felipe Castillo",
        "fecha_nacimiento": "2004-03-08",
        "calificaciones": [7.8, 7.5, 8.0, 7.2]
    },
    {
        "nombre": "Victoria Medina",
        "fecha_nacimiento": "2005-11-15",
        "calificaciones": [8.5, 8.2, 8.8, 8.5]
    },
    {
        "nombre": "Emiliano Silva",
        "fecha_nacimiento": "2004-06-02",
        "calificaciones": [6.2, 6.5, 6.0, 6.8]
    },
    {
        "nombre": "Ximena Castro",
        "fecha_nacimiento": "2005-05-20",
        "calificaciones": [9.2, 9.5, 9.0, 9.8]
    },
    {
        "nombre": "Andrés Morales",
        "fecha_nacimiento": "2004-09-11",
        "calificaciones": [7.0, 7.2, 6.8, 7.5]
    },
    {
        "nombre": "Renata Ortega",
        "fecha_nacimiento": "2005-07-29",
        "calificaciones": [8.0, 8.2, 7.8, 8.5]
    },
    {
        "nombre": "Joaquín Vargas",
        "fecha_nacimiento": "2004-01-30",
        "calificaciones": [5.8, 6.0, 5.5, 6.2]
    },
    {
        "nombre": "Elena Navarro",
        "fecha_nacimiento": "2005-10-08",
        "calificaciones": [9.8, 9.5, 9.2, 9.9]
    },
    {
        "nombre": "Gabriel Mendoza",
        "fecha_nacimiento": "2004-04-22",
        "calificaciones": [7.5, 7.8, 7.2, 8.0]
    },
    {
        "nombre": "Daniela Rojas",
        "fecha_nacimiento": "2005-03-01",
        "calificaciones": [8.5, 8.8, 8.2, 8.9]
    },
    {
        "nombre": "Adrián Cruz",
        "fecha_nacimiento": "2004-12-20",
        "calificaciones": [6.5, 6.8, 6.2, 7.0]
    }
]

def func_superior_order() -> None:
    serparacion('-:-')
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(f'Numeros iniciales: {numbers}')
    print(f'Funcion de orden superior map(lambda x: x**2, numbers): {list(map(lambda x: x**2, numbers))}')
    print(f'Funcion de orden superior filter(lambda x: x % 2 == 0, numbers): {list(filter(lambda x: x % 2 == 0, numbers))}')
    print(f'Funcion de orden superior reduce(lambda x, y: x + y, numbers): {reduce(lambda x, y: x + y, numbers)}')
    print(f'Funcion de orden superior sorted(numbers, reverse=True): {sorted(numbers, reverse=True)}')
    basetwo = partial(int, base=2)
    basetwo.__doc__ = 'Convert base 2 string to an int.'
    basetwo.__name__ = 'basetwo'
    print(f'Funcion de orden superior partial(int, base=2): {basetwo.__doc__}')
    print(basetwo('10010')) 
    print(f'bin(18): {bin(18)}')

def extra() -> None:
    serparacion('-:-')
    while True:
        print('\nPor favor serlecciona una de las opciones a mostrar:')
        print('1 - Promedio calificaciones de los estudiantes.')
        print('2 - Mostrar los mejores estudiantes (promedio >= 9).')
        print('3 - Mostrar estudiantes ordenados desde el más joven.')
        print('4 - Mostrar la mayor calificación entre todos los estudiantes.')
        print('0 - Salir.')
        option = input('Opción seleccionada: ')
        match option:
            case '1':
                print(f"\n{'Nombre':<20} | {'Promedio':<10}")
                print("-" * 33)
                for student in students:
                    print(f"{student['nombre']:<20} | {average_grades(student["calificaciones"]):.2f}")
            case '2':
                print(f"\n{'Nombre':<20} | {'Promedio':<10}")
                print("-" * 33)
                for student in students:
                    aver = list(best_average_grades(student["calificaciones"]))
                    if len(aver) > 0: print(f"{student['nombre']:<20} | {aver[0]:.2f}")
            case '3':
                print(f"\n{'Nombre':<20} | {'Fecha Nacimiento':<18}")
                print("-" * 41)
                for student in sorted(students, key=lambda x: x["fecha_nacimiento"], reverse=True):
                    print(f"{student['nombre']:<20} | {student["fecha_nacimiento"]}")
            case '4':
                print(f"\n{'Nombre':<20} | {'Promedio':<10}")
                print("-" * 33)
                highest_grade_value = highest_grade(students)
                for student in students:
                    if max(student["calificaciones"]) == highest_grade_value:
                        print(f"{student['nombre']:<20} | {max(student['calificaciones']):.2f}")
            case '0':
                print('\nSalir.')
                break
            case _:
                print('\nOpción no válida. Por favor, intenta de nuevo.')
    
def average_grades(grades: list) -> float:
    return reduce(lambda x, y: x + y, grades) / len(grades)    

def best_average_grades(grades: list) -> filter:
    return filter(lambda x: x >= 9, [average_grades(grades)])

def highest_grade(students: list) -> float:
    return max(list(map(lambda student: max(student["calificaciones"]), students)))

def main():
    print('\nFUNCIONES DE ORDEN SUPERIOR')
    func_superior_order()
    extra()

if __name__ == '__main__':
    main()
