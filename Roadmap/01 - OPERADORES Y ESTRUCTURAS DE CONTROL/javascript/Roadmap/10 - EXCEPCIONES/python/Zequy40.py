'''
*EJERCICIO:
* Explora el concepto de manejo de excepciones según tu lenguaje.
* Fuerza un error en tu código, captura el error, imprime dicho error
* y evita que el programa se detenga de manera inesperada.
* Prueba a dividir "10/0" o acceder a un índice no existente
* de un listado para intentar provocar un error.
'''
#Distinto a otros lenguajes que utilizan Try Catch, en Python se usa try except:

try:
    # Intentar dividir por cero
    resultado = 10 / 0
except ZeroDivisionError as e:
    # Capturar la excepción ZeroDivisionError
    print(f"Error: {e}")
    resultado = None

print("Después de la excepción. Resultado:", resultado)

# Intentar acceder a un índice no existente en una lista
lista = [1, 2, 3]
try:
    elemento = lista[10]
except IndexError as e:
    # Capturar la excepción IndexError
    print(f"Error: {e}")
    elemento = None

print("Después de la excepción. Elemento:", elemento)


#Cada bloque except captura la excepción correspondiente, imprime el error y, en este caso, asigna un valor predeterminado es un variable despues del error
#para que se pueda asignar otro valor (None) para evitar que el programa se detenga abruptamente.

'''
DIFICULTAD EXTRA:
 * Crea una función que sea capaz de procesar parámetros, pero que también
 * pueda lanzar 3 tipos diferentes de excepciones (una de ellas tiene que
 * corresponderse con un tipo de excepción creada por nosotros de manera
 * personalizada, y debe ser lanzada de manera manual) en caso de error.
 * - Captura todas las excepciones desde el lugar donde llamas a la función.
 * - Imprime el tipo de error.
 * - Imprime si no se ha producido ningún error.
 * - Imprime que la ejecución ha finalizado.
 '''
# Definir una excepción personalizada
class MiExcepcionPersonalizada(Exception):
    pass #Se utiliza pass una funcion en Python que permite que no haga nada, en este paso.

def procesar_parametros(parametro):
    try:
        # Procesar parámetros y lanzar excepciones
        if not isinstance(parametro, int):
            raise TypeError("El parámetro debe ser un entero")
        
        if parametro == 0:
            raise ValueError("El parámetro no puede ser cero")
        
        if parametro < 0:
            raise MiExcepcionPersonalizada("El parámetro no puede ser negativo")

        # Simular procesamiento con éxito
        resultado = parametro * 2
        print("Resultado del procesamiento:", resultado)

    except TypeError as e:
        print(f"Error de tipo: {e}")

    except ValueError as e:
        print(f"Error de valor: {e}")

    except MiExcepcionPersonalizada as e:
        print(f"Error personalizado: {e}")

    except Exception as e:
        print(f"Error inesperado: {e}")

    finally:
        print("Ejecución finalizada")

# Ejemplo de uso
try:
    procesar_parametros(5)
    procesar_parametros("cadena")  # Provocará un TypeError
    procesar_parametros(0)         # Provocará un ValueError
    procesar_parametros(-1)        # Provocará un MiExcepcionPersonalizada

except Exception as e:
    print(f"Se ha producido un error general: {e}")
