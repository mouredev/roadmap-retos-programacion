"""
Ejercicio
"""

try:
    print(10/1)
    print([1,2,3,4][4])
except Exception as e:
    print(f"Se ha producido un error: {e} ({type(e).__name__})")

"""
Extra
"""

class StrTypeError(Exception):
    pass

def process_params(parametros: list):
    if len(parametros) < 3:
        raise IndexError()
    elif parametros[1] == 0:
        raise ZeroDivisionError()
    elif type(parametros[2]) == str:
        raise StrTypeError("El tercer elemento no puede ser una cadena de texto.")

    print(parametros[2])
    print(parametros[0]/parametros[1])
    print(parametros[2] + 5)

try:
    process_params([1,2,3,4])
except IndexError as e:
    print("El numero de elementos de la lista debe ser mayor que dos.")
except ZeroDivisionError as e:
    print("El segundo elemento de la lista no puede ser cero.")
except StrTypeError as e:
    print(f"{e}")
except Exception as e:
    print(f"Se ha producido un error inesperado: {e}.")
else:
    print("No se ha producido ningun error.")
finally:
    print("El programa finaliza sin detenerse.")