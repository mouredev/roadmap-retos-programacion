"""
Funciones definidas por el usuario
"""

# Simple


def greet():
    print("Hello, World")


greet()

# Con retorno


def return_greet():
    return "Hello, Python!"


print(return_greet())

# Con un argumento


def arg_greet(name):
    print(f"Hello, {name}!")


arg_greet("Sandro")

# Con argumentos


def args_greet(greet, name):
    print(f"{greet}, {name}!")


args_greet("Hi", "Sandro")
args_greet(name="Sandro", greet="Hi")


# Con un argumento predeterminado


def default_arg_greet(name="Python"):
    print(f"Hola, {name}!")


default_arg_greet("Brais")
default_arg_greet()

# Con argumentos y return


def return_args_greet(greet, name):
    return f"{greet}, {name}!"


print(return_args_greet("Hi", "Brais"))

# Con retorno de varios valores


def multiple_return_greet():
    return "Hola", "Python"


greet, name = multiple_return_greet()
print(greet)
print(name)

# Con un número variable de argumentos


def variable_arg_greet(*names):
    for name in names:
        print(f"Hello, {name}!")


variable_arg_greet("Python", "Sandro", "Gomez", "Enjoy")

# Con un número variable de argumentos con palabra clave


def variable_key_arg_greet(**names):
    for key, value in names.items():
        print(f"{value} ({key})!")


variable_key_arg_greet(
    language="Python",
    name="Sandro",
    alias="Gomez",
    age=31
)

"""
Functions inside Functions
"""


def outer_function():
    def inner_function():
        print("Inner function Hello, Python !")
    inner_function()


outer_function()

"""
Language Functions (built-in)
"""

print(len("SandroGomez"))
print(type(31))
print("SandroGomez".upper())

"""
Variables locals and globals
"""

global_var = "Python"


def hello_python():
    local_var = "Hello"
    print(f"{local_var}, {global_var}!")


print(global_var)
# print(local_var) cannot acces, outside of function

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
    return count


print(print_numbers("Fizz", "Buzz"))
