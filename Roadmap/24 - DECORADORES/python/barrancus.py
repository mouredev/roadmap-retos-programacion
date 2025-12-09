#24 - Python - Patrones de Diseño - Decoradores
# EJERCICIO:
# Explora el concepto de "decorador" y muestra cómo crearlo
# con un ejemplo genérico.
# 
# DIFICULTAD EXTRA (opcional):
# Crea un decorador que sea capaz de contabilizar cuántas veces
# se ha llamado a una función y aplícalo a una función de tu elección.
# 
class Counter:
    def __iter__(self):
        self.a = 1
        return self
    
    def __next__(self):
        x = self.a
        self.a += 1
        return x

def serparacion(cadena) -> str:
    global contador
    print(f'\nEjercicio {next(contador)}. {cadena * 20}')

contador = iter(Counter())

def my_decorator(func):
    """Decorador propio"""
    def print_pre_post(*args, **kwargs):
        print('Comenzamos la ejecución.\n')
        func(*args, **kwargs)
        print('\nFinalizamos la ejecución.')
    return print_pre_post

def call_counter(func):
    """Decorador que cuenta las llamadas a una función."""
    def wrapper(*args, **kwargs):
        wrapper.calls += 1
        print(f'La función "{func.__name__}" ha sido llamada {wrapper.calls} veces.')
        return func(*args, **kwargs)
    wrapper.calls = 0
    return wrapper

@call_counter
def greet(name):
    """Función que saluda a una persona."""
    print(f'Hola, {name}!')

@my_decorator
def calculator(x: int, y: int) -> None:
    """Función que ejecuta varias operaciones aritméticas."""
    print(f'Núm1  | OP | Núm2 |   | Result')
    print(f'{"-"*35}')
    print(f'{x:<5} | +  | {y:<5}  =   {x+y:6<.2f}')
    print(f'{"-"*35}')
    print(f'{x:<5} | -  | {y:<5}  =   {x-y:6<.2f}')
    print(f'{"-"*35}')
    print(f'{x:<5} | *  | {y:<5}  =   {x*y:6<.2f}')
    print(f'{"-"*35}')
    print(f'{x:<5} | /  | {y:<5}  =   {x/y:6<.2f}')
    print(f'{"-"*35}')
    print(f'{x:<5} | // | {y:<5}  =   {x//y:6<.2f}')
    print(f'{"-"*35}')
    print(f'{x:<5} | %  | {y:<5}  =   {x%y:6<.2f}')
    print(f'{"-"*35}')

def main():
    serparacion('-:-')
    calculator(20, 7)
    serparacion('-:-')
    greet('Alice')
    greet('Bob')
    greet('Charlie')
    greet('Diana')
    greet('Eve')
    
if __name__ == "__main__":
    main()
