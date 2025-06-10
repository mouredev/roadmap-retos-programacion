try:
  print(10/0)
except Exception:
  print("No se puede dividir por cero.")

try:
  print([1, 2, 3, 4][4])
except Exception as e:
  print(f"Se ha producido un error: {e} ({type(e).__name__})")
  
print("Fin del programa.")

"""
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

class StrTypeError(Exception): # Creamos una excepción personalizada.
    pass


def process_params(parameters):

    if len(parameters) < 3: # Si la lista tiene menos de 3 elementos, lanzamos una excepción IndexError.
        raise IndexError()
    elif parameters[1] == 0: # Si el segundo elemento de la lista es un cero, lanzamos una excepción ZeroDivisionError.
        raise ZeroDivisionError()
    elif type(parameters[2]) == str: # Si el tercer elemento de la lista es una cadena de texto, lanzamos una excepción StrTypeError.
        raise StrTypeError(
            "El tercer elemento no puede ser una cadena de texto.")

    print(parameters[2])
    print(parameters[1]/parameters[0])
    print(parameters[2] * 7)


try:
    process_params([1, 3, 5, 7])
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
    print("La ejecución ha finalizado.")