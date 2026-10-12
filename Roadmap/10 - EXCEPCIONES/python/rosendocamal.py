"""
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
"""

try:
    user_name: str = input()
except (ValueError, KeyboardInterrupt) as e:
    print(e)
else:
    print("No hubo error...")
finally:
    print("Perfecto..."); print()

try:
    cociente: float = 10 / 0
except ZeroDivisionError:
    print("No se puede dividir entre cero.")
finally:
    print()

try:
    lista: list[any] = [None, None, 1, 2, "a", 5]
    print(lista[len(lista)])
except IndexError as e:
    print("Te pasaste de la raya: %s" % e)
finally:
    print()

# EXTRA

def capturar_tres_errores(array: list[int]) -> None:
    if not isinstance(array, list):
        raise TypeError("Error del tipo de dato: Solo se permite listas de enteros.")

    try:
        print("="*10)
        for i in range(0, len(array)):
            print(i / 2)
        else:
            print("="*10)
    except (ValueError, ZeroDivisionError) as e:
        print("Ha ocurrido un error: %s" % e)
    else:
        print("El proceso se ejecutó sin errores.")
    finally:
        print("El proceso ha finalizado.")

lista = [i**2 for i in range(5)]

capturar_tres_errores(lista)
capturar_tres_errores("hola")