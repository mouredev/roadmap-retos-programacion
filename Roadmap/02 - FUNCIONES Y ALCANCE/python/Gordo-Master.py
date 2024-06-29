"""
Funciones definidas por el usuario
"""

# Simple

def greet():
    print("¡Hola Python!")

greet()

# Con retorno

def return_greet() -> str:
    return "¡Hola, Python!"

print(return_greet())

# Con argumentos

def arg_greet(greet,name):
    print(f"{greet}, {name}!")

arg_greet("Hello","Gordo-Master")
arg_greet(name="Gordo-Master",greet="Hello")

# Con un argumento predeterminado

def default_arg_greet(name ="Python"):
    print(f"Hola {name}!")

default_arg_greet("Gordo-Master")
default_arg_greet()

# Con argumento y return

def return_arg_greet(greet,name):
    return f"{greet}, {name}!"

print(return_arg_greet("Hi","Gordo-Master"))

# Con retorno de varios valores

def multiple_return_value():
    return "Hola" , "Python"

greet, name = multiple_return_value()
print(greet)
print(name)

# Con un número variable de argumentos

def variable_arg_greet(*names):
    for name in names:
        print(f"Hola, {name}!")

variable_arg_greet("Python", "Gordo-Master", "comunidad")


# Con un número variable de argumentos con palabra claves


def variable_key_arg_greet(**names):
    for param, name in names.items():
        print(f"{name} ({param})!")

variable_key_arg_greet(
    language = "Python", 
    name = "Gordo-Master", 
    age = 29
)


"""
Funciones dentro de funciones
"""

def outer_funtion():
    def inner_funtion():
        print(f"Función interna: Hola Python")
    inner_funtion()


outer_funtion()

"""
Funciones del lenguaje (built-in)
"""

print(len("Gordo-Master"))
print(type(28))
print("Gordo-Master".upper())

"""
Variable locales y globales
"""

global_var = "Python"


def hello_python():
    local_var = "Hola"
    print(f"{local_var}, {global_var}")

print(global_var)
# print(local_var) No se puede acceder desde fuera de la función

hello_python()


"""Ejercicio Extra"""

def numbers_printer(text_1: str, text_2: str) -> int:
    
    number_count = 0

    for i in range(1,101):
        if i % 3 == 0 and i % 5 == 0:
            print(text_1 + text_2)
        elif i % 3 == 0:
            print(text_1)
        elif i % 5 == 0:
            print(text_2)
        else:
            print(i)
            number_count += 1
    
    return number_count

num_count = numbers_printer("FIZZ","BUZZ")
print(f"Cantidad de veces que salen numeros: {num_count}")
