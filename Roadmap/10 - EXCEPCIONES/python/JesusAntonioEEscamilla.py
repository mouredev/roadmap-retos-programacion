# #10 - Python -> Jesus Antonio Escamilla

"""
EJERCIÓ
"""
def division_by_zero():    
    try:
        print(10/0)
    except Exception as e:
        print(f"Se encontró un error: {e} {(type(e).__name__)}")

def access_index_invalid():
    try:
        print([1,2,3,4][4])
    except Exception as e:
        print(f"Se encontró un error: {e} {(type(e).__name__)}")

# Ejemplo
print("\nIntentando dividir por cero:")
division_by_zero()
    
print("\nIntentando acceder a un índice inválido:")
access_index_invalid()



"""
EXTRA
"""
class exceptionPersonalizada(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

def procesar_lista(lista):
    if len(lista) < 3:
        raise TypeError("Tiene que ser mas de 3 elementos")

    if not all(isinstance(x, (int, float)) for x in lista):
        raise ValueError("Los parámetros tienen que ser del mismo tipo")

    if not lista:
        raise exceptionPersonalizada("La lista no es válida")

    print('La ejecución ha finalizado sin errores')

print("\nExtra")
try:
    procesar_lista([1, 2, 3, 4])
except Exception as e:
    print(f"Ocurrió un error: {e}")
finally:
    print("Programa Finalizado")