"""
 * EJERCICIO:
 * Explora el concepto de manejo de excepciones según tu lenguaje.
 * Fuerza un error en tu código, captura el error, imprime dicho error
 * y evita que el programa se detenga de manera inesperada.
 * Prueba a dividir "10/0" o acceder a un índice no existente
 * de un listado para intentar provocar un error.
"""

try:
    my_var = 10 / 0
except ZeroDivisionError as e:
    print(e)

try:
    my_var = [1, 2, 3]
    print(my_var[10])
except Exception as e:
    print(e)
    print(f"Tipo de excepción: {e.__class__.__name__}")

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

print('-' * 35)


class MyException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(message)


def my_function(param_1: int, param_2: float, param_3: str):
    if (
        not isinstance(param_1, int)
        or not isinstance(param_2, float)
        or not isinstance(param_3, str)
    ):
        raise ValueError(
            'Los valores de cada parámetro deben ser del tipo específicado para cada uno en la documentación'
        )
    if param_1 > 1000:
        raise MyException('El valor de "param_1" no puede ser mayor a 1000')
    if param_3.count(' ') > 1:
        raise SyntaxError('El valor del "param_3" no puede tener más de un espacio en blanco')
    print(param_3.count(' '))
    return [param_1, param_2, param_3]


try:
    test_var = my_function(2500, 10.5, 'avg')
    test_var = my_function(1, 'hola', 'avg')
    test_var = my_function(1, 10.5, 'avg   ')
    test_var = my_function(1, 10.5, 'avg')
except Exception as e:
    print(f'{e.__class__.__name__}: {e}')
else:
    print("No se ha producido ningún error al correr el código")
    print(test_var)
finally:
    print('Ejecución finalizada')
