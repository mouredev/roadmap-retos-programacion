"""
/*
 * EJERCICIO:
 * Explora el concepto de manejo de excepciones según tu lenguaje.
 * Fuerza un error en tu código, captura el error, imprime dicho error
 * y evita que el programa se detenga de manera inesperada.
 * Prueba a dividir "10/0" o acceder a un índice no existente
 * de un listado para intentar provocar un error.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea una función que sea capaz de procesar parámetros, pero que también
 * pueda lanzar 3 tipos diferentes de excepciones (una de ellas tiene que
 * corresponderse con un tipo de excepción creada por nosotros de manera
 * personalizada, y debe ser lanzada de manera manual) en caso de error.
 * - Captura todas las excepciones desde el lugar donde llamas a la función.
 * - Imprime el tipo de error.
 * - Imprime si no se ha producido ningún error.
 * - Imprime que la ejecución ha finalizado. 
 */
"""

# EJERCICIO:

while True:
    try:
        num1 = int(input('Ingrese un numero: '))
        num2 = int(input('Ingrese otro numero: '))
        print(f'{num1} dividido entre {num2} es {num1 / num2}')
    except ZeroDivisionError as e:
        print(f'No se puede dividir por cero: {e}, intente de nuevo.')

# DIFICULTAD EXTRA:


class MiException(Exception):
    def __init__(self, msj):
        self.msj = msj


def procesar_parametros(param1):
    if param1 == 1:
        raise IndexError
    elif param1 == '':
        raise TypeError
    elif param1 < 0:
        raise ValueError
    elif param1 == 23:
        raise MiException('El parametro no puede ser "23"')


try:
    procesar_parametros(23)
except IndexError:
    print('El parametro debe ser diferente de 1')
except TypeError:
    print('El parametro no debe ser un string')
except ValueError:
    print('El parametro no debe ser negativo')
