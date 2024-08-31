# Operaciones con cadenas en Python

# Acceso a caracteres específicos
s = "Hola, mundo!"
print(f"Carácter en la posición 0: {s[0]}")
print(f"Último carácter: {s[-1]}")

# Subcadenas
substring = s[6:11]
print(f"Subcadena desde la posición 6 hasta 10: {substring}")

# Longitud de la cadena
length = len(s)
print(f"Longitud de la cadena: {length}")

# Concatenación
s1 = "Hola"
s2 = "mundo"
concatenated = s1 + ", " + s2 + "!"
print(f"Concatenación de cadenas: {concatenated}")

# Repetición
repeated = s1 * 3
print(f"Repetición de cadena 'Hola' tres veces: {repeated}")

# Recorrido
for char in s:
    print(char, end=' ')
print()  # Salto de línea después del recorrido

# Conversión a mayúsculas y minúsculas
uppercase = s.upper()
lowercase = s.lower()
print(f"Mayúsculas: {uppercase}")
print(f"Minúsculas: {lowercase}")

# Reemplazo
replaced = s.replace("mundo", "Python")
print(f"Reemplazo de 'mundo' por 'Python': {replaced}")

# División
words = s.split(", ")
print(f"División de la cadena por ', ': {words}")

# Unión
joined = "-".join(words)
print(f"Unión de palabras con '-': {joined}")

# Interpolación de cadenas (format y f-string)
name = "Juan"
age = 30
formatted = "Mi nombre es {} y tengo {} años.".format(name, age)
f_string = f"Mi nombre es {name} y tengo {age} años."
print(formatted)
print(f_string)

# Verificación
contains_hola = "Hola" in s
print(f"La cadena contiene 'Hola': {contains_hola}")

# Conteo de ocurrencias
count_e = s.count('e')
print(f"Número de veces que 'e' aparece en la cadena: {count_e}")

# Búsqueda de subcadena
index_mundo = s.find('mundo')
print(f"Índice de la primera aparición de 'mundo': {index_mundo}")

# Verificación de mayúsculas/minúsculas
is_upper = s.isupper()
is_lower = s.islower()
print(f"¿Toda la cadena está en mayúsculas?: {is_upper}")
print(f"¿Toda la cadena está en minúsculas?: {is_lower}")

# Espacios en blanco
whitespace_string = "   Hola   "
stripped = whitespace_string.strip()
print(f"Cadena con espacios en blanco alrededor: '{whitespace_string}'")
print(f"Cadena sin espacios en blanco alrededor: '{stripped}'")

# Comprobación de tipo de caracteres
is_alpha_numeric = s.isalnum()
is_alpha = s.isalpha()
is_digit = s.isdigit()
print(f"¿La cadena es alfanumérica?: {is_alpha_numeric}")
print(f"¿La cadena contiene solo letras?: {is_alpha}")
print(f"¿La cadena contiene solo dígitos?: {is_digit}")


# Métodos de cadenas en Python

# Métodos de acceso y búsqueda
print(s.capitalize())  # Devuelve una copia de la cadena con el primer carácter en mayúscula.
print(s.casefold())    # Devuelve una versión de la cadena con todas las letras en minúsculas, adecuada para comparaciones sin distinción entre mayúsculas y minúsculas.
width = 20
print(s.center(width))  # Devuelve una cadena centrada en un ancho especificado, con relleno opcional.
sub = 'mundo'
print(s.count(sub))      # Cuenta el número de ocurrencias de una subcadena en la cadena.
encoding = 'utf-8'
print(s.encode(encoding))  # Codifica la cadena en bytes utilizando el formato especificado.
suffix = '!'
print(s.endswith(suffix))  # Devuelve True si la cadena termina con el sufijo dado, False de lo contrario.
tabsize = 8
print(s.expandtabs(tabsize))  # Expande las tabulaciones en la cadena utilizando espacios.
sub = 'mundo'
print(s.find(sub))       # Devuelve el índice de la primera ocurrencia de la subcadena, -1 si no se encuentra.

