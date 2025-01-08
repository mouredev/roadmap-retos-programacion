"""/*
 * EJERCICIO:
 * Explora el concepto de manejo de excepciones según tu lenguaje.
 * Fuerza un error en tu código, captura el error, imprime dicho error
 * y evita que el programa se detenga de manera inesperada.
 * Prueba a dividir "10/0" o acceder a un índice no existente
 * de un listado para intentar provocar un error.
 */"""

print("Ejercicio base:")
print("----------------")

# Excepciones, capturando un KeyError
db = {10:"Excepciones"}
def imprimir_clave(llave):
    try:
        dato = db[llave]
        print(f"El Ejercicio {llave} es {dato}")
    except KeyError as e:
        print(f"{llave} no esta en la DB\nError {e}")

# Pruebas
imprimir_clave(2)
imprimir_clave(10)
imprimir_clave(2)
print("----------------")

"""* DIFICULTAD EXTRA (opcional):
 * Crea una función que sea capaz de procesar parámetros, pero que también
 * pueda lanzar 3 tipos diferentes de excepciones (una de ellas tiene que
 * corresponderse con un tipo de excepción creada por nosotros de manera
 * personalizada, y debe ser lanzada de manera manual) en caso de error.
 * - Captura todas las excepciones desde el lugar donde llamas a la función.
 * - Imprime el tipo de error.
 * - Imprime si no se ha producido ningún error.
 * - Imprime que la ejecución ha finalizado."""


print("----------------")
print("Ejercicio extra")
print("----------------")

# Ecepción Propia
class Error_letra(Exception):
    def __init__(self,letra):
        self.mensaje = f"Letra Prohibida: {letra}"
        super().__init__(self.mensaje)
        
def analizador(letra):
    # generar excepción
    resultado = letra.upper()
    
    # 2º excepción
    second = letra[1]
    
    # 3º excepción
    if second.lower() == "ñ":
        raise Error_letra(letra)
    print("Analizador Exitoso")

# He necesitado esta función para poder anidar las excepciones y no repetir bucles de try except
def check_analizador(letra):
    try:
        analizador(letra)
        
    except AttributeError as e:
        print(f"Error_1: {e}")
        
    except IndexError as e:
        print(f"Error_2: {e}")
        
    except Error_letra as e:
        print(f"Error_3: {e}")
        
    except Exception as e:
        print(e)
        
    else:
        print("No hubo Errores")
        
    finally:
        print("Proceso Ejecutado\n")
    

# Pruebas
'''Error_1'''
check_analizador(7)
    
'''Error_2'''
check_analizador("l")
    
'''Error_3'''
check_analizador("uñ")

'''Correcto'''
check_analizador("ul")

print("----------------")