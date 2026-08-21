"""
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
"""
def funcion_sin_parametros():
    print("Esta es una función sin parámetros ni retorno.")

funcion_sin_parametros()

def funcion_con_parametros(param1, param2):
    print(f"Esta es una función con parámetros: {param1} y {param2}.")

def funcion_saludar(nombre):
    mensaje= f"Esta es una función con un parámetro: {nombre}. ¡Hola, {nombre}!"
    print(mensaje)

funcion_con_parametros("parametro 1", "parametro2")
funcion_saludar("Alice")

def funcion_con_argumentos_clave(param1, param2):
    print(f"Esta es una función con argumentos clave: {param1} y {param2}.")

funcion_con_argumentos_clave(param2="valor2", param1="valor1")

def funcion_con_valores_por_defecto(param1, exp=2):
    mensaje = param1 ** exp
    print(mensaje)

funcion_con_valores_por_defecto(2)
funcion_con_valores_por_defecto(2, 3) #aqui se remplaza el valor por defecto de exp

def funcion_con_argumentos_arbitrarias(*argumentosArbitarios):
    suma= sum(argumentosArbitarios)
    print(f"Esta es una función con argumentos de posición arbitrarios: {argumentosArbitarios}. La suma es: {suma}.\n")

funcion_con_argumentos_arbitrarias(1, 2, 3, 4, 5)

def funcion_con_argumentos_clave_arbitrarios(**argumentosClaveArbitrarios):
    mensaje = f"Esta es una función con argumentos de clave arbitrarios: {argumentosClaveArbitrarios}.\n"
    print(mensaje)

funcion_con_argumentos_clave_arbitrarios(param1="valor1", param2="valor2", param3="valor3")

def funcion_con_argumentos_arbitrarias_y_clave_arbitrarios(*argumentosArbitarios, **argumentosClaveArbitrarios):
    suma= sum(argumentosArbitarios)
    mensaje = f"Esta es una función con argumentos de posición arbitrarios: {argumentosArbitarios} y \nargumentos de clave arbitrarios: {argumentosClaveArbitrarios}. \nLa suma es: {suma}."
    print(mensaje)

funcion_con_argumentos_arbitrarias_y_clave_arbitrarios(1, 2, 3, 4, 5, param1="valor1", param2="valor2", param3="valor3")
