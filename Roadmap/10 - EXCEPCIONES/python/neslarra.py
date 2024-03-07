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

print("""
Una excepción es un error detectado en tiempo de ejcución, es decir, el programa
pasó OK la revisión sintáctica pero aún así al ejecutar encontró una falla.
Por ejemplo, tenemos un programa que pide ingresar un divisor:
...
divisor = input("Ingrese divisor: ")
print(f"{123 // int(divisor)}")
...
El programa es sintácticamente correcto, aún así, si ingreso una "a" entonces
me va a devolver un error "ValueError", pero sin ingreso un "0" el devolverá
un error "ZeroDivisionError" 

Éstas son excepciones predefindas en cada clase. Pero puede que tengamos que controlar algún tipo
"error lógico" o "de regla de negocio" para lo cual podemos definir excepciones propias.

Por ejemplo, supongamos que el divisor requerido tiene que se rmayor a 3 y menor a 9: creo una
clase que herede Exception a la cual la invoco con "raise" cuando encuentre que esta nueva regla
no se cumple.

class FueraDeRangoError(Exception):
    def __init__(self):
        self.message = "Solo valores entre 3 y 9 (exclusive)."

    def __str__(self):
        return self.message

Probar "ingresando" una letra, un 0, un 2 (o un 10) y luego, para el caso, un 6.

""")


class FueraDeRangoError(Exception):
    def __init__(self):
        self.message = "Solo valores entre 3 y 9 (exclusive)."

    def __str__(self):
        return self.message


def funcion(divisor):
    resto = 123 // int(divisor)
    if not (3 < int(divisor) < 9):
        raise FueraDeRangoError
    return resto


while True:
    try:
        divisor = input("Ingrese divisor: ")
        resto = funcion(divisor)
    except Exception as e:
        print(f"Te topaste con la excepción {e.__class__.__name__} => {e}")
    else:
        print(f"Resto = {resto}")
        break

print(f"\n{'#' * 50}\nDificultad Extra\n{'#' * 50}", end="\n\n")
print(f"Los lineamientos de la dificultad extra están incluídos en el ejemplo de la explicación.")
