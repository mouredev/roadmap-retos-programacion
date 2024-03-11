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
    message = "Esta es mi excepción personalizada"

def exception_function(item_1,item_2,item_3):
    try:
        #result = item_1+item_2
        #result = (int(item_1) + int(item_2))/item_3
        result = (item_1 + item_2)/item_3
    except TypeError as error :
        print(f"La función ha dado un \"{error}\"")
    except ValueError as error:
        print(f"La función ha dado un \"{error}\"")
    except:
        try:
            raise MyException()
        except MyException as error:
            print(error.message)
    else:
        print(f"el resultado es: {result}")

exception_function(1,"alex",9)
exception_function(6,3,0)
