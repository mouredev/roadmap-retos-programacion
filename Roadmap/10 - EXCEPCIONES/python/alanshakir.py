"""
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
"""

#SyntaxError: error de sintaxis

#Excepciones

#ZeroDivisionError
#NameError
#TypeError
#ValueError
#RuntimeError
"""
Formato de las excepciones:
    try:
    
    except:
    
    else:
    
    finally:
    try y except son primordiales
    else y finally no son tan necesarios, va a depender de lo que se esta buscando
"""

#ValueError
while True:
    try: 
        my_variable = int(input("introduzca un valor numerico: "))
        break
    except ValueError:
        print("No ha ingresado un valor numerico")

#ZeroDivisionError, TypeError, NameError
try: 
    my_variable = 10/0
    #my_variable = 10 + "20" #si descomentas ingresa al TypeError
    #my_variable = 20 + name*2 #si descomentas ingresa al NameError
    #my_variable_list = [5, 26, "hola", "python", "retos programacion"] #si descomentas ingresa al IndexError
    #print(my_variable_list[5]) #si descomentas ingresa al IndexError
except ZeroDivisionError:
    print("No se puede dividir entre cero")
except TypeError:
    print("El tipo de datos no son correctos")
except NameError:
    print("variable no esta definida")
except IndexError:
    print("El indice esta fuera de rango")

#captura el error
try:
    my_variable = 25
    my_variable_two = "20"
    print(my_variable - my_variable_two)
except Exception as error:
    print("Se ha producido un error: ", type(error))


#Extra

class ErrorPersonalizado(Exception):
    pass



def manejo_except(my_list_param: list):
    
    if my_list_param[1] == 0:
        raise ZeroDivisionError("El segundo valor no puede ser Cero(0)")
    elif len(my_list_param) < 3:
        raise IndexError("La lista debe contener mas de 3 elementos")
    else:
        if type(my_list_param[0]) == str or type(my_list_param[1]) == str or type(my_list_param[2]) == str:
                raise ErrorPersonalizado("Debe ser una lista numerica")
                
      
try:
    manejo_except([2 , 6, 5])
except Exception as error:
    print("Ha ocurrido un error de tipo: ", type(error))
else:
    print("No se ha producido ningun error, la ejecucion continua")
finally:
    print("La ejecucion a finalizado")
