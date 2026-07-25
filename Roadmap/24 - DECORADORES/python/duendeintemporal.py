#24 { Retos para Programadores } PATRONES DE DIESEÑO: DECORADORES 

# Bibliography reference
# I use GPT as a reference and sometimes to correct or generate proper comments.

"""  
* EJERCICIO:
 * Explora el concepto de "decorador" y muestra cómo crearlo
 * con un ejemplo genérico.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un decorador que sea capaz de contabilizar cuántas veces
 * se ha llamado a una función y aplícalo a una función de tu elección.

"""

log = print
log('Retos para Programadores #24')

# The decorator pattern is a structural design pattern that allows behavior to be added
# to individual objects, either statically or dynamically, without affecting the behavior
# of other objects from the same class. In Python, decorators are implemented using
# higher-order functions.

import time
import functools

# Generic decorator function
def decorator(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kwargs):
        print("Before calling the function")
        result = fn(*args, **kwargs)
        print("After calling the function")
        return result
    return wrapper

# Decorator to log execution time
def log_execution_time(fn):
    @functools.wraps(fn)
    async def wrapper(*args, **kwargs):
        start = time.time()  # Start time
        result = await fn(*args, **kwargs)
        end = time.time()  # End time
        print(f"Execution time for {fn.__name__}: {(end - start) * 1000:.2f} milliseconds")
        return result
    return wrapper

# Example function that simulates a time-consuming task
async def fetch_data():
    await asyncio.sleep(3)  # Simulate a delay of 3 seconds
    return "Data fetched!"

# Decorated function
logged_fetch_data = log_execution_time(fetch_data)

# Using the decorated function
import asyncio

async def main():
    result = await logged_fetch_data()
    print(result)  # Data fetched!
    

# Run the main function
asyncio.run(main()) # Data fetched!
    # Execution time for fetch_data: 3008.05 milliseconds

# EXTRA DIFFICULTY EXERCISE

# Decorator to count function calls
def count_calls(fn):
    call_count = 0  # Private variable to keep track of calls through closure

    @functools.wraps(fn)
    def wrapper(*args, **kwargs):
        nonlocal call_count
        call_count += 1
        print(f"Function has been called {call_count} times.")
        return fn(*args, **kwargs)
    return wrapper

# Original function
@count_calls
def hi_girl():
    print('Hi Girl! 🌹')
    return '🌼'

# Using the decorated function
print(hi_girl())  # Function has been called 1 times. Hi Girl! 🌹
print(hi_girl())  # Function has been called 2 times. Hi Girl! 🌹
print(hi_girl())  # Function has been called 3 times. Hi Girl! 🌹

# Trying to access hi_girl directly will not result in an error, but the call count will still be tracked.

