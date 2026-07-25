"""
Excepciones
"""

def dividir():
    try:
        print(10/0)
        
        mi_lista = [1, 2, 3]
        print(mi_lista[3])
        
    except Exception as e:
        print(f"Error: {e}")

dividir()


"""
 * DIFICULTAD EXTRA (opcional):
 * Crea una función que sea capaz de procesar parámetros, pero que también
 * pueda lanzar 3 tipos diferentes de excepciones (una de ellas tiene que
 * corresponderse con un tipo de excepción creada por nosotros de manera
 * personalizada, y debe ser lanzada de manera manual) en caso de error.
 * - Captura todas las excepciones desde el lugar donde llamas a la función.
 * - Imprime el tipo de error.
 * - Imprime si no se ha producido ningún error.
 * - Imprime que la ejecución ha finalizado. 
"""

class StrTypeError(Exception):
    print("El segundo elemento no puede ser una cadena de texto")

def procesar_parametro(parametros : list):
    
    if len(parametros) < 3:
        raise IndexError()
    elif parametros[1] == 0:
        raise ZeroDivisionError()
    elif type(parametros[0]) == str:
        raise StrTypeError()
    
    print(parametros[2])
    print(parametros[0]/parametros[1])    
    print(parametros[0] + 5)
    
try:    
    procesar_parametro([1, 3, 2])
except IndexError as e:
    print(f"El numero de elementos de la lista debe ser mayor que dos")
except ZeroDivisionError as e:
    print(f"EL segundo elemento de la lista no puede ser un 0")
except StrTypeError as e:
    print(f"{e}")
except Exception as e:
    print(f"Se ha producido un error inesperado: {e}")
else:
    print("No se ha producido ningun erro")
finally:
    print("El programa finaliza")
    
    