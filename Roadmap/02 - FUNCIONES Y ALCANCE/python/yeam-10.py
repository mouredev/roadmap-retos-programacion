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
 .
 *
 * Presta especial atención a la sintaxis que debes utilizar en cada uno de los casos.
 * Cada lenguaje sigue una convenciones que debes de respetar para que el código se entienda.
 */
 """

"""

RESPUESTA
La funcion es un bloque de codigo fuente que contiene un conjunto 
de instrucciones y que puede ser utilizada 
desde el codigo fuente que escribes tantas veces como necesites.
"""

#Sin parametro ni retorno
def saludar():
    print("Hola buenos dias")
saludar()


#Con parametro sin retorno

def EsMayorQueCero(param):
    if param > 0:
        print(param, "es mayor que cero")
    else:
        print(param,"no es mayor que cero")
numero = int(input("Introduce un numero:"))
EsMayorQueCero(numero)

#Con varios parametros y retorno

def Sumar(param1, param2):
    return param1 + param2
sumando1 = int(input("Introduce el primer numero:"))
sumando2 = int(input("Introduce el segundo numero:"))
resultado = Sumar(sumando1,sumando2)
print("EL resultado de la suma es:", resultado)

#Funciones dentro de otra funcion

def funcion1():
    def funcion2():
        print("Imprime funcion 2")
    print("Imprime funcion 1")
    funcion2()
funcion1()

print("Ejemplo de funcion creada en python", {round(65.987)})

#Ejemplo de una variable global

x = 20

def mostrarX():
    print("El valor de X es", x)
mostrarX()

#Ejemplo de variable local

def mostraLocal(num):
    n = 20
    return num * n
print(mostraLocal(6))



#DIFICULTAD EXTRA (opcional):
"""
* DIFICULTAD EXTRA (opcional):
 * Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
 * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
 *   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
 *   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
 *   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
 *   - La función retorna el número de veces que se ha impreso el número en lugar de los textos
"""

def EjercicioExtra(cadena1, cadena2):
    count = 0
    for i in range(1,101):
        if i % 5 == 0 and i % 3 == 0:
            print(cadena1+cadena2)
        elif i % 3 == 0:
            print(cadena1)
        elif i % 5 == 0:
            print(cadena2)
        else:
            print(i)
            count += 1
    return count
print("Numero de veces", {EjercicioExtra("Mickey","Mouse")} )