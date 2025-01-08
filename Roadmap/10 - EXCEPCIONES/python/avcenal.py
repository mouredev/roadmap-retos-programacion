"""
* EJERCICIO:
 * Explora el concepto de manejo de excepciones según tu lenguaje.
 * Fuerza un error en tu código, captura el error, imprime dicho error
 * y evita que el programa se detenga de manera inesperada.
 * Prueba a dividir "10/0" o acceder a un índice no existente
 * de un listado para intentar provocar un error.
"""
def index_exception():
    try:
        result = 10/0
    except ZeroDivisionError as error:
        print(f"Vaya parece que ha habido un error del tipo \"{error}\"")
    else:
        print(f"El resultado es {result}")

index_exception()

"""
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

class MyException(Exception):
    pass

def exception_function(item_1,item_2,item_3):
    if item_1 == 1:
        raise IndexError
    elif item_3> 5:
        raise TypeError
    elif type(item_2) == str:
        raise MyException("Esta es mi excepción personalizada")
    
try:
    exception_function(2,"alex",5)
except TypeError as error :
    print(f"La función ha dado un \"{error}\"")
except ValueError as error:
    print(f"La función ha dado un \"{error}\"")
except MyException as error:
    print(f"{error}")
except:
    print("La función ha dado un error genérico")
finally:
    print("el programa ha finalizado")
