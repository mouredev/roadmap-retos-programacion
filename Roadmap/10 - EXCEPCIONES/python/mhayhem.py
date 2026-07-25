# EJERCICIO:
# Explora el concepto de manejo de excepciones según tu lenguaje.
# Fuerza un error en tu código, captura el error, imprime dicho error
# y evita que el programa se detenga de manera inesperada.
# Prueba a dividir "10/0" o acceder a un índice no existente
# de un listado para intentar provocar un error.

def sum(n1: int, n2: int):
    try:
        return n1 + n2
    except Exception as e:
        return f"Ha habido un error {e}: ({type(e).__name__})"


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

def catch_errors(array: list):
    if len(array) < 2:
        raise IndexError()
    elif array[1] == 0:
        raise ZeroDivisionError()
    elif array[1] > array[0]:
        raise HigherDividendError("EL segundo elemento no puede ser mayor que el primer elemento")
    
    print(array[5])
    
    print(array[0] / array[1])
    
try:
    catch_errors([1])
except IndexError as e:
    print(f"El array debe de contener mínimo 2 elementos: {e}.")
except ZeroDivisionError as e:
    print(f"El segundo elemento del array no puede ser cero: {e}.")
except HigherDividendError as e:
    print(f"{e}")
except Exception as e:
    print(f"Se produjo un error inexperado: {e}")
else:
    print("Se ejecuto sin errores")
finally:
    print("Ejecución finalizada")