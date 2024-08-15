# #24 PATRONES DE DISEÑO: DECORADORES

"""
 * EJERCICIO:
 * Explora el concepto de "decorador" y muestra cómo crearlo
 * con un ejemplo genérico.
"""

def decorador(funcion):
    def saludar():
        print ("-"*60)
        print (f"{funcion.__name__}")
        return funcion()
    return saludar

@decorador
def hola_mundo():
    print ("Saludo en Español")

@decorador
def hello_world():
    print ("Saludo en Inglés")

@decorador
def hasta_luego():
    print ("Despedida en Español")

@decorador
def goodbye():
    print ("Despedida en Inglés")
    
hola_mundo()
goodbye()
hasta_luego()
hasta_luego()

"""
 * DIFICULTAD EXTRA (opcional):
 * Crea un decorador que sea capaz de contabilizar cuántas veces
 * se ha llamado a una función y aplícalo a una función de tu elección.
"""
# Esta parte la copié de Moure porque no entendí muy bien la manera de contar las llamadas

def call_counter(function):
    def counter_function():
        counter_function.call_count += 1
        print(
            f"La función '{function.__name__} se ha llamado {counter_function.call_count}' veces.")
        return function

    counter_function.call_count = 0
    return counter_function

@call_counter
def hola_mundo():
    print ("Saludo en Español")

@call_counter
def hello_world():
    print ("Saludo en Inglés")

@call_counter
def hasta_luego():
    print ("Despedida en Español")

@call_counter
def goodbye():
    print ("Despedida en Inglés")
    
hola_mundo()
goodbye()
hasta_luego()
hasta_luego()
goodbye()
goodbye()
hola_mundo()