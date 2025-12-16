# Funciones

# Simples

def saludo():
    print("Hola Python!")

saludo()

# Con retorno

def retorno():
    return "Buenos dias"

print(retorno())

# Con un argumento

def arg_saludo(name):
    print(f"Hola, {name}")

arg_saludo("David")

# Con argumentos 

def args_saludo(greet, name):
    print(f"{greet}, {name}!")

args_saludo("Hi", "David")
args_saludo(name="David", greet="Hi")

# Con un argumento predeterminado

def default_arg_saludo(name="Python"):
    print(f"Hola, {name}")

default_arg_saludo("David")
default_arg_saludo()

# Con argumentos y retorno

def return_args_saludo(greet, name):
    return f"{greet}, {name}!"

print(return_args_saludo("Hi", "David"))

# Con retorno de varios valores

def multiple_return_greet():
    return "Hola", "Python"

greet, name = multiple_return_greet()
print(greet)
print(name)

# Con un número variable de argumentos

def variable_arg_greet(*names):
    for name in names:
        print(f"Hola, {name}")

variable_arg_greet("Python", "David", "Oriol", "Maribel")

# Con un número variable de argumentos con palabra clave

def variable_key_args_greet(**names):
    for key, value in names.items():
        print(f"{value} ({key})") 

variable_key_args_greet(
    language="Python",
    name="David", 
    alias="descobedoc",
    age=52
    )

# Funciones dentro de funciones

def function_ext():
    def function_int():
        print("Hola, Python!")
    function_int()

function_ext()

# Funciones del lenguaje (built-in)

print("descobedoc")
print(len("descobedoc"))
print(type(52))
print("descobedoc".upper())
print("descobedoc".capitalize())

# Variables globales y locales

global_var = "Python"

def hello_python():
    local_var = "Hola"
    print(f"{local_var}, {global_var}")

print(global_var)
# print(local_var) No se puede llamar una variable local desde fuera de la función

hello_python()

# Dificultad extra

def fizzbuzz():
    first_string = input("Introduce la primera palabra: ")
    second_string = input("Introduce la segunda palabra: ") 
    number = 0
    for index in range(1, 101):
        if index % 3 == 0 and index % 5 == 0:
            print(first_string + second_string)
        elif index % 3 == 0:
            print(first_string)
        elif index % 5 == 0:
            print(second_string)
        else:
            print(index)
            number += 1
    return print(number)

fizzbuzz()