# Autor: Héctor Adàn
# GitHub: https://github.com/hectorio23
import sys

'''
/*
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

# Función para dividir dos números e intentar forzar un error
def dividir():
    try:
        divisor = 0
        if divisor == 0:
            raise ValueError("División por cero")
        resultado = 10 / divisor  # Intento de dividir por cero
        print(f"El resultado de la división es: {resultado}")
    except Exception as e:
        print(f"Se produjo un error: {e}")

# Función que puede lanzar excepciones personalizadas
def procesar_parametro(parametro):
    try:
        if parametro == 0:
            raise ValueError("El parámetro no puede ser cero")
        elif parametro < 0:
            raise ValueError("El parámetro no puede ser negativo")
        else:
            print("Procesamiento exitoso")
    except ValueError as ve:
        print(f"Se produjo un error: {ve}")
    except Exception as e:
        print(f"Error inesperado: {e}")
    else:
        print("No se produjo ningún error.")
    finally:
        print("La ejecución ha finalizado.")

# Función principal (equivalente a main en C++)
if __name__ == "__main__":
    # Forzar un error al dividir por cero
    print("Intentando dividir por cero:")
    dividir()

    print("\n---------------------------------------\n")

    # Intento de procesar un parámetro
    print("Intentando procesar parámetro:")
    procesar_parametro(-3)
