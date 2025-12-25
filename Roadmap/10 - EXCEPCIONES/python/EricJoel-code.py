## Excepciones

try:
    print(10/0)  # Esto generará una excepción de división por cero
    
    print([1, 2, 3][5])  # Esto generará una excepción de índice fuera de rango
    
except Exception as e:
    print(f"Se ha producido un error: {e} ({type(e).__name__})")
    
    
## Extra

"""
Crea una función que sea capaz de procesar parámetros, pero que también pueda lanzar 3 tipos diferentes de excepciones (una de ellas tiene que corresponderse con un tipo de excepción creada por nosotros de manera personalizada, y debe ser lanzada de manera manual) en caso de error.
- Captura todas las excepciones desde el lugar donde llamas a la función.
- Imprime el tipo de error.
- Imprime si no se ha producido ningún error.
- Imprime que la ejecución ha finalizado.""" 

class MiExcepcionPersonalizada(Exception):
    pass

def procesar_parametros(param):
    if not isinstance(param, int):
        raise TypeError("El parámetro debe ser un entero.")
    if param < 0:
        raise ValueError("El parámetro no puede ser negativo.")
    if param == 42:
        raise MiExcepcionPersonalizada("El parámetro no puede ser 42.")
    return param * 2 

try:
    resultado = procesar_parametros(42)
    print(f"Resultado: {resultado}")
except TypeError as te:
    print(f"Error de tipo: {te} ({type(te).__name__})")
except ValueError as ve:
    print(f"Error de valor: {ve} ({type(ve).__name__})")
except MiExcepcionPersonalizada as me:
    print(f"Error personalizado: {me} ({type(me).__name__})")
else:
    print("No se ha producido ningún error.")
finally:
    print("El programa finaliza sin detenerse.")
    
    