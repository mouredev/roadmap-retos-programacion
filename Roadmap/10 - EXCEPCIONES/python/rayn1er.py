# /*
#  * EJERCICIO:
#  * Explora el concepto de manejo de excepciones según tu lenguaje.
#  * Fuerza un error en tu código, captura el error, imprime dicho error
#  * y evita que el programa se detenga de manera inesperada.
#  * Prueba a dividir "10/0" o acceder a un índice no existente
#  * de un listado para intentar provocar un error.
#  *
#  * DIFICULTAD EXTRA (opcional):
#  * Crea una función que sea capaz de procesar parámetros, pero que también
#  * pueda lanzar 3 tipos diferentes de excepciones (una de ellas tiene que
#  * corresponderse con un tipo de excepción creada por nosotros de manera
#  * personalizada, y debe ser lanzada de manera manual) en caso de error.
#  * - Captura todas las excepciones desde el lugar donde llamas a la función.
#  * - Imprime el tipo de error.
#  * - Imprime si no se ha producido ningún error.
#  * - Imprime que la ejecución ha finalizado.
#  */

#las excepciones son herramientas que nos permiten controlar como reacciona el software cuando se produce un error sin que este se detenga, en python contamos con try y except para manejar estos errores

print (4/2) # si ejecutamos esto el programa se ejecuta sin problemas puesto que podemos dividir
# print(4/0) sin embargo si ejecutamos esto el programa nos arroja un error, puesto que no podemos dividir entre 0, esto es un error conocido como zerodivisionerror
# print(2 + "2") si ejecutamos esto tambien nos fallara el programa, puesto que no podemos sumar un int con un string

#podemos manejar el error sin problemas utilizando un condicional para verificar si alguno de los numeros es 0 y en base a eso decidir si se realiza la operacion o no

def division(a, b):
    if a ==0 or b == 0:
        return "Uno de los números es 0, no se puede dividir."
    else:
        return f'La división es igual a {a / b}'

print(division(20,0)) 

#para hacer lo mismo con try: simplemente escribimos en el nuestro codigo y en el except el codigo que se ejecuta en caso de un error

def division_try(a,b):
    try:
        r = a / b
        print(r)
    except:
        print(f'No se puede divir si uno de los numeros es 0')
    finally:
        print(f'Se Ha ejecutado correctamente, has recibido el resultado de una division o un error?')

division_try(20,0)

def list_try(value : list,index = int):
    try:
        return value[index]
    except:
        print("El indice deseado no se encuentra en la lista")


list_try(['hola','como','estas'],3)



# extra

class DictChecker(Exception):
    pass

my_dict = {'a' : 1, 'b' : 2}

# if len(my_dict) >= 1:
#     raise DictChecker("Diccionario con mas de dos valores") # comentado para no romper la ejecucion del sistema


def parameters(a,b):
    

    try:
        print(f'{a} + {b} = {a+b}')
        print(f'{a} - {b} = {a-b}')
        print(f'{a} * {b} = {a*b}')
        print(f'{a} / {b} = {a/b}')
        print(f'{list(a)} + {b} = {a+b}')
        

    except ZeroDivisionError:
        
        print(f"Uno o ambos valores son 0")
    
    except TypeError:
        print(f'Uno o ambos valores son un str')
    
    
    else:
        print(f'El programa se ha ejecutado sin errores')
    

    finally:
        
        print("La ejecucion del codigo ha terminado")
        
parameters(20,20)