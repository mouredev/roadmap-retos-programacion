""" * EJERCICIO:
 * - Crea ejemplos de funciones básicas que representen las diferentes
 *   posibilidades del lenguaje:
 *   Sin parámetros ni retorno, con uno o varios parámetros, con retorno...
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
 */"""

def funcion_sin_retorno_ni_parametros():
    print("esta es la funcion")

funcion_sin_retorno_ni_parametros()

def con_uno_o_varios_parametros_y_retorno(altura, anchura):
    area = altura * anchura
    return area

print(con_uno_o_varios_parametros_y_retorno(23, 56))

def con_numero_random_de_parametros(*numeros):
    if len(numeros) >= 1:
        return "Esta funcion no esta vacia"
    if len(numeros) < 1:
        return "Esta funcion está vacia"

print(con_numero_random_de_parametros(0, 4, 5, 7, 8))

# Ejemplo de funciones dentro de funciones

def funcion_en_funcion (altura):
    def hacer_cuadrado():
        trend = altura**2
        return trend
    treta = hacer_cuadrado()
    return treta

print ("Esto es una funcion dentro de otra funcion: ", funcion_en_funcion(45))

# Esta es una funcion del sistema

from math import sqrt

print(sqrt(25))

# Variable local y global

variable_global = "esto es una varible global"

print (variable_global)

def ejemplo():
    variable_local = "esto es una variable local"
    print (variable_local)

ejemplo()

# DIFICULTAD EXTRA

"""Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
 * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
 *   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
 *   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
 *   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
 *   - La función retorna el número de veces que se ha impreso el número en lugar de los textos."""

def polanco(wave, thunder):
    uno = len(wave)
    dos = len(thunder)

    for i in range (0, 101):
        print(i)
        if i == 100:
            numero = uno * dos
            if numero % 3 == 0 and numero % 5 == 0:
                return wave, thunder
            elif numero % 3 == 0:
                return wave
            elif numero % 5 == 0:
                return thunder

print(polanco("estadio", "dia"))
