"""
* DIFICULTAD EXTRA (opcional):
 * Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.

 *   - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
    *   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
    *   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
    *   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.

 * Presta especial atención a la sintaxis que debes utilizar en cada uno de los casos.
 * Cada lenguaje sigue una convenciones que debes de respetar para que el código se entienda.
 */
"""

def funcion(var_1, var_2):

    for i in range(1,101):
        if i % 3 == 0 and i % 5 == 0:
            print(f"el numero {i} es {var_1} y {var_2}")
        elif i % 3 == 0:
            print(f"el numero {i} es {var_1}")
        elif i % 5 == 0:
            print(f"el numero {i} es {var_2}")

funcion ("multiplo de 3", "multiplo de 5")