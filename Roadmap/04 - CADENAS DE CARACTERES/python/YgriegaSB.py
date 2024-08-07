# Concatenacion
cadena1 = "Hola"
cadena2 = "Mundo"
concatenacion = cadena1 + " " + cadena2
print(concatenacion)  # Output: Hola Mundo

# Caracteres por indice
cadena = "Python"
primer_caracter = cadena[0]
print(primer_caracter)  # Output: P

# longitud 
cadena = "Python"
longitud = len(cadena)
print(longitud)  # Output: 6

# Subcadenas
cadena = "Python"
subcadena = cadena[2:5]
print(subcadena)  # Output: thon

# Busqueda de subcadenas
cadena = "Python es un lenguaje de programación"
subcadena = "lenguaje"
if subcadena in cadena:
    print("La subcadena está presente en la cadena")
else:
    print("La subcadena no está presente en la cadena")

# Conversion mayus y minus
cadena = "Python"
mayusculas = cadena.upper()
minusculas = cadena.lower()
print(mayusculas)  # Output: PYTHON
print(minusculas)  # Output: python

# Reemplazo de subcadenas
cadena = "Python es genial"
nueva_cadena = cadena.replace("genial", "increíble")
print(nueva_cadena)  # Output: Python es increíble

# separacion de cadenas en listas
cadena = "Python es genial"
palabras = cadena.split()
print(palabras)  # Output: ['Python', 'es', 'genial']

# Operaciones con cadenas de caracteres en Python

# Formateo de cadenas
nombre = "Juan"
edad = 30
cadena_formateada = "Mi nombre es {} y tengo {} años".format(nombre, edad)
print(cadena_formateada)  # Output: Mi nombre es Juan y tengo 30 años

# Concatenación de cadenas con la función join()
lista_palabras = ["Hola", "Mundo"]
cadena_concatenada = " ".join(lista_palabras)
print(cadena_concatenada)  # Output: Hola Mundo

# Eliminación de espacios en blanco
cadena_espacios = "    Python    "
cadena_sin_espacios = cadena_espacios.strip()
print(cadena_sin_espacios)  # Output: Python

# Conteo de ocurrencias de subcadenas
cadena = "Python es genial y Python es divertido"
conteo = cadena.count("Python")
print(conteo)  # Output: 2

# Verificación de si una cadena comienza o termina con una subcadena
cadena = "Python es genial"
print(cadena.startswith("Python"))  # Output: True
print(cadena.endswith("genial"))    # Output: True

# Reversión de una cadena
cadena = "Python"
cadena_reversa = cadena[::-1]
print(cadena_reversa)  # Output: nohtyP

# División de una cadena en subcadenas de longitud fija
cadena = "Python es genial"
subcadenas = [cadena[i:i+3] for i in range(0, len(cadena), 3)]
print(subcadenas)  # Output: ['Pyt', 'hon', ' es', ' ge', 'nia', 'l']

# Verificación de si una cadena contiene solo dígitos
cadena = "12345"
print(cadena.isdigit())  # Output: True

# Verificación de si una cadena contiene solo caracteres alfabéticos
cadena = "Python"
print(cadena.isalpha())  # Output: True

# Formateo de cadenas con f-strings (Python 3.6+)
nombre = "Juan"
edad = 30
cadena_formateada = f"Mi nombre es {nombre} y tengo {edad} años"
print(cadena_formateada)  # Output: Mi nombre es Juan y tengo 30 años

# Concatenación de cadenas con %
nombre = "Juan"
edad = 30
cadena_concatenada = "Mi nombre es %s y tengo %d años" % (nombre, edad)
print(cadena_concatenada)  # Output: Mi nombre es Juan y tengo 30 años

# Inversión de palabras en una cadena
cadena = "Hola Mundo"
palabras_invertidas = " ".join(reversed(cadena.split()))
print(palabras_invertidas)  # Output: Mundo Hola

# Relleno de cadenas con ceros a la izquierda
numero = 42
cadena_rellena = str(numero).zfill(5)
print(cadena_rellena)  # Output: 00042

# Búsqueda y reemplazo utilizando expresiones regulares
import re
cadena = "El número de teléfono es 123-456-7890"
nueva_cadena = re.sub(r'\b(\d{3})-(\d{3})-(\d{4})\b', r'(\1) \2-\3', cadena)
print(nueva_cadena)  # Output: El número de teléfono es (123) 456-7890

""" 
EJERCICIO
 * - Palíndromos: se lee igual hacia adelante que hacia atrás.
 * - Anagramas: se forman mediante la reorganización de las letras de otra palabra
 * - Isogramas: todas las letras en la palabra aparecen una sola vez
"""

print("\n --------------------------------------------------------- \n")

# check palindromo
def are_palindromos(word1, word2):
    reversed_word2 = word2[::-1]
    return reversed_word2 == word1

# check Anagramas
def are_anagramas(word1, word2):
    return sorted(word1) == sorted(word2)

# check Isogramas
def are_isogramas(word1, word2):
    for i in range(len(word1)):
        for j in range(i + 1, len(word1)):
            if word1[i] == word1[j]:
                return False
    for i in range(len(word2)):
        for j in range(i + 1, len(word2)):
            if word2[i] == word2[j]:
                return False
    return True


def check_words(word1, word2):
    if(are_palindromos(word1, word2) == True):
        print(f"Son Palindromos {word1} y {word2}")
    else:
        print(f"No son Palindromos {word1} y {word2}")
    if(are_anagramas(word1, word2) == True):
        print(f"Son Anagramas {word1} y {word2}")
    else:
        print(f"No son Palindromos {word1} y {word2}")
    if(are_isogramas(word1, word2) == True):
        print(f"Son Isogramas {word1} y {word2}")
    else:
        print(f"No son Palindromos {word1} y {word2}")

check_words("amor", "roma")
check_words("barco", "arco")
check_words("loma", "malo")