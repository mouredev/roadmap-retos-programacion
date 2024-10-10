"""
/*
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
 */
"""

a = 5
b = 0

try:
    c = a/b
except ZeroDivisionError:
    print("No se puede dividir entre cero")

try:
    print(5/0)
except Exception as e:
    print(f"No se puede dividir: {e}({type(e).__name__})")

my_list = [0,2,4,6,8]

try:
    number = 10
    if number in my_list:
        print(number)
    if number not in my_list:
        my_list.append(number)
        print(my_list)
except:
    print("Este número no pertenece a la lista")

