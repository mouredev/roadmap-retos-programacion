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

arg_greet("Mario")


# Con argumentos
def args_greet(greet, name):
    print(f"{greet}, {name}!")

args_greet("Hi","Mario")


#Con un argumento predeterminado
def default_arg_greet(name = "Pedro", greet = "Hi"):
    print(f"{greet}, {name}!")

default_arg_greet(greet = "Hola")
default_arg_greet("Mario")


# Con argumentos y return
def return_args_greet(greet, name):
    return f"{greet}, {name}!"

print(return_args_greet("Hi", "Mario"))


# Con retorno de varios valores
def multiple_return_greet():
    return "Hola","Python"

greet, name = multiple_return_greet()
print(greet)
print(name)


# Con un número variable de argumentos
def variable_arg_greet(*names):
    for name in names:
        print(f"Hola, {name}!")

variable_arg_greet("Python", "Mario", "Pedro", "Comunidad")


# Con un número variable de argumentos con palabra clave
def variable_key_arg_greet(**names):
    for param, name in names.items():
        print(f"{name} ({param})!")

variable_key_arg_greet(language="Python", name="Mario", alias="Pedro", group="Comunidad")


"""
Funciones dentro de funciones
"""

def outer_function():
    def inner_function():
        print("Hola, Python!")
    inner_function()

outer_function()


"""
Funciones de lenguaje (built-in)
"""

print(len("Eyyyy"))
print(type("Mario"))
print("Mouredev".upper())

"""
Variables locales y globales
"""

global_variable = "Python"
local_variable = "Hola"

print(global_variable)

def hello_python():
    print(f"Hello, {global_variable}")

hello_python()


"""
Ejercicio extra
"""
def ejerc_extra(string1, string2):
    print("Comienza el ejercicio extra:")
    cont_num = 0
    for num in range(1,101):
        if num%3 == 0 and num%5 == 0:
            print(string1+string2)
        elif num%5 == 0:
            print(string2)
        elif num %3 == 0:
            print(string1)
        else:
            print(num)
            cont_num += 1
    
    print(f"Números printeados: {cont_num}")

ejerc_extra("Hola", "Adiós")
    



