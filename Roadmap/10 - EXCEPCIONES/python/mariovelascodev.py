#Ejercicio

mi_variable = 2

#Capturamos el tipo de error producido en el codigo
try:
    print(variable)
except Exception as e:
    print(f"Se ha producido un error: {e}")

#Capturamos un tipo de error especifico
try:
    print(10/0)
except ZeroDivisionError:
    print("No se puede dividir por cero")

mi_lista = [0, 1, 2]
try:
    print(mi_lista[4])
except IndexError:
    print("El indice al que intentas acceder no existe en la lista")

#Extra

# Creamos una excepción personalizada
class MiExcepcionPersonalizada(Exception):
    pass


def procesa_parametros(parametros: list):
    if parametros[2] == 0:
        raise ZeroDivisionError()
    elif type(parametros[0]) == str:
        raise MiExcepcionPersonalizada
    elif len(parametros) < 3:
        raise IndexError()
    
    print(parametros[2] / parametros[1])
    print(parametros[0])
    print(parametros[2])

try:
    procesa_parametros([1, 2, 3])
except ZeroDivisionError:
    print("El segundo parametro no puede ser 0")
except MiExcepcionPersonalizada:
    print("El primer elementos no puede ser una cadena")
except IndexError:
    print("El numero de elementos debe ser mayor que 2")
except Exception as e:
    print(f"Se ha producido un error del tipo: {e}")
else:
    print("No se han producido errores")
finally:
    print("El programa ha finalizado")