# Métodos de formato e información
print(s.format())        # Formatea la cadena con valores especificados.
mapping = {'name': 'Juan', 'age': 30}
print(s.format_map(mapping))  # Similar a format, pero utiliza un diccionario para proporcionar los valores.
sub = 'mundo'
print(s.index(sub))       # Devuelve el índice de la primera ocurrencia de la subcadena, genera una excepción si no se encuentra.
print(s.isalnum())        # Devuelve True si todos los caracteres de la cadena son alfanuméricos, False de lo contrario.
print(s.isalpha())        # Devuelve True si todos los caracteres de la cadena son alfabéticos, False de lo contrario.
print(s.isascii())        # Devuelve True si todos los caracteres de la cadena son ASCII, False de lo contrario.
print(s.isdecimal())      # Devuelve True si todos los caracteres de la cadena son decimales, False de lo contrario.
print(s.isdigit())        # Devuelve True si todos los caracteres de la cadena son dígitos, False de lo contrario.
print(s.isidentifier())   # Devuelve True si la cadena es un identificador válido, False de lo contrario.
print(s.islower())        # Devuelve True si todos los caracteres de la cadena están en minúsculas, False de lo contrario.
print(s.isnumeric())      # Devuelve True si todos los caracteres de la cadena son numéricos, False de lo contrario.
print(s.isprintable())    # Devuelve True si todos los caracteres de la cadena son imprimibles, False de lo contrario.
print(s.isspace())        # Devuelve True si todos los caracteres de la cadena son espacios en blanco, False de lo contrario.
print(s.istitle())        # Devuelve True si la cadena sigue el formato de título, False de lo contrario.
print(s.isupper())        # Devuelve True si todos los caracteres de la cadena están en mayúsculas, False de lo contrario.

# Métodos de manipulación y transformación
iterable = ['Hola', 'mundo']
print(s.join(iterable))   # Une los elementos de un iterable con la cadena como separador.
width = 20
print(s.ljust(width))     # Devuelve una cadena justificada a la izquierda en un ancho especificado.
print(s.lower())          # Devuelve una copia de la cadena con todos los caracteres en minúsculas.
print(s.lstrip())         # Devuelve una copia de la cadena con los espacios en blanco iniciales eliminados.
x = 'aeiou'
y = '12345'
z = '.,!'
translation_table = str.maketrans(x, y, z)
print(s.translate(translation_table))  # Aplica una tabla de traducción creada por maketrans.
sep = ','
print(s.partition(sep))   # Divide la cadena en una tupla (pre-sep, sep, post-sep).
old = 'mundo'
new = 'Python'
count = 1
print(s.replace(old, new, count))  # Reemplaza las ocurrencias de una subcadena con otra.
sub = 'mundo'
print(s.rfind(sub))       # Devuelve el índice de la última ocurrencia de la subcadena, -1 si no se encuentra.
print(s.rindex(sub))      # Devuelve el índice de la última ocurrencia de la subcadena, genera una excepción si no se encuentra.
width = 20
print(s.rjust(width))     # Devuelve una cadena justificada a la derecha en un ancho especificado.
sep = ','
maxsplit = 1
print(s.rsplit(sep, maxsplit))  # Divide la cadena en una lista de subcadenas, comenzando desde la derecha.
print(s.rstrip())         # Devuelve una copia de la cadena con los espacios en blanco finales eliminados.
sep = ','
maxsplit = 1
print(s.split(sep, maxsplit))   # Divide la cadena en una lista de subcadenas.
keepends = True
print(s.splitlines(keepends))   # Divide la cadena en una lista de líneas.
prefix = 'Hola'
start = 0
end = len(s)
print(s.startswith(prefix, start, end))  # Devuelve True si la cadena comienza con el prefijo dado, False de lo contrario.
chars = ' \t'
print(s.strip(chars))     # Devuelve una copia de la cadena con los caracteres iniciales y finales eliminados.
print(s.swapcase())       # Devuelve una copia de la cadena con las mayúsculas convertidas en minúsculas y viceversa.
print(s.title())          # Devuelve una versión de la cadena con cada palabra capitalizada.
print(s.translate(translation_table))  # Aplica una tabla de traducción creada por maketrans.
print(s.upper())          # Devuelve una copia de la cadena con todos los caracteres en mayúsculas.
width = 20
print(s.zfill(width))     # Rellena la cadena con ceros a la izquierda hasta alcanzar la longitud especificada.



# Ejercicio Extra

# * DIFICULTAD EXTRA (opcional):
# * Crea un programa que analice dos palabras diferentes y realice comprobaciones
# * para descubrir si son:
# * - Palíndromos
# * - Anagramas
# * - Isogramas

"""
Definicion:
    Palíndromo: 
    - Una palabra, frase o secuencia que se lee igual en ambos sentidos.
    Ejemplos: "reconocer, radar, oso, salas, anilina".
    Anagrama: 
    - Una palabra o frase formada reorganizando las letras de otra palabra o frase.
    Ejemplos: "amor/Roma, Avisar/Varias, Posta/Pasto", 
    Isograma: 
    - Una palabra en la que no hay letras repetidas (cada letra aparece una sola vez).
    Ejemplo: "murciélago, ligero, cumbre, farsante, ajedrez".

"""

