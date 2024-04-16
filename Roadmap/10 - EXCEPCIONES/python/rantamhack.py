print("\n\n=====================================¿QUE ES UNA EXCEPCION?=====================================\n\n")


print("Al programar en Python algunas veces podemos anticipar errores de ejecucion, incluso en un programa sintactica y\nlogicamente correcto, puede llegar a haber errores causados por entrada de datos invalidos o inconsistencias predecibles.")


print("\n\n=====================================EJERCICIO=====================================\n\n")

'''
 * Explora el concepto de manejo de excepciones segun tu lenguaje.
 * Fuerza un error en tu codigo, captura el error, imprime dicho error
 * y evita que el programa se detenga de manera inesperada.
 * Prueba a dividir "10/0" o acceder a un i­ndice no existente
 * de un listado para intentar provocar un error.
'''

def index_error():
    
    try:
        my_list = [1, 2, 3, 4]
        print(my_list[4])
    except IndexError as e:
        print(f"El elemento no existe en my_list: {e}")
        
index_error()

print("El programa continua")

print("\n\n==========================================================================\n\n")

def division_zero():
    
    a = 10
    b = 0
    
    try:
        division = a / b
        print(division)
    except ZeroDivisionError as e:
        print(f"Dividir por cero no es posible: {e}")
        
division_zero()

print("El programa continua")
    

print("\n\n=====================================DIFICULTAD EXTRA=====================================\n\n")


'''
 * Crea una funcion que sea capaz de procesar parmetros, pero que tambien
 * pueda lanzar 3 tipos diferentes de excepciones (una de ellas tiene que
 * corresponderse con un tipo de excepcion creada por nosotros de manera
 * personalizada, y debe ser lanzada de manera manual) en caso de error.
 * - Captura todas las excepciones desde el lugar donde llamas a la funcion.
 * - Imprime el tipo de error.
 * - Imprime si no se ha producido ningun error.
 * - Imprime que la ejecucion ha finalizado
'''

class StrTypeError(Exception):
    pass


def process_params(parameters: list):

    if len(parameters) < 3:
        raise IndexError()
    elif parameters[1] == 0:
        raise ZeroDivisionError()
    elif type(parameters[2]) == str:
        raise StrTypeError(
            "El tercer elemento no puede ser una cadena de texto.")

    print(parameters[2])
    print(parameters[0]/parameters[1])
    print(parameters[2] + 5)


try:
    process_params([1, 2, 3, 4])
except IndexError as e:
    print("El numero de elementos de la lista debe ser mayor que dos.")
except ZeroDivisionError as e:
    print("El segundo elemento de la lista no puede ser un cero.")
except StrTypeError as e:
    print(f"{e}")
except Exception as e:
    print(f"Se ha producido un error inesperado: {e}")
else:
    print("No se ha producido ningun error.")
finally:
    print("El programa finaliza sin detenerse.")
