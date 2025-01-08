def div_0():
    while True:
        n = int(input('ingrese un numero: '))
        if n == 0:
            break
        try:
            print(n / 0)
        except ZeroDivisionError as e: print(f'Error: {e}')
    
div_0()


'''
EXTRA
'''

# Definición de una excepción personalizada
class MiExcepcionPersonalizada(Exception):
    def __init__(self, mensaje):
        super().__init__(mensaje)


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
        print(f"Error: {ve}\nTipo: {type(ve).__name__}")
    except IndexError as ie:
        print(f"Error: {ie}\nTipo: {type(ie).__name__}")
    except MiExcepcionPersonalizada as me:
        print(f"Error: {me}\nTipo: {type(me).__name__}")
    else:
        print("No se ha producido ningún error.")
    finally:
        print("La ejecución ha finalizado.")

try:
    procesar_parametros(0)
    procesar_parametros(1)
    procesar_parametros(2)
    procesar_parametros(3)
    procesar_parametros()
except Exception as e:
    print("Tipo de error:", type(e).__name__)
