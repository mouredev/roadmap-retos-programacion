#/*
# * EJERCICIO:
# * - Crea ejemplos de funciones básicas que representen las diferentes
# *   posibilidades del lenguaje:
# *   Sin parámetros ni retorno, con uno o varios parámetros, con retorno...
# * - Comprueba si puedes crear funciones dentro de funciones.
# * - Utiliza algún ejemplo de funciones ya creadas en el lenguaje.
# * - Pon a prueba el concepto de variable LOCAL y GLOBAL.
# * - Debes hacer print por consola del resultado de todos los ejemplos.
# *   (y tener en cuenta que cada lenguaje puede poseer más o menos posibilidades)
# *
# * DIFICULTAD EXTRA (opcional):
# * Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
# * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
# *   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
# *   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
# *   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
# *   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
# *
# * Presta especial atención a la sintaxis que debes utilizar en cada uno de los casos.
# * Cada lenguaje sigue una convenciones que debes de respetar para que el código se entienda.
# */

# Funciones básicas

def saludo_basico():
    print("Hola")

def saludo_personalizado(nombre: str):
    print(f'Hola {nombre}')
    
def suma(a: int, b: int):
    return a + b

# No podemos crear funciones dentro de funciones en Python, lo que si podemos hacer es llamar a una función dentro de otra.
def suma_rango(a: int, b: int):
    suma = 0
    for i in range(a, b+1):
        suma += i
    
    return suma

print(f'La suma del rango de 1 a 200 es: {suma_rango(1, 200)}')

# De este modo también acabamos de usar funciones ya creadas en python, como range().

# Variable LOCAL y GLOBAL
# En Python, una variable declarada dentro de una función es local a esa función, a menos que se declare global.

age = 25

def get_age():
    global age # Hay que asignar antes de la variable local.
    age = 30
    print(f'La edad dentro de la función es: {age}')# Imprime 30
    print(f'La edad fuera de la función es: {age}')# Imprime 25
    
get_age()

# Dificultad extra
def string_to_number(string1: str, string2: str) -> int:
    
    number = 0
    
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print(f'{string1} {string2}')
        elif i % 3 == 0:
            print(f'{string1}')
        elif i % 5 == 0:
            print(f'{string2}')
        else:
            number += 1
            print(i)
    
    return number


times = string_to_number('Hola caracola', 'Hola caraculo')

print(f'Se ha impreso el número {times} veces')