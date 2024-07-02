def manejo_de_excepciones():
    try:
        resultado_division = 10 / 0
    except ZeroDivisionError as e:
        print(f"Error capturado: {e}")

    try:
        lista = [1, 2, 3]
        elemento = lista[5]
    except IndexError as e:
        print(f"Error capturado: {e}")

    print("El programa continúa ejecutándose a pesar de los errores.")

manejo_de_excepciones()

#EXTRA
"""DIFICULTAD EXTRA (opcional):
 * Crea una función que sea capaz de procesar parámetros, pero que también
 * pueda lanzar 3 tipos diferentes de excepciones (una de ellas tiene que
 * corresponderse con un tipo de excepción creada por nosotros de manera
 * personalizada, y debe ser lanzada de manera manual) en caso de error.
 * - Captura todas las excepciones desde el lugar donde llamas a la función.
 * - Imprime el tipo de error.
 * - Imprime si no se ha producido ningún error.
 * - Imprime que la ejecución ha finalizado. 
 */"""

class MiExcepcionPersonalizada(Exception):
    def __init__(self, mensaje):
        self.mensaje = mensaje
        super().__init__(self.mensaje)

def procesar_parametros(parametro):
    if parametro == "zero_division":
        raise ZeroDivisionError("Intentaste dividir por cero.")
    elif parametro == "index_error":
        raise IndexError("Índice fuera de los límites.")
    elif parametro == "mi_excepcion":
        raise MiExcepcionPersonalizada("Esto es una excepción personalizada.")
    else:
        print(f"El parámetro {parametro} se ha procesado correctamente.")

def main():
    parametros = ["zero_division", "index_error", "mi_excepcion", "sin_error"]
    for parametro in parametros:
        try:
            procesar_parametros(parametro)
        except ZeroDivisionError as e:
            print(f"Error capturado: {e}")
        except IndexError as e:
            print(f"Error capturado: {e}")
        except MiExcepcionPersonalizada as e:
            print(f"Error capturado: {e}")
        except Exception as e:
            print(f"Error desconocido capturado: {e}")
        else:
            print("No se ha producido ningún error.")
        finally:
            print("La ejecución ha finalizado.")

main()
