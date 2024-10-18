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
 *
 * Presta especial atención a la sintaxis que debes utilizar en cada uno de los casos.
 * Cada lenguaje sigue una convenciones que debes de respetar para que el código se entienda.
"""

def funcion_a()->None:
    print("Funcion sin parámetros ni retorno")

def funcion_b(a,b)->None:
    print("Funcion con dos parámetros y sin retorno")

def funcion_c(a,b):
    print("Funcion con dos parametrs y retorno")
    return a+b

def funcion_d():
    print("Dentro de d")
    def funcion_e():
        print("Hola dentro de e")
    funcion_e()

def funcion_f():
    x = 6 #no afecta a la x del entorno global
    print(x)


"""
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
def divisible3(num:int)->bool:
    return num%3 == 0

def divisible5(num:int)->bool:
    return num%5 == 0

def funcion_extra(cadena1:str,cadena2:str)->int:
    contador = 0

    for n in range(1,101):
        if divisible3(n) and not divisible5(n):
            print(cadena1)
        elif not divisible3(n) and divisible5(n):
            print(cadena2)
        elif divisible3(n) and divisible5(n):
            print(f"{cadena1} {cadena2}")
        else:
            print(n)
            contador +=1
    return contador


funcion_d()
x = 5#variable global
print(x)


cadena1 = input("Ingrese la primera cadena: ")
cadena2 = input("Ingrese la segunda cadena: ")


repeticiones = funcion_extra(cadena1,cadena2)

print(f"Se han impreso {repeticiones} números.")