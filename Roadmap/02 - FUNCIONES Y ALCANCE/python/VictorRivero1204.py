"""
Funciones definidas por el usuario
"""

# Simple

def greet():
    print("Hola, Python!") 

greet()

# Con retorno 

def return_greet():
    return "Hola, Python 2!"

print(return_greet())

# Con argumento

def arg_greet(name):
    print(f"Hola, {name}!")

arg_greet("Victor")

# Con argumentos

def arg_greet(greet, name):
    print(f"{greet}, {name}!")

arg_greet("Hi", "Victor")
arg_greet(name="Victor", greet="Hi")

# Con un argumento predeterminado

def default_arg_greet(name = "Python"):
    print(f"Hola, {name}!")

default_arg_greet("Victor")
default_arg_greet()

# Con argumentos y return

def return_arg_greet(greet, name):
    return f"{greet}, {name}!"

print(return_arg_greet("Hi", "Victor"))

# Con retorno de varios valores

def multiple_return_greet():
    return "Hola", "Python"

print(multiple_return_greet())

greet, name = multiple_return_greet()
print(greet)
print(name)

# Con un numero variable de argumentos

def variable_arg_greets(*names):
    for name in names:
        print(f"Hola, {name}!")

variable_arg_greets("Python", "Victor", "Jose", "Maria")

# Con un numero variable de argumentos con palabra clave 

def variable_key_arg_greets(**names):
    for key, value in names.items():
        print(f"{value}  ({key})")

variable_key_arg_greets(
    language="Python", 
    name="Victor", 
    user="VictorRivero1204", 
    edad=23
)

"""
Funciones dentro de funciones
"""

def outer_function():
    def inner_function():
        print("Funcion interna: Hola, Python!")
    inner_function()

outer_function()

"""
Funciones del lenguaje (built-in)
"""

print(len("Victor"))
print(type(23))
print("Victor" .upper())

"""
Variables locales y globales
"""

global_var = "Python"


def hello_python():
    local_var = "Hola"
    print(f"{local_var}, {global_var}!")

print(global_var)
# print(local_var) No se puede acceder desde fuera de la funcion

hello_python()

"""
Extra
"""

def print_numbers(text_1, text_2) -> int:
    count = 0 
    for number in range (1, 101):
        if number % 3 == 0 and number % 5 == 0:
            print(text_1 + text_2)
        elif number % 3 == 0:
            print(text_1)
        elif number % 5 == 0:
            print(text_2)
        else:
            print(number)
            count += 1
    return count

print(print_numbers("Fizz", "Buzz"))