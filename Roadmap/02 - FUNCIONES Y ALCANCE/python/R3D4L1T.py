#!/usr/bin/env python3

"""
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
"""


# función simple
def func():
    print("salud!!!!")


# función con parámetros
def nombre_edad(n, e):
    print(f"mi nombre es: {n} y mi edad es:{e} ")


# función con parámetro y return
def suma(n1, n2):
    return n1 + n2


def funcExterior():
    def funcInt():
        print("hola desde la función interior")

    funcInt()


def extra(txt1, txt2):
    for item in range(1, 101):
        if item % 5 == 0 and item % 3 == 0:
            print(f"valor:{item} --> {txt1} {txt2}")
        elif item % 3 == 0:
            print(f"valor:{item} --> {txt1}")
        elif item % 5 == 0:
            print(f"valor:{item} --> {txt2}")
        else:
            pass


if __name__ == "__main__":
    func()  # llamada a la función
    nombre_edad("Pablo", 57)  # llamada a la función con parámetros
    nombre_edad(
        n="Pedro", e=91
    )  # llamada a la función mediante asignacion  a los parámetros
    print(f"la suma de 3 y 1 es:{suma(3,1)}")
    cuadrado = lambda x: x**2  # ejemplo de función lambda
    print(f"El cuadrado de 3 es: {cuadrado(3)}")

    funcExterior()  # llamada a la función exterior la cual contiene a otra función

    extra("multiplo de 3", "multiplo de 5")
