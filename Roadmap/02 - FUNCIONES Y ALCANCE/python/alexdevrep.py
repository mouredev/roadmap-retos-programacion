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

#Función sin parámetros ni retorno
def simpleFunction ():
    print("Hola, Python")

simpleFunction()

#Función con un parámetro
def oneArg (Arg1):
    print(Arg1)

oneArg("Hola, Alexdevrep")

#Función con varios parámetros
def manyArgs (día, mes, año):
    print("Hoy es"+" "+ día+" "+"de"+" "+mes+" "+"del"+" "+año)

manyArgs("10","enero","2024")

#Función con retorno
def retorno (a,b):
    return a + b

resultado = retorno(2,3)
print(resultado)

#Funciones dentro de funciones
def funcionPadre(sum3):
    def funcionHijo(sum1,sum2):
        return sum1 + sum2
    resultadoHijo = funcionHijo(1,2)
    print(resultadoHijo + sum3)
funcionPadre(3)

#Funciones ya creadas en el lenguaje
print(max(1,2,3,4,35)) #Max devuelve el valor máxnimo que hay dentro de una tupla, una lista, o un diccionario

#Variable local
def resta():
    rest1 = 5
    print(rest1 -3)

resta()

#Variable global
sumando = 8
def suma():
    print (sumando + 10)
suma()

#Dificultad extra
def extra (string1, string2):
    numero = 0
    i=1
    for i in range (1,101):
        if (i%3==0 and i%5==0):
            print(string1+" "+string2)
            continue
        elif (i%3==0):
            print(string1)
            continue
        elif (i%5==0):
            print(string2)
            continue
        else:
            print(i)
        i=i+1
        numero= numero +1
    return numero
     
print("Número de veces que se ha impreso el contador:",extra("Hola Python","Hola alexdevrep"))