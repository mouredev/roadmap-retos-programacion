"""
Funciones definidas por el usuario
"""
# simple función que imprime un mensaje


def hola():
    print("Hola mundo")  # Hola mundo

# función simple con retorno sin argumentos


def hola_mundo() -> str:
    return "Hola mundo"  # Hola mundo necesito un print o guardar el resultado en una variable

# función con argumentos y retorno de valor


def saludo(tipo: str, nombre: str) -> str:
    return f"{tipo}: {nombre}"  # Hola Franxisco


print(saludo("Chau", "Franxisco"))

# función con argumentos predeterminados


def saludo2(tipo: str, nombre: str = "Franxisco") -> str:
    return f"{tipo}: {nombre}"  # Hola Franxisco


print(saludo2("Hola"))

# función con multiples retornos str


def saludo3(tipo: str, nombre: str = "Franxisco") -> str:
    return tipo, nombre


# desacoplar los valores
tipo, nombre = saludo3("Buenas", "Valencia")
print(tipo)  # Hola
print(nombre)  # Franxisco

# función con multiples argumentos *


def saludo_args(*args: str) -> str:
    for arg in args:
        print(f"Hola: {arg}")


# Hola: Franxisco Hola: Valencia Hola: Python
saludo_args("Franxisco", "Valencia", "Python")
saludo_args()

# función con multiples argumentos **kwargs


def saludo_kwargs(**kwargs: str) -> str:
    for key, value in kwargs.items():
        print(f"{key}: {value}")


saludo_kwargs(nombre="Franxisco", ciudad="Valencia", lenguaje="Python")
saludo_kwargs(nombre="Franxisco", lenguaje="Python", pais="España")
saludo_kwargs()

# función dentro de otra función


def outer_function():
    print("Outer function")

    def inner_function():
        print("Inner function")
    inner_function()


outer_function()

# funciones built-in
print(len("Hola mundo"))  # 10
print(type("Hola mundo"))  # <class 'str'>

# funciones built-in por tipo de dato
print(str(5))  # 5
print(int("5"))  # 5
print(float("5"))  # 5.0
print(bool(5))  # True
print("Hola mundo".upper())  # HOLA MUNDO
print("Hola mundo".lower())  # hola mundo
print("Hola mundo".split())  # ['Hola', 'mundo']
print("Hola, mundo".split(","))  # ['Hola ', 'mundo']
print("Hola mundo".replace("mundo", "Python"))  # Hola Python
print("Hola mundo".find("mundo"))  # 5
print("Hola mundo".count("o"))  # 2
print("Hola mundo".startswith("Hola"))  # True
print("Hola mundo".endswith("mundo"))  # True
print("Hola mundo".isnumeric())  # False
print("Hola mundo".isalpha())  # False
print("Hola mundo".isalnum())  # False
print("Hola mundo".islower())  # False
print("Hola mundo".isupper())  # False
print("Hola mundo".istitle())  # False
print("Hola mundo".isspace())  # False
print("Hola mundo".strip())  # Hola mundo
print("Hola mundo".lstrip())  # Hola mundo
print("Hola mundo".rstrip())  # Hola mundo
print("Hola mundo".center(20))  # Hola mundo
print("Hola mundo".ljust(20))  # Hola mundo
print("Hola mundo".rjust(20))  # Hola mundo
print("Hola mundo".zfill(20))  # 000000000Hola mundo
print("hola mundo".capitalize())  # Hola mundo
print("Hola mundo".title())  # Hola Mundo
print("Hola mundo".swapcase())  # hOLA MUNDO

# ejemplos ambito de variables
# variable global
x = 5
# variable local


def sumar(x: int, y: int) -> int:
    return x + y


print(sumar(7, 5))  # 12
print(x)  # 5

'''
DIFICULTAD EXTRA
'''


def print_numbres(text_1: str, text_2: str) -> int:
    count = 0
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print(f"{i}: {text_1} + {text_2}")
        elif i % 3 == 0:
            print(f"{i}: {text_1}")
        elif i % 5 == 0:
            print(f"{i}: {text_2}")
        else:
            print(i)
            count += 1
    print(f"Total de veces que salen nros: {count}")


print_numbres("Fizz", "Buzz")
