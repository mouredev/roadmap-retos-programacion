# EJERCICIO:
# Explora el concepto de manejo de excepciones según tu lenguaje.
# Fuerza un error en tu código, captura el error, imprime dicho error
# y evita que el programa se detenga de manera inesperada.
# Prueba a dividir "10/0" o acceder a un índice no existente
# de un listado para intentar provocar un error.


def divide(a, b):
    try:
        result = a / b
        print(f"Resultado de {a} / {b} = {result}")
    except ZeroDivisionError as e:
        print(f"Error: {type(e).__name__}, no se puede dividir por cero.")


divide(10, 2)
divide(10, 0)
divide(15, 3)


def buscar_elemento(lista, indice):
    try:
        elemento = lista[indice]
        print(f"Elemento en el índice {indice}: {elemento}")
    except IndexError as e:
        print(f"Error: {type(e).__name__}, índice fuera de rango.")

mi_lista = [1, 2, 3, 4, 5]
buscar_elemento(mi_lista, 2)
buscar_elemento(mi_lista, 10)


#
# DIFICULTAD EXTRA (opcional):
# Crea una función que sea capaz de procesar parámetros, pero que también
# pueda lanzar 3 tipos diferentes de excepciones (una de ellas tiene que
# corresponderse con un tipo de excepción creada por nosotros de manera
# personalizada, y debe ser lanzada de manera manual) en caso de error.
# - Captura todas las excepciones desde el lugar donde llamas a la función.
# - Imprime el tipo de error.
# - Imprime si no se ha producido ningún error.
# - Imprime que la ejecución ha finalizado.

class TypeErrorPersonalizado(Exception):
    def __init__(self, mensaje):
        self.mensaje = mensaje
        super().__init__(self.mensaje)

def procesar_parametros(parametros):
    if len(parametros) < 3:
        raise IndexError("La lista debe tener al menos 3 elementos.")
    if parametros[1] == 0:
        raise ZeroDivisionError("El segundo elemento no puede ser cero.")
    if isinstance(parametros[2], str):
        raise TypeErrorPersonalizado("El tercer elemento no puede ser una cadena.")

    print(f"Tercer elemento: {parametros[2]}")
    print(f"División: {parametros[0] / parametros[1]}")
    print(f"Suma: {parametros[2] + 5}")

print("=" * 40)
print("Probando con parámetros correctos:")


try:
    procesar_parametros([10, 2, 3])
    procesar_parametros([10, 1, "cadena"])
except IndexError as e:
    print(f"Error: {type(e).__name__}, {e}")
except ZeroDivisionError as e:
    print(f"Error: {type(e).__name__}, {e}")
except TypeErrorPersonalizado as e:
    print(f"Error: {type(e).__name__}, {e}")
else:
    print("No se ha producido ningún error.")
finally:
    print("Ejecución finalizada.")