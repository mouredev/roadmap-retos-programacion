"""
EJERCICIO
"""

try:
    print(10 / 0)
except Exception as e:
    print(f"se ha cometido un error: {e}, {type(e).__name__}")
try:
    print([1, 2, 3, 4][4])

except Exception as e:
    print(f"se ha cometido un error: {e}, {type(e).__name__}")


"""
EXTRA
"""
class StrTypeErrorPersonal(TypeError):
    pass

def process_params(parametros: list):

    if len(parametros) < 3:
        raise IndexError()
    elif parametros[1] == 0:
        raise ZeroDivisionError()
    elif type(parametros[2]) == str:
        raise StrTypeErrorPersonal("el tercer elemento no puede ser un string")

    print(parametros[2])
    print(parametros[0] / parametros[1])
    print(parametros[2] + 5)


try:
    process_params([1, 2, "rick", 4])  
except IndexError:
    print("el # de elementos de la lista debe ser mayor que dos")
except ZeroDivisionError:
    print("el segundo elemento de la lista no puede ser cero")
except StrTypeErrorPersonal as e:
    print(e)  
except Exception as e:
    print(f"se ha producido un error inesperado: {e}")
else:
    print("no se ha producido ningún error")
finally:
    print("el programa finaliza sin detenerse")

