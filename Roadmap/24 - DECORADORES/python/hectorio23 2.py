#!/usr/bin/python3.11
# Autor: Héctor Adán
# GitHub: https://github.com/hectorio23 

'''
EJERCICIO:
Explora el concepto de "decorador" y muestra cómo crearlo
con un ejemplo genérico.

DIFICULTAD EXTRA 
Crea un decorador que sea capaz de contabilizar cuántas veces
se ha llamado a una función y aplícalo a una función de tu elección.
'''

def custom_decorator(func):
    def envoltura():
        print("Algo se está haciendo antes de llamar a la función")
        func()
        print("Algo se está haciendo después de llamar a la función")
    return envoltura

@custom_decorator
def do_something():
    print("Esta es mi función")

do_something()


def counter(func):
    def container(*args, **kwargs):
        container.llamadas += 1
        print(f"Se ha llamado a {func.__name__} {container.llamadas} veces")
        return func(*args, **kwargs)
    container.llamadas = 0
    return container

@counter
def saludar():
    print("¡Hola Mundo!")

saludar()
saludar()
saludar()
