"""
Funciones simples
"""

# Sin parametro ni retorno

def greet():
    print("Hola, Python!")


greet()

# Con un parametro sin retorno

def greet_arg(name):
    print(f"Hola, {name}!")


greet_arg("Mizadlo")

# Con multiple parametro sin retorno

def greet_multiple_args(greet, name):
    print(f"{greet}, {name}!")


greet_multiple_args("Hi", "Mizadlo")
greet_multiple_args(name = "Mizadlo", greet = "Hi") # Indicando parametros

# Sin parametro con retorno

def return_greet():
    return "Hola, Python!"


print(return_greet())

# Con un parametros con retorno

def return_greet_arg(name):
    return f"Hola, {name}!"


print(return_greet_arg("Mizadlo"))

# Con multiples parametros con retorno

def return_greet_multiple_args(greet, name):
    return f"{greet}, {name}!"


print(return_greet_multiple_args("Hi", "Mizadlo"))

# Con un argumento predeterminado

def default_greet_arg(name = "Python"):
    print(f"Hola, {name}!")


default_greet_arg("Mizadlo")
default_greet_arg()

# Con retorno de multiple valores

def multiple_return_greet():
    return "Hola", "Python"


greet, name = multiple_return_greet()
print(greet)
print(name)

# Con un numero variable de parametros

def variable_arg_greet(*names):
    for name in names:
        print(f"Hola, {name}!")


variable_arg_greet("Python", "Mizadlo", "Garcia", "Javascript")

# Con un numero variable de parametros con palabra clave

def variable_key_arg_greet(**names):
    for key, value in names.items():
        print(f"{value} ({key})!")


variable_key_arg_greet(
    language = "Python",
    name = "Mizadlo",
    last_name = "Garcia",
    age = 33
)

"""
Funciones anidadas
"""

def outer_function():
    def inner_function():
        print("Funcion interna: Hola, Python !")
    inner_function()


outer_function()

"""
Funciones del lenguaje (built-in)
"""

print(len("Mizadlo"))
print(type(33))
print("Mizadlo".upper())

"""
Variables locales y globales
"""

global_var = "Python"

def hello_phyton():
    local_var = "Hola"
    print(f"{local_var}, {global_var}!")

print(global_var)
# print(local_var) No se puede acceder desde fuera de la funcion hello_python()

hello_phyton()

"""
Extra
"""

def print_numbers(text_1, text_2) -> int:
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


print_numbers("Fizz", "Buzz")