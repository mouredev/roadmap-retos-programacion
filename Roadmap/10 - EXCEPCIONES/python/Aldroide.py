""" Excepciones
    Prueba a dividir "10/0" o acceder a un índice no existente
    de un listado para intentar provocar un error.
"""

# Capturar excepciones
a = 7
b = 0

try:
    100/0
except:
    print("Se produjo un error")


try:
    r = a/b
except ZeroDivisionError:
    print("Error no pudes divir entre cero.")
finally:
    print("Trata de nuevo")


"""
Ejercicio Extra
"""


def procesar_errores(parametro):
    try:
        if parametro == 1:
            raise ValueError("¡Este es un valor incorrecto!")
        elif parametro == 2:
            raise IndexError("¡Índice fuera de rango!")
        else:
            print("Parámetro válido:", parametro)
    except ValueError as error:
        print(f"Error: {error}")
    except IndexError as error:
        print(f"Error: {error}")
    else:
        print("No se ha producido ningún error.")
    finally:
        print("La ejecución ha finalizado.")


# Funcion
try:
    procesar_errores(0)
    procesar_errores(1)
    procesar_errores(2)
except Exception as e:
    print("Tipo de error:", type(e).__name__)
