"""
EJERCICIO:
 * Explora el concepto de manejo de excepciones según tu lenguaje.
 * Fuerza un error en tu código, captura el error, imprime dicho error
   y evita que el programa se detenga de manera inesperada.
 * Prueba a dividir "10/0" o acceder a un índice no existente
   de un listado para intentar provocar un error.

DIFICULTAD EXTRA (opcional):
 * Crea una función que sea capaz de procesar parámetros, pero que también
   pueda lanzar 3 tipos diferentes de excepciones (una de ellas tiene que
   corresponderse con un tipo de excepción creada por nosotros de manera
   personalizada, y debe ser lanzada de manera manual) en caso de error.
 *   Captura todas las excepciones desde el lugar donde llamas a la función.
 *   Imprime el tipo de error.
 *   Imprime si no se ha producido ningún error.
 *   Imprime que la ejecución ha finalizado.
"""

try:
    print(10/0)
    print([3,4,7][1])

except Exception as e:
    print(f"Se ha producido un error {e} de tipo: {type(e).__name__}")

print("")

'''
Extra
'''

class StrMethodError(Exception):
    pass

def process_params(parameters: list):
    
    try:
        num
    except NameError:
        raise NameError("La variable 'num' no esta definida")
    
    try:
        exec(parameters[5])
    except SyntaxError:
        raise SyntaxError
    
    try:
        int(parameters[4])
    except ValueError:
        raise ValueError
    
    try:
        parameters[4].append("!")
    except AttributeError:
        raise StrMethodError("Solo las listas pueden hacer uso del metodo append()")
    
    print(parameters[1] + num)
    print(exec(parameters[5]))
    print(int(parameters[4]))


try:
    process_params([2, 0, 6, 10, "hello", "x === 5"])
except NameError as e:
    print(f"❌Error: {e} | Tipo de Error: {type(e).__name__}")
except SyntaxError as e:
    print(f"❌Error: {e} | Tipo de Error: {type(e).__name__}")
except ValueError as e:
    print(f"❌Error: {e} | Tipo de Error: {type(e).__name__}")
except StrMethodError as e:
    print(f"❌Error: {e}")
except Exception as e:
    print(f"❌Ha ocurrido un error inesperado. | Error: {e} | Tipo de Error: {type(e).__name__}")
else:
    print("✅No se ha producido ningun error.")
finally:
    print("✅La ejecucion ha finalizado")