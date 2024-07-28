#Reto 10

''' * Explora el concepto de manejo de excepciones según tu lenguaje.
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
 * - Imprime que la ejecución ha finalizado.'''


try:
    raise ValueError
except ValueError:
    print("El valor del argumento es inapropiado para la operación")



try:
    print(15/0)
except ZeroDivisionError:
    print(f"No puedes dividir entre cero: {ZeroDivisionError}")

lista =[1,2,3,4,5,6]
try:
    print(lista[8])
except IndexError:
    print(f"Se ha producido un error: {IndexError}")



#Reto Extra

class TypeCharError(TypeError):
    pass

def procesador_de_parametros(indice, num_1, cadena):
    lista = [1,2,3,4,5]
    print(lista[indice])
    suma = 13 + num_1
    print(suma)
    if cadena.isalpha():
        char_alpha = cadena
        print(char_alpha)
    else:
        raise TypeCharError("El caracter debe ser alphabético")
    

try:
    procesador_de_parametros(7,"12","ar54")
except IndexError as error_indice:
    print(f"Ocurrio un error: {error_indice}")
except TypeError as error_tipo:
    print(f"Ocurrio un error: {error_tipo}")
except TypeCharError as error_de_character:
    print(f"Ocurrio un error: {error_de_character}")
except Exception as excepcion:
    print(f"Ocurrio un error inesperado: {excepcion}")
else:
    print("No ha ocurrido ningún error")
finally:
    print("La ejecución ha finalizado")