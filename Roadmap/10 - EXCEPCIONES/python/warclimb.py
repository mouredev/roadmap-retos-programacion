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

# Fuerzo error de índice no existente
def no_index(posicion):
    try:
        lista = [1,2,3]
        print(lista[posicion])

    except IndexError as e:
        print(f"Error: {e}. No existe el índice en la posicion {posicion}")

    finally:
        print("Ejecución finalizada")

''' DIFICULTAD EXTRA (opcional):
 * Crea una función que sea capaz de procesar parámetros, pero que también
 * pueda lanzar 3 tipos diferentes de excepciones (una de ellas tiene que
 * corresponderse con un tipo de excepción creada por nosotros de manera
 * personalizada, y debe ser lanzada de manera manual) en caso de error.
 * - Captura todas las excepciones desde el lugar donde llamas a la función.
 * - Imprime el tipo de error.
 * - Imprime si no se ha producido ningún error.
 * - Imprime que la ejecución ha finalizado.''' 

# Función que lanza excepciones personalizadas
def test_excepciones(param):
    try:
        # comprobamos el numero que se pasa por parametro
        if param == 1:
            # incluimos un mensaje en el error
            raise ValueError("ValueError: La función espera un valor determinado pero recibe otro.")
        elif param == 2:
            raise TypeError("TypeError: El tipo de dato no es el esperado.")
        elif param == 3:
            raise Exception("Exception: Error general.")
        elif param == 4:
            raise IndexError("IndexError: El índice no existe.")
        else:
            print("Todo bien!")

    # Capturamos los errores
    except ValueError as e:
        print(f"Error! {e}")

    except TypeError as e:
        print(f"Error! {e}")

    except Exception as e:
        print(f"Error! {e}")
    
    except IndexError as e:
        print(f"Error! {e}")

    finally:
        print("Ejecución finalizada")

# vamos a probar!
if __name__ == "__main__":
    # Ejercicio manejo de excepciones
    division(10, 0)
    no_index(3)
    
    # EXTRA
    test_excepciones(2)