"""
 EJERCICIO:
 Explora el concepto de funciones de orden superior en tu lenguaje 
 creando ejemplos simples (a tu elección) que muestren su funcionamiento.

 DIFICULTAD EXTRA (opcional):
 Dada una lista de estudiantes (con sus nombres, fecha de nacimiento y 
 lista de calificaciones), utiliza funciones de orden superior para 
 realizar las siguientes operaciones de procesamiento y análisis:
 - Promedio calificaciones: Obtiene una lista de estudiantes por nombre
   y promedio de sus calificaciones.
 - Mejores estudiantes: Obtiene una lista con el nombre de los estudiantes
   que tienen calificaciones con un 9 o más de promedio.
 - Nacimiento: Obtiene una lista de estudiantes ordenada desde el más joven.
 - Mayor calificación: Obtiene la calificación más alta de entre todas las
   de los alumnos.
 - Una calificación debe estar comprendida entre 0 y 10 (admite decimales).
"""
from functools import reduce
from random import uniform, randint, choice
from datetime import datetime
from typing import Any, Union

type_number = Union[int, float]
type_str_number = Union[oct, hex, bin]

print(f"{'#' * 47}")
print(f"##  Explicación  {'#' * 30}")
print(f"{'#' * 47}")

print(r"""Para profundizar sobre este tema buscar "programación funcional en python".
Las funciones de orden superior son funciones capaces de recibir como argumento y/o retornar otra función, por ejemplo:

1- función "operar" que recibe como argumento la función a ejecutar ("sumar" o "multiplicar") más sus argumentos:
    def sumar(*args: type_number) -> type_number:
        return sum(args)
    
    
    def multiplicar(*args: type_number) -> type_number:
        return reduce(lambda a, b: a * b, args)
    
    
    def operar(funcion, *args: type_number) -> type_number:
        return funcion(*args)
    
    
    print("Aritmética pasando función como argumento: ")
    print(f"\tSumar: {operar(sumar, 1, 2.1, 3, 4.75)}")
    print(f"\tMultiplicar: {operar(multiplicar, 1, 2, 3)}")

2- función "conversor" que recibe un string y retorna una función ("binario", "hexadecimal" o "octal"):
    def conversor(tipo: str) -> type_str_number:
        def binario(numero: int) -> str:
            return bin(numero).lstrip("0b")
    
        def hexadecimal(numero: int) -> str:
            return hex(numero).lstrip("0x")
    
        def octal(numero: int) -> str:
            return oct(numero).lstrip("0o")
    
        funcion = {"binario": binario, "hexadecimal": hexadecimal, "octal": octal}
    
        return funcion[tipo]
    
    
    data = 27
    print("Calculo conversiones numéricas con funcioón que retorna función: ")
    print(f"\tBinario: {conversor('binario')(data)}")
    print(f"\tHexa: {conversor('hexadecimal')(data)}")
    print(f"\tOctal: {conversor('octal')(data)}")

3- usando "lambda" que es una función aónima para resolver un paso sencillo:
    data = 3
    circulo = lambda r: (3.1416 * pow(r, 2)).__round__(2)
    area = circulo(data)
    print("Calculo área de círculo usando lambda: ", end="")
    print(area)

4- usando "map" que aplica una función a un iterable:
    data = ["2.7178", "3.1416", "12", "123.45678", "49"]
    mapa = lambda a: float(a).__round__(2)
    lista_mapeada = map(mapa, data)
    print("Paso a decimal de dos pocisiones con map: ", end="")
    print(list(lista_mapeada))

5- usando "filter" que mantiene o excluye elementos de un iterable:
    data = ["Hola", 123, (1, 2, 3), "Chau", 34, 33, "76", 3.1416, {"azul", "rojo", "amarillo"}, "2.7178"]
    filtro = lambda a: a.__class__.__name__ in ("int", "float") or (a.__class__.__name__ == "str" and a.replace('.', '', 1).isdecimal())
    lista_filtrada = filter(filtro, data)
    print("Extraigo tipos numéricos de lista de tipo heterogéneos con filter: ", end="")
    print(list(lista_filtrada))

6- usando reduce que aplica una función a un iterable tomando de a dos elementos por vez (el resultado de aplicar la función + el elemento que sigue):
    data = "lorem ipsum dolor sit amet consectetur adipiscing elit sed do eiusmod tempor"
    cuenta_o = lambda a, b: a + sum(1 for x in b if x == 'o')
    reduccion = reduce(cuenta_o, data, 0)
    print("Cuento 'o' en texto usando reduce: ", end="")
    print(reduccion)

Todo ésto retorna:

Aritmética pasando función como argumento: 
    Sumar: 10.85
    Multiplicar: 6

Calculo conversiones numéricas con funcioón que retorna función: 
    Binario: 11011
    Hexa: 1b
    Octal: 33

Calculo área de círculo usando lambda: 28.27

Paso a decimal de dos pocisiones con map: [2.72, 3.14, 12.0, 123.46, 49.0]

Extraigo tipos numéricos de lista de tipo heterogéneos con filter: [123, 34, 33, '76', 3.1416, '2.7178']

Cuento 'o' en texto usando reduce: 7
""")

