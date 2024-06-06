'''
 * EJERCICIO:
 * Explora el concepto de manejo de excepciones según tu lenguaje.
 * Fuerza un error en tu código, captura el error, imprime dicho error
 * y evita que el programa se detenga de manera inesperada.
 * Prueba a dividir "10/0" o acceder a un índice no existente
 * de un listado para intentar provocar un error.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea una función que sea capaz de procesar parámetros, pero que también
 * pueda lanzar 3 tipos diferentes de excepciones (una de ellas tiene que
 * corresponderse con un tipo de excepción creada por nosotros de manera
 * personalizada, y debe ser lanzada de manera manual) en caso de error.
 * - Captura todas las excepciones desde el lugar donde llamas a la función.
 * - Imprime el tipo de error.
 * - Imprime si no se ha producido ningún error.
 * - Imprime que la ejecución ha finalizado. 
 */
'''

'''
Ejercicio
'''
try:
    print(10/1)
    print([1, 2, 3][4])
except Exception as e:  ## Error padre
    print(f"Error: {e} -- Tipo de Error: {type(e).__name__}")

print("Continuando con el programa...")

'''
Extra
'''
class StrTypeError(Exception):
    pass

def procesar_parametros(parametro: list):
    
    if len(parametro) < 3:
        raise IndexError()
    elif parametro[1] == 0:
        raise ZeroDivisionError()
    elif type(parametro[2]) == str:
        raise StrTypeError("El tercer parametro no puede ser un string.")

    print(parametro[2])
    print(parametro[0]/parametro[1])
    print(parametro[2]+ 5)
try:
    procesar_parametros([1, 2, 3, 4])
except IndexError as e:
    print("El parametro debe tener al menos 3 elementos.")
except ZeroDivisionError as e:
    print("No se puede dividir por 0.")
except StrTypeError as e:
    print(e)
except Exception as e:
    print(f"Error inesperado: {type(e).__name__} - {e}")
else: # Cuando no se cumple ninguna excepción
    print("No se ha producido ningún error.")
finally:  # Pase lo que pase se va a ejecutar
    print("La ejecución ha finalizado sin errores.")