# ╔═════════════════════════════════════╗
# ║ Autor:  Kenys Alvarado              ║
# ║ GitHub: https://github.com/Kenysdev ║
# ║ 2024 -  Python                      ║
# ╚═════════════════════════════════════╝

# -----------------------------------
# * DECORADORES
# -----------------------------------
# Mas info: https://geekflare.com/es/python-decorators/

"""
* EJERCICIO #1:
* Explora el concepto de "decorador" y muestra cómo crearlo
* con un ejemplo genérico.
"""
print("EJERCICIO #1:")

# ______________________
# Decorando una funcion:

def my_decorator(func):
    # *args para manejar un número variable de argumentos posicionales.
    # **kwargs para argumentos de palabras clave.
    def wrapper(*args, **kwargs):
        print("\nAntes de que se llame a la función.")
        func(*args, **kwargs)
        print("Despues de llamarla")
    return wrapper

@my_decorator
def say_hello(first_name: str, last_name: str):
    print(f"Hola, {first_name} {last_name}!")

say_hello("Zoe", "Roy")

# NOTA: Sin el decorador, esto seria el equivalente:
my_decorator(say_hello("Ben", "Yun"))

# ______________________
# Decorando una clase:

def class_decorator(cls):
    class Wrapper(cls):
        def greet(self):
            print("\nAntes de llamar al método")
            super().greet()
            print("Después de llamar al método")
    return Wrapper

@class_decorator
class MyClass:
    def greet(self):
        print("Hola!")

obj = MyClass()
obj.greet()

""" 
* EJERCICIO #2:
* Crea un decorador que sea capaz de contabilizar cuántas veces
* se ha llamado a una función y aplícalo a una función de tu elección.
"""
print("\nEJERCICIO #2:")

def count_calls(func):
    def wrapper(*args):
        wrapper.calls += 1
        func(*args)
        print(f"Ha sido llamada {wrapper.calls} veces")
        
    wrapper.calls = 0
    return wrapper

@count_calls
def function_a(func_name: str):
    print(f"\nLa función '{func_name}':")

@count_calls
def function_b(func_name: str, example: str):
    print(f"\nLa función{func_name} - {example}:")

function_a("A")
function_a("A")
function_a("A")

function_b("B", "args_ejm")
function_b("B", "args_ejm")