print(f"\n{'#' * 52}")
print(f"##  Dificultad Extra  {'#' * 30}")
print(f"{'#' * 52}")


def get_random_student(function: str) -> Any:
    def get_valid_name() -> str:
        import requests
        api_names_url = "https://randomuser.me/api/"
        lower_letters = list(map(chr, range(ord("a"), ord("z") + 1)))

        while True:
            req = requests.get(api_names_url)
            data = req.json()
            firstname = data["results"][0]["name"]["first"]
            lastname = data["results"][0]["name"]["last"]
            if all([c.lower() in lower_letters for c in firstname + lastname]):  # evitar otros alfabetos
                break
        return firstname + " " + lastname

    def get_valid_birthdate() -> datetime:
        return datetime(randint(1996, 2005), randint(1, 12), randint(1, 28))

    def get_list_grades() -> list:
        base = choice([0, 5, 8])  # to enforce a better grades sample
        return list(map(lambda a: uniform(base, 10).__round__(2), range(1, 11)))

    f_name = {"get_valid_name": get_valid_name, "get_valid_birthdate": get_valid_birthdate, "get_list_grades": get_list_grades}
    return f_name[function]


def get_student_list(total: int) -> list:
    student_list = []
    print(f"\nAdding {total} students .", end="")
    for ind in range(total):
        student_list.append({"name": get_random_student("get_valid_name")(),
                             "birthdate": get_random_student("get_valid_birthdate")(),
                             "grades": get_random_student("get_list_grades")()})
        print(".", end="")
    print()
    return student_list


def get_average_grades() -> list:
    averages = []

    avg_grades = lambda a, b: (a / b).__round__(2)
    for s in student_list:
        suma = reduce(lambda a, b: a + b, s["grades"])      # obvio, sum() funciona... es para dar ejemplo de reduce
        largo = s["grades"].__len__()
        averages.append({"name": s["name"], "average": avg_grades(suma, largo)})
    return averages


def print_stats(function: str) -> None:
    def list_students():
        for std in student_list:
            print(f"\tStudent: {std['name']}  /  Birthdata: {std['birthdate'].strftime('%b %d, %Y')}  /  Grades: {std['grades']}")

    def average_grades_per_student():
        for avg in sorted(get_average_grades(), key=lambda d: d["average"], reverse=True):
            print(f"\tStudent: {avg['name']}  /  Average: {avg['average']}")

    def best_averages():
        for avg in filter(lambda a: a["average"] >= 9.0, sorted(get_average_grades(), key=lambda d: d["average"], reverse=True)):
            print(f"\tStudent: {avg['name']}  /  Average: {avg['average']}")

    def best_student():
        std = (sorted(get_average_grades(), key=lambda d: d["average"], reverse=True)[0])
        print(f"\tStudent: {std['name']}  /  Average: {std['average']}")

    def get_birthdate():
        for std in sorted(student_list, key=lambda d: d["birthdate"]):
            print(f"\tStudent: {std['name']}  /  Birthdata: {std['birthdate'].strftime('%b %d, %Y')}")

    f_callable = {"list_students": list_students, "average_grades_per_student": average_grades_per_student,
                  "best_averages": best_averages, "get_birthdate": get_birthdate, "best_student": best_student}
    f_callable[function]()


student_list = sorted(get_student_list(30), key=lambda d: d["name"])

print("\nStudents")
print_stats("list_students")
print("\nAverage grades")
print_stats("average_grades_per_student")
print("\nAverages >= 9.0")
print_stats("best_averages")
print("\nBest student")
print_stats("best_student")
print("\nBirthdates")
print_stats("get_birthdate")
