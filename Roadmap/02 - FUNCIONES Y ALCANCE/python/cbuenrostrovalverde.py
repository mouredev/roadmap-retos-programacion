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
 */'
 '''

# Función sin parámetros ni retorno.

def saludar():
    print('Hola')

# Función con uno o varios parámetros.

def saludarNombre(nombre):
    print(f'Hola {nombre}')

def suma(val1, val2):
    return val1 + val2

'''
Cuando existe return dentro de la función, realizará el cálculo, pero no lo imprime por consola.
Para ello lo que tenemos que hacer es, si queremos el resultado, poner un print. print(suma(5, 5))
'''

# Funciones dentro de funciones:

def crear_saludo_personalizado(idioma):
    def saludar(nombre):
        if idioma == 'es':
            print(f'Hola {nombre}')
        elif idioma == 'en':
            print(f'Hello {nombre}')
        elif idioma == 'fr':
            print(f'Bonjour {nombre}')
        else:
            print('Idioma no soportado. Prueba con uno existente.')
    return saludar

# Crear funciones personalizadas
saludo_en_español = crear_saludo_personalizado("es")
saludo_en_ingles = crear_saludo_personalizado("en")
saludo_en_frances = crear_saludo_personalizado("fr")
saludo_en_chino = crear_saludo_personalizado("cn")

# Ejemplo
saludo_en_español("Carlos")
saludo_en_ingles("Carlos")
saludo_en_chino("Carlos")

# Funciones ya creadas en Python3

#print
print('Hola Mundo')

# max()
print(max(5, 4, 6, 12, 20))

# min()
print(min(5, 4, 6, 12, 20))

# upper()
print('estoy aprendiendo python'.upper())

# Prueba de variable LOCAL y GLOBAL
contador = 0

def incrementar():
    global contador  # ahora sí modificamos la global
    contador += 1
    print(contador)

incrementar()
incrementar()

'''
DIFICULTAD EXTRA (opcional):
 * Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
 * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
 *   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
 *   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
 *   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
 *   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
 '''

def numero_texto(text1, text2):
    count = 0
    for numero in range(1, 101):
        if numero % 3 == 0:
            print(text1)
        elif numero % 5 == 0:
            print(text2)
        elif numero % 3 == 0 and numero % 5 == 0:
            print(text1 + text2)
        else:
            count += 1
    return count

numero_texto('Hello', 'World')