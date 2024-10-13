"""* EJERCICIO:
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
 * - Imprime que la ejecución ha finalizado. """

#División entre cero
def divideByZero():        
    try:
        print(10 / 0)        
    except ZeroDivisionError as e: 
        print("Error: No se puede dividir entre cero", e)        
    finally:
        print("La ejecución ha finalizado")        

divideByZero()

#Acceso a un índice inexistente
numeros = [1,2,3,4]

def listado():
    try:
        print(numeros[10])
    except IndexError as e:
        print('Error de: ', e)

listado()

#EXTRA
print("\n-----EXTRA-----\n")

numeros2 = ["pepe",2,3,4]

class Excepcion(Exception): #Excepción personalizada que hereda de la superclase Exception
    pass

def procParam(parametros: list):    
    if len(parametros) < 4:
        raise IndexError("No hay suficientes parámetros")
    elif parametros[2] == 0:
        raise ZeroDivisionError("No se puede dividir entre cero")
    elif type(parametros[0]) is not int:
        raise Excepcion("El primer elemento de la lista no es un entero")
            
    print(parametros[0] + 5)
    print(parametros[3])
    print(parametros[1] / parametros[2])    
    
try:
    procParam(numeros2)
except IndexError as error:
    print(error)
except ZeroDivisionError as error:
    print(error)
except Excepcion as error:
    print(f"Error de tipo: {type(error).__name__} {error}")
else:
    print("No se han producido errores")
finally:
    print("La ejecución ha finalizado")

