""" #10 EXCEPCIONES """

# --------------- EJERCICIO -----------------

print("-------------- EJERCICIO --------------")

try:
    # al ingresar una letra, da error ValueError
    n1 = int(input("Ingresa un numero: "))
    n2 = int(input("Ingresa otro numero: "))
except ValueError as e:
    print("Debes ingresar un numero")

print("El programa continua trabajando")


def division(number1, number2):
    return number1/number2


try:
    result = division(n1, n2)
except ZeroDivisionError as e:
    print(f"Error inesperado: {e}")
except NameError as e:
    print("ingresaste letras en la division")
else:
    print(result)

# ------------------- EXTRA ---------------------

print("-------- EJERCICIO EXTRA -----------")


class PersonalizedError(Exception):
    """ Excepcion personalizada """

    def __init__(self, msg, code_error):
        self.message = msg
        self.code_error = code_error


def prosessing_params(*params):
    """ Prosesando parametros """
    if len(params) < 1:
        raise PersonalizedError("Tu lista no puede estar vacía", 100)
    if len(params) > 10:
        raise PersonalizedError(
            "Excediste el limite de articulos de tu lista", 200)


try:
    # prosessing_params("Leche", "Harina", "Aceite")
    prosessing_params()
except PersonalizedError as e:
    print(f"{e.message} - Codigo de error: {e.code_error}")
else:
    print("Tu lista ha sido guardada correctamente")
finally:
    print("Nos vemos pronto")
