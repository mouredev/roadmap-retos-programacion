"""
 * Funciones
"""

# Simple

def language():
    print("Python")

language()

# Con retorno

def return_language():
    return "Python"

print(return_language())

# Con multiples retornos

def multiple_return_language():
    return "This is", "Python"

text, language = multiple_return_language()

print(text)
print(language)

# Con un argumento

def argument_language(language):
    print("The language is", language)

argument_language("Python")

# Con varios argumentos

def arguments_language(language, version):
    print(f"The language is {language} and the version is {version}")

arguments_language("Python", "3.12.3")

# Con un argumento predeterminado

def default_argument_language(language="not JavaScript"):
    print("The language is", language)

default_argument_language()  # not JavaScript
default_argument_language("Python")

# Con argumentos posicionales

def positional_arguments_language(language, version):
    print(f"The language is {language} and the version is {version}")

positional_arguments_language(version="3.12.3", language="Python")

# Con un numero de variables de argumentos (args)

def args_language(*languages):
    for language in languages:
        print(language)

args_language("Python", "JavaScript", "TypeScript")

# Con un nuemero de argumentos de palabras clave (kwargs)

def kwargs_language(**languages):
    for key, value in languages.items():
        print(f"{key}: {value}")

kwargs_language(language_1="Python", language_2="JavaScript", language_3="TypeScript")

# Funciones dentro de funciones

def other_function():
    def inside_function():
        print("Inside function")

    inside_function()

other_function()

# Algunas funciones ya creadas del lenguaje

print("Hello")
print(type("Hello"))
print(len("Hello"))
print("Hello".upper())
print("Hello".replace("Hello", "HI"))

# Variable LOCAL y GLOBAL

global_variable = "Global variable"

def scope():
    local_variable = "Local variable"
    print(f"{local_variable} and {global_variable}")

print(global_variable)
# print(local_variable)  # No se puede acceder a la variable local

scope()

"""
 * Extra
"""

def extra(text_1, text_2):
    count = 0
    for number in range(1, 101):
        if number %3 == 0 and number %5 == 0:
            print(text_1, text_2)
        elif number %3 == 0:
            print(text_1)
        elif number %5 == 0:
            print(text_2)
        else:
            print(number)
            count += 1
    return count

print(extra("This is", "Python"))