


print("\n\n=======================================EJERCICIO=======================================\n\n")

"""
 * EJERCICIO:
 * Explora el concepto de "decorador" y muestra como crearlo
 * con un ejemplo generico.
"""

def func_decorator(func_parameter):
    def internal_function(*args, **kwargs):
        print("\nEste texto se imprime antes de realizar un calculo ")
        func_parameter(*args, **kwargs)
        print("Este texto se imprime despues de realizar el calculo\n")
        
    return internal_function


@func_decorator
def suma(num1, num2):
    print(f"El resultado de la suma es {num1 + num2}")
    
@func_decorator    
def resta(num1, num2):
    print(f"El resultado de la resta es {num1 - num2}")
    
@func_decorator    
def potencia(base, exponente):
    print(f"El resultado de elevar {base} a la potencia {exponente} es: {pow(base, exponente)}")

suma(10, 5)
resta(10, 5)
potencia(base=5, exponente=3)


print("\n\n=======================================DIFICULTAD EXTRA=======================================\n\n")


"""
 * DIFICULTAD EXTRA (opcional):
 * Crea un decorador que sea capaz de contabilizar cuantas veces
 * se ha llamado a una funcion y aplicalo a una funcion de tu eleccion.
"""

def decorator_counter(func_parameter):
    def func_counter(*args):
        func_counter.counter += 1
        if func_counter.counter == 1:
            print(f"La funcion ha sido llamada {func_counter.counter} vez")
        else:
            print(f"La funcion ha sido llamada {func_counter.counter} veces")
        return func_parameter(*args)
            
    func_counter.counter = 0    
    return func_counter

@decorator_counter
def multiply(a, b):
    print(a * b)
    
multiply(5, 3)
multiply(7, 2)
multiply(15, 17)
multiply(24, 31)

