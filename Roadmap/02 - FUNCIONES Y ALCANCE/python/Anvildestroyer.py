"""
* EJERCICIO:
 * - Comprueba si puedes crear funciones dentro de funciones.
 * - Utiliza algún ejemplo de funciones ya creadas en el lenguaje.
 * - Pon a prueba el concepto de variable LOCAL y GLOBAL.
 * - Debes hacer print por consola del resultado de todos los ejemplos.
 *   (y tener en cuenta que cada lenguaje puede poseer más o menos posibilidades)
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
 * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
 *   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
 *   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
 *   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
 *   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
 *
 * Presta especial atención a la sintaxis que debes utilizar en cada uno de los casos.
 * Cada lenguaje sigue una convenciones que debes de respetar para que el código se entienda.
"""

# funciones sin parametro ni retorno:


def saludo():
    print("¡Hola, mundo!")


saludo()

# funciones con un parametro:


def cuadrado(n):
    return n ** 2


print(cuadrado(5))

# funciones con varios parametros:


def suma(a, b, c):
    return a + b + c


print(suma(1, 2, 3))

# funciones con retorno:


def multiplicar(x, y):
    return x * y


resultado = multiplicar(4, 5)
print(resultado)


# funciones con funciones anidadas:

def funcion_externa(a, b):
    def funcion_interna(c, d):
        return c + d
    resultado = funcion_interna(a, b)
    return resultado


print(funcion_externa(5, 10))
