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
    resultado = 10/0
    print(resultado)
except IOError:
    print("Error de entrada/salida.")
except ZeroDivisionError:
    print("Error de division por cero.")
else:
    print("No han ocurrido errores")
    print("El resultado de la divison es", resultado)
finally:
    print("La ejecucion ha finalizado")


"""
Extra
"""


class MyExcepcion(TypeError):
    pass


def division(value1, value2):
    result = value1/value2
    return result

def program(value1, value2):

    try:
       resultado = division(value1, value2)

    except MyExcepcion as ex:
        print("Excepcion MyExcepcion: Es un tipo de dato string", type(ex))
    except TypeError:
        print("Excepcion TypeError: No es un tipo de dato entero")
    except ZeroDivisionError:
        print("Excepcion ValueEror: No se puede dividr entre cero")
    
    else:
        print("No han ocurrido errores")
        print("El resultado de la divison es", resultado)
    finally:
        print("La ejecucion ha finalizado")

print()
program(5, "uno")
program(7, 0)
program(20, -5)
program(15, 2)