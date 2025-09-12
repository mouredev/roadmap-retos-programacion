# #10 EXCEPCIONES
#### Dificultad: Media | Publicación: 04/03/24 | Corrección: 11/03/24

## Ejercicio


'''
* EJERCICIO:
 * Explora el concepto de manejo de excepciones según tu lenguaje.
 * Fuerza un error en tu código, captura el error, imprime dicho error
 * y evita que el programa se detenga de manera inesperada.
 * Prueba a dividir "10/0" o acceder a un índice no existente
 * de un listado para intentar provocar un error.
'''
def main():
    while True:
        print("Ingresa dos numeros a dividir")
        a = int(input("Ingresa un numero: "))
        b = int(input("Ingresa otro numero: "))
        
        try:
            resultado = a / b
            print(resultado)
            if resultado != 0:
                break
        except Exception as e: 
            print(f"{e}")
            print("El divisor no puede ser 0")
    print("Gracias! :D")


    '''
    * DIFICULTAD EXTRA (opcional):
    * Crea una función que sea capaz de procesar parámetros, pero que también
    * pueda lanzar 3 tipos diferentes de excepciones (una de ellas tiene que
    * corresponderse con un tipo de excepción creada por nosotros de manera
    * personalizada, y debe ser lanzada de manera manual) en caso de error.
    * - Captura todas las excepciones desde el lugar donde llamas a la función.
    * - Imprime el tipo de error.
    * - Imprime si no se ha producido ningún error.
    * - Imprime que la ejecución ha finalizado. `
    '''
    # Creamos nuestro propio tipo de error, que hereda el comportamiento de Exception
    class StrTypeError(Exception):
        pass

    def my_function(parameters):

        my_list = parameters

        if len(my_list) < 4:
            raise IndexError()
    
        elif my_list[1] == 0:
            raise ZeroDivisionError()
        
        elif type(my_list[2]) == str:
            raise StrTypeError("El tercer elemento no puede ser una cadena de texto.")
           
        
        print(my_list[3])
        print(my_list[4]/my_list[1])
        print(my_list[2] + my_list[4])

    try:
        my_function([1, 2, 3, 4, 5])
    except IndexError as e:
        print(f"El numero de indices no puede ser menor a 4 ({e})")
    except ZeroDivisionError as e:
        print(f"El segundo elemento no puede ser cero: ({type(e).__name__})")
    except StrTypeError as e:
        # Nuestro error personalizado ya viene con mensaje
        print(e)
    except Exception as e:
        print(f"Ha ocurrido un error inesperado ({e}). Trabajamos en ello")
    else:
        print("El programa se ejecuto con normalidad")
    finally:
        print("Fin del programa")

    

  

    

if __name__=="__main__":
 main()
