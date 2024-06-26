"""
funcion es un bloque de codigo que sirve para reutilizar el codigo
"""

# Simple
def greeting():
    print("Hola, Python!")

greeting()

# Simple con parametro
def greeting(name):
    print(f"Hola, {name}!")

greeting("Marcos")


# Con retorno sin parametro
def greeting():
    return "Hello, World" 

greet = greeting()
print(greet)

# Con parametro, valor por defecto
def default_arg_greet(name = "Python"):
    print(f"Hola, {name}!")

default_arg_greet("Marcos")
default_arg_greet()

# Con parametros y return
def arg_suma(a, b):
    return a + b 

result = arg_suma(5, 5)
print(result)

# Con retorno de varios valores
def multiple_return():
    return "Hola", "Marcos"

greet, name = multiple_return()
print(greet)
print(name)

# Con un numero variables de argumentos
def variable_arg_greet(*name):
    for name in name:
        print(f"Hello, {name}")

variable_arg_greet("Python", "Marcos", "Andres")

# Con un número variable de argumentos con palabra clave
def variable_key_arg_greet(**names):
    for key, value in names.items():
        print(f"{key}: {value}")

variable_key_arg_greet(
    lenguage="Python", 
    name="Marcos", 
    last_name="Andres",
    age=25
)

"""
Funciones dentro de otras funciones
"""

def outer_function():
    def inner_function():
        print("Funcion interna: Hola python")
    inner_function()

outer_function()

"""
Funciones del lenguaje
"""

print(len("Marcos"))
print(type("Hello Python"))
print("Marcos".upper())
print("Python".lower())


"""
Variables locales y globales
"""

global_var = "Marcos"
print(global_var)

def hello_python():
    local_var = "Hello" 
    print(f"{local_var}, {global_var}")

hello_python()

# print(local_var) no se puede acceder desde fuera de la función

"""
DIFICULTAD EXTRA (opcional):
"""
def print_numbers(text_1, text_2):
    count = 0
    for number in range(1, 101):
        if(number % 3 == 0 and number % 5 == 0):
            print(f"{text_1}{text_2}")
        elif(number % 3 == 0):
            print(text_1)
        elif(number % 5 == 0):
            print(text_2)
        else:
            print(number)
            count += 1
    return f"Veces que se imprimio un número: {count}"

print(print_numbers('Fizz', 'Buzz'))
