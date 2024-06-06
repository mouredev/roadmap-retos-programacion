try:
    resultado = 10 / 0
except ZeroDivisionError as e:
    # Este bloque captura la excepción específica ZeroDivisionError
    print("Ha ocurrido un error: %s" % e)
except Exception as e:
    # Este bloque captura cualquier otra excepción
    print("Ha ocurrido un error inesperado: %s" % e)
else:
    # Este bloque se ejecuta si no hay errores
    print("El resultado es %s" % resultado)
finally:
    # Este bloque se ejecuta siempre
    print("Este bloque se ejecuta siempre")

lista = [1, 2, 3]

try:
    # Intentamos acceder a un índice fuera de rango
    elemento = lista[5]
except IndexError as e:
    print("Error de índice: %s" % e)
else:
    print("El elemento es %s" % elemento)
finally:
    print("Este bloque se ejecuta siempre 2")

#EJERCICIO OPCIONAL
class ErrorPersonalizado(Exception):
    """Excepción lanzada cuando ocurre un error específico definido por el usuario."""
    pass

def procesar_parametros(param):
    if not param:
        raise ValueError("El parámetro no puede estar vacío")
    elif not isinstance(param, int):
        raise TypeError("El parámetro debe ser un número entero")
    elif param < 0:
        raise ErrorPersonalizado("El parámetro no puede ser negativo")

    print("Procesando el parámetro %s" % param)
    return param * 2

# Intentamos llamar a la función y capturamos las excepciones
try:
    #resultado = procesar_parametros(1)
    #resultado = procesar_parametros(-1)
    resultado = procesar_parametros("hola")
    print("Resultado: %s" % resultado)
except ValueError as ve:
    print("Error de valor: %s" % ve)
except TypeError as te:
    print("Error de tipo: %s" % te)
except ErrorPersonalizado as ep:
    print("Error personalizado: %s" % ep)
except Exception as e:
    print("Error inesperado: %s" % e)
else:
    print("No se ha producido ningún error.")
finally:
    print("La ejecución de la función ha finalizado.")



# El programa sigue ejecutándose hasta aqui
print("El programa ha finalizado correctamente.")