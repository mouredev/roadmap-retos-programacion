"""
Funciones definidas por el usuario
"""

# Simple

def greet():
    print("Hola, Python!")

greet()

# Con retorno

def return_greet():
    return "Hola, Python!"

print(return_greet())

# Con un argumento

def arg_greet(name):
    print(f"Hola, {name}!")

arg_greet("Angel")

# Con argumentos

def arg_greet(greet, name):
    print(f"{greet}, {name}!")

arg_greet("Hi", "Angel")

# Con un argumento predeterminado

def default_arg_greet(name="Python"):
    print(f"Hola, {name}!")


default_arg_greet("Angel")
default_arg_greet()

# Con argumentos y retorno

def return_args_greet(greet, name):
    return f"{greet}, {name}"

print(return_args_greet("Hi", "Angel"))

# Con retorno de varios valores

def multiple_return_greet():
    return "Hola", "Python"

greet, name = multiple_return_greet()
print(greet)
print(name)

# Con numero variables de argumentos

def variable_arg_greet(*names):
    for name in names:
        print(f"Hola, {name}")

variable_arg_greet("Python", "Angel", "Miguel", "Comunidad")

# Con un numero de variable de argumentos con palabra clave

def variable_key_arg_greet(**names):
    for key, value in names.items():
        print(f"{value} ({key})!")

variable_key_arg_greet(
    language="Python",
    name="Angel",
    alias="AngelBlk",
    age=30
)

"""
Funciones dentro de funciones
"""

def outer_function():
    def inner_function():
        print("Funcion interna: Hola, Python !")
    inner_function()

outer_function()

"""
Funciones del lenguaje (buit-in)
"""

print(len("Angel"))
print(type(30))
print("Angel".upper())

"""
Variables locales y globales
"""

global_var = "Python"


def hello_python():
    local_var = "Hola"
    print(f"Hello, {global_var}!")

print(global_var)
# print(local_var) No se puede acceder desde fuera de la funcion

hello_python()

"""
Extra
"""

def print_numbers(text_1, text_2)-> int:
    count = 0
    for number in range(1, 101):
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