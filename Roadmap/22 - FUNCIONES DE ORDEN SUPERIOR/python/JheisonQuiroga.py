"""
/*
 * EJERCICIO:
 * Explora el concepto de funciones de orden superior en tu lenguaje 
 * creando ejemplos simples (a tu elección) que muestren su funcionamiento.
"""

# 1. Ejemplo 1
# Asignando una función a una variable
def greet(name):
    return f"Hello, {name}!"

greet_someone = greet
print(greet_someone("Duban")) # Hello, Duban!

# 2. Ejemplo 2
# Pasando una función como argumento y retornando una función
def call_function(func, name):
    return func(name)

print(call_function(greet, "Duban")) # Hello, Duban!

# 3. Ejemplo 3
# Retornando una función
def compose_greet_func():
    def greet(name):
        return f"Hello, {name}!"
    return greet


greet_function = compose_greet_func()
print(greet_function("Duban")) # Hello, Duban!

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
 */
"""
from datetime import datetime
from typing import List, Tuple
from functools import reduce
import textwrap

class Student:
    def __init__(self, name: str, birthday: str, qualifications: List[float]) -> None:
        self.name = name
        self.birthday = datetime.strptime(birthday, "%d/%m/%Y")
        # Validando las calificaciones entre 0 - 10
        for grade in qualifications:
            if not 0 <= grade <= 10:
                raise ValueError(f"La calificación {grade} no se encuentra en el rango válido [0 - 10]")
            
        self.qualifications = qualifications

    def __str__(self) -> str:
        return f"{self.name}, fecha de nacimiento: ({self.birthday.strftime("%d/%m/%Y")}, calificaciones: {self.qualifications})"
    
    def average(self):
        average = round(sum(self.qualifications) / len(self.qualifications), 2)
        return average
    
    def outstanding_student(self) -> bool:
        """Determina si el estudiante tiene un promedio de 9 o superior"""
        return self.average() >= 9
    
    # Método para obtener la lista de promedios
    @classmethod
    def get_averages(cls, student_list: List['Student']) -> List[Tuple[str, float]]:
        averages = map(lambda student: (student.name, student.average()), student_list)
        return list(averages)
    
    # Método de clase para obtener los mejores estudiantes
    @classmethod
    def best_students(cls, students: List['Student']) -> List[Tuple[str, float]]:
        return list(map(
            lambda e: (e.name, e.average()), filter(lambda e: e.outstanding_student(), students)))
    
    @classmethod
    def youngest_student(cls, students:List['Student']):
        """Método para obtener a los estudiantes mas joves, utiliza una función de orden superior
        que es sorted"""
        sorted_students = sorted(students, key=lambda e: e.birthday, reverse=True)
        return list(map(lambda e: (e.name, e.birthday.strftime("%d/%m/%Y")), sorted_students))
    
    @classmethod
    def best_qualification(cls, students: List['Student']):
        all_qualifications = [qualification for est in students for qualification in est.qualifications]
        return reduce(
            lambda a, b: a if a > b else b, map(
                lambda qual: qual, all_qualifications 
            )
        )
    
students = [
    Student("Duban", "19/06/1998", [9.9, 9.0, 9.1]),
    Student("Anderson", "13/08/2005", [1.0, 3.5, 8.0]),
    Student("Josman", "05/05/2000", [9.0, 8.5, 9.5])
]

if __name__ == "__main__":
    print(textwrap.dedent(f"""\
        {"-" * 5}Resultados del analísis{"-" * 5}
        1. Promedio de calificaciones:\
"""))
    for name, average in Student.get_averages(students):
        print(f"{' ' * 5} - {name}: {average} ")
    
    print("2. Mejores estudiantes:")
    for name, average in Student.best_students(students):
        print(f"{' ' * 5} - {name}: {average} ")

    print("3. Estudiantes más jovenes:")
    for name, birthday in Student.youngest_student(students):
        print(f"{' ' * 5} - {name}: {birthday} ")

    print("4. Mejor calificación:")

    print(" " * 5, "-", Student.best_qualification(students))