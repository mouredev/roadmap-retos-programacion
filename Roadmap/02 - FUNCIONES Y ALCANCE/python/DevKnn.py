"""
 z EJERCICIO:
  - Crea ejemplos de funciones básicas que representen las diferentes
    posibilidades del lenguaje
    Sin parámetros ni retorno, con uno o varios parámetros, con retorno...
    Comprueba si puedes crear funciones dentro de funciones.
    Utiliza algún ejemplo de funciones ya creadas en el lenguaje.
    Pon a prueba el concepto de variable LOCAL y GLOBAL.
    Debes hacer print por consola del resultado de todos los ejemplos.
    (y tener en cuenta que cada lenguaje puede poseer más o menos posibilidades)
    Comprueba si puedes crear funciones dentro de funciones.
    Utiliza algún ejemplo de funciones ya creadas en el lenguaje.
    Pon a prueba el concepto de variable LOCAL y GLOBAL.
    Debes hacer print por consola del resultado de todos los ejemplos.
    (y tener en cuenta que cada lenguaje puede poseer más o menos posibilidades)
"""

titulo1 = "Hola"
titulo2 = "Python"

#funcion que no devuelve un parametro, ni retorno
def myFuction():
    print("Funcion que no devuelve un parametro, ni retorno")
myFuction()
#Funcion que espear un parametro y es llamado a nivel local
def myFuction1(x):
    x = "hola"
    print("Funcion que espear un parametro y es llamado a nivel local",x)
myFuction1(titulo1)
#Funcion que espear dos parametro y es llamado a nivel global
def myfuction3():
    print(("Mi funcion"))   
    def dentroDeLaFunction(x=None):
        print("Dentro de la funcion")
        if x is None:
            x = []
            x.append(titulo1)
            x.append(titulo2)
            print(x)
        return x
    dentroDeLaFunction()
myfuction3()

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
 */"""
 
def index(txt1, txt2):
    txt2 = "Mundo"
    i = 0
    while(i<=100):
        if i % 3 == 0 and i % 5 == 0:
            print(txt1 + txt2)
        if i % 3 == 0:
            print(txt1)
        elif i % 5 == 0:
            print(txt2)
        else:
            print(i)
        i+=1
    return i

txt1 = "Hola"
tx2 = "Python"
print(index(txt1, tx2))
