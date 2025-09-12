# #02 FUNCIONES Y ALCANCE
#### Dificultad: Fácil | Publicación: 08/01/24 | Corrección: 15/01/24

## Ejercicio

'''
* EJERCICIO:
'''

''' *** Funciones Basicas sin parametros ni retorno *** '''

def saludo():
    print("Hola, python")
    
saludo()

''' *** Funciones basicas con parametros *** '''

def suma(a,b):
    print(f"La suma de {a} + {b} = {a + b}")

suma(3,4)

''' *** Funciones basicas con retorno *** '''
def multiplicacion(a,b):
    return a * b

print(f"La multiplicacion de 3 * 2 = {multiplicacion(3,2)}")

'''
 * - Comprueba si puedes crear funciones dentro de funciones.
'''
def funcion_():
    def otra_funcion():
        print("Esto es una funcion dentro de otra funcion")
    otra_funcion()

funcion_()
print()
print(12)

'''
 * - Pon a prueba el concepto de variable LOCAL y GLOBAL.
'''
x = "Variable Global"

def variable():
    x = "Variable Local"
    print(x)

variable()
print(x)


'''
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
'''

def funcion_extra(cadena_1,cadena_2):
    contador = 0
    for i in range(1,101):
        if i % 3 == 0 and i % 5 == 0:
            print(cadena_1,cadena_2)
        elif i % 3 == 0:
            print(cadena_1)
        elif i % 5 == 0:
            print(cadena_2)
        else:
            contador +=1
            print(i)
    return contador
contador = funcion_extra("Fizz","Buzz")
print()
print(f"La cantidad de veces que se imprimio un numero es {contador} veces")

