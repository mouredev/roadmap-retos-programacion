"""
Excepciones
"""

try:
    print(5/5)
    my_list = [2,4,6,8]
    print(my_list[8])

# Si ocurre cualquier excepción en el bloque try. se captura aquí y se guarda en la variable 'e'.  
# {e} → muestra el mensaje de error específico que generó Python. Por ejemplo: 'list index out of range' si intentaste acceder a una posición inexistente en una lista.
# {type(e).__name__} → muestra el nombre de la clase de excepción que ocurrió. Por ejemplo: 'IndexError', 'ValueError', 'ZeroDivisionError', etc.
except Exception as e:
    print(f"Se ha producido un error: {e} ({type(e).__name__})") 
    
print("Hola") # Esta línea se ejecuta sin importar si hubo error o no


"""* DIFICULTAD EXTRA (opcional):
 * Crea una función que sea capaz de procesar parámetros, pero que también
 * pueda lanzar 3 tipos diferentes de excepciones (una de ellas tiene que
 * corresponderse con un tipo de excepción creada por nosotros de manera
 * personalizada, y debe ser lanzada de manera manual) en caso de error.
 * - Captura todas las excepciones desde el lugar donde llamas a la función.
 * - Imprime el tipo de error.
 * - Imprime si no se ha producido ningún error.
 * - Imprime que la ejecución ha finalizado. """


print("------------------------")



# Definimos una excepción personalizada llamada StrTypeError que hereda de Exception
class StrTypeError(Exception):
    pass  # No hace nada extra, solo sirve para identificar un tipo de error propio

# Definimos una función que recibe una lista llamada 'parameters'
def process_params(parameters: list):

    # Validación 1: si la lista tiene menos de 3 elementos, lanza IndexError
    if len(parameters) < 3:
        raise IndexError()
    
    # Validación 2: si el segundo elemento (índice 1) es cero, lanza ZeroDivisionError
    elif parameters[1] == 0:
        raise ZeroDivisionError()

    # Validación 3: si el tercer elemento (índice 2) es una cadena, lanza nuestro error personalizado
    elif type(parameters[2]) == str:
        raise StrTypeError("El tercer elemento de la lista no puede ser una cadena de texto")

    # Si todo está bien, ejecuta estas operaciones:
    print(parameters[2])             # Imprime el valor del tercer elemento
    print(parameters[0] / parameters[1])  # Divide el primer elemento entre el segundo
    print(parameters[2] + 5)         # Suma 5 al tercer elemento (debe ser un número)

# Aquí empieza el manejo de excepciones
try:
    # Llama a la función con una lista de ejemplo
    process_params([1,3,6,4])
    
# Si ocurre IndexError, entra aquí
except IndexError as e:
    print("El numero de elementos de la lista debe ser mayor que 2")

# Si ocurre ZeroDivisionError, entra aquí
except ZeroDivisionError as e:
    print("El segundo elemento de la lista no puede ser cero")

# Si ocurre nuestro error personalizado StrTypeError, entra aquí
except StrTypeError as e:
    print(e)  # Muestra el mensaje personalizado

# Si ocurre cualquier otro error no previsto, entra aquí
except Exception as e:
    print(f"Se ha producido un error inesperado: {e}")

# Si no se produce ninguna excepción, se ejecuta este bloque
else:
    print("No se ha producido ningun error")

# Este bloque se ejecuta siempre, haya ocurrido o no una excepción
finally:
    print("El programa finaliza")
