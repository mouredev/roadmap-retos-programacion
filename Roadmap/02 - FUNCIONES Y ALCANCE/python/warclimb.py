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
"""

# FUNCIONES BÁSICAS DE PYTHON

# Ejemplo de función sin parámetros
def pi():
    return 3.141592653589


# Ejemplo de función con parámetros y sin retorno
def cifrar(texto, clave):
    diccionario = "abcdefghijklmnopqrstuvwxyz"
    # Convierte el texto a lista y sustituye cada letra por otra situada en el diccionario en la posición de las veces que indique la clave
    texto = list(texto.lower())
    for i in range(len(texto)):
        if texto[i] in diccionario:
            # recorre el diccionario de izquierda a derecha
            texto[i] = diccionario[(diccionario.index(texto[i]) + clave) % len(diccionario)]
    # Convierte la lista en texto y lo devuelve
    return "".join(texto)


# Bueno, ya que estamos hago también la de descifrar, que es otra función sin parámetros y sin retorno
def descifrar(texto, clave):
    diccionario = "abcdefghijklmnopqrstuvwxyz"
    # Convierte el texto a lista y sustituye cada letra por otra situada en el diccionario en la posición de las veces que indique la clave
    texto = list(texto.lower())
    for i in range(len(texto)):
        if texto[i] in diccionario:
            # recorremos el diccionario de derecha a izquierda
            texto[i] = diccionario[(diccionario.index(texto[i]) - clave) % len(diccionario)]
    # Convierte la lista en texto y lo devuelve
    return "".join(texto)

# Ejemplo de función con parámetros y un retorno
def fuerza_gravitacional(masa1, masa2, distancia):
    # constante de gravitación universal
    G = 6.674 * (10 ** -11)
    # 
    F = G * (masa1 * masa2) / (distancia ** 2)
    return F

# crear funciones dentro de una función



# Vamos con el codigo principal:

if __name__ == "__main__":
    # Función sin parámetros que devuelve el número PI
    print(pi())

    # Función con parámetros y sin retorno que cifra un texto
    cifrado = cifrar("Hola Mundo", 5878)
    print(cifrado)

    # Función sin parámetros y sin retorno que descifra un texto
    descifrado = descifrar(cifrado, 5878)
    print(descifrado)

    # Función con parámetros que calcula la gravitacional entre dos cuerpos
    ## Vamos a calcularla entre la Luna y la Starship con la info de masa y distancia
    masa_luna = 7.342 * 10**22
    masa_starship = 5000000
    distancia_luna_starship = 384402 # aqui iria alguna info de posicion dinamica, pero bueno... es un ejemplo

    # Calculamos y mostramos resultado
    print(fuerza_gravitacional(masa_luna, masa_starship, distancia_luna_starship))



""" * DIFICULTAD EXTRA (opcional):
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