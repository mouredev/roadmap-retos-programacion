"""
Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
 * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
 *   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
 *   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
 *   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
 *   - La función retorna el número de veces que se ha impreso el número en lugar de los textos
"""

def funcion(parametro1: str, parametro2: str):
    veces_numero = 0
    for num in range(1,101):
        cadena_a_imprimir = ""
        if num % 3 == 0 and num % 5 == 0:
            cadena_a_imprimir = parametro1 + " " + parametro2
            print(cadena_a_imprimir)
        elif num % 3 == 0:
            cadena_a_imprimir = parametro1
            print(cadena_a_imprimir)
        elif num % 5 == 0:
            cadena_a_imprimir = parametro2
            print(cadena_a_imprimir)
        else:
            print(num)
            veces_numero+=1
    return veces_numero

print(funcion("cadena 1", "cadena 2"))