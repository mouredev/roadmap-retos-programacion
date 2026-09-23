"""
Funciones definidas por el usuario
"""

# Simple

def saludo():
    print("Hola, Python!")


saludo()

# Con retorno

def return_saludo():
    return "Hola, Python!"


print(return_saludo())

# Con argumentos

def saludo_argumento(frase, name):
    print(f"{frase} {name}")

saludo_argumento("Hola", "Neslin")

# Con un argumento predeterminado

def default_arg_saludo(greet, name="Python"):
    print(f"{greet} {name}")

default_arg_saludo("Hello")


# Con argumentos y retorno

def return_args_sal(greet, name):
    return f"{greet}, {name}!"

print(return_args_sal("Hi", "Neslin"))

# Con retorno de varios valores

def multiple_return_sal():
    return "Hola", "Python"

greet, name = multiple_return_sal()
print(greet)
print(name)
   
# Con un número variable de argumentos

def variable_arg_greet(*names):
    for name in names:
        print(f"Hola, {name}!")

variable_arg_greet("Python", "SQL", "JS")

# Con un número variable de argumentos con palabras clave

def variable_key_arg_greet(**names):
    for key, value in names.items(): # DICCIONARIO
        print(f"Hola, {value} ({key})!")

variable_key_arg_greet(
    Language="Python", 
    name="Nox",
    apodo="NoxDev",
    edad="18"
)

# Funciones dentro de funciones

def outer_function():
    def inner_function():
        print("Función Interna en Python")
    inner_function()

outer_function()
 
# Funciones del lenguaje

print(len('Neslin'))
print(type('Neslin'))
print('Neslin'.upper())

# Variables locales y globales

global_variable = "Python"

def hello_python():
    local_variable = "Hola"
    print(f"{local_variable}, {global_variable}!")

hello_python()

"""
DIFICULTAD EXTRA:
"""

def print_numbers(text_1, text_2)-> int:

    i = 0
    for number in range(1, 101):
        if number % 3 == 0 and number % 5 == 0:
            print(text_1 + ' y también ' + text_2)

        elif number % 3 == 0:
            print(text_1)

        elif number % 5 == 0:
             print(text_2)

        else:
            print(number)
            i += 1


    return i


print(print_numbers("Es múltiplo de 3", "Es múltiplo de 5"))

