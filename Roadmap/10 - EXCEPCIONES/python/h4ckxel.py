'''
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
'''

#Declaramos las variables necesarias
numero1 = 10
numero2 = 0
listado= ["Hola","Python","Alexdevrep","Mundo"]

#División

def dividir(numero1, numero2):
    try:
        resultado = numero1 / numero2
        print(resultado)

    except ZeroDivisionError: # En este bloque indicamos el error que queremos que capture el programa
        print("No se puede dividir un número por cero")

    finally:
        print("Finalizando el programa")

dividir(numero1, numero2)

#Listado

def iterarLista():
    try:
        #Intentamos acceder a un índice que no existe
        print(listado[6])
    except:
        print("Índice no existente en la lista")
    finally:
        print("Programa finalizado")

iterarLista()

#Dificultad EXTRA

#Vamos a crear una función que multiplique un número natural de una cifra por 5

class NoneException(Exception):
    pass #Creamos una excepcion personalizada

def multiplo(numero3):
    try:
        
        if numero3 is None:
            raise NoneException("Es necesario dar un número para multiplicar") #Generamos manualmente la excepcion con raise
        elif 9 < numero3 < 100:
            raise Exception("El número tiene 2 cifras.")
        elif numero3 < 0:
            raise ValueError("El número es negativo, no se puede multiplicar.")
        else:
            producto = 5 * numero3
            print(producto)

    except ValueError as e:
        print(f'Error: {e}')
    except NoneException as e:
        print(f'Error: {e}')
    except Exception as e:
        print(f"Error: {e}")
    
    finally:
        print("Cerrando el programa")


entrada = input("Por favor ingrese el número a multiplicar: ")
numero3= int(entrada) if entrada else None
multiplo(numero3)


