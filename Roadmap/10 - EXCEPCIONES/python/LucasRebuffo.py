""" /*
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
 */ """

# try:
#     print([1].pop())
#     print([].pop())
# except Exception as e:
#     print(e)
# finally:
#     print("Finaliza la ejecucion ...")

class MyException(Exception):
    pass

def parametros(parametros: list):

    try:
        if len(parametros) < 3:
            raise IndexError
        elif parametros[1] == 0:
            raise ZeroDivisionError
        print(parametros[2])
        print(parametros[0]/parametros[1])

    except Exception as e:
        print(f"Se ha producido un error: {e} ({type(e).__name__})")


parametros([1, 0, 3])

