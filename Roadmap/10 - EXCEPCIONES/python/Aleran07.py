# 10

# Manejo basico de excepciones
try:
    x = 10 / 0
except ZeroDivisionError:
    print("No se puede dividir por cero.")

# Capturar cualquier tipo de error
try:
    num = int(input("Ingresa un número: "))
except Exception as e:
    print("Hubo un error:", e)

# Manejo con else
try:
    x = 10 / 2
except ZeroDivisionError:
    print("Error")
else: # solo se ejecuto si no hubo error
    print("Todo salió bien, x es:", x)

# Manejo con finally
try:
    archivo = open("test.txt")
except FileNotFoundError:
    print("Archivo no encontrado")
finally: # Siempre se ejecuta, haya error o no
    print("Intento de abrir archivo finalizado.")


"""* Crea una función que sea capaz de procesar parámetros, pero que también
 * pueda lanzar 3 tipos diferentes de excepciones (una de ellas tiene que
 * corresponderse con un tipo de excepción creada por nosotros de manera
 * personalizada, y debe ser lanzada de manera manual) en caso de error.
 * - Captura todas las excepciones desde el lugar donde llamas a la función.
 * - Imprime el tipo de error.
 * - Imprime si no se ha producido ningún error.
 * - Imprime que la ejecución ha finalizado."""

class MiPrimerError(Exception):
    pass # Excepcion creada por mi para mostrar que el saldo es insuficiente

saldo_en_la_cuenta = 100

def saldo_insuficiente(saldo):
    # 1 error saldo negativo
    if saldo < 0:
        raise ValueError("El saldo no puede ser negativo")
    
    # 2 error saldo no es un numero
    if not isinstance(saldo, (int, float)):
        raise TypeError("El saldo debe ser un numero")
    
    # 3 error saldo insuficiente
    if saldo > saldo_en_la_cuenta:
        raise MiPrimerError("El saldo supera al valor de la cuenta")
    
    return saldo + saldo_en_la_cuenta

try:
    cuenta = saldo_insuficiente(150)
    print("Nuevo saldo en cuenta: ", cuenta)
except Exception as e:
    print("Se produjo un error de tipo:", type(e).__name__)
    print("Mensaje del error:", e)
else:
    print("No se produjo ningun error")
finally:
    print("La ejecucion a finalizado")
