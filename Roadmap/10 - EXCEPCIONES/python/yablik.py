try:
    # Intenta ejecutar código propenso a errores
    resultado = 10 / 0  # División por cero
    lista = [1, 2, 3]
    elemento = lista[5]  # Acceso a un índice no existente
except ZeroDivisionError as error:
    # Captura y maneja el error de división por cero
    print("Error de división por cero:", error)
except IndexError as error:
    # Captura y maneja el error de índice fuera de rango
    print("Error de índice fuera de rango:", error)
except Exception as error:
    # Captura y maneja otros errores no específicos
    print("Error inesperado:", error)
else:
    # Se ejecuta si no se produce ninguna excepción
    print("Operación exitosa.")
finally:
    # Se ejecuta siempre, independientemente de si se produce una excepción o no
    print("Fin del programa.")

#Dificultad extra

# Definición de excepción personalizada
class MiExcepcionPersonalizada(Exception):
    def __init__(self, mensaje):
        super().__init__(mensaje)

# Función que procesa parámetros y lanza excepciones
def procesar_parametros(parametro):
    try:
        if parametro == 1:
            raise ValueError("¡Este es un valor incorrecto!")
        elif parametro == 2:
            raise IndexError("¡Índice fuera de rango!")
        elif parametro == 3:
            raise MiExcepcionPersonalizada("¡Esto es una excepción personalizada!")
        else:
            print("Parámetro válido:", parametro)
    except ValueError as ve:
        print("Error:", ve)
    except IndexError as ie:
        print("Error:", ie)
    except MiExcepcionPersonalizada as me:
        print("Error:", me)
    else:
        print("No se ha producido ningún error.")
    finally:
        print("La ejecución ha finalizado.")

# Llamada a la función con manejo de excepciones
try:
    procesar_parametros(0)
    procesar_parametros(1)
    procesar_parametros(2)
    procesar_parametros(3)
except Exception as e:
    print("Tipo de error:", type(e).__name__)
