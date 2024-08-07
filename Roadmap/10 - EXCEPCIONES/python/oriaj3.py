"""	
10 -EXCEPCIONES

Autor de la solución: Oriaj3	

Teoría:

Las excepciones son errores que se producen durante la ejecución de un programa. 
Cuando se produce una excepción, el programa se detiene y se genera un mensaje 
de error que indica la causa del problema.

En Python, las excepciones se manejan con bloques try-except. El código que
puede generar una excepción se coloca dentro del bloque try
y el código que maneja la excepción se coloca dentro del bloque except.

Las excepciones se pueden clasificar en dos tipos:
- Excepciones del sistema: son las que proporciona el propio lenguaje.
- Excepciones personalizadas: son las que creamos nosotros mismos.

Las excepciones del sistema se pueden capturar de manera individual o todas
juntas. Si se capturan todas juntas, se debe tener cuidado de no ocultar
errores importantes.

Las excepciones personalizadas se crean mediante la herencia de la clase
Exception. Esto permite definir un comportamiento específico para cada tipo
de excepción.

Las excepciones se pueden lanzar de manera manual con la palabra clave raise.

Las excepciones se pueden capturar y manejar de manera anidada, es decir, se
puede capturar una excepción dentro de otra excepción. Esto es útil para
proporcionar información adicional sobre el error. 
"""

"""
* EJERCICIO:
 * Explora el concepto de manejo de excepciones según tu lenguaje.
 * Fuerza un error en tu código, captura el error, imprime dicho error
 * y evita que el programa se detenga de manera inesperada.
 * Prueba a dividir "10/0" o acceder a un índice no existente
 * de un listado para intentar provocar un error.
"""
try: 
    print(10/0)
    print([1, 2, 3, 4][4])
except Exception as e:
    print(f"Se ha producido un error: {e} ({type(e).__name__})")

lista = [1, 2, 3, 4]

try:
    print(lista[4])
except Exception as e:
    print(f"Se ha producido un error: {e} ({type(e).__name__})")

"""
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

class MyNegativeException(Exception):
    error_type = "MyNegativeException"

    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"{self.error_type}: {self.message}"
    

def process_params(parameters: list):

    if len(parameters) < 3:
        raise IndexError()
    elif parameters[1] == 0:
        raise ZeroDivisionError()
    elif type(parameters[2]) == str:
        raise TypeError(
            "El tercer elemento no puede ser una cadena de texto.")
    elif parameters[2] < 0:
        raise MyNegativeException("El tercer elemento no puede ser negativo.")

    print(parameters[2])
    print(parameters[0]/parameters[1])
    print(parameters[2] + 5)

#Llamada a la función process_params con diferentes parámetros que producen errores.
try: 
    process_params([1, 0, 3])
except IndexError as e:
    print(f"Se ha producido un error: {e} ({type(e).__name__})")
except ZeroDivisionError as e:
    print(f"Se ha producido un error: {e} ({type(e).__name__})")
except MyNegativeException as e:
    print(f"Se ha producido un error: {e} ({type(e).__name__})")
except Exception as e:
    print(f"Se ha producido un error: {e} ({type(e).__name__})")
#Imprime si no se ha producido ningún error.
else:
    print("No se ha producido ningún error.")

finally:
    print("La ejecución ha finalizado.")

#Llamada a la función process_params con parámetros correctos.
try: 
    process_params([10, 2, 3])
except IndexError as e:
    print(f"Se ha producido un error: {e} ({type(e).__name__})")
except ZeroDivisionError as e:
    print(f"Se ha producido un error: {e} ({type(e).__name__})")
except MyNegativeException as e:
    print(f"Se ha producido un error: {e} ({type(e).__name__})")
except Exception as e:
    print(f"Se ha producido un error: {e} ({type(e).__name__})")
#Imprime si no se ha producido ningún error.
else:
    print("No se ha producido ningún error.")

finally:
    print("La ejecución ha finalizado.")






