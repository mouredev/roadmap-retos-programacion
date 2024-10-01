#EXCEPCIONES


try:      
    print(nico)
except Exception as e:
    print(f"SE A PRODUCIDO UN ERROR {e}")



#Ejercicio Extra

class StrTypeError(Exception):
    pass

def procesar_parametros(parametros: list):

    if len(parametros) < 4:
        raise IndexError()
    elif parametros[1] == 0:
        raise ZeroDivisionError()
    elif type(parametros[2]) == str:
        raise StrTypeError("El segundo elemento no puede ser una cadena de texto")
    

    print(parametros[4])
    print(parametros[0]/parametros[1])
    print(parametros[2] * 10)





try: 
    procesar_parametros([1,0,"nico"])
except IndexError as e:
    print("El numero de elementos de la lista tiene que ser mayor a tres.")
except ZeroDivisionError as e:
    print("El segundo elemento de la lista no puede ser cero.")
except StrTypeError as e:
    print(f"{e}")
except Exception as e:
    print(f"Se a producido un error inesperado: {e}")
else:
    print("No se han producido errores.")
finally:
    print("Se termino el programa")

