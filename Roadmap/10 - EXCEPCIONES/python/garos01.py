a = 5
b = 0
try:
    # Intenta ejecutar el código que podría generar un error
    resultado = a / b  # Intentando dividir por cero
except ZeroDivisionError as error:
    # Captura la excepción específica y maneja el error
    print(f"Error: {error}")
else:
    # Este bloque se ejecuta si no hay excepciones
    print(f"La división fue exitosa: {resultado}")
finally:
    # Este bloque se ejecuta siempre, independientemente de si hubo una excepción o no
    print("Fin del manejo de excepciones")


lista = [1, 2, 3]
try:
    # Intenta acceder a un índice no existente de una lista
    elemento = lista[4]  # Intentando acceder a un índice no existente
except IndexError as error:
    # Captura la excepción específica y maneja el error
    print(f"Error: {error}")
else:
    # Este bloque se ejecuta si no hay excepciones
    print(f"Elemento obtenido: {elemento}")
finally:
    # Este bloque se ejecuta siempre, independientemente de si hubo una excepción o no
    print("Fin del manejo de excepciones")


# Ejercicio extra


class MiExcepcionPersonalizada(Exception):
    pass


def procesar_parametros(parametro):
    try:
        if parametro == 0:
            raise ValueError("El parámetro no puede ser cero.")
        elif parametro < 0:
            raise ValueError("El parámetro no puede ser negativo.")
        elif parametro > 100:
            raise MiExcepcionPersonalizada("El parámetro es demasiado grande.")
        else:
            print("El parámetro es válido.")
    except ValueError as error:
        print("Error:", error)
    except MiExcepcionPersonalizada as error_personalizado:
        print("Error personalizado:", error_personalizado)
    else:
        print("No se ha producido ningún error.")
    finally:
        print("La ejecución ha finalizado.")


try:
    procesar_parametros(50)
    print()
    procesar_parametros(0)
    print()
    procesar_parametros(-5)
    print()
    procesar_parametros(200)
except Exception as error:
    print(f"Error capturado desde el lugar donde se llama a la función: {error}")
finally:
    print("Fin del programa.")
