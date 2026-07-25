
lista = ["Sergio", 4, "Mica"]

try:
    print(lista[3])
except Exception as e:
    print(e)
    

try:
    print(10/0)
except Exception as e:
    print(e)


# DIFICULTAD EXTRA:

class IntTypeError(Exception):
    pass

def proceso(parametros):
    try:
        if len(parametros) < 3:
            raise IndexError("Se a producido un IndexError")
        elif type(parametros[1]) == int:
            raise IntTypeError("Error de integer en lista de cadena")
        print(parametros[1])
        print("parametros ingresados")
    except IndexError as e:
        print(e)
    except IntTypeError as e:
        print(e)
    except Exception as e:
        print(e)
    else:
        print("No se ha producido ningún error")
    finally:
        print("La ejecución ha finalizado")

proceso(lista)
