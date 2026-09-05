"""Excepciones"""

try:
    print(10/1)

    my_list = [1,2,3,4]
    print(my_list[2])

except Exception as e:
    print(f"Error: {e}.")
   
"""Extra"""

class StrTypeError(Exception):
    pass

def process_params(parameters:list):

    if len(parameters) < 3:
        raise IndexError()
    elif parameters[1] == 0:
        raise ZeroDivisionError()
    elif type(parameters[2]) == str:
        raise StrTypeError("El segundo elemento no puede ser una cadena de texto")

    print(parameters[2])
    print(parameters[0]/parameters[1])
    print(parameters[2] + 5)
   
try:
    process_params([1,2,3,4])
except IndexError as e:
    print("El número de la lista debe ser mayor a 2.")
except ZeroDivisionError as e:
    print("No se puede dividir por cero.")
except StrTypeError as e:
    print(f"{e}")
except Exception as e:
    print(f"Se ha producido un error: {e}")
else:
    print("No hay errores.")
finally:
    print("El programa finaliza sin detenerse.")

print("El programa finaliza.")