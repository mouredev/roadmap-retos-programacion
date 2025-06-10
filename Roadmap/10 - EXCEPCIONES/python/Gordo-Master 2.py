"""
Excepciones
"""

try:
    x = 10 / '0'
except ZeroDivisionError:
    print("Error de división con 0")
except TypeError as ty:
    print(f"Error de tipo: {ty}")
else:
    print(x)
finally:
    print("Aquí termina el manejo de las excepciones")

try:
    print(10/1)
    print([1, 2, 3, 4][4])
except Exception as e:
    print(f"Se ha producido un error: {e} ({type(e).__name__})")


"""
Extra
"""
### Debe ser entero, positivo y mayor que 0
def condition_ver(number):
    if type(number) is float:
        raise Exception(f"No se acepta valores flotantes, [{number}] es un valor flotante")
    if not type(number) is int:
        raise TypeError(f"El tipo de dato debe ser un int, [{number}] no lo es")
    if not number > 0:
        raise ValueError(
            f"El número no puede ser negativo ni 0, [{number}] no cumple con esta condición"
            )
        


def geometric_progression(first_number,reason,position):
    try:    
        condition_ver(first_number)
        condition_ver(reason)
        condition_ver(position)
    except TypeError as e:
        print(f"{type(e).__name__}: {e}")
    except ValueError as e:
        print(f"{type(e).__name__}: {e}")
    except Exception as e:
        print(f"{type(e).__name__}: {e}")
    else:
        s = first_number
        for i in range(1,position):
            s *= reason
        print (f"El valor en la {position}º de la progresión geometrica, con valor inicial: {first_number}, y razon: {reason} es: {s}")
    finally:
        print("Ha terminado el programa")


# geometric_progression(1,0,3)

class StrTypeError(Exception):
    pass

def process_params(parameters: list):

    if len(parameters) < 3:
        raise IndexError()
    elif parameters[1] == 0:
        raise ZeroDivisionError()
    elif type(parameters[2]) == str:
        raise StrTypeError("El tercer elemento no puede ser un cadena de texto")

    print(parameters[2])
    print(parameters[0]/parameters[1])
    print(parameters[2] + 5)

try:
    process_params([1,2,3,4])
except IndexError as e:
    print("El número de elementos de la lista debe ser mayor que dos")
except ZeroDivisionError as e:
    print("El segundo elemento de la lista no puede ser un cero (0)")
except StrTypeError as e:
    print(f"{type(e).__name__} : {e} ")
except Exception as e:
    print(f"Se ha producido un error inesperado: {e} ({type(e).__name__})")
else:
    print("No se ha producido ni un error")
finally:
    print("El programa finaliza sin deterse")

