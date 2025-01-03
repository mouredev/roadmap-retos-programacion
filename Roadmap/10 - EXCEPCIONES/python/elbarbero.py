"""
 * EJERCICIO:
 * Explora el concepto de manejo de excepciones según tu lenguaje.
 * Fuerza un error en tu código, captura el error, imprime dicho error
 * y evita que el programa se detenga de manera inesperada.
 * Prueba a dividir "10/0" o acceder a un índice no existente
 * de un listado para intentar provocar un error.
 *
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
import random

class MyCustomException(Exception):
    def __init__(self, msg):
        self.message = msg
    
    def __str__(self):
        return f"{self.message}"


def myFunction():
    try:
        value = int(input("Introduce texto: "))
        if value == 0:
            raise MyCustomException("No se puede dividir por cero chaval")
        l = ["a", 3]
        r_value = random.choice(l)
        print(4 + 5 / (value + r_value))
    except ValueError as ex:
        print("Debe introducir un número\n" + str(ex))
    except TypeError as ex:
        print("Debe introducir un número para realizar la operación\n" + str(ex))
    else:
        print("Ha salido todo bien")
    


if __name__ == "__main__":

    try:
        print(10/0)
    except ZeroDivisionError as ex:
        print(ex)
    
    myFunction()

