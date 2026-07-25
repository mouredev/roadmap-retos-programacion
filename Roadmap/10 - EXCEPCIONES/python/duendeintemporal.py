#10 { Retos para Programadores }  EXCEPCIONES

# Bibliography reference
#Python Notes for Professionals. 800+ pages of professional hints and tricks (GoalKicker.com) (Z-Library)
# GPT


""" 
 * EJERCICIO:
 * Explora el concepto de manejo de excepciones según tu lenguaje.
 * Fuerza un error en tu código, captura el error, imprime dicho error
 * y evita que el programa se detenga de manera inesperada.
 * Prueba a dividir "10/0" o acceder a un índice no existente
 * de un listado para intentar provocar un error.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea una función que sea capaz de procesar parámetros, pero que también
 * pueda lanzar 3 tipos diferentes de excepciones (una de ellas tiene que
 * corresponderse con un tipo de excepción creada por nosotros de manera
 * personalizada, y debe ser lanzada de manera manual) en caso de error.
 * - Captura todas las excepciones desde el lugar donde llamas a la función.
 * - Imprime el tipo de error.
 * - Imprime si no se ha producido ningún error.
 * - Imprime que la ejecución ha finalizado.

"""

log = print

import time

# Short for print()
log = print

# Simulating window load event
def on_load():
    body_style = {
        'background': '#000',
        'text-align': 'center'
    }
    
    title = 'Retosparaprogramadores #10.'
    title_style = {
        'font-size': '3.5vmax',
        'color': '#fff',
        'line-height': '100vh'
    }
    
    # Simulating setting styles and appending title to body
    log(f"Body style: {body_style}")
    log(f"Title: {title} with style: {title_style}")
    
    time.sleep(2)  # Simulating delay
    log('Retosparaprogramadores #10.')

on_load()

# Runtime errors in Python are instances of the Exception class. 
# The Exception class can also be used as-is, or as the base for user-defined exceptions. 
# It's possible to raise any type of value - for example, strings - but you're strongly encouraged to use Exception or one of its derivatives.

num = 0
result = None

try:
    if isinstance(num, (int, float)) and num != 0:
        result = 10 / num
    elif num == 0:
        raise ValueError("It seems you've tried to divide by zero, which is not permitted. Please enter a valid non-zero number.")
    else:
        raise TypeError("It seems you've tried to divide by a non-number value, which is not permitted. Please enter a valid number.")
except Exception as error:
    log('Something went wrong! ' + str(error))

log(result)  # Something went wrong! It seems you've tried to divide by zero, which is not permitted. Please enter a valid non-zero number. & None

# Note: Python raises ZeroDivisionError for division by zero, but we explicitly raise a ValueError to inform about it.

# Example of handling exceptions in a promise-like manner using a function
def promise_example():
    try:
        result = 102
        raise Exception("explicitly rejected promise")
    except Exception as error:
        log("Promise rejected: " + str(error))

promise_example() # Promise rejected: explicitly rejected promise

# There are several specific core error types in Python:
# ValueError - raised when a function receives an argument of the right type but inappropriate value.
# TypeError - raised when an operation or function is applied to an object of inappropriate type.
# KeyError - raised when a dictionary key is not found.
# IndexError - raised when a sequence subscript is out of range.
# SyntaxError - raised when the parser encounters a syntax error.
# AttributeError - raised when an invalid attribute reference is made.

def get_user_name(user):
    try:
        name = user['name'].upper()
        log(f"User name: {name}")
    except KeyError:
        log('KeyError: Cannot read property "name" of undefined or null')
    except Exception as e:
        log('Instance of general Exception: ' + str(e))

get_user_name({'name': 'Roxy'})  # User name: Roxy
get_user_name({})  # KeyError: Cannot read property "name" of undefined or null

# Extra exercises
def check_values(arr, index):
    try:
        if not isinstance(arr, list):
            raise TypeError('The first parameter must be of type list.')
        elif len(arr) == 0:
            raise ValueError('You provided an empty array as a parameter!')

        if index >= len(arr) or index < 0:
            raise IndexError(f"{index} is not a valid index for the array given.")

        log(f"The position given corresponds to this value: {arr[index]}")
        log("There's no errors when executing the function.")

    except Exception as e:
        log(f"{type(e).__name__}: Ooops! {e}")
    finally:
        log('The process is finished')

check_values([8, 5, 6, 4], 8)  # IndexError: Ooops! 8 is not a valid index for the array given & The process is finished
check_values([], 4)  # ValueError: Ooops! You provided an empty array as a parameter! & The process is finished
check_values([0, 76, 32, 1, 4, 2], 'Kia')  # TypeError: Ooops! The first parameter must be of type list. & The process is finished
check_values([4, 5, 3, 18, 22], 3)  # The position given corresponds to this value: 18
# There's no errors when executing the function.
# The process is finished                                                                                                                                                                                                                                                                                                                                                                                                                                       