import os
import signal
import sys
import time

## utilidades
# Colores y estilos
COLOR_RED = '91'
COLOR_BLUE = '34'
COLOR_CYAN = '96'
COLOR_GREEN = '32'
COLOR_YELLOW = '33'
COLOR_GRAY = '90'
COLOR_PURPLE = '95'
COLOR_BLACK = '30'
COLOR_WHITE = '37'

# Funcion generica para imprimir en color
def color_text(text, color_code, bold=False):
    bold_code = '1;' if bold else ''    
    return f"\033[{bold_code}{color_code}m{text}\033[0m"

# Funciones de impresión
def error(text, bold=False): print(color_text(text, COLOR_RED, bold=bold))       ###--- ROJO ---###
def info(text, bold=False): print(color_text(text, COLOR_BLUE, bold=bold))       ###--- AZUL ---###
def info_2(text, bold=False): print(color_text(text, COLOR_CYAN, bold=bold))       ###--- CYAN ---###
def success(text, bold=False): print(color_text(text, COLOR_GREEN, bold=bold))    ###--- VERDE ---###
def warning(text, bold=False): print(color_text(text, COLOR_YELLOW, bold=bold))  ###--- AMARILLO ---###
def debug(text, bold=False): print(color_text(text, COLOR_PURPLE, bold=bold))    ###--- PURPURA ---###
def debug_2(text, bold=False): print(color_text(text, COLOR_GRAY, bold=bold))      ###--- GRIS ---###
def others(text, bold=False): print(color_text(text, COLOR_BLACK, bold=bold))    ###--- NEGRO ---###
def standard(text, bold=False): print(color_text(text, COLOR_WHITE, bold=bold))  ###--- BLANCO ---###

# Función de captura de Ctrl+C
def sig_handler(sig, frame):
    warning('\n\n[!] Ejecucion cancelada por el usuario ...\n')
    sys.exit(1)

signal.signal(signal.SIGINT, sig_handler)

# Función para limpiar la terminal
def clean_terminal():
    os.system('clear' if os.name == 'posix' else 'cls')

def welcome():
    info('\n\n[+] Bienvenido al comprobador de palabras'.upper())
    info_2('\n[i] Introduzca una palabra para comprobar si es: Palindromo, Isograma, Anagrama')
    info_2('[i] Para salir escriba pulse "ctrl + C"')

def user_input():
    prompt_1 = '\n[+] Escriba la primera palabra:'
    prompt_2 = '\n[+] Escriba la segunda palabra:'
    
    while True:
        word_1 = input(''.format(info(prompt_1))).lower().strip()
        word_2 = input(''.format(info(prompt_2))).lower().strip()
        
        # Comprobar que solo sean letras
        if not word_1.isalpha() or not word_2.isalpha():
            warning('[!] Solo se permiten palabras, evite números, símbolos y espacios.')
        else:
            return (word_1.lower(), word_2.lower())
        
# Comprabar si text_ y word_2 son un palindromo
def is_palindrome(word_1: str, word_2: str):
    if word_1 == word_2[::-1]:
        success("[+] Las palabras forman un palíndromo.")
    else:
        error("[-] Las palabras no forman un palíndromo.")

# Comprobar si son isogramas
def is_isogram(word_1: str, word_2: str):
    success("[+] La primera palabra es un isograma.") if len(word_1) == len(set(word_1)) else error("[-] La primera palabra no es un isograma.")
    success("[+] La segunda palabra es un isograma.") if len(word_2) == len(set(word_2)) else error("[-] La segunda palabra no es un isograma.")
    
    word_3 = word_1 + word_2
    success("[+] El conjunto de las dos palabras forman un isograma.") if len(word_3) == len(set(word_3)) else error("[-] El conjunto de las dos palabras no forman un isograma.")

# Comprobar si es anagrama
def is_anagram(word_1: str, word_2: str):
    success("[+] Las palabras son un anagrama.") if sorted(list(word_1)) == sorted(list(word_2)) else error("[-] Las palabras no son un anagrama.")


# Entrada del programa
if __name__ == '__main__':

    clean_terminal()
    welcome()
    texts = user_input()
    info_2('\n[-]- SUS RESULTADOS -[-]\n')
    # Palindromo
    is_palindrome(word_1=texts[0], word_2=texts[1])
    # Isograma
    is_isogram(word_1=texts[0], word_2=texts[1])
    # Anagrama
    is_anagram(word_1=texts[0], word_2=texts[1])
    info_2('\n[-]- FINAL -[-]\n\n')
