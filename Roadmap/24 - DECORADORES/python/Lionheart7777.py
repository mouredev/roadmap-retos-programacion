# EJERCICIO
def print_call(funct):
    def print_func(*args, **kwargs):
        print(f"La función '{funct.__name__}' ha sido llamada")
        return funct(*args, **kwargs)
    return print_func

@print_call
def example_function():
    pass

@print_call
def example_function_2():
    pass

@print_call
def example_function_3():
    pass

example_function()
example_function_2()
example_function_3()

#EXTRA

def call_counter(func):
    def wrapper(*args, **kwargs):
        wrapper.call_count += 1
        print(f"La función '{func.__name__}' ha sido llamada {wrapper.call_count} veces")
        return func(*args, **kwargs)
    
    wrapper.call_count = 0
    return wrapper
        

@call_counter
def example_function_4():
    pass

@call_counter
def example_function_5():
    pass

example_function_4() #ha sido llamada 1 veces
example_function_5()
example_function_4()
example_function_4() #ha sido llamada 3 veces
example_function_5() #ha sido llamada 2 veces

@call_counter
def sumar(a, b):
    return a + b

print(sumar(2, 3))  # TypeError: wrapper() takes 0 positional arguments


# EJEMPLO SIMPLE

"""
    
def decorator(func):
    def wrapper():
        print("Welcome")
        return func()
    return wrapper

@decorator
def hola():
    print("Hello Python")
hola()

@decorator
def adiós():
    print("Bye Python")
adiós()
"""


# DECORADOR INTERNAMENTE
"""
def print_call(funct):
    def print_function(*args, **kwargs):
        print(f"La función {funct.__name__} se ha llamado")
        return funct(*args, **kwargs)
    return print_function

#@print_call
def sumar(a, b):
    return a + b

sumar = print_call(sumar) # comprobando lo que internamente hace el decorador

print(sumar(2, 3))
print(sumar.__name__) # print_function
"""
