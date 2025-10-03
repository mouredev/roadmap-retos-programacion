# @Author Daniel Grande (Mhayhem)

from functools import wraps

# EJERCICIO:
# Explora el concepto de "decorador" y muestra cómo crearlo
# con un ejemplo genérico.

def decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("This is a rwapper.")
        return func(*args, **kwargs)
    return wrapper

@decorator
def simple_function():
    return "Tihs is a simple function"

print(simple_function())

# DIFICULTAD EXTRA (opcional):
# Crea un decorador que sea capaz de contabilizar cuántas veces"
# se ha llamado a una función y aplícalo a una función de tu elección.

def calls_counter(func):
    @wraps(func) 
    def wrapper(*args, **kwargs):
        wrapper.calls += 1 # añadimos una nueva llamada
        print(f"La {func.__name__} ha sido llamada {wrapper.calls}") # mostramos nombre de función y veces que la llamamos
        return func(*args, **kwargs) # retornamos la función
    wrapper.calls = 0 # inicializamos la variable de veces llamada
    return wrapper 

@calls_counter
def greet():
    pass # evitamos demasiadas líneas en terminal ya que no necesitamos ningún retorno en este ejemplo.