'''
 * EJERCICIO:
 * Muestra ejemplos de todas las operaciones que puedes realizar con cadenas de caracteres
 * en tu lenguaje. Algunas de esas operaciones podrían ser (busca todas las que puedas):
 * - Acceso a caracteres específicos, subcadenas, longitud, concatenación, repetición,
 *   recorrido, conversión a mayúsculas y minúsculas, reemplazo, división, unión,
 *   interpolación, verificación...
 *
'''

from collections import Counter

# el clásico string:
hola = "El veloz murcielago hindú comía feliz cardillo y kiwi."
print(hola)

# subcadena, acceso a caracteres específicos
subcadena = hola[0:4]
print(subcadena)

# longitud de la cadena
print(f"La cadena {hola} tiene {len(hola)} caracteres")

# concatenación
test_concatenar = "murcielago" + " " + "hipopotamo" + "(concatenado)"
print(test_concatenar)

# Aprovechamos la repeción para crear un separador
def separador():
    print("-" * 25)

separador()

# recorrido
for i in hola:
    print(i)

# conversión a mayúsculas, minúsculas, capitalizar, titulo e invertir
def transformacion(s):
   return s.upper(), s.lower(), s.capitalize(), s.title(), s.swapcase()

print(transformacion(hola))

# reemplazo
print(f"Transformacion:\n {'\n'.join(transformacion(hola))}")

# división
separacion = hola.split(" ")
print(separacion)
print(separacion[-1]) # accedemos a la ultima palabra

# unión, volvemos a unir la cadena con algun extra
continua = "con su amigo el hipopotamo."
continua2 = continua.split(" ")


del separacion[6:] # borramos parte de la lista

# Ahora si, unimos las dos listas en un string
union = separacion + continua2
union = " ".join(union)
print(union)

# interpolación
# Print con f-strings
print(f"""La frase inicial era:
      \n - '{hola}'
      \ny ahora es:
      \n - '{union}'""")

# Print con format
print("""La frase inicial era:
      \n - '{}'
      \ny ahora es:
      \n - '{}'""".format(hola, union))

# verificación del string
hola_num = "1234"
text = "hola mundo, esto es una prueba 1 2 3"
print(hola_num.isalnum()) # comprobamos si es alfanumerico en una variable de solo numeros
print(text.isalpha()) # comprobamos si es alfabetico
print(hola_num.isdigit()) # comprobamos si es numerico
print(text.islower()) # comprobamos si esta en minusculas
print(text.isupper()) # comprobamos si esta en mayusculas
print(text.isspace()) # comprobamos si esta en espacios
print(text.istitle()) # comprobamos si esta en titulo
print(text == "") # comprobamos si esta vacio


'''
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que analice dos palabras diferentes y realice comprobaciones
 * para descubrir si son:
 * - Palíndromos
 * - Anagramas
 * - Isogramas
'''

# Palindromo si es un palindromo, que se lea igual de izquierda a derecha o al revés
def palindromo(palabra1, palabra2):
    palabra1 = palabra1.lower()
    if palabra1 == palabra1[::-1]:
        print(f"{palabra1} es un palíndromo")
    if palabra2 == palabra2[::-1]:
        print(f"{palabra2} es un palindromo")
    else:
        print(f"Ni {palabra1} ni {palabra2} son palíndromos")

# Anagrama, comprobamos si cambiando el orden puede formar otra palabra
def anagrama(palabra1, palabra2):
    pass

# Isograma, cada letra aparece el mismo número de veces
def isograma(palabra):
    # convert the word to lowercase and count the occurrences of each letter
    counts = Counter(palabra.lower())
    
    # if all letters appear the same number of times, it's an isogram
    if len(set(counts.values())) == 1:
        print(f"{palabra} es un isograma")
    else:
        print(f"{palabra} no es un isograma")

# Comprobamos si es un isograma
isograma("abba")  # es un isograma
isograma("calabaza")  # no es un isograma


# Heterograma, que no tiene ninguna letra repetida
def heterograma(palabra1, palabra2):
    # convert the word to lowercase and create a set of its letters
    letras1 = set(palabra.lower())
    letras2 =
    
    # if the length of the set is equal to the length of the word, it's a heterogram
    if len(letras1) == len(palabra):
        print(f"{palabra1} es un heterograma")
    else:
        print(f"{palabra} no es un heterograma")

# comprobamos si es un heterograma
heterograma("esternocleidomastoideo")  # no es un heterograma
heterograma("centrifugado")  # es un heterograma
