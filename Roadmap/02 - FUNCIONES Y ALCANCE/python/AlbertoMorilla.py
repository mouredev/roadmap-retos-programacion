"""
Funciones definidas por el usuario
"""
# Simple

def saludar():
    print("Hola kiyo")

saludar()

# Con retorno

def retornar_saludo():
    return "Hola kiyo"

saludo = retornar_saludo()
print(retornar_saludo())

# Con un argumento

def arg_saludo(name):
    print (f"Hola, {name}!")

arg_saludo("Alberto")

# Con argumentos

def args_saludo(saludo, name):
    print (f"{saludo}, {name}!")

args_saludo("Ei", "Alberto") 

# Con un argumento predeterminado

def default_arg_saludo(name="Python"):
    print(f"Hola, {name}!")

default_arg_saludo("Betico")
default_arg_saludo()

# Con argumentos y retorno

def return_args_saludo(name="Python"):
    return f"{saludo}, {name}!"

print(return_args_saludo())

# Con retorno de varios valores

def return_multiple_values():
    return "Hola", "Ei"

saludo, name = return_multiple_values()
print(saludo)
print(name)

# Con un numero variable de argumentos

def variable_arg_saludo(*names):
    for name in names:
        print(f"Hola, {name}!")

variable_arg_saludo("Python", "Alberto", "Betico")

# Con un numero variable de argumentos con palabra clave

def variable_arg_saludo(**names):
    for key, valeu in names.items():
        print(f"Hola, {valeu} ({key})!")

variable_arg_saludo(
    lenguaje="Python",
    name="Alberto", 
    edad="36", 
    alias="Pepino"
    )

"""
Funciones dentro de funciones
"""

def otra_function():
    def inner_function():
        print("Hola, soy una función interna")
    inner_function()

otra_function()

"""
Funciones del lenguaje (built-in)
"""

print(len("Morilla".upper()))
print(type("Morilla"))
print("Morilla".upper())

"""
Variables locales y globales
"""

global_var = "Python"


def hello_python():
    local_var = "hola"
    print(f"{local_var}, {global_var}!")

print(global_var)
# print(local_var) No se puede acceder desde fuera de la funcion

hello_python()

"""
Extra
"""

def print_numbers(text1, text2)-> int:
    count = 0
    for number in range(1, 101):
        if number % 3 == 0 and number % 5 == 0:
            print(text1 + text2)
        elif number % 3 == 0:
            print(text1)
        elif number % 5 == 0:
            print(text2)       
        else:
            print(number)
            count += 1
    return count

print(print_numbers("Fizz", "Buzz"))