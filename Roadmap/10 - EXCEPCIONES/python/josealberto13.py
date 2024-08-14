""" EJERCICIO:
 * Explora el concepto de manejo de excepciones según tu lenguaje.
 * Fuerza un error en tu código, captura el error, imprime dicho error
 * y evita que el programa se detenga de manera inesperada.
 * Prueba a dividir "10/0" o acceder a un índice no existente
 * de un listado para intentar provocar un error."""

def dividir():
    while True:
        n1 = int(input("Ingresa un numero para dividir: "))
        n2 = int(input("Ingresa el numero divisor: "))
        try:
            div = n1 / n2
            return div
        except:
            print("¡ERROR! No se puede dividir entre 0")

# print(dividir())


""" Clase de Brais Moure """
try:
    print([1,2,3,4][4])
except Exception as error:          # investigar más sobre el manejo de errores
    print(f"Se ha producido un error: {error} ({type(error).__name__})")


""" DIFICULTAD EXTRA (opcional):
 * Crea una función que sea capaz de procesar parámetros, pero que también
 * pueda lanzar 3 tipos diferentes de excepciones (una de ellas tiene que
 * corresponderse con un tipo de excepción creada por nosotros de manera
 * personalizada, y debe ser lanzada de manera manual) en caso de error.
 * - Captura todas las excepciones desde el lugar donde llamas a la función.
 * - Imprime el tipo de error.
 * - Imprime si no se ha producido ningún error.
 * - Imprime que la ejecución ha finalizado. """

class strTypeError(Exception):
    pass

def process_params(paramteros: list):

    if len(paramteros) < 2:
        raise IndexError()
    elif paramteros[1] == 0:
        raise ZeroDivisionError()
    elif type(paramteros[2]) == str:
        raise strTypeError("El tercer elemento de la lista no debe ser una cadena de texto")

    
    print(paramteros[1])
    print(paramteros[0]/paramteros[1])
    print(paramteros[0]/paramteros[2])
    
# Manejo de Errores 

try:
    process_params([2, 4, 6, 8])
except IndexError as error:
    print(f"El número de parámetros deben ser más de dos ({type(error).__name__})")
except ZeroDivisionError as error:
    print(f"El segundo parámetro no debe ser igual a cero ({type(error).__name__})")
except strTypeError as error:
    print(f"{error}")
except Exception as error:
    print(f"Se ha producido un error inesperado: ({error})")
else:
    print("El programa se ha ejecutado correctamente")
finally:
    print("El programa finaliza")








