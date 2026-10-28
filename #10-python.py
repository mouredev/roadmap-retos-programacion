'''
*
* EJERCICIO:
* Explora el concepto de manejo de excepciones según tu lenguaje.
* Fuerza un error en tu código, captura el error, imprime dicho error
* y evita que el programa se detenga de manera inesperada.
* Prueba a dividir "10/0" o acceder a un índice no existente
* de un listado para intentar provocar un error.
*
'''
Lista = [1,2,3,4]

try: 
    print (0/1)
    print (Lista[3])
  

except Exception as e:
    print (f"{type(e).__name__} {e}")
finally:
    print ("Acabó el programa")        


'''
DIFICULTAD EXTRA (opcional):
* Crea una función que sea capaz de procesar parámetros, pero que también
* pueda lanzar 3 tipos diferentes de excepciones (una de ellas tiene que
* corresponderse con un tipo de excepción creada por nosotros de manera
* personalizada, y debe ser lanzada de manera manual) en caso de error.
* - Captura todas las excepciones desde el lugar donde llamas a la función.
* - Imprime el tipo de error.
* - Imprime si no se ha producido ningún error.
* - Imprime que la ejecución ha finalizado.
'''
class StrTypeError(Exception):
    pass

def procesa(parametros: list):
    if len(parametros) < 1:
        raise IndexError() 
    
    elif parametros[0] == 0:
        raise ZeroDivisionError()
    
    elif type(parametros[1]) == str:
        raise StrTypeError ("Hay un texto en la 1ª posición")   
    

    print(parametros[1])
    print(3/parametros[0])
    print(parametros[1]+3)

Lista = [1, '2', 3, 4]

try:
    procesa(Lista)
except ZeroDivisionError as e:
    print("Has intentado dividir por 0")
except IndexError as e:
    print("Has accedido a una posicion que no existe")
except StrTypeError as e:
    print(f"{e}")
finally:    
    print(Lista)



