# #10 EXCEPCIONES
#### Dificultad: Media | Publicación: 04/03/24 | Corrección: 11/03/24

## Ejercicio


''' * EJERCICIO:
 * Explora el concepto de manejo de excepciones según tu lenguaje.
 * Fuerza un error en tu código, captura el error, imprime dicho error
 * y evita que el programa se detenga de manera inesperada.
 * Prueba a dividir "10/0" o acceder a un índice no existente
 * de un listado para intentar provocar un error.
'''

# Fuerzo error de división por cero
def division(num1, num2):
    try:
        division = num1/num2
        print(f'Resultado: {division}')

    except ZeroDivisionError as e:
        print("Error: ", e)

    finally:
        print("Ejecución finalizada")

def no_index(posicion):
    try:
        lista = [1,2,3]
        print(lista[posicion])

    except IndexError as e:
        print(f"Error: {e}. No existe el índice en la posicion {posicion}")

    finally:
        print("Ejecución finalizada")

division(10,4)
no_index(5)

''' DIFICULTAD EXTRA (opcional):
 * Crea una función que sea capaz de procesar parámetros, pero que también
 * pueda lanzar 3 tipos diferentes de excepciones (una de ellas tiene que
 * corresponderse con un tipo de excepción creada por nosotros de manera
 * personalizada, y debe ser lanzada de manera manual) en caso de error.
 * - Captura todas las excepciones desde el lugar donde llamas a la función.
 * - Imprime el tipo de error.
 * - Imprime si no se ha producido ningún error.
 * - Imprime que la ejecución ha finalizado.''' 

 def test_excepciones(param):
    try:
        if param == 1:
            raise ValueError("Error 1")
        elif param == 2:
            raise TypeError("Error 2")
        else:
            print("Todo bien!")

    except ValueError as e:
        print(f"Error: {e}")

    except TypeError as e:
        print(f"Error: {e}")

    finally:
        print("Ejecución finalizada")