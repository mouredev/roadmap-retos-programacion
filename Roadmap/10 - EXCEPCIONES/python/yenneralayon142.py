"""
Excepciones
"""
try:
    print(10/0)
    print([10,21,31][5])
except Exception as e:
    print(f"Se ha detectado un error: {e}")

"""
Extra
"""
class StrTypeError(Exception):
    pass

def errors(parameters:list):
    
    if len(parameters) < 3:
        raise IndexError
    elif parameters == 0:
        raise ZeroDivisionError
    elif type(parameters[2]) == str:
        raise StrTypeError("El tercer elemento no puede ser una cadena de texto")

    print(parameters[2])
    print(parameters[0] / parameters[1])
    print(parameters[2] + 5)
try:
    errors([1,2,3,4,5,6])
except IndexError as e:
    print("El número de elementos de la lista debe ser mayor a 1")
except ZeroDivisionError as e:
    print("El segundo elemento de la lista no puede ser un cero")
except StrTypeError as e:
    print(f"{e}")
except Exception as e:
    print(f"Se ha producido un error inesperado: {e}")
else:
    print("No se ha producido ningún error")
finally:
    print("El programa finaliza sin detenerse")