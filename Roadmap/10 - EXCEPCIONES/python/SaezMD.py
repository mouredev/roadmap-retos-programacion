#10 Excepciones
"""
 * EJERCICIO:
 * Explora el concepto de manejo de excepciones según tu lenguaje.
 * Fuerza un error en tu código, captura el error, imprime dicho error y evita que el programa se detenga de manera inesperada.
 * Prueba a dividir "10/0" o acceder a un índice no existente de un listado para intentar provocar un error.
 
 * DIFICULTAD EXTRA (opcional):
 * Crea una función que sea capaz de procesar parámetros, pero que también pueda lanzar 3 tipos diferentes de excepciones (una de ellas tiene que
 * corresponderse con un tipo de excepción creada por nosotros de manera personalizada, y debe ser lanzada de manera manual) en caso de error.
 * - Captura todas las excepciones desde el lugar donde llamas a la función.
 * - Imprime el tipo de error.
 * - Imprime si no se ha producido ningún error.
 * - Imprime que la ejecución ha finalizado.
"""

#handling exceptions in Python

colors = ['red', 'green', 'blue']
try:
    print(colors[3])
except IndexError as e:
    print(e)
    print(f"There is an error: {e} ({type(e).__name__})")

print('Continue to run')

# 2 exceptions in the same line:
import math
x = 1
y = -2
 
try:
    value = x / y
    print(math.log(value))
except (ZeroDivisionError, ValueError) as e:
    print('Got an error:', e)

#Without using except:

def linux_interaction():
    import sys
    if "linux" not in sys.platform:
        #raise RuntimeError("Function can only run on Linux systems.")
        print('raise RuntimeError("Function can only run on Linux systems.")')
    print("Doing Linux things.")

linux_interaction()

#Divide by 0
(x,y) = (10,0)

try:
    z = x/y
    print(z)

except ZeroDivisionError:
    print("divide by zero")
finally:
    print("let's go")


#Extra
#type of errors: by 0, negative, not a number

# define Python user-defined exceptions
class InvalidNumber(Exception):
    "Raised when the value is between 2 and 10"
    pass

def handlingErrors(number1: int, number2: int)-> int:
    """"function to handle exceptions"""

    try:
        solution = number1 / number2
        if solution <10 and solution >2:
            raise InvalidNumber

    except ZeroDivisionError:
        print("Impossible to divide by 0.")

    except IndexError:
        print("Out of place.")

    except InvalidNumber:
        print("Number not OK.")


    else:
        print("No errors found.")
    finally:
        print("Check errors mode off.")

handlingErrors(22,2)

    

