# ------ Ejercicio

a: int = 10
b: int = 0

try:
    c = a / b
except Exception as e:
    print(f"* Error inesperado: {e}, {type(e).__name__}")
finally:
    c = 0

print("a:", a, "b:", b, "c:", c)


# ------ Extra

class MyCustomException(Exception):
    pass


def exceptions(*params):
    if not all(isinstance(param, int) for param in params):
        raise TypeError()
    
    if params[1] == 0:
        raise ZeroDivisionError()
    
    if params[2] % 2 == 0:
        raise MyCustomException("El tercer elemento no puede ser par")

    print(params[0] / params[1])
    print(int(params[2] / 2) + 1)


try:
    exceptions(1, 2, 13)
except TypeError as e:
    print("* Error, todos los elementos deben ser números enteros")
except ZeroDivisionError as e:
    print("* Error, el segundo elemento no puede ser cero")
except MyCustomException as e:
    print("* Error, el tercer elemento no puede ser par")
except Exception as e:
    print("* Error inesperado:", e)
else:
    print("* No se presento ninguna excepción")
finally:
    print("* Programa finalizado")
