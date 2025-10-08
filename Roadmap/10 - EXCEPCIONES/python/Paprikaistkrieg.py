#Manejo de Excepciones


"""
El manejo de excepciones en Python se realiza utilizando las palabras clave try, except, else y finally.
Estas palabras clave permiten manejar errores de manera controlada y evitar que el programa se detenga abruptamente.
el bloque try contiene el código que puede generar una excepción,
el bloque except contiene el código que maneja la excepción si ocurre,
el bloque else contiene el código que se ejecuta si no ocurre ninguna excepción,
y el bloque finally contiene el código que se ejecuta siempre, haya o no una excepción.
"""
from operator import index


try:
    #numero = int(input("Ingresa un número: ")) # Solicita al usuario que ingrese un número
    resultado = 10 / 0 # Intenta dividir 10 por el número ingresado
    print(f"El resultado es: {resultado}") # Imprime el resultado de la división
    #mi_lista = [1, 2, 3]
    print(mi_lista[3])  # Esto generará un IndexError
except ValueError: 
    print("Error: Debes ingresar un número válido.") # Maneja el error si el usuario no ingresa un número válido
except ZeroDivisionError: 
    print("Error: No se puede dividir por cero.") # Maneja el error si el usuario ingresa cero
except Exception as e:
    print(f"Ocurrió un error inesperado: {e}")  # Maneja cualquier otro error inesperado
else:
    print("La operación se realizó con éxito.")  # Se ejecuta si no hubo ninguna excepción
finally:
    print("Gracias por usar el programa.")  # Se ejecuta siempre, haya o no una excepción. Se usa para liberar recursos o realizar tareas de limpieza.

#El bloque finally se ejecuta siempre, haya o no una excepción. Se usa para liberar recursos o realizar tareas de limpieza.



#XTRAJ

class StringTypeError(Exception):
    """Excepción personalizada para errores de tipo de cadena."""
    pass

def process_params(params: list):
    try:
        if len(params) < 3:
            raise IndexError()   # Lanza una excepción si la lista tiene menos de 3 elementos
        if params[1] == 0:
            raise ZeroDivisionError()  # Lanza una excepción si el segundo elemento es cero
        elif type(params[1]) is str:
            raise StringTypeError("el segundo elemento debe ser un número.")  # Lanza una excepción si el segundo elemento es una cadena
        print(params[2])  # Imprime el tercer parámetro
        print(params[0]/params[1])
        print(params[2] + 5)
        print(params[4])  # Intenta acceder al quinto elemento de la lista
    except IndexError as quote:
        print("El número de parámetros debe ser mayor que 3.")  # Maneja cualquier error que ocurra al acceder al elemento
    except ZeroDivisionError as zde:
        print("No se puede dividir por cero en el segundo parámetro.")  # Maneja el error de división por cero
    except StringTypeError as ste:
        print(f"Error: {ste}")  # Maneja el error de tipo de cadena personalizado
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")
    else:
        print("Los parámetros se procesaron correctamente.(esto indica que no hubo excepciones o errores)")  # Se ejecuta si no hubo ninguna excepción
    finally:
        print("El programa finalizó correctamente.")  # Se ejecuta siempre, haya o no una excepción. Se usa para liberar recursos o realizar tareas de limpieza.

process_params([1, 2, 3, 4, 5])  # Llama a la función con una lista de parámetros válida