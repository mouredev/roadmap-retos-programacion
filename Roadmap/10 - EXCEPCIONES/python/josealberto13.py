""" EJERCICIO:
 * Explora el concepto de manejo de excepciones según tu lenguaje.
 * Fuerza un error en tu código, captura el error, imprime dicho error
 * y evita que el programa se detenga de manera inesperada.
 * Prueba a dividir "10/0" o acceder a un índice no existente
 * de un listado para intentar provocar un error."""

def dividir():
    while True:
        n1 = int(input("Ingresa un numero para dividir: "))
        n2 = int(input("Ingresa el numero divisor: "))
        try:
            div = n1 / n2
            return div
        except:
            print("¡ERROR! No se puede dividir entre 0")

print(dividir())


""" Clase de Brais Moure """
try:
    print([1,2,3,4][4])
except Exception as error:          # investigar más sobre el manejo de errores
    print(f"Se ha producido un error: {error} ({type(error).__name__})")




""" DIFICULTAD EXTRA (opcional):
 * Crea una función que sea capaz de procesar parámetros, pero que también
 * pueda lanzar 3 tipos diferentes de excepciones (una de ellas tiene que
 * corresponderse con un tipo de excepción creada por nosotros de manera
 * personalizada, y debe ser lanzada de manera manual) en caso de error.
 * - Captura todas las excepciones desde el lugar donde llamas a la función.
 * - Imprime el tipo de error.
 * - Imprime si no se ha producido ningún error.
 * - Imprime que la ejecución ha finalizado. """