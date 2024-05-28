 # EJERCICIO:
 # Explora el concepto de manejo de excepciones según tu lenguaje.
 # Fuerza un error en tu código, captura el error, imprime dicho error
 # y evita que el programa se detenga de manera inesperada.
 # Prueba a dividir "10/0" o acceder a un índice no existente
 # de un listado para intentar provocar un error.
 
 # DIFICULTAD EXTRA (opcional):
 # Crea una función que sea capaz de procesar parámetros, pero que también
 # pueda lanzar 3 tipos diferentes de excepciones (una de ellas tiene que
 # corresponderse con un tipo de excepción creada por nosotros de manera
 # personalizada, y debe ser lanzada de manera manual) en caso de error.
 # - Captura todas las excepciones desde el lugar donde llamas a la función.
 # - Imprime el tipo de error.
 # - Imprime si no se ha producido ningún error.
 # - Imprime que la ejecución ha finalizado.
 

try:
    #Descomentar una linea para ver su error
    #print(var)
    #print(0/0)  
    #print(1+"2")
    #print([1,2,3,4][4]) 
    #import modulo
    #from math import po
    #print(type.uno)  
    print(int("hola"))
     
except Exception as error:
    print(f"Se ha encontrado un error del tipo: {error}")
    
#Extra

class ToMuchError(Exception):
    pass

def num_func (a,b,c):
    
    if(c>3):
        raise ToMuchError("El valor de c es demasiado grande")
    print(a+b)
    print(a/c)
   
        
    
try:
    #num_func (1,2,3)
    #num_func (1,2,0)
    #num_func ("1",2,3)  
    num_func (1,2,5)
      
    
except ZeroDivisionError:
    print("No se puede dividir por cero")
    
except TypeError:
    print("Los datos a y b tienen que ser del tipo int ")

except Exception as e:
    print(f"Se ha producido un error inesperado: {e}")
    
else:
    print("El programa a fianlizado sin errores")
    
finally:
    print("El programa a fianlizado.")