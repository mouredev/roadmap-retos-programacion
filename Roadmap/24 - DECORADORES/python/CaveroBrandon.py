"""EJERCICIO:
Explora el concepto de "decorador" y muestra cómo crearlo
con un ejemplo genérico"""
from datetime import datetime


def do_not_disturb(func):
    def wrapper_do_not_disturb(*args):
        if 19 <= datetime.now().hour < 24:
            print(f'- The action "{func}" cannot be completed at this time -')
            print(f'Time when the action was attempted: {datetime.now().hour}:{datetime.now().minute}')
        else:
            func(*args)

    return wrapper_do_not_disturb


@do_not_disturb
def turn_lights_on(room='Hall'):
    print(f'The lights of "{room}" were turned on')


@do_not_disturb
def ring_the_bell(bell='Front door'):
    print(f'The bell from "{bell}" was ringed')


turn_lights_on('Bedroom')
ring_the_bell()

"""DIFICULTAD EXTRA (opcional):
 * Crea un decorador que sea capaz de contabilizar cuántas veces
 * se ha llamado a una función y aplícalo a una función de tu elección."""


def function_caller_counter(func):
    def wrapper_function_caller_counter():
        function_caller_counter.counter += 1
        func()
        print(f'This decorator was used {function_caller_counter.counter} times')
    function_caller_counter.counter = 0
    return wrapper_function_caller_counter


@function_caller_counter
def show_time():
    print(f'The current time is: {datetime.now().hour}:{datetime.now().minute}')


show_time()
show_time()
