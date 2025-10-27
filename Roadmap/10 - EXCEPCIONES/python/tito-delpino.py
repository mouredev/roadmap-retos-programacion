#  * EJERCICIO:
#  * Explora el concepto de manejo de excepciones según tu lenguaje.
#  * Fuerza un error en tu código, captura el error, imprime dicho error
#  * y evita que el programa se detenga de manera inesperada.
#  * Prueba a dividir "10/0" o acceder a un índice no existente
#  * de un listado para intentar provocar un error.

try:
  print(10 / 0)
except Exception as error:
  print(f"Se produjo un error: {error}")

listado = ["cabeza", "perro","caballo"]
try:
  print(listado[4])
except Exception as error2:
  print(f"Se produjo un error: {error2} ({type(error2).__name__})")

print('/' * 50)
#  * DIFICULTAD EXTRA (opcional):
#  * Crea una función que sea capaz de procesar parámetros, pero que también
#  * pueda lanzar 3 tipos diferentes de excepciones (una de ellas tiene que
#  * corresponderse con un tipo de excepción creada por nosotros de manera
#  * personalizada, y debe ser lanzada de manera manual) en caso de error.
#  * - Captura todas las excepciones desde el lugar donde llamas a la función.
#  * - Imprime el tipo de error.
#  * - Imprime si no se ha producido ningún error.
#  * - Imprime que la ejecución ha finalizado.

class Excepcion_personalizada(Exception):
  pass

def procesar_parametros(parametros: list):
  
  if len(parametros) < 3:
    raise IndexError()
  elif parametros[2] == 0:
    raise ZeroDivisionError()
  elif type(parametros[3]) == str:
    raise Excepcion_personalizada("El tercer numero no puede ser un string")

  print(parametros[4])
  print(parametros[0]/parametros[1])
  print(parametros[3] + 6)

try:
  procesar_parametros([0,1,2,3,4])
except IndexError as error3:
  print(f"Se produjo el error {type(error3).__name__}")
except ZeroDivisionError as error4:
  print(f"El tercer numero de la lista no puede ser un 0")
except Excepcion_personalizada as error4:
  print(f"{error4}")
except Exception as error5:
  print(f"Se produjo un error inesperado: {error5}")
else:
  print("No se produjo ningun error")
finally:
  print("Programa finalizado sin petar")