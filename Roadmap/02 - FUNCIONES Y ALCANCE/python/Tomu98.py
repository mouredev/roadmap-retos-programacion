""" Reto 02: Funciones y Alcance"""

""" Funciones definidas por el usuario """

# Simple
def greet():
    print("Hola, Python!")

greet()

# Con retorno
def return_greet():
    return "Hola, Python!"

print(return_greet())

# Con un argumento
def arg_greet(name: str):
    print(f"Hola, {name}!")

arg_greet("Tomu")

# Con más argumentos
def args_greet(greet: str, name: str):
    print(f"{greet}, {name}!")

args_greet("Hi", "Tomu")
args_greet(name="Tomu", greet="Hi")

# Con un argumento predeterminado
def default_arg_greet(name: str="Python"):
    print(f"Hola, {name}!")

default_arg_greet("Tomu")
default_arg_greet()

# Con argumentos y retorno
def return_args_greet(greet: str, name: str):
    return f"{greet}, {name}!"

print(return_args_greet("Hi", "Tomu"))

# Con retorno de varios valores
def multiple_return_greet():
    return "Hola", "Python"

greet, name = multiple_return_greet()
print(greet)
print(name)

# Con un número variable de argumentos
def variable_arg_greet(*names: str):
    for name in names:
        print(f"Hola, {name}!")

variable_arg_greet("Python", "Tomu", "Brais")

# Con un número variable de argumentos con palabra clave
def variable_key_arg_greet(**names: str):
    for key, value in names.items():
        print(f"{value} ({key})!")

variable_key_arg_greet(
    language="Python",
    name="Abel",
    alias="Tomu",
    age="25"
)



""" Funciones dentro de funciones """

def outer_function():
    def inner_function():
        print("Función interna: Hola, Python!")
    inner_function()

outer_function()



""" Funciones del lenguaje (Built-in) """

print(len("Tomu"))
print(type("Tomu"))
print(sum([21, 12]))
print(min([21, 12]))
print(max([21, 12]))



""" Variables locales y globales """

global_var = "Python"

def hello_python():
    local_var = "Hola"
    print(f"{local_var}, {global_var}!")

print(global_var)
# print(local_var) No se puede acceder desde fuera de la función

hello_python()



""" Reto extra """

def print_numbers(texto1: str, texto2: str) -> int:
    count = 0
    for number in range(1, 101):
        if number % 3 == 0 and number % 5 == 0:
            print(f"{texto1} + {texto2}")
        elif number % 3 == 0:
            print(texto1)
        elif number % 5 == 0:
            print(texto2)
        else:
            print(number)
            count += 1
    return count

print(print_numbers("Fizz", "Buzz"))
