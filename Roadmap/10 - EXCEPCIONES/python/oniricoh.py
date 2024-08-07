
def division(x :int, y :int) ->float:
    try:
        return x/y
    except ZeroDivisionError:
        return "No se puede dividir entre 0"

print(division(10, 0))


###############################################################################
## DIFICULTAD EXTRA
###############################################################################

class DividendError(Exception):
    pass

def division(x: int, y: int):
    try:
        if y == 0:
            raise ZeroDivisionError("No se puede dividir por cero")
        elif x < y:
            raise DividendError("El dividendo debe ser mayor al divisor")
        result = x / y
        print("Resultado de la división:", result)
    except ZeroDivisionError as err:
        print("Error:", err)
    except DividendError as err:
        print("Error:", err)
    except Exception as e:
        print("Error inesperado:", e)
    else:
        print("No se ha producido ningún error.")
    finally:
        print("La ejecución ha finalizado.")

x = int(input("Introduce un valor para X: "))
y = int(input("Introduce un valor para Y: "))

division(x, y)
