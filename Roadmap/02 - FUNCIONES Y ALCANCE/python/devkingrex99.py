"""
funciones definidas por el usuario
"""

#simple

def saludar():
    print("hola python")



saludar()

#con retorno
def return_greet():
    return "hola python"




greet = return_greet()
print(greet)


#con argumentos

def arg_greet(name):
    print(f"hola, {name}!")


arg_greet("Alice")


#con un agumento predeterminado

def args_greet(name, greeting="Hola"):
    print(f"{greeting}, {name}!")

args_greet("Alice")
args_greet("Bob", "¡Hola!")


def default_args_greet(name, greeting="Hola"):
    print(f"{greeting}, {name}!")


default_args_greet("Alice")
default_args_greet("Bob", "¡Hola!")


default_args_greet("charlie", greeting="¡Hola!")
default_args_greet("david", greeting="buenos dias")


#argumentos y retorno


def return_args_greet(greeting, name):
    return f"{greeting}, {name}!"


greet = return_args_greet("Hola", "Alice")
print(greet)

#con retorno de varios valores

def multiple_returns():
    return"hola", "python"



greet1, greet2 = multiple_returns()
print(greet1)
print(greet2)


#con un numero variable de argumentos


def variable_args_greet(*names):
    for name in names:
        print(f"hola, {name}!")


variable_args_greet("Alice", "Bob", "Charlie")

#con un numero variable de argumentos con palabras clave

def variable_arg_greet(**names):
    for param in names:
        print(f"hola,{param}!")

"""
funciones dentro de funciones
"""


def outer_funstion():
    def inner_function():
        print("funcion interna: hola, python!")
        inner_function()

outer_funstion()
"""
funciones del lenguage(Built-in)
"""

print(len("mouredev"))
print(type("36"))
print("mouredev".upper())

"""
variable locales y globales
"""

global_var = " python"

print(global_var)

def hello_python():
    local_var ="hola"
    print(f"{local_var},{global_var}!")

global_var = "python"
hello_python()

print(global_var)
#print(local_var) no se puede acceder desde fuera de la funcion
"""
#extra
"""

def print_numbers(text_1, text_2) -> int :
    count = 0
    for number in range(1, 101):
        if number % 3 == 0 and number % 5 == 0:
            print(number)
        elif number %3 == 0:
            print(text_1)
        elif number %5 == 0:
            print(text_2)
        else: 
            print(number)
            count += 1
    return count


print(print_numbers("Fizz","Buzz"))