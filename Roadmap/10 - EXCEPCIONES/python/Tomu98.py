""" Reto 10: Excepciones """

try:
    print(10/1)
    print([1, 2, 3, 4][4])
except Exception as e:
    print(f"Se ha producido un error: {e}")



""" Reto extra """

class StrTypeError(Exception):
    pass

def process_params(parameters: list):
    if len(parameters) < 3:
        raise IndexError()
    elif parameters[1] == 0:
        raise ZeroDivisionError()
    elif type(parameters[2]) == str:
        raise StrTypeError("El tercer elemento no puede ser una cadena de texto.")

    print(parameters[2])
    print(parameters[0]/parameters[1])
    print(parameters[2] + 5)

try:
    process_params([1, 2, 3, 4])
except IndexError as e:
    print("El número de elementos de la lista debe ser mayor que dos.")
except ZeroDivisionError as e:
    print("El segundo elemento de la lista no puede ser un cero.")
except StrTypeError as e:
    print(f"{e}")
except Exception as e:
    print(f"Se ha producido un error inesperado: {e}")
else:
    print("No se ha producido ningún error.")
finally:
    print("El programa finaliza")
