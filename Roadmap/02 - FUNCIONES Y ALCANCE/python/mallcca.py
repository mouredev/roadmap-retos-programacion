'''
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
 '''

# Ejemplo de función
print('------------------------------')
print('Ejemplo de función sencilla')
print('------------------------------')
def suma(a, b):
    return a + b

print(suma(10, 20))

print('------------------------------')
print('Ejemplo de función lambda')
print('------------------------------')
fun = lambda x, y: x + y
print(fun(10, 20))

print('------------------------------')
print('Ejemplo de funciones que retornan muchos valores')
print('------------------------------')
def generate_123():
    return 1, 2, 3

print(generate_123())

print('------------------------------')
print('Ejemplo de funciones que retornan muchos valores')
print('------------------------------')
def generate_123():
    return 1, 2, 3

print(generate_123())

print('------------------------------')
print('Ejemplo de función dentro de otra función')
print('------------------------------')
def suma_y_resta(a, b):
    def resta(a, b):
        return a - b
    return a + b, resta(a, b)

print(suma_y_resta(10, 300))


print('------------------------------')
print('Ejemplo usando variables globales')
print('------------------------------')
global PI 
PI = 3.1415

def get_pi():
    return PI

print(get_pi())

'''
 * DIFICULTAD EXTRA (opcional):
 * Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
 * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
 *   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
 *   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
 *   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
 *   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
'''
print('------------------------------')
print('Dificultad extra ...')
print('------------------------------')

def funcion(a, b):
    c_str = 0
    c_int = 0
    for num in range(101):                 
        if num%3 == 0 and num%5 == 0:
            print(a + b)
        elif num%3 == 0:
            print(a)
        elif num%5 == 0:
            print(b)
        else:
            c_int += 1
            print(num)

    return '# veces que se ha impreso un número: ' + str(c_int)

print(funcion('Texto 1', 'Texto 2'))


