"""
EJERCICIO:
- Muestra ejemplos de creación de todas las operaciones que puedes 
realizar con cadenas de caracteres.
- Acceso a caracteres específicos, subcadenas, longitud, 
concatenación, repetición, recorrido, conversión a mayúsculas y 
minúsculas, reemplazo, división, unión, interpolación, 
verificación...

DIFICULTAD EXTRA (opcional):
- Crea un programa que analice dos palabras diferentes y realice 
comprobaciones para descubrir si son:
- Palíndromos
- Anagramas
- Isogramas

by adra-dev.
"""

"""
Cadenas:
    Una cadena de texto es una secuencia inmutable de caracteres que 
    en Python se representa con el tipo de dato str.Esta secuencia 
    se puede delimitar con comillas simples('') o con comillas dobles
    ("").Aunque se pueden utilizar ambos tipos de comillas, las 
    cadenas se deben cerrar con el mismo tipo de comillas usado en la
    apertura.
"""

# Creacion
cadena_comillas_dobles = "Cadena de texto"
print(cadena_comillas_dobles)
cadena_comillas_simples = 'Cadena de texto'
print(cadena_comillas_simples)

"""
Acceso a los elementos de una cadena:
    Las cadenas de texto son un tipo de dato compuesto, es decir, 
    estan formadas por elementos mas pequenos que tienen significado,
    los caracters. Al tratarse de un tipo de dato compuesto podemos 
    acceder a la cadena como un todo o a las partes que la componen.
"""
serie = 'Juego de tronos'
print(serie)

print(serie[0])

print(serie[1])

print(serie[-1])

print(serie[-2])

print(serie[-3])

"""
Acceso a una subcadena:
    Para acceder a una procion de una cadena, es decir, a una 
    subcadena, hay que indicar la posicion de inicio y la posicion 
    limite separadas por dos puntos [posicion_inicio:posicion_limite]
    . Al escribir la posicion limite debemos tener cuidado, puesto 
    que el operador [posicion_inicio:posicion_limite] devuelve la 
    subcadena que va desde el caracter que ocupa la <<posicion_inicio>> 
    hasta el caracter que ocupa la <<posicion limite>>, sin incluirlo.
"""

print(serie[0:5])

print(serie[0:4])

print(serie[0:20])

print(serie[:5])

print(serie[9:])

print(serie[:])

"""
Operadores especiales:
    Existen 4 operadores que nos permiten operar con cadenas de texto:
    el operador de suma(+), el operador de asignacion de suma(+=), el
    operador de multipliacion(*) y el operador modulo(%).
"""

# (+) permite concatenar cadenas de caracteres, no incluye los espacios.

num_temp = 8

fecha_estreno = "22 de abril"

mensaje = "La temporada " + str(num_temp) + " de " + serie + " se estreno el " + fecha_estreno + " de 2019."

print(mensaje)

# (*) permite concatenar una cadena varias veces.

texto_a = "Hace " + 3 * "mucho " + "tiempo. . ."
print(texto_a)

texto_b = "Hace " + "mucho " * 3 + "tiempo. . ."
print(texto_b)

# (+=) permite agregar cadenas al final de una cadena de caracteres.

personajes = ["Daenerys Targaryen", "John Snow", "Ayra Stark", "Cersei Lannister"]

personajes_principales = ""

for nombre in personajes:
    personajes_principales += nombre + ", "
    
print(personajes_principales)

# (%) permite interpolar variables dentro de una cadena.

"""
Metodos para la manipulacion de cadenas.
"""

# len devuelve la longitud de la cadena
print(len(serie))

# count devuelve el numero de veces que se repite la subcadena
cadena = "Hace mucho mucho mucho tiempo..."
print(cadena.count("mucho"))

# find devuelve la posicion de la primera ocurriencia de la subcadena
frase = "Erase una vez una princesa llamada Jasmine."
print(frase.find("una"))

# index realiza lo misma funcion que el metodo find(), pero genera un error si no encuentra la subcadena.
print(frase.index("una"))

# rfind realiza la busqueda desde el final de la cadena
print(frase.rfind("una"))

# rindex realiza la busqueda desde el final de la cadena
print(frase.rindex("una"))

# capitalize devuelve una copia de la cadena convirtiendo el primer caracter a mayuscula y el resto a minuscula.
cadena = "pyTHon"
print(cadena.capitalize())

# lower devuelve una copia de la cadena convirtiendo todos los caracteres a minuscula
print(cadena.lower())

# upper devuelve una copia de la cadena convirtiendo todos los caracteres a mayuscula
print(cadena.upper())

# swapcase devuelve una copia de la cadena invirtiendo los caracters
print(cadena.swapcase())

# strip devuelve uan copia de la cadena tras eliminar los caracteres iniciales y finales
cadena = "\t Estoy aprendiendo mucho sobre Python. \n"
print(cadena.strip())

# lstrip elimina solamente los caracteres iniciales que corresponden 
print(cadena.lstrip())

# rstrip elimana solamente los caracteres finalesen lugar de los iniciales
print(cadena.rstrip())

# replace devuelve una copia de cadena tras reemplazar las ocurrencias de la subcadena
cadena = "Soy un excelente programador de Java."
print(cadena.replace("Java", "Python"))

# split divide la cadena utilizando un caracter separador indicado
cadena = "Grupo A\tGrupo B\tGrupo C"
print(cadena.split("\t"))

# join Devuelve una cadena resultante de unir las cadenas del iterable indicado como argumento
print(" - ".join(personajes))

"""
Formateo de una cadena
"""

# Operador % permite interpolar variables dentro de una cadena de caracteres

nombre = "Maria"
print("%s domina lenguajes como Java y C++ " %nombre)

nuevo_lenguaje= "Python"
print("%s domina lenguajes como Java y C++ y quiere aprender a programar %s" %(nombre, nuevo_lenguaje))


# Funcion str.format() permite realizar un formateo de la cadena desde la que se realiza la llamada.
print("{0} domina lenguajes como Java y C++ y quiere aprender a programar {1}".format(nombre, nuevo_lenguaje))

print("{nom} domina lenguajes como Java y C++ y quiere aprender a programar {nl}".format(nom =nombre, nl =nuevo_lenguaje))


# F-strings se representan con una f al principio y contienen llaves con las variables cuyos valores se insertan en la cadena
print(f"{nombre} domina lenguajes como Java y C++ y quiere aprender a programar {nuevo_lenguaje} \n")

print("---------")


"""
Extra
"""

def check(word1: str, word2: str):

    # Palíndromos
    print(f"¿{word1} es un palíndromo?: {word1 == word1[::-1]}")
    print(f"¿{word2} es un palíndromo?: {word2 == word2[::-1]}")

    # Anagramas
    print(f"¿{word1} es anagrama de {word2}?: {sorted(word1) == sorted(word2)}")

    # Isogramas

    def isogram(word: str) -> bool:

        word_dict = dict()
        for character in word:
            word_dict[character] = word_dict.get(character, 0) + 1

        isogram = True
        values = list(word_dict.values())
        isogram_len = values[0]
        for word_count in values:
            if word_count != isogram_len:
                isogram = False
                break

        return isogram

    print(f"¿{word1} es un isograma?: {isogram(word1)}")
    print(f"¿{word2} es un isograma?: {isogram(word2)}")


check("radar", "pythonpythonpythonpython")
# check("amor", "roma")
            
            
check("rallar", "seder")
check("caucasus", "seder")
check("caucasus", "ambidiestramente")
check("PUBVEXINGFJORD-SCHMALTZY", "hola")