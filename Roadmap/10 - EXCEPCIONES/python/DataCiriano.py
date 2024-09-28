"""
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
"""

def division():

    try:
        denominator = int(input("Enter a number for the denominator: "))
        divider = int(input("Enter a number for the divider "))
        
        result = denominator / divider
        
        return result
            
    except ZeroDivisionError as e:
        print(f"Error: {e}")

    except ValueError as e:
        print(f"Error: {e}")
        
        
print(division())

#-----EXTRA-----

#Function to calculate the division by 2 of the number 10. If it is not divided by 2, it throws a custom error

class MyPersonalException(Exception):
    pass

def process_parameter(parameter):
    try:
        
        result = 10 / parameter
        
        if parameter != 2:
            raise MyPersonalException("Error: The parameter in not 2")
        
        print("Successful operation. Result:", result)
    
    except ZeroDivisionError as e:
        print("Error: ZeroDivisionError -", e)
    except MyPersonalException as e:
        print("Custom error -", e)
    except Exception as e:
        print("General error -", e)
    else:
        print("No errors detected.")
    finally:
        print("The execution has finished.")


try:
    parameter = int(input("Enter a number to divide 10: "))
    process_parameter(parameter)
except ValueError as e:
    print(f"Error: ValueError- {e}")
    print("Please enter a valid number.")
except Exception as e:
    print("Calling function error -", e)
