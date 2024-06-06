# #10 EXCEPCIONES

""" * EJERCICIO:
 * Explora el concepto de manejo de excepciones según tu lenguaje.
 * Fuerza un error en tu código, captura el error, imprime dicho error
 * y evita que el programa se detenga de manera inesperada.
 * Prueba a dividir "10/0" o acceder a un índice no existente
 * de un listado para intentar provocar un error.
"""

# Error de división por cero
print ("-"*60)
try:                
    div = 10/0  

except ZeroDivisionError as zde :                     # Se pasa el error capturado
    print (zde," Error")


# Error de tipo
print ("-"*60)

try:                        # Con try se prueba un bloque de código para buscar errores"Hello
    x= "Hello"

    if not type(x) is int:
        raise TypeError("Error ,esto no es un entero") # Captura el error
        
    else:
        print (x)

except TypeError as zde :                     # Se pasa el error capturado
    print (zde)



print ("-"*60)

try:

    lista = [1,2,3,4]
    print (lista[5])

except IndexError as ide:
    print ("Error de tipo:",ide)
finally:                    
    print ("Este bloque se ejecuta siempre")


print ("-"*60)

"""
 * DIFICULTAD EXTRA (opcional):
 * Crea una función que sea capaz de procesar parámetros, pero que también
 * pueda lanzar 3 tipos diferentes de excepciones (una de ellas tiene que
 * corresponderse con un tipo de excepción creada por nosotros de manera
 * personalizada, y debe ser lanzada de manera manual) en caso de error.
 * - Captura todas las excepciones desde el lugar donde llamas a la función.
 * - Imprime el tipo de error.
 * - Imprime si no se ha producido ningún error.
 * - Imprime que la ejecución ha finalizado. 
"""
class StrError (Exception):
     pass

def process_parameters(a:list):
       
        if type(a[0])==str or type(a[1])==str:
             raise StrError("Error, no se pueden dividir strings")
        elif len(a)>2:
             raise Exception ("El programa sólo sirve para dividir 2 números")
        elif a[1]==0:
             raise ZeroDivisionError("No se puede dividir por 0")
      
        return (a[0]/a[1])



try:

    #print (process_parameters([3,0])) Error de división por 0
    # print (process_parameters(["a",3])) Error no se pueden dividir strings
    #print (process_parameters([3,2,5])) Error de programa
    print (process_parameters([10,5])) # El programa corre correctamente

except ZeroDivisionError as se:
    print ("Error de tipo:", se)
except StrError as st:
    print (st)
except Exception as e:
    print (e)

else:
     print ("No se ha producido ningún error")

finally:
     print ("La ejecución ha finalizado")



