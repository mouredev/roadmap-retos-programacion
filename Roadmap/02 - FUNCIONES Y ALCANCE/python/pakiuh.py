'''
/*
 * EJERCICIO:
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
 */
'''
#funcion báisco sin parámetros ni retorno

def imprimir_hola():
    print("Hola")
imprimir_hola()

def saludo_personal(nombre, apellido):
    print(f"¿Cómo esta Vd Sr {nombre} {apellido}?")

saludo_personal("Francisco", "Camps")

def sumar(num1, num2):
    return num1+num2

print(f"La suma de 3 y 5 es {sumar(3,5)}")

def acciones_jarra(accion):
    return f"voy a {accion} la jarra"

def que_hacer_jarra(accion, funcion_parametro):
    print(f"Voy a {accion} después de {funcion_parametro("abrirla")}")

que_hacer_jarra("tirarla", acciones_jarra)

#funciones ya creadas por el lenguaje

nombre = "Paco"
print(type(nombre))
print(hash(nombre))

def escribir_nombre(nom):
    apellido = "Camps"
    print(f"el nombre es {nom} y el apellido es {apellido}")

escribir_nombre(nombre)
"""
 * DIFICULTAD EXTRA (opcional):
 * Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
 * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
 *   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
 *   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
 *   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
 *   - La función retorna el número de veces que se ha impreso el número en lugar de los texto
"""


def fizz_buzz(palabra1, palabra2):
    for i in range(101):
        if i % 3 == 0 and i % 5 == 0:
            print(f"{palabra1}{palabra2}")
        elif i % 3 == 0:
            print(palabra1)
        elif i % 5 == 0:
            print(palabra2)

fizz_buzz("Gandalf", "Saruman")