"""
 * EJERCICIO:
 * Explora el concepto de manejo de excepciones según tu lenguaje.
 * Fuerza un error en tu código, captura el error, imprime dicho error
 * y evita que el programa se detenga de manera inesperada.
 * Prueba a dividir "10/0" o acceder a un índice no existente
 * de un listado para intentar provocar un error.
"""

def manejar_excepciones():
    try:
        # Forzamos un error de división por cero
        resultado = 10 / 0
    except ZeroDivisionError as e:
        print(f"Error capturado: {e}")
    
    try:
        # Forzamos un error de índice fuera de rango
        lista = [1, 2, 3]
        elemento = lista[5]
    except IndexError as e:
        print(f"Error capturado: {e}")

    print("El programa continúa ejecutándose sin problemas.")

# Llamamos a la función para ver el manejo de excepciones en acción
manejar_excepciones()


"""
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

# Definimos una excepción personalizada
class CustomError(Exception):
    pass

def procesar_parametros(param):
    if not isinstance(param, int):
        raise TypeError("El parámetro debe ser un entero.")
    if param < 0:
        raise ValueError("El parámetro no puede ser negativo.")
    if param == 0:
        raise CustomError("El parámetro no puede ser cero.")
    return param * 2

def main():
    parametros = [10, -5, "texto", 0, 5]
    
    for param in parametros:
        try:
            resultado = procesar_parametros(param)
            print(f"Resultado: {resultado}")
        except TypeError as e:
            print(f"Error de tipo: {e}")
        except ValueError as e:
            print(f"Error de valor: {e}")
        except CustomError as e:
            print(f"Error personalizado: {e}")
        except Exception as e:
            print(f"Error inesperado: {e}")
        else:
            print("No se ha producido ningún error.")
        finally:
            print("La ejecución ha finalizado.\n")

if __name__ == "__main__":
    main()
