#/*
# * EJERCICIO:
# * Explora el concepto de manejo de excepciones según tu lenguaje.
# * Fuerza un error en tu código, captura el error, imprime dicho error
# * y evita que el programa se detenga de manera inesperada.
# * Prueba a dividir "10/0" o acceder a un índice no existente
# * de un listado para intentar provocar un error.

def error_conversion():
    try:
        texto = "hola mundo"
        numero = int(texto)
        print(numero)
    except Exception as ex:
        print("Ocurrió un error: ", ex)

def error_division():
    try:
        valor = 0
        numero = 10 / valor
        print(numero)
    except Exception as ex:
        print("Ocurrió un error: ", ex)

def error_indice():
    try:
        lista = ["A", "B", "C"]
        letra = lista[4]
        print(letra)
    except Exception as ex:
        print("Ocurrió un error: ", ex)

error_conversion()
error_division()
error_indice()

# *
# * DIFICULTAD EXTRA (opcional):
# * Crea una función que sea capaz de procesar parámetros, pero que también
# * pueda lanzar 3 tipos diferentes de excepciones (una de ellas tiene que
# * corresponderse con un tipo de excepción creada por nosotros de manera
# * personalizada, y debe ser lanzada de manera manual) en caso de error.
# * - Captura todas las excepciones desde el lugar donde llamas a la función.
# * - Imprime el tipo de error.
# * - Imprime si no se ha producido ningún error.
# * - Imprime que la ejecución ha finalizado. 
# */

class ResultadoException(Exception):
    mensaje = "El resultado no puede ser mayor que 100"

def division_de_dos_numeros(dividendo, divisor):
    error = None
    dividendo_int = 0
    divisor_int = 0
    resultado = 0
    
    try:
        dividendo_int = int(dividendo)
        divisor_int = int(divisor)
    except Exception as ex:
        print("Ocurrió un error: ", ex)
        return
    
    try:
        resultado = dividendo_int / divisor_int
        print(f"{dividendo_int} / {divisor_int} = {resultado}")
    except Exception as ex:
        print("Ocurrió un error: ", ex)
        return
    
    try:
        resultado = dividendo_int / divisor_int
        if resultado > 100:
            raise ResultadoException
    except ResultadoException as ex:
        print("Ocurrió un error: ", ex.mensaje)
        return
    
    print(error) if error != None else print("No se ha producido ningún error")
    
    print("\nLa ejecución ha finalizado\n")

print("\n===== Teste 01: error conversión =====")
division_de_dos_numeros(200, None)
print("\n===== Teste 02: error división =====")
division_de_dos_numeros(200, 0)
print("\n===== Teste 03: error personalizado =====")
division_de_dos_numeros(200, 1)
print("\n===== Teste 04: ningún error =====")
division_de_dos_numeros(200, 3)