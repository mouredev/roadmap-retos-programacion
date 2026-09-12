"""
Ejercicio
"""
try:
    print(10/1)
    mi_lista = [1, 2, 3, 4]
    print(mi_lista[4])
    
    
except Exception as e:
    print(f"Se ha producido un error: {e}")
    
"""
Extra
"""
class StrTypeError(Exception):
    pass

def proceso_parametros(parametros: list):
    if len(parametros) < 3:
        raise IndexError("La lista de parámetros debe tener al menos 3 elementos.")
    elif parametros[1] == 0:
        raise ZeroDivisionError("El segundo parámetro no puede ser cero.")
    elif type(parametros[2]) == str:
        raise StrTypeError("El tercer elemento no puede ser una cadena de texto")
    
    print(parametros[2])
    print(parametros[0]/parametros[1])
    print(parametros[2] + 5)
        
    
try:
    proceso_parametros([1, 2, 3, 4])    
except IndexError as e:
    print(f"Error de índice: {e}")
except ZeroDivisionError as e:
    print(f"Error de división por cero: {e}")
except StrTypeError as e:
    print(f"{e}")
except Exception as e:
    print(f"Se ha producido un error inesperado: {e}")
else:
    print("No se ha producido un error.")
finally:
    print("Fin del programa.")

