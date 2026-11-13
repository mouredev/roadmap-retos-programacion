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

# Con argumento

def arg_greet(name):
    print(f"Hola, {name}!")

arg_greet("Angel")

# Con argumentos

def args_greet(greet,name):
    print(f"{greet}, {name}!")

args_greet("Hi","Angel")
args_greet(name="Angel",greet="Hi")

# Con argumentos predeterminado

def degault_arg_greet(name="Nombre?"):
    print(f"Hola, {name}!")

degault_arg_greet("Angel")
degault_arg_greet()

# Con argumentos y retorno

def return_args_greet(greet, name):
    return f"{greet}, {name}"

print(return_args_greet("Hi", "Angel"))

# Con retorno de varios valores

def multiple_returb_greet():
    return "Hola", "Python"

greet, name = multiple_returb_greet()
print(greet)
print(name)

# Con un numero variable de argumentos

def variable_arg_greet(*names):
    for name in names:
        print(f"Hola, {name}!")

variable_arg_greet("Python", "Angel", "Comunidad")

# Con un numero variable de argumentos con palabra clave

def variable_key_arg_greet(**names):
    for key, Value in names.items():
        print(f"Hola, {Value} ({key})!")

variable_key_arg_greet(
    lenguage="Python",
    name="Angel",
    alias="Dev",
    edad=26
)

"""
Funciones dentro de funciones
"""

def outer_function():
    def inner_function():
        print(f"Funcion interna: Hola, Python")
    
    inner_function()

outer_function()

"""
Funciones del lenguaje (built-in)
"""

print(len("AngelCurup"))
print(type("AngelCurup"))
print("AngelCurup".upper())

"""
Variables locales y globales
"""

global_variable = "Python"

print(global_variable)


def hello_python():
    local_var = "Hola"
    print(f"{local_var}, {global_variable}")


print(global_variable)
# print(local_var) no se puede acceder desde fuera de la 

hello_python()

"""
Extra
"""

def print_numbers(text_1, text_2):
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

print(print_numbers("texto1", "texto2"))