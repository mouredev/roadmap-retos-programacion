"""
 * EJERCICIO:
 * Explora el concepto de manejo de excepciones según tu lenguaje.
 * Fuerza un error en tu código, captura el error, imprime dicho error
 * y evita que el programa se detenga de manera inesperada.
 * Prueba a dividir "10/0" o acceder a un índice no existente
 * de un listado para intentar provocar un error.
"""

def excepcion(input_str):
    lista = [10, 20, 30, 40, 50]
    num = len(lista)
    input = int(input_str)

    try:
        division = num/input
        print("División de ", len(lista), "entre ", input, "es: ", division)
        
    except:
        print("No es posible dividir entre", input)
    
    else:
        print("No ha habido ningún problema.")

    try:
        print("El elemento de la lista en la posición", input, "es:", lista[input])
    
    except:
        print("No hay ningún elemento de la lista en la posición", input)


input_str = input("Introduce un número cualquiera: ")
excepcion(input_str)


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

class MiExcepcionPersonalizada(Exception):
    def __init__(self, mensaje="Error personalizado"):
        self.mensaje = mensaje
        super().__init__(self.mensaje)

def procesar_parametros(param1, param2):
    try:
        if not isinstance(param1, int) or not isinstance(param2, int):
            raise ValueError("Ambos parámetros deben ser enteros.")
        
        if param2 == 0:
            raise ZeroDivisionError("No se puede dividir entre cero.")

        # Simulación de un error personalizado
        if param1 == 42:
            raise MiExcepcionPersonalizada("¡Error personalizado!")

        resultado = param1 / param2
        print("Resultado:", resultado)

    except ValueError as ve:
        print(f"Error de valor: {ve}")
    except ZeroDivisionError as zde:
        print(f"Error de división entre cero: {zde}")
    except MiExcepcionPersonalizada as mep:
        print(f"Error personalizado: {mep}")
    except Exception as e:
        print(f"Otro tipo de error: {e}")
    else:
        print("No se ha producido ningún error.")
    finally:
        print("La ejecución ha finalizado.")

# Ejemplo de uso:
try:
    procesar_parametros(10, 2)
    procesar_parametros("a", 2)
    procesar_parametros(42, 5)
except Exception as e:
    print(f"Excepción capturada: {e}")
