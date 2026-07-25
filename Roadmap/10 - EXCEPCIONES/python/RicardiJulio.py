#  * EJERCICIO:
#  * Explora el concepto de manejo de excepciones según tu lenguaje.
#  * Fuerza un error en tu código, captura el error, imprime dicho error
#  * y evita que el programa se detenga de manera inesperada.
#  * Prueba a dividir "10/0" o acceder a un índice no existente
#  * de un listado para intentar provocar un error.
#  *
#  * DIFICULTAD EXTRA (opcional):
#  * Crea una función que sea capaz de procesar parámetros, pero que también
#  * pueda lanzar 3 tipos diferentes de excepciones (una de ellas tiene que
#  * corresponderse con un tipo de excepción creada por nosotros de manera
#  * personalizada, y debe ser lanzada de manera manual) en caso de error.
#  * - Captura todas las excepciones desde el lugar donde llamas a la función.
#  * - Imprime el tipo de error.
#  * - Imprime si no se ha producido ningún error.
#  * - Imprime que la ejecución ha finalizado.

a = 10
b = 2

try:
    c = a/b
except Exception as ex:
    print('Ha ocurrido un error del tipo', type(ex))
    
lista = [1,2,3]

try:
    print(f'{lista[2]}')
except Exception as ex:
    print('Ha ocurrido un error del tipo', type(ex))

# DIFICULTAD EXTRA:

class MiExcepion(Exception):
    """Mi excepcion se lanza si una operacion es mayor o igual a 1000"""
    def __init__(self,resultado):
        self.resultado = resultado
        self.mensaje = f'MiExcepcion {resultado}'
        super().__init__(self.mensaje)
        
def multiplicar(a,b):
    resultado = a*b
    if resultado >= 1000:
        raise MiExcepion(resultado)
    return resultado

def manejo_excepciones(a,b):
    try:
        resm = multiplicar(a,b)
        print(resm)
        resd = a/b
        print(resd)
    except MiExcepion as ex:
        print(f'Ha ocurrido {ex}')
    except ZeroDivisionError as ex:
        print(f'Ha ocurrido {ex}')
    except TypeError as ex:
        print(f'Ha ocurrido {ex}')
    else:
        print('No ha ocurrido ningun error.')
    finally:
        print('Ha terminado la ejecucion.')

manejo_excepciones(100,2)
manejo_excepciones(100,12)
manejo_excepciones(10,0)
manejo_excepciones(15,'20')
