"""
# #04 CADENAS DE CARACTERES
> #### Dificultad: Media | Publicación: 22/01/24 | Corrección: 29/01/24

## Ejercicio

```
/*
 * EJERCICIO:
 * Muestra ejemplos de todas las operaciones que puedes realizar con cadenas de caracteres
 * en tu lenguaje. Algunas de esas operaciones podrían ser (busca todas las que puedas):
 * - Acceso a caracteres específicos, subcadenas, longitud, concatenación, repetición, recorrido,
 *   conversión a mayúsculas y minúsculas, reemplazo, división, unión, interpolación, verificación...
 *

"""

Cadenas_caracteres1 = "Hola Mundo"
cadenas_caracteres2 = "Hola Mundo2"

print("Cadenas de caracteres: ", Cadenas_caracteres1)
print("Cadenas de caracteres 2: ", cadenas_caracteres2)

#concatenación
print("Longitud de la cadena 1 + 2: ", Cadenas_caracteres1 + " " + cadenas_caracteres2)

#repetición
print("Longitud de la cadena 1 varias veces: ", Cadenas_caracteres1 * 3)

#indexación
print("Primer caracter de la cadena 1: ", Cadenas_caracteres1[0])
print("Último caracter de la cadena 1: ", Cadenas_caracteres1[1])
print("Primer caracter de la cadena 2: ", Cadenas_caracteres1[2])
print("Último caracter de la cadena 2: ", Cadenas_caracteres1[3])

#longitud
print("Longitud de la cadena 1: ", len(Cadenas_caracteres1))
print("Longitud de la cadena 2: ", len(cadenas_caracteres2))

#slicing
print("Subcadena de la cadena 1: ", Cadenas_caracteres1[0:3])

#buscando un caracter
print("Buscando un caracter en la cadena 1: ", "a" in Cadenas_caracteres1)
print("Buscando un caracter en la cadena 1: ", "x" in Cadenas_caracteres1)

#reemplazo
print("Reemplazando un caracter en la cadena 1: ", Cadenas_caracteres1.replace("o", "a"))

#split
print("Dividiendo la cadena 1: ", Cadenas_caracteres1.split(" "))

#mayúsculas y minúsculas
print("Cadena 1 en mayúsculas: ", Cadenas_caracteres1.upper())
print("Cadena 1 en minúsculas: ", Cadenas_caracteres1.lower())
print("Cadena 1 en mayúsculas y minúsculas: ", Cadenas_caracteres1.swapcase())
print("Cadena 1 en mayúsculas y minúsculas: ", Cadenas_caracteres1.title())
print("Cadena 1 en mayúsculas y minúsculas: ", Cadenas_caracteres1.capitalize())

#Eliminacion de espacios al principio y al final de la cadena
cadena_espacios = "   Hola Mundo   "
print("Cadena con espacios al principio y al final: ", cadena_espacios)
print("Cadena sin espacios al principio y al final: ", cadena_espacios.strip())

#Busqueda al principio y al final de la cadena
print("Cadena empieza con 'Hola': ", Cadenas_caracteres1.startswith("Hola"))
print("Cadena termina con 'Mundo': ", Cadenas_caracteres1.endswith("Mundo"))
print("Cadena empieza con 'Mundo': ", Cadenas_caracteres1.startswith("Mundo"))

#Busqueda de posición de un caracter en la cadena
print("Posición del caracter 'Mun' en la cadena 1: ", Cadenas_caracteres1.find("Mun"))

#Busqueda de ocurrencias de un caracter en la cadena
print("Número de ocurrencias del caracter 'o' en la cadena 1: ", Cadenas_caracteres1.count("o"))

#Formateo de cadenas
print("Formateo de cadenas: ", "La cadena 1 es: {} y la cadena 2 es: {}".format(Cadenas_caracteres1, cadenas_caracteres2))

#Interpolación de cadenas
print(f"Interpolación de cadenas: La cadena 1 es: {Cadenas_caracteres1} y la cadena 2 es: {cadenas_caracteres2}")

#Transformación en lista de caracteres
print("Transformación en lista de caracteres: ", list(Cadenas_caracteres1))

#Transformación de lista de caracteres en cadena
cc=[Cadenas_caracteres1, " ", cadenas_caracteres2,"!"]
print("Transformación de lista de caracteres en cadena: ", ".".join(cc))

#Transformaciones numericas
cn= "123456"
print("Numero original: ", cn, type(cn))
print("Transformación a número: ", int(cn),type(int(cn)))
print("Transformación a número con decimales: ", float(cn),type(float(cn)))

#varias
print("Cadena 1 es alfanumérica: ", Cadenas_caracteres1.isalnum())
print("Cadena 1 es alfabética: ", Cadenas_caracteres1.isalpha())
print("Cadena numerica (cn) 1 es decimal: ", cn.isdecimal())
print("Cadena 1 es decimal: ", Cadenas_caracteres1.isdecimal())


"""
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que analice dos palabras diferentes y realice comprobaciones
 * para descubrir si son:
 * - Palíndromos
 * - Anagramas
 * - Isogramas
 """
def analisis_palabras(palabra1: str, palabra2: str):
    # Palíndromos
    es_palindromo1 = palabra1 == palabra1[::-1]
    es_palindromo2 = palabra2 == palabra2[::-1]

    # Anagramas
    es_anagrama = sorted(palabra1) == sorted(palabra2)

    # Isogramas
    es_isograma1 = len(set(palabra1)) == len(palabra1)
    es_isograma2 = len(set(palabra2)) == len(palabra2)

    print(f"Palabra 1: {palabra1}, Palíndromo: {es_palindromo1}, Isograma: {es_isograma1}")
    print(f"Palabra 2: {palabra2}, Palíndromo: {es_palindromo2}, Isograma: {es_isograma2}")
    print(f"¿Son anagramas?: {es_anagrama}")

analisis = analisis_palabras("radd", "ila")
print("Análisis de palabras: ", analisis)
