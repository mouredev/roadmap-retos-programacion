"""
EJERCICIO:
Explora el concepto de manejo de excepciones según tu lenguaje.
Fuerza un error en tu código, captura el error, imprime dicho error
    y evita que el programa se detenga de manera inesperada.
Prueba a dividir "10/0" o acceder a un índice no existente
    de un listado para intentar provocar un error.

DIFICULTAD EXTRA (opcional):
Crea una función que sea capaz de procesar parámetros, pero que también
    pueda lanzar 3 tipos diferentes de excepciones (una de ellas tiene que
    corresponderse con un tipo de excepción creada por nosotros de manera
    personalizada, y debe ser lanzada de manera manual) en caso de error.
- Captura todas las excepciones desde el lugar donde llamas a la función.
- Imprime el tipo de error.
- Imprime si no se ha producido ningún error.
- Imprime que la ejecución ha finalizado.
"""

def area_rectangle(base: int, height: int) -> int|None:
    """
    Calculates the area of a rectangle.

    Parameters:
    - base (int): The base length of the rectangle.
    - height (int): The height of the rectangle.

    Returns:
    - int | None: The area of the rectangle, or None if an error occurs.
    """
    try:
        area = base * height
    except TypeError as e:
        print(f"Se ha producido un error. {e}")
        return None

    return area

def divide(dividend: int, divider: int) -> float|None:
    """
    Divides two numbers.

    Parameters:
    - dividend (int): The number to be divided.
    - divider (int): The number to divide by.

    Returns:
    - float | None: The result of the division, or None if an error occurs.
    """
    try:
        result = dividend / divider
    except ZeroDivisionError as e:
        print(f"Se ha producido un error. {e}")
        return None
    except TypeError as e:
        print(f"Se ha producido un error. {e}")
        return None

    return result

# print(area_rectangle(2, 3))
# print(area_rectangle("2", "3"))
# print(divide(4, 2))
# print(divide(4, 0))
# print(divide(4, "2"))

# EXTRA

class NotIntTypeError(Exception):
    """Custom exception to indicate that not all inputs are integers."""

def parameters_multiplication(args: list[int]):
    """
    Validates a list of parameters before performing a multiplication.

    Parameters:
    - args (list[int]): A list of integers to be validated.

    Raises:
    - IndexError: If the list contains fewer than 2 elements.
    - ValueError: If any element is zero.
    - NotIntTypeError: If any element is not an integer.
    """
    if len(args) < 2:
        raise IndexError("Debe haber al menos dos parametros.")
    if any(number == 0 for number in args):
        raise ValueError("No puede haber ceros.")
    if not all(isinstance(number, int) for number in args):
        raise NotIntTypeError("Todos los parámetros deben ser enteros.")


try:
    parameters_multiplication([1, 2, 3, 4])
    #parameters_multiplication([1])
    #parameters_multiplication([1, 0, 3])
    #parameters_multiplication(["s", 2.2, 3])
except IndexError as e:
    print(f"Ha ocurrido un error. {e}")
except ValueError as e:
    print(f"Ha ocurrido un error. {e}")
except NotIntTypeError as e:
    print(f"Ha ocurrido un error. {e}")
except Exception as e:
    print(f"Se ha producido un error inesperado. {e}")
else:
    print("No ha ocurrido ningun error.")
finally:
    print("El programa se ha ejecutado con exito.")
