##10 - EXCEPCIONES
"""
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
 */"""

#try para capturar una posible parte de error
try :
    valor = int(input("que numero vas a dividir : "))
    print("el resultado es : " , valor/0)

except ZeroDivisionError as Error : #captura de la excepcion exacta
    print("el error es :" , Error)

#clase propia de excepcion
class MiExcepcion(Exception):
    def __init__(self, parametro_generico = "mensaje de error generico") -> None: #parametro
        super().__init__(parametro_generico)

        self.parametro_generico = parametro_generico

        #forzando 3 tipos de error
        if type(parametro_generico) is str :
            try :
                parametro_generico + 45.6
                print("no saltare nunca xd")
            except Exception as error :         #captura cualquier excepcion
                print("el error es : ", error)

        elif type(parametro_generico) is int:

            try :
                parametro_generico - "1234"
                print("tampoco saltere")

            except Exception as error :
                print("el error es : " , error)

        elif type(parametro_generico) is list :
            try :
                elementos = len(parametro_generico)
                print(parametro_generico[elementos + 2])

            except Exception as error :
                print("el error es : " , error)

        else :
            print("tipo de dato no definido para forzar excepcion")


error_int = MiExcepcion(123)
error_str = MiExcepcion("hola mundo")
error_list = MiExcepcion([1 , 2, "hola mundo"])



