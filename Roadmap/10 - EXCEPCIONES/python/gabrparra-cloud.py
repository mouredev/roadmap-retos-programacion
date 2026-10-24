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
 */
 """
try:
    print(10/0)
except Exception as Error:
    print(f"se ha producido un error {Error}")

try:
    print([1,2,3][3])
except Exception as Error:
    print(f"se ha producido un error {Error}")

class StrTypeError(Exception):
    pass

def funtion(parameters: list):
   # try:
        if len(parameters) < 2:
            raise IndexError()
        elif parameters[1] == 0:
            raise ZeroDivisionError()
        elif type(parameters[2]) == str:
           raise StrTypeError("El segundo elemento debe ser un entero")
            
        print(parameters[2])
        print(parameters[0]/parameters[1])
        print(parameters[2]+5)
    #except Exception as Error:
    #    print(f"se ha producido en error {Error} ({type(Error).__name__})")

try:
    funtion([1,2,1])
except IndexError as Error:
    print(f"El numero de elementos de la lista debe ser mayor que dos {Error} ({type(Error).__name__})")
except ZeroDivisionError as Error:
    print(f"El segundo elemento de la lista no puede ser cero {Error} ({type(Error).__name__})")
except StrTypeError as Error:
    print(f"El segundo elemento debe ser un entero {Error} ({type(Error).__name__})")
except Exception as Error:
     print(f"se ha producido en error {Error} ({type(Error).__name__})")
else:
    print("Se termino sin errores")
finally:
    print("el programa finaliza")

    

