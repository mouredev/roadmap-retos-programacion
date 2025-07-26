# EJERCICIO:
# Explora el concepto de manejo de excepciones según tu lenguaje.
# Fuerza un error en tu código, captura el error, imprime dicho error
# y evita que el programa se detenga de manera inesperada.
# Prueba a dividir "10/0" o acceder a un índice no existente
# de un listado para intentar provocar un error.

def sum(n1: int, n2: int):
    try:
        return n1 + n2
    except TypeError:
        return "TypeError: no se puede operar con strings"


# DIFICULTAD EXTRA (opcional):
# Crea una función que sea capaz de procesar parámetros, pero que también
# pueda lanzar 3 tipos diferentes de excepciones (una de ellas tiene que
# corresponderse con un tipo de excepción creada por nosotros de manera
# personalizada, y debe ser lanzada de manera manual) en caso de error.
# - Captura todas las excepciones desde el lugar donde llamas a la función.
# - Imprime el tipo de error.
# - Imprime si no se ha producido ningún error.
# - Imprime que la ejecución ha finalizado. 

class HigherDividendError(Exception):
    pass

def cath_errors(num1: int, num2: int):
    try:
        
        if num2 > num1:
            raise HigherDividendError("El Dividendo no puede ser mayor que el divisor")
        
        print(f"{num1 / num2}, No se ha producido ningún error")
    except TypeError:
        print("TypeError: Elemento ínválido, solo números")
    except ZeroDivisionError:
        print("ZeroDivisionError: No se puede dividir por cero")
    except  HigherDividendError as e:
        print(f"HigherDividendError: {e}")
    finally:
         print("Ejecución finalizada")