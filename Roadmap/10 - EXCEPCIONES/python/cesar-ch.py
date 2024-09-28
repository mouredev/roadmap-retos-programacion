"""
    #10 EXCEPCIONES
"""

try:
    resultado = 10 / 0
except Exception as e:
    print(f"Ocurrió un error: {e}")
else:
    print(f"El resultado es: {resultado}")
finally:
    print("La ejecución ha finalizado.")


lista = ["a", "b", "c"]

try:
    elemento = lista[4]
except Exception as e:
    print(f"Ocurrió un error: {e}")
else:
    print(f"El elemento en el índice 4 es: {elemento}")
finally:
    print("La ejecución ha finalizado.")


"""
    DIFICULTAD EXTRA (opcional):
"""


class MiError(Exception):
    pass


def procesar_parametros(a, b):
    if type(a) != int or type(b) != int:
        raise MiError("Los parámetros deben ser enteros.")
    return a / b


try:
    resultado = procesar_parametros(10, "a")
except ZeroDivisionError as e:
    print(f"Ocurrió un error: {e}")
    print(f"El tipo de error es: {type(e)}")
except MiError as e:
    print(f"Ocurrió un error: {e}")
    print(f"El tipo de error es: {type(e)}")
else:
    print(f"El resultado es: {resultado}")
finally:
    print("La ejecución ha finalizado.")
