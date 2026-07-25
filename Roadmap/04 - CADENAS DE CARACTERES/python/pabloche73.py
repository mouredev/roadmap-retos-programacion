# Operaciones con cadenas

mi_cadena = "Hola Mundo!"
print(mi_cadena * 3) # Repetición
print(mi_cadena.title()) # Título, transforma la primera en mayúscula
print(mi_cadena.lower()) # Minúsculas

# Transformamos el texto en una lista y asignamos cada letra a una variable
a, b, c, d, e, f, g, h, i, j, k = list(mi_cadena) 
print (a)
print (b)
print (c)
print (d)
print (e)
print (f)
print (g)
print (h)
print (i)
print (j)
print (k)


print(mi_cadena.replace("!","!!!")) # Reemplazo
print(mi_cadena + ",que tal?") # Concatenación

print(mi_cadena[-2]) # Accedemos por indice a un caracter específico
print(mi_cadena[0])

mi_lista = mi_cadena.split() # Crea una lista a partir del texto
print(mi_lista)
nueva_cadena = "*".join(mi_lista) # Creacion y unión de una cadena a partir de una lista
print(nueva_cadena)

print(mi_cadena.count("u")) # Busca en la cadena y devuelve la cantidad de ocurrencias
print(mi_cadena.find("o")) # Busca en la cadena y devuelve el valor d ela primer ubicacion

print(mi_cadena[0:3])  # Slicing o rebanado
print(mi_cadena[::2])  

cadena_ordenada = sorted(mi_cadena.lower()) # Ordena la cadena
print (cadena_ordenada)

# Extra!!

def anagram (word1, word2):
    if sorted(word1.lower()) != sorted(word2.lower()):
        print (f"{word1} no es anagrama de {word2} o viceversa")
    else: 
        print (f"{word1} y {word2} son anagramas")

def palindromo (word1, word2):
    inversa = word1.lower()[::-1]
    if inversa == word2.lower():
        print (f"{word1} y {word2} son palíndromos")
    else:
        print (f"{word1} y {word2} no son palíndromos")

def isograma (word1, word2):
    """
    A continuacion comparamos el len del Set word1/word2 y el len de word1/word2
    Como el set no admite repetidos si hay letras repetidas en la palabra
    el set va a tener un len menor y devolver True
    """
    repeticion1 = len(set(word1)) < len(word1)
    repeticion2 = len(set(word2)) < len(word2)
    if repeticion1:
        print(f"{word1} no es un isograma")
    else:
        print(f"{word1} es un isograma")
    if repeticion2:
        print(f"{word2} no es un isograma")
    else:
        print(f"{word2} es un isograma")

correcta=True
while correcta:    
    palabra1=input("Palabra 1: ")
    palabra2=input("Palabra 2: ")
    if palabra1.lower() != palabra2.lower():
        anagram (palabra1, palabra2)
        palindromo(palabra1, palabra2)
        isograma(palabra1, palabra2)
        correcta = False
    else:
        print("Las palabras no pueden ser iguales")




    