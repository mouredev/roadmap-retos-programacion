"""
Ejercicio
"""
try:
    result = 10 / 1
    print(f"El resultado es: {result}")
    print([1, 2, 3, 4][4])

except Exception as e:
    print(f"Intentalo de nuevo: {e} ({type(e).__name__})")


"""
Extra
"""

class StrTypeError(Exception):
    ...

def process_params(parameter: list):
    try:
        if len(parameter) < 3:
            raise IndexError()
        elif parameter[1] == 0:
            raise ZeroDivisionError()
        elif type(parameter[2]) == str:
            raise StrTypeError("El tercer elemento no puede ser una cadena de texto.")

        print(parameter[2])
        print(parameter[0]/parameter[1])
        print(parameter[2] + 5)
    except IndexError as e:
        print(f"El número de elementos de la lista debe ser mayor que dos.")
    except ZeroDivisionError as e:
        print(f"El segundo elementos de la lista no puede ser un cero.")
    except StrTypeError as e:
        print(f"{e}")
    except Exception as e:
        print(f"Se ha producido un error inesperado: {e}")
    else: # Se ejecuta si no ocurre ningún error.
        print("No se ha producido ningún error")
    finally: # Se ejecuta siempre.
        print("El programa finaliza sin detenerse.")

process_params([1, 2, 3, 4])