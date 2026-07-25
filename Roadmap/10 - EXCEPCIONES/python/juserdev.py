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

'''
  ->  para el manejo de excepciones es mejor caputurar los errores en una varia como en el caso
        -> except ZeroDivisionError as e:
      de esta manera tenemos capturado el erro en la variable e y asi no se detiene el programa
      y muestra el error
        ->  division by zero
  
  ->  El bloque try se utiliza para el bloque que puede fallar
  ->  El bloque except captura y maneja los errores sin detener el programa
  ->  Es mejor capturar el error con "as e" para imprimi detalles del fallo
'''

def dividir(a,b):
  try:
    print(a/b)
    print("no se ha producido ningun error")
  except ZeroDivisionError as e:
    print("Error -> ", e)

dividir(10, 0)

my_list = [1,2,3,4]

def get_list(i):
  try:
    print(my_list[i])
  except IndexError as e:
    print("Error -> ", e)

get_list(4)


### EXTRA ###

class StrTypeError(Exception):
  pass

def get_errors(params: list):
  if len(params) < 3:
   raise IndexError()
  if params[1] == 0:
    raise ZeroDivisionError()
  if type(params[2] == str):
    raise StrTypeError("El tercer elemento no puede ser una cadera de texto")

  print(params[0])
  print(params[0]/params[1])
  print(params[0] + 5)


try:
  get_errors([1,2,"str",4])
except IndexError as e:
  print("El numero de elemtnos de la lista debe ser mayor que tres")
except ZeroDivisionError:
  print(" El segundo elemento de la lista no puede ser cero")
except StrTypeError as e:
  print(f"{e}")
except Exception as e:
  print(f"se ha producido un error inesperado: {e}")
else:
  print("No se ha producido ningun error")
finally:
  print("el programa finalizo sin deneterse")