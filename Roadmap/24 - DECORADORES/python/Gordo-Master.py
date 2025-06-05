"""
Decoradores
"""

# Sirven para agregar funcionalidades a una funcion o metodo, y ademas no se crea una nueva instancia.
# Tambien tiene la caracteristica que van responsabilizando la ejecución de las funciones a la envoltura.

def decorator(func):
    
    def wrapper():
        print("Comenzando el proceso...")
        func()
        print("Terminado el proceso...")
    
    return wrapper()

@decorator
def count_to_ten():
    for i in range(10):
        print(i+1)

count_to_ten

def print_call(func):
    def print_funtion():
        print(f"La función '{func.__name__}' ha sido llamada")
    return print_funtion

@print_call
def example_funtion1():
    pass

@print_call
def example_funtion2():
    pass

@print_call
def example_funtion3():
    pass


example_funtion1()
example_funtion2()
example_funtion3()

"""
Ejercicio extra
"""

def call_counter(func):
    def counter_func():
        func.call_count += 1
        print(f"La función '{func.__name__}'ha sido llamada {func.call_count} veces")
        return func

    func.call_count = 0
    return counter_func

@call_counter
def example_funtion4():
    pass

@call_counter
def example_funtion5():
    pass

example_funtion4()
example_funtion4()
example_funtion4()
example_funtion5()
example_funtion4()
example_funtion5()