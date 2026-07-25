"""
* EJERCICIO:
 * Explora el concepto de manejo de excepciones según tu lenguaje.
 * Fuerza un error en tu código, captura el error, imprime dicho error
 * y evita que el programa se detenga de manera inesperada.
 * Prueba a dividir "10/0" o acceder a un índice no existente
 * de un listado para intentar provocar un error.
"""

def divide(number_1: int, number_2: int)-> float:
    try:
        return number_1 / number_2
    except ZeroDivisionError as error:
        print (f"No se puede dividir entre 0: Error = {error}")

divide(9, 0)

def get_by_index(index: int):

    my_list = ["Python", "Rust", "c#", "Kotlin"]

    try:
        return my_list.pop(index)
    except IndexError as error:
        print(f"Índice fuera de rango. Error: {error}")

print(get_by_index(4))


"""
* DIFICULTAD EXTRA (opcional):
 * Crea una función que sea capaz de procesar parámetros, pero que también
 * pueda lanzar 3 tipos diferentes de excepciones (una de ellas tiene que
 * corresponderse con un tipo de excepción creada por nosotros de manera
 * personalizada, y debe ser lanzada de manera manual) en caso de error.
 * - Captura todas las excepciones desde el lugar donde llamas a la función.
 * - Imprime el tipo de error.
 * - Imprime si no se ha producido ningún error.
 * - Imprime que la ejecución ha finalizado.
"""

class InvalidEmail(Exception):
    def __init__(self, mensaje):
        super().__init__(mensaje)


def validate_email(email: str):
    email = email.split("@")
    if len(email) != 2:
        return False
    email = email[1].split(".")
    if len(email) != 2:
        return False
    return True


def sign_up():
    rewards = ["Coupon 10€", "Coupon 5€", "Coupon 20€"]

    name = input("Introduce tu nombre: ")
    age = int(input("Introduce tu edad: "))
    email = input("Introduce tu email: ")
    if not validate_email(email):
        raise InvalidEmail("Formato de email incorrecto.")
    index = int(input("Dame un número del 1 al 3 para conseguir tu premio de bienvenida: "))
    if index < 1 or index > len(rewards):
        raise IndexError("Número fuera de rango. Debe estar entre 1 y 3.")
    return rewards[index - 1]



try:
    reward = sign_up()

except ValueError as error:
    print(f"Tipo de error: {type(error).__name__}")
    print(f"La edad debe ser un número entero. Error: {error}")

except IndexError as error:
    print(f"Tipo de error: {type(error).__name__}")
    print(f"Debes introducir un índice entre 1 y 3. Error: {error}")

except InvalidEmail as error:
    print(f"Tipo de error: {type(error).__name__}")
    print(error)

except Exception as error:
    print(f"Se ha producido un error inesperado: {error}")

else:
    print(f"Todos los datos correctos. Tu recompensa de bienvenida es {reward} ")

finally:
    print("Proceso finalizado")


