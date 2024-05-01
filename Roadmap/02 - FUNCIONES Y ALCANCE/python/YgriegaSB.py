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
 */
"""

def printHola(name):
    print(f"¡Hola, {name}!")

printHola('Andy')


def suma(num1, num2):

    def resta(num1, num2):
        return print(f"Resta: entre {num1} - {num2} = {num1-num2}");

    resta(num1, num2)
    return print(f"Suma: entre {num1} + {num2} = {num1+num2}");


suma(20, 10.4)


# sort function
arr = [5,1,25,2,15,12,9,7,20]
print(arr)
arr.sort()
print(arr)


# Ejercicio
def string_parameters(param1, param2):
    num_characters = len(param1) + len(param2)
    return num_characters

print(string_parameters('Hola', 'Mundo'))


# Ejercicio Extra
def print_numbers(range1, range2):
    counter=0
    for i in range(range1, range2):
        if(i%5==0 and i%3==0):
            print('FizzBuzz')
        elif(i%3==0):
            print('Fizz')
        elif(i%5==0):
            print('Buzz')
        else:
            print(i)
            counter += 1
    return print(f"cantidad de numeros: {counter}")
     
print_numbers(1, 101)

