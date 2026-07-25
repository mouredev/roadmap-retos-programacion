'''
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
 *
 * Presta especial atención a la sintaxis que debes utilizar en cada uno de los casos.
 * Cada lenguaje sigue una convenciones que debes de respetar para que el código se entienda.
 */
'''
print("Funciones en python")
print("Funcion sin parametros ni retorno\n")

def funcion1():
    print("Hola")
def funcion2():
    print("Inicio de funcion2")
    print("Llamamos a funcion1")
    funcion1()
    def funcion3():
        print("Inicio de funcion3 dentro de funcion2") # intentamos hacer una funcion dentro de otra funcion
    funcion3()
    print("Fin de funcion2\n")

funcion2() # Con esto comprobamos que podemos definir una funcion dentro de otra funcion

print("Funcion con uno o mas parametros y retorno")
def funcionParam(x, y, z):
    return x + y + z

resultado = funcionParam(1, 2, 3)
print("El resultado de la funcion al llamarlo es ", resultado, '\n')

print("Bariables locales vs globales")
x = 10

def varGlobal():
    global y
    y = 5
print("x = ", x)
try:
    z = x / y
    print(z)
except NameError:
    print("La variable y es una variable local del bloque de la funcion varGlobal()")
finally:
    print("Hacemos que y sea una variable global")
    varGlobal()
    print("y = ", y)
    z = x/y
    print("El resultado de x / y es ", z)
'''
 * DIFICULTAD EXTRA (opcional):
 * Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
 * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
 *   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
 *   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
 *   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
 *   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
'''
print("\nPrueba Extra")
def extra(string1, string2):
    count = 0
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print(string1, string2)    
        elif i % 5 == 0:
            print(string2)
        elif i % 3 == 0:
            print(string1)
        else:
            print(i)
            count += 1
    print("Numero de veces que se imprimio un numero: ", count)
extra("Hola", "Mundo")
        