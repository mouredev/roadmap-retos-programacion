"""
 * EJERCICIO:
 * Explora el concepto de "decorador" y muestra cómo crearlo
 * con un ejemplo genérico.
"""

# Los decoradores en Python son una forma de modificar el comportamiento de una función o método. 
# Son muy útiles para añadir funcionalidades adicionales de manera concisa y reutilizable.

# Definimos el decorador
def mi_decorador(func):
    def envoltura(*args, **kwargs):
        print("Algo se está haciendo antes de llamar a la función")
        resultado = func(*args, **kwargs)
        print("Algo se está haciendo después de llamar a la función")
        return resultado
    return envoltura

# Usamos el decorador en una función
@mi_decorador
def saludar(nombre):
    print(f"Hola, {nombre}!")

# Llamamos a la función decorada
saludar("Mundo")



"""
 * DIFICULTAD EXTRA (opcional):
 * Crea un decorador que sea capaz de contabilizar cuántas veces
 * se ha llamado a una función y aplícalo a una función de tu elección.
"""

# Definimos el decorador
def contador_llamadas(func):
    def envoltura(*args, **kwargs):
        envoltura.contador += 1
        print(f"La función {func.__name__} ha sido llamada {envoltura.contador} veces")
        return func(*args, **kwargs)
    envoltura.contador = 0
    return envoltura

# Usamos el decorador en una función
@contador_llamadas
def saludar(nombre):
    print(f"Hola, {nombre}!")

# Llamamos a la función decorada varias veces
saludar("Mundo")
saludar("Python")
saludar("Decoradores")
