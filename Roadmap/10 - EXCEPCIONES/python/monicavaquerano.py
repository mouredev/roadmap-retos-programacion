# 10 EXCEPCIONES
# Monica Vaquerano
# https://monicavaquerano.dev

"""
EJERCICIO:
Explora el concepto de manejo de excepciones según tu lenguaje.
Fuerza un error en tu código, captura el error, imprime dicho error
y evita que el programa se detenga de manera inesperada.
Prueba a dividir "10/0" o acceder a un índice no existente
de un listado para intentar provocar un error.
"""

print("--- EXCEPCIONES ---")
# El manejo de excepciones en Python permite a los programas manejar situaciones inesperadas o errores de manera controlada.
# Manejo de excepciones
print("\n* Manejo de excepciones")
try:
    a = 10 / 0
    print(a)
except ZeroDivisionError as error:
    print(f"Ha ocurrido un error: {error}")

print("\n* Manejo de varias excepciones")
try:
    print(x)
except ZeroDivisionError as error:
    print(f"Ha ocurrido un error: {error}")
except Exception as error:
    print(f"Algo más salió mal: {error}")

print("\n* El uso del bloque 'else'")
try:
    print("Todo bien por acá")
except ZeroDivisionError as error:
    print(f"Ha ocurrido un error: {error}")
except Exception as error:
    print(f"Algo más salió mal: {error}")
else:
    print("Esta vez nada puede malir sal.")

print("\n* El uso del bloque 'finally'")
try:
    print(10 / 0)
except ZeroDivisionError as error:
    print(f"Ha ocurrido un error: {error}")
except Exception as error:
    print(f"Algo más salió mal: {error}")
finally:
    print("El bloque 'try except' se terminó.")


print("\n* Levantar o forzar una excepción (raise an exception)")
print("x =", x := -1)
try:
    if x < 0:
        raise Exception("Sorry, no numbers below zero")
except Exception as error:
    print(f"Se levantó la siguiente excepción: {error}")


print("\nDIFICULTAD EXTRA (opcional):")
"""
Crea una función que sea capaz de procesar parámetros, pero que también
pueda lanzar 3 tipos diferentes de excepciones (una de ellas tiene que
corresponderse con un tipo de excepción creada por nosotros de manera
personalizada, y debe ser lanzada de manera manual) en caso de error.
- Captura todas las excepciones desde el lugar donde llamas a la función.
- Imprime el tipo de error.
- Imprime si no se ha producido ningún error.
- Imprime que la ejecución ha finalizado. 
"""


def exceptionHandler(params):
    print("\nProcesando excepciones...")
    if len(params) < 3:
        raise IndexError
    elif params[0] == 0:
        raise ZeroDivisionError
    elif params[1] != "monica":
        raise NameError


list = [1, "bob", 3, 4]

try:
    exceptionHandler(list)
except ZeroDivisionError:
    print(f"No es posible dividir entre cero")
except IndexError:
    print(f"No es posible accesar a ese indice")
except NameError:
    print(f"Este no es el nombre correcto, variable no esta definida")
except Exception as e:
    print(f"Ha ocurrido el siguiente error: {e}")
else:
    print("Nada ha salido mal")
finally:
    print("La ejecución de la función ha finalizado")
