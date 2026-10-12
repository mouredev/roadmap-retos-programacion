"""
 * EJERCICIO:
 * Explora el concepto de "decorador" y muestra cómo crearlo
 * con un ejemplo genérico.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un decorador que sea capaz de contabilizar cuántas veces
 * se ha llamado a una función y aplícalo a una función de tu elección.
"""

def decorator(func):
    def wrapper():
        print("Before calling the function.")
        func()
        print("After calling the function.")
    return wrapper

@decorator
def greet():
    print("Hello, World!")

greet(); print()

def decorator_name(func):
    def wrapper(*args, **kwargs):
        print("Before execution")
        result = func(*args, **kwargs)
        print("After execution")
        return result
    return wrapper

@decorator_name
def add(a, b):
    return a + b

print(add(5, 3)); print()

def call_counter(func) -> None:
    calls: list = []

    def create_msg(func, times: int) -> str:
        msg = str()

        if times == 1:
            msg = f"La función «{func.__name__}» se ha llamado una vez."
        elif times > 1:
            msg = f"La función «{func.__name__}» se ha llamado {times} veces."
        else:
            msg = f"La función «{func.__name__}» no se ha llamado."

        return msg
    
    def wrapper(*args, **kwargs) -> None:
        calls.append(func)
        
        func(*args, **kwargs)

        call_times = calls.count(func)
        
        print(create_msg(func, call_times)); print()
    return wrapper 

@call_counter
def hello_world():
    print("Hello, World!")

hello_world()
hello_world()
hello_world()
hello_world()
hello_world()