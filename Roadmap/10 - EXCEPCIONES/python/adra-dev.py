"""
EJERCICIO:
Explora el concepto de manejo de excepciones según tu lenguaje.
Fuerza un error en tu código, captura el error, imprime dicho error
y evita que el programa se detenga de manera inesperada.
Prueba a dividir "10/0" o acceder a un índice no existente
de un listado para intentar provocar un error.

DIFICULTAD EXTRA (opcional):
Crea una función que sea capaz de procesar parámetros, pero que también
pueda lanzar 3 tipos diferentes de excepciones (una de ellas tiene que
corresponderse con un tipo de excepción creada por nosotros de manera
personalizada, y debe ser lanzada de manera manual) en caso de error.
- Captura todas las excepciones desde el lugar donde llamas a la función.
- Imprime el tipo de error.
- Imprime si no se ha producido ningún error.
- Imprime que la ejecución ha finalizado.
"""

"""
Excepciones:

Una excepcion es un error logico que se produce en tiempo de ejecucion.
Las exepciones van asociadas a distintos tipos, y ese mismo tipo es el 
que se muestra en el mensaje de error.  Todo esto para disponer de 
informacion suficiente para encontrar el fallo y solucionalro o gestionarlo.
Algunos ejemplos son 
    * ZeroDivisionError
    * NameError
    * TypeError
"""

# a = 0 
# b = 10 
# c = b/a
# print(c)

# a = []
# print(a[10])


"""
Gestion de excepciones:

La gestion de excepciones es una tecnica de programacion para 
controlar los errores producidos durante la ejecucion de una 
aplicacion. Se controlan de una forma parecida a una sentencia 
condicional. Si no se produce una excepcion (general o especifica), 
que seria el caso normal, la aplicacion continua con las siguientes 
instrucciones y si se produce una, se ejecutaran las instrucciones 
indicadas por el desarrollador para su tratamiento, que pueden 
continuar la aplicacion o detenerla, dependiendo de cada caso.
"""

try:
    print(10/0)
    print([1, 2, 3, 4][4])
except Exception as e:
    print(f"Se ha producido un error: {e} ({type(e).__name__})")

"""
Extra
"""

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
    print("El número de elementos de la lista debe ser mayor que dos.")
except ZeroDivisionError as e:
    print("El segundo elemento de la lista no puede ser un cero.")
except StrTypeError as e:
    print(f"{e}")
except Exception as e:
    print(f"Se ha producido un error inesperado: {e}")
else:
    print("No se ha producido ningún error.")
finally:
    print("El programa finaliza sin detenerse.")