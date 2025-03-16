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

# Función sin parámetros, ni retorno

def firstFunction():
    print('Hola mundo.')

firstFunction()

# Función con un parámetro, con variables locales y utilizando una función ya creada por el lenguaje.

def circleArea(r):
    PI = 3.141592
    result = PI * r**2
    print(round(result, 2))

circleArea(2)

# Función con retorno y con una variable global.

num = 2

def returnFunction():
    return num * num

print(returnFunction())

# Función con un parámetro y retorno.

def welcome(name):
    return f"Bienvenido/a, {name}."

print(welcome("Python"))

# Función creada dentro de otra función

def rectangleArea(b, a):
    def calculate():
        return b * a

    return calculate()

print(rectangleArea(10, 5))

# Dificultad Extra:

# Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
def fizzBuzz(str1, str2):
    
    if isinstance(str1, str) and isinstance(str2, str):

        total_times = 0

        # La función imprime todos los números del 1 al 100.
        for i in range(1,101):

            # Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
            if i % 5 == 0 and i % 3 == 0:
                print(str1 + str2)
            
            # Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
            elif i % 5 == 0:
                print(str2)
            
            # Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
            elif i % 3 == 0:
                print(str1)

            else:
                total_times += 1


        # La función retorna el número de veces que se ha impreso el número en lugar de los textos.
        return total_times
    
    else:
        return "Se tiene que indicar por parámetro dos cadenas de texto(Por ejemplo: 'Fizz', 'Buzz'). Inténtalo de nuevo..."


print(fizzBuzz("Fizz", "Buzz"))