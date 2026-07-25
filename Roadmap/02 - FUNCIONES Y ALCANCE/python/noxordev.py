"""
Funciones definidas por el usuario
"""

# Funciones simples

from multiprocessing import Value


def saludo():
    print("Hola, mundo!")

saludo()

# Con retorno

def saludo_retorno():
    return "Hola, mundos!"

return_saludo = saludo_retorno()
print(return_saludo)

# Con Argumentos

def saludo_argumento(saludo, nombre):
    print(f"{saludo}, {nombre}!")

saludo_argumento("Hola", "Noxordev")
saludo_argumento(nombre="Noxordev", saludo="Hola")

# Argumentos predeterminados

def saludo_argumento_predeterminado(saludo="Hola", nombre="Ejemplo"):
    print(f"{saludo}, {nombre}!")

saludo_argumento_predeterminado("Hola", "Noxordev")

# Argumentos y retornos

def saludo_argumento_retorno(saludo, nombre):
    return f"{saludo}, {nombre}!"

print(saludo_argumento_retorno("Hola", "Noxordev"))

# Con retorno de varios valores

def saludo_argumento_retorno_varios():
    return "Hola", "Noxordev"

saludo, nombre = saludo_argumento_retorno_varios()
print(saludo)
print(nombre)

# Con un número variable de argumentos

def saludo_argumento_retorno_varios_variables(*nombres):
    for nombre in nombres:
        print(f"Hola, {nombre}!")

saludo_argumento_retorno_varios_variables("Noxordev", "Juan", "Maria", "Victor")

# Con un número variable de argumentos y palabra clave

def variable_key_arg_greet(**names):
    for key, value in names.items():
        print(f"Hola, {value} ({key})!")

variable_key_arg_greet(
    language="Python", 
    Name="Brais", 
    Alias="MoureDev", 
    Age="36"
    )

"""
Funciones dentro de funciones
"""

def outer_function():
    def inner_function():
        print("Hola, Python!")
    inner_function()

outer_function()

"""
Funciones del lenguaje
"""

print(len("Noxordev"))
print(type(36))
print("Noxordev".upper())
print("noxordev".capitalize())
print("noxordev".title())
print("noxordev".swapcase())
print("noxordev".lower())
print("noxordev".upper())
print("noxordev".capitalize())
print("noxordev".title())
print("noxordev".swapcase())

"""
Variables locales y globales
"""

global_variable = "Python"
print(global_variable)

def hello_python():
    local_var = "Hola"
    print(f"{local_var}, {global_variable}!")

print(global_variable)
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