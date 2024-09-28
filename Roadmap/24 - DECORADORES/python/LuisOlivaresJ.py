"""
* Explora el concepto de "decorador" y muestra cómo crearlo
* con un ejemplo genérico.
""" 

#Decorator wraps a function, modifying its behavior.

#Example
import functools


def do_twice(func):
    @functools.wraps(func)  # Used to preserve information about the original function.
    def wraper(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs)
        
    return wraper

@do_twice
def say_something(name):
    print(f"Hello, {name}!")
    return f"Goodbye {name}!"


msg = say_something("Luis")  # Hello!\nHello!
print(msg)


"""
 * Crea un decorador que sea capaz de contabilizar cuántas veces
 * se ha llamado a una función y aplícalo a una función de tu elección.
"""

calls_to_my_function = 0

def decorator(func):
    def wraper():
        global calls_to_my_function

        func()
        calls_to_my_function += 1
        print(f"Number of calls to my_function: {calls_to_my_function}")
    return wraper
    #return func
    
@decorator
def my_function():
    print("Inside my function!")

my_function()
my_function()
my_function()