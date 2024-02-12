"""
 * EJERCICIO:
 * Crea ejemplos de funciones básicas que representen las diferentes
 * posibilidades del lenguaje:
 * Sin parámetros ni retorno, con uno o varios parámetros, con retorno...
 * Comprueba si puedes crear funciones dentro de funciones.
 * Utiliza algún ejemplo de funciones ya creadas en el lenguaje.
 * Pon a prueba el concepto de variable LOCAL y GLOBAL.
 * Debes hacer print por consola del resultado de todos los ejemplos.
"""

# FUNCIONES BÁSICAS DE PYTHON

# Ejemplo de función sin parámetros
def pi():
    return 3.141592653589


# Ejemplo de función con parámetros y sin retorno
def cifrar(texto, clave):
    diccionario = "abcdefghijklmnopqrstuvwxyz"
    # Convierte el texto a lista y sustituye cada letra por otra situada en el diccionario en la posición de las veces que indique la clave
    texto = list(texto.lower()) # list y lower son funciones que vienen incluida en el lenguaje
    for i in range(len(texto)): # range y len también vienen con Python
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
def procesar_datos(datos):
    def limpiar_datos(datos):
        datos = datos.replace(",", ".")
        return datos
    def convertir_datos(datos):
        datos = datos.split()
        return datos
    return convertir_datos(limpiar_datos(datos))

""" * DIFICULTAD EXTRA (opcional):
 * Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
 * La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
 * Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
 * Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
 * Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
 * La función retorna el número de veces que se ha impreso el número en lugar de los textos.
"""

def retornaNumero(text1: str, text2: str) -> int:
    # contar numero de veces que se imprime text1 y numero de veces text2
    text1_contador = 0
    text2_contador = 0
    for x in range(1, 101):
        if x % 3 == 0 and x % 5 == 0:
            print(text1 + text2)
            text1_contador += 1
            text2_contador += 1
        elif x % 3 == 0:
            print(text1)
            text1_contador += 1
        elif x % 5 == 0:
            print(text2)
            text2_contador += 1
        else:
            print(x)

    return f"Se ha impreso: \n {text1}: {text1_contador} veces \n {text2}: {text2_contador} veces"
        
##################################
# Vamos con el codigo principal:
##################################

if __name__ == "__main__":
    # Función sin parámetros que devuelve el número PI
    print("__Ejemplo función sin parámetros que devuelve el número PI__")
    print(f"Número PI: {pi()}")

    # Función con parámetros y sin retorno que cifra un texto
    print("__Ejemplo función con parámetros y sin retorno que modifica una variable global__")
    cifrado = cifrar("Hola Mundo", 5878)
    print(f"Texto cifrado: {cifrado}")

    # Función sin parámetros y sin retorno que descifra un texto
    descifrado = descifrar(cifrado, 5878)
    print(f"Texto descifrado: {descifrado}")
    print("-"*48)

    # Función con parámetros que calcula la gravitacional entre dos cuerpos
    ## Vamos a calcularla entre la Luna y la Starship con la info de masa y distancia
    print("__Ejemplo función con parámetros___")
    masa_luna = 7.342 * 10**22
    masa_starship = 5000000
    distancia_luna_starship = 384402 # aqui iria alguna info de posicion dinamica, pero bueno... es un ejemplo
    
    ## Calculamos y mostramos resultado
    print(f"Fuerza gravitacional entre la Luna y la Starship en órbita: {fuerza_gravitacional(masa_luna, masa_starship, distancia_luna_starship)}")
    print("-"*48)

    # Funciones lambda, esto es un tipo de función simple y sin nombre que se puede usar en cualquier parte del código
    ## vamos a usarla para calcular la energía cinematica de un cuerpo
    print("__Ejemplo función Lambda__")
    energia_cinetica = lambda masa, velocidad: (masa * velocidad ** 2) / 2
    print(f"Energía cinética del cuerpo es de: {energia_cinetica(10, 5)} j")  

    print("-"*48)

    # Funciones dentro de funciones
    print("__Ejemplo función dentro de función__")
    print(procesar_datos("40, 55, 87, 65, 8, 6, 00, 78, 9, 68"))
    print("-"*48)

    # Mostramos el ejercicio extra
    print("__Ejercicio extra__")
    print(retornaNumero("Fizz","Buzz"))
