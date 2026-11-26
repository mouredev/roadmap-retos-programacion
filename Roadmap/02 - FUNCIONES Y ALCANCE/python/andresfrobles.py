""#02 FUNCIONES Y ALCANCE"""


saludoVar = "Hola global"  # Variable global


def saludo():
    print("Hola Mundo")


def saludoUsuario(usuario):
    saludovar = "Hola"  # variable local solo dentro de la funcion
    # cadenas conb formato
    print(f"{saludoVar} {usuario}")


def saludoUsuarioValidado(usuario, validado):
    if validado == 1:
        print(f"Hola {usuario}, haz sido validado")
        return validado
    else:
        print(f"El usuario {usuario} no existe")


saludo()
saludoUsuario("Hola soy Andres")
confirmado = saludoUsuarioValidado("Andres Robles", 0)
print(confirmado)


# funcion dentro de otra
def saludoAdicional():
    def hola():
        print("Como estás, soy una funcion dentro de otra\n\n")
    hola()


saludoAdicional()


"""
 EJERCICIO:
 
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
 
"""

"""Ejercicio Extra"""
def ejercicio_extra(param1,param2):
    contador=0
    for i in range(1,101):
        if(i%15==0):
            print(f"{param1}  {param2}")
        elif(i%3==0):
            print(param1)
        elif(i%5==0):
            print(param2)
        else:
            print(i)
            contador+=1
    return contador

print(ejercicio_extra("DOS","TRES"))