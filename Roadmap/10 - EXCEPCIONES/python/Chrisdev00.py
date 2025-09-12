"""
EJERCICIO:
Explora el concepto de manejo de excepciones según tu lenguaje.
Fuerza un error en tu código, captura el error, imprime dicho error
y evita que el programa se detenga de manera inesperada.
Prueba a dividir "10/0" o acceder a un índice no existente
de un listado para intentar provocar un error.

DIFICULTAD EXTRA (opcional):
Crea una función que sea capaz de procesar parámetros, pero que también
pueda lanzar 3 tipos diferentes de excepciones (una de ellas tiene que
corresponderse con un tipo de excepción creada por nosotros de manera
personalizada, y debe ser lanzada de manera manual) en caso de error.
- Captura todas las excepciones desde el lugar donde llamas a la función.
- Imprime el tipo de error.
- Imprime si no se ha producido ningún error.
- Imprime que la ejecución ha finalizado. 

"""

# En Python, el manejo de excepciones es una técnica que te permite lidiar con situaciones excepcionales 
# o errores que pueden ocurrir durante la ejecución de un programa. 
# Las excepciones pueden ser errores de sintaxis, errores de tiempo de ejecución, 
# errores de lógica del programa, entre otros.

# El manejo de excepciones en Python se logra utilizando bloques try, except, finally y, 
# opcionalmente, else.

try:
    name = input('Enter your name:')
    year_born = input('Year you born:')
    age = 2019 - year_born
    print(f'You are {name}. And your age is {age}.')
except TypeError:
    print('Type error occur')
except ValueError:
    print('Value error occur')
except ZeroDivisionError:
    print('zero division error occur')
else:
    print('Este bloque se ejecuta si no se lanza ninguna excepcion en el bloque try')
finally:
    print('Esto se ejecuta siempre')

# Dividiendo entre 0

try:
    x = 1 / 0  
except ZeroDivisionError as e:    
    print("Ha ocurrido un error:", e)  
else:
    print("No se ha producido ninguna excepción.")
finally:
    print("Esto se ejecuta siempre.")  # Este bloque se ejecuta siempre, haya excepción o no

# acceder a un índice no existente en una lista para provocar un error y luego maneja esa excepción:
    
try:
    lista = [1, 2, 3]
    indice = lista[5]  
except IndexError as e:
    print("Ha ocurrido un error:", e)  
else:
    print("No se ha producido ninguna excepción.")
finally:
    print("Esto se ejecuta siempre.")  


######## ---------------------- EXTRA -------------------------- ###############
    

class MiExcepcionPersonalizada(Exception):
    def __init__(self, mensaje):
        self.mensaje = mensaje

def procesar_parametros(parametros):
    try:
        if len(parametros) < 3:
            raise ValueError("Se necesitan al menos 3 parámetros")
        
        if not isinstance(parametros[0], int) or not isinstance(parametros[1], int) or not isinstance(parametros[2], int):
            raise TypeError("Los parámetros deben ser enteros")

        if parametros[0] + parametros[1] <= parametros[2]:
            raise MiExcepcionPersonalizada("La suma de los dos primeros parámetros no es mayor que el tercero")
                
        print("No se ha producido ningún error")

    except ValueError as ve:
        print("Error:", ve)
    except TypeError as te:
        print("Error:", te)
    except MiExcepcionPersonalizada as mep:
        print("Error personalizado:", mep.mensaje)
    except Exception as e:
        print("Error desconocido:", e)
    finally:
        print("La ejecución ha finalizado")


try:
    parametros = [1, 2, '3']
    procesar_parametros(parametros)
    parametros_dos = [1, 4, 8]
    procesar_parametros(parametros_dos)
    parametros_tres = [1, "a"]
    procesar_parametros(parametros_tres)
except Exception as e:
    print("Excepción capturada:", type(e).__name__)


