"""
Operaciones con cadenas
"""

# Concatenar
c1 = "Hola"
c2 = "python"

c3 = c1 + " " + c2 # Podemos concatenar con strings fuera de variables
print(c3)

# Repetición
print(c3 * 3)

# Index
print(c3[1]) # Desde el indice 1

# Longitud
print(len(c3))

# Slicing
print(c3[3:7]) # Recorre del 3 al 6
print(c3[3:]) # Recorre del 3 al final
print(c3[:4]) # Recorre del principio hasta el 3

# Busqueda
print("a" in c3) # True
print("w" in c3) # False

# Remplazo
print(c1.replace("o", "a"))

# División
print(c3.split(" ")) # Dividimos por espacio (" ")

# Conversión
# Mayusculas
print(c3.upper())

# Minusculas
print(c3.lower())

# Primera letra mayusculas de cada palabra
print(c3.title())

# Solo primera letra de la primera palabra
print(c3.capitalize())

# Eliminación de espacio al principio y al final
print(" juanma gonzalez ". strip())

# Busqueda al principio y final
print(c3.startswith("H"))
print(c3.endswith("on"))

# Busqueda de posición
# Muestra el indice donde comienza la palabra
print("Hola Juanma como estas hoy?".find("estas"))

# Busqueda de ocurrencia
print(c3.count("o")) # Cuantas veces aparece el caracter o palabra

# Formateo
print("Saludo: {}, lenguaje: {}!".format(c1, c2))

# f string(Python), interpolación (lenguajes) 
print(f"Saludo: {c1}, lenguaje: {c2}")

# Transformacion en lista de caracteres
print(list(c3))

c4 = list(c3)

# Transformación de lista en cadena
print(c4)
print("".join(c4))

# Transformaciones númericas
c4 = "12345" # Texto
print(c4)
print(type(c4))
c4 = int(c4) # Integer
print(c4)
print(type(c4))
c4 = float(c4) # Float
print(c4)
print(type(c4))

"""
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que analice dos palabras diferentes y realice comprobaciones
 * para descubrir si son:
 * - Palíndromos
 * - Anagramas
 * - Isogramas
"""


def check_palabra(palabra1, palabra2) -> str:
    # Palindromos
    palindromo(palabra1)
    palindromo(palabra2)
    
    # Anagramas
    anagrama(palabra1, palabra2)

    # heterograma
    heterograma(palabra1)
    heterograma(palabra2)
    
    # Isograma
    isograma(palabra1)
    isograma(palabra2)

        
def palindromo(palabra):
    """Esta función se encarga de mirar si la palabra y la palabra ordenada al
    revés son iguales"""
    if palabra == palabra[::-1]:
        print(f"La palabra {palabra} es un palíndromo")

    else:
        print(f"La palabra {palabra} no es un palíndromo")

def anagrama(palabra1, palabra2):
    """Esta función se encarga de mirar si las palabras ordenandolas por orden
    alfabetico son iguales"""
    if sorted(palabra1) == sorted(palabra2):
        print(f"La palabra {palabra1} y la palabra {palabra2} son anagramas")
    else:
        print(f"La palabra {palabra1} y la palabra {palabra2} no son anagramas")

def heterograma(palabra):
    """Esta funcón compara la longitud de la palabra con la longitud del set
    de esa palabra, el set elimina los caracteres repetidos asi que si las 
    longitudes son iguales no hay caracteres repetidos"""
    if len(palabra) == len(set(palabra)):
        print(f"La palabra {palabra} es un heterograma")
    else:
        print(f"La palabra {palabra} no es un heterograma")

def isograma(palabra):
    """Esta función almacena el numero de veces que sale cada letra en una
    palabra para ver si es exactamente el mismo siempre que sean 2 o mas"""
    dict_palabra = dict()
    for letra in palabra:
        dict_palabra[letra] = dict_palabra.get(letra, 0) + 1
    isograma = True
    values = list(dict_palabra.values())
    isograma_len = values[0]
    if isograma_len <= 1: 
        isograma = False
        print(f"La palabra {palabra} es un isograma? {isograma}")
    else: 
        for contador_letra in values:
            if (contador_letra != isograma_len):
                isograma = False
                print(f"La palabra {palabra} es un isograma? {isograma}")
        
        print(f"La palabra {palabra} es un isograma? {isograma}")
            
# Caso de uso             
check_palabra("radar", "python")
check_palabra("amor", "roma")
check_palabra("radar", "pythonpython")
