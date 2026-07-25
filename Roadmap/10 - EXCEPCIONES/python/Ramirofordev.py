# Manejo de Excepciones
try:
    print("yo" / 2)
except Exception:
    print("No se puede dividir entre un string")

try:
    print(10/0)
except ZeroDivisionError:
    print("No se puede dividir entre 0.")


class StrTypeError(Exception):
    pass

def process_params(parameters: list):


    if len(parameters) < 3:
        raise IndexError()
    elif parameters[1] == 0:
        raise ZeroDivisionError()
    elif type(parameters[1]) == str:
        raise StrTypeError("El segundo elemento no puede ser una cadena de texto.")

    print(parameters[2])
    print(parameters[0/parameters[1]])

    
try:
    process_params([1, "nacho", 3])
except IndexError as e:
    print("EL numero de elementos de la lista debe ser mayor que dos.")
except ZeroDivisionError as e:
    print("No se puede dividir entre 0.")
except StrTypeError as e:
    print(f"{e}")
except Exception as e:
    print(f"Se ha producido un error inesperado: {e}")
finally:
    print("El programa finaliza")