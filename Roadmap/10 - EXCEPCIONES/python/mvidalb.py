'''
Ejercicio
'''

try:
    print(10/1)
    print([1, 2, 3, 4][4])

except Exception as e:
    print(f"Error: {e}")    #type(e).__name__ para conocer el tipo de error

finally:
    print("Esto siempre se ejecuta")


'''
Ejercicio extra
'''
class StrTypeError(Exception):
    pass



def process_params(parameters: list):

    if len(parameters) < 3:
        raise IndexError()
    elif parameters[1] == 0:
        raise ZeroDivisionError()
    elif type(parameters[2])== str:
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
    print(f"Error: {e}")
except Exception as e:
    print(f"Se ha producido un error inesperado: {e}")
else:       # Se ejecuta cuando no se produce ningún error
    print("No se ha producido ningún error")
finally:    # Se ejecuta siempre
    print("La ejecución ha finalizado.")

