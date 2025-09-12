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

variable_global = "GLOBAL"  # accesible por todas las funciones


def funcion_sin_parametros():
    variable_local = "LOCAL"  # solo accesible en esta funcion
    print("funcion_sin_parametros:")
    print(" - no recibe parametros")
    print(" - no tiene retorno")
    print(f" - tiene acceso a la variable global: {variable_global}")
    print(f" - tiene acceso a la variable local: {variable_local}\n")


def funcion_con_parametros(param1, param2):
    print("funcion_con_parametros:")
    print(f" - recibe 2 parametros: {param1} y {param2}")
    print(" - no tiene retorno")
    print(f" - tiene acceso a la variable global: {variable_global}")
    try:
        print(f" - tiene acceso a la variable local: {variable_local}\n")
    except NameError:
        print(" - no tiene acceso a la variable local\n")


def funcion_con_retorno(param1, param2):
    print("funcion_con_parametros:")
    print(f" - recibe 2 parametros: {param1} y {param2}")
    print(" - tiene retorno")
    print(f" - tiene acceso a la variable global: {variable_global}")
    try:
        print(f" - tiene acceso a la variable local: {variable_local}\n")
    except NameError:
        print(" - no tiene acceso a la variable local\n")

    return param1 + param2


def funcion_con_parametros_por_defecto(param1=1, param2=2):
    print("funcion_con_parametros_por_defecto:")
    print(
        f" - siempre tiene 2 parametros: {param1} y {param2} (aunque no se indiquen en la llamada)"
    )
    print(" - tiene retorno")
    print(f" - tiene acceso a la variable global: {variable_global}")
    try:
        print(f" - tiene acceso a la variable local: {variable_local}\n")
    except NameError:
        print(" - no tiene acceso a la variable local\n")

    return param1 + param2


def funcion_con_varios_retornos():
    print("esta funcion devuelve 2 valores en el retorno")
    return "valor1", "valor2"


def funcion_con_funcion():
    def suma(param1, param2):
        return param1 + param2

    print(f"reultado funcion_con_funcion: {suma(1,2)}")


def funcion_extra(param1="fizz", param2="buzz"):
    contador_param1 = 0
    contador_param2 = 0
    contador_p1_p2 = 0

    for _ in range(1, 101):
        if _ % 3 == 0 and _ % 5 == 0:
            print(f"{param1}-{param2}")
            contador_p1_p2 += 1
        elif _ % 3 == 0:
            print(param1)
            contador_param1 += 1
        elif _ % 5 == 0:
            print(param2)
            contador_param2 += 1
        else:
            print(_)

    print("Se ha cambiado el valor original:")
    print(f" - Por el valor {param1}: {contador_param1} veces")
    print(f" - Por el valor {param2}: {contador_param2} veces")
    print(f" - Por el valor {param1}-{param2}: {contador_p1_p2} veces")


funcion_sin_parametros()
funcion_con_parametros("uno", "dos")
retorno = funcion_con_retorno(1, 2)
print(retorno)

retorno = funcion_con_parametros_por_defecto()
print(retorno)
retorno = funcion_con_parametros_por_defecto(param1=2)
print(retorno)
retorno = funcion_con_parametros_por_defecto(param2=1)
print(retorno)
retorno = funcion_con_parametros_por_defecto(3, 4)
print(retorno)

retorno1, retorno2 = funcion_con_varios_retornos()
print(retorno1)
print(retorno2)

funcion_con_funcion()

print("El propio print() es un ejemplo de funcion del lenguaje")

funcion_extra()
