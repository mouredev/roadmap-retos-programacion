# /*
#  * EJERCICIO:
#  * Explora el concepto de manejo de excepciones según tu lenguaje.
#  * Fuerza un error en tu código, captura el error, imprime dicho error
#  * y evita que el programa se detenga de manera inesperada.
#  * Prueba a dividir "10/0" o acceder a un índice no existente
#  * de un listado para intentar provocar un error.
#  */



try:
    print(10/0)
except Exception as e:
    print(f"Ha ocurrido un error -> {e} | TYPE:{type(e).__name__}")


try:
    lista = [1,2,3,4]
    print(lista[4])
except Exception as e:
    print(f"Ha ocurrido un error -> {e} | TYPE:{type(e).__name__}")





#  * DIFICULTAD EXTRA (opcional):
#  * Crea una función que sea capaz de procesar parámetros, pero que también
#  * pueda lanzar 3 tipos diferentes de excepciones (una de ellas tiene que
#  * corresponderse con un tipo de excepción creada por nosotros de manera
#  * personalizada, y debe ser lanzada de manera manual) en caso de error.
#  * - Captura todas las excepciones desde el lugar donde llamas a la función.
#  * - Imprime el tipo de error.
#  * - Imprime si no se ha producido ningún error.
#  * - Imprime que la ejecución ha finalizado. 

class StrTypeError(Exception):
    pass

def processParam(parametros: list):
    if len(parametros) < 3:
        raise IndexError
    elif parametros[1] == 0:
        raise ZeroDivisionError
    elif type(parametros[2]) == str:
        raise StrTypeError ("El tercer elemento no puede ser un string")
    
    print(parametros[2])
    print(parametros[0]/parametros[1])
    print(parametros[2] + 5)


try:
    processParam([1,4,6,5])
except IndexError as e:
    print("El número de elementos no es suficiente ")
except ZeroDivisionError as e:
    print(f"Se ha producido un error -> {e} | TYPE:{type(e).__name__}")
except StrTypeError as e:
    print(e)
except Exception:
    print("Se ha producido un error general!")
else:
    print("Código correcto!")
finally:
    print("Fin del programa! ")
    


