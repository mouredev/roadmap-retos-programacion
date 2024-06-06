# Teoría

# Las excepciones en Python son eventos que ocurren durante la ejecución de un programa y que 
# interrumpen el flujo normal de ejecución. Pueden ser causadas por errores de sintaxis, 
# errores durante la ejecución del programa o condiciones inesperadas que hacen que el 
# programa no pueda continuar su ejecución normal.

# Para controlar las excepciones en Python, se utiliza el bloque `try` junto con uno o más 
# bloques `except`. El código que puede generar una excepción se coloca dentro del bloque 
# `try`, y el código que maneja la excepción se coloca dentro del bloque `except`. Si se 
# produce una excepción dentro del bloque `try`, Python busca un bloque `except` cuyo tipo de 
# excepción coincida con la excepción producida. Si encuentra uno, ejecuta el código dentro de 
# ese bloque `except`. Si no se encuentra ningún bloque `except` adecuado, la excepción se 
# propaga hacia arriba en la pila de llamadas.

#Aquí tienes un ejemplo de cómo se controlan las excepciones en Python:
def example():
    try:
        # Código que puede generar una excepción
        numero = int(input("Ingrese un número: "))
        resultado = 10 / numero
        print("El resultado es:", resultado)

    except ValueError:
        # Manejo de la excepción ValueError (cuando se ingresa un valor no válido)
        print("Error: Por favor ingrese un número válido.")

    except ZeroDivisionError:
        # Manejo de la excepción ZeroDivisionError (cuando se intenta dividir por cero)
        print("Error: No se puede dividir por cero.")

    except Exception as e:
        # Manejo de cualquier otra excepción no especificada
        print("Se produjo un error:", e)

    else:
        # Se ejecuta si no se produce ninguna excepción
        print("No se produjeron errores.")

    finally:
        # Se ejecuta siempre, sin importar si se produjo una excepción o no
        print("Finalizando programa.")

# En este ejemplo, el bloque `try` contiene el código que puede generar una excepción 
# (división por cero o conversión de cadena a entero). Los bloques `except` manejan diferentes 
# tipos de excepciones que pueden ocurrir. El bloque `else` se ejecuta si no se produce 
# ninguna excepción, y el bloque `finally` se ejecuta siempre, sin importar si se produce una 
# excepción o no.


# Ejercicio
def ejercicio_1():
    mi_lista=[1,2,3]

    try:
        print('\n[+] Imprimiendo elemento de la lista:')
        print(mi_lista[7])
    except IndexError as error:
        print(f'[!] Indice incorrecto: {error}')
    finally:
        print('[+] Programa finalizado correctamente.\n')

def ejercicio_2():
    try:
        print('\n[+] Dividiendo entre 0:')
        print(10/0)
    except ZeroDivisionError as error:
        print(f'[!] No se puede dividir entre 0: {error}')
    finally:
        print('[+] Programa finalizado correctamente.\n')

ejercicio_1()
ejercicio_2()

# Extra
class MiExcepcionPersonalizada(Exception):
    pass

def ejercicio_extra(parametro):
    try:
        if not isinstance(parametro, int):
            raise TypeError('El parametro debe ser un número entero.')
        elif parametro == 0:
            raise ValueError('El parametro no puede ser cero.')
        elif parametro < 0:
            raise MiExcepcionPersonalizada('El parametro no puede ser negativo.')
        else:
            print("Procesamiento exitoso.")
    
    except TypeError as error:
        print(f'[!] Error: {error}')
    except ValueError as error:
        print(f'[!] Error: {error}')
    except Exception as error:
        print(f'[!] Error: {error}')
    else:
        print("No se produjeron errores.")
    finally:
        print("Finalizando ejecución.")

try:
    ejercicio_extra("texto")
    print('')
    ejercicio_extra(0)
    print('')
    ejercicio_extra(10)
    print('')
    ejercicio_extra(-10)
    print('')

except Exception as e:
    print("Se produjo un error:", e)
finally:
    print("Ejecución finalizada.")
