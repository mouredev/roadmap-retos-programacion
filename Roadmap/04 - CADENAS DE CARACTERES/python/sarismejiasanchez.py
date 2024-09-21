# #04 CADENAS DE CARACTERES
"""
 * EJERCICIO:
 * Muestra ejemplos de todas las operaciones que puedes realizar con cadenas de caracteres
 * en tu lenguaje. Algunas de esas operaciones podrían ser (busca todas las que puedas):
 * - Acceso a caracteres específicos, subcadenas, longitud, concatenación, repetición, recorrido,
 *   conversión a mayúsculas y minúsculas, reemplazo, división, unión, interpolación, 
verificación...
 *
"""
# Creando un string
print("Creando un string".upper())

letter = "S"                        # Un string puede ser un caracter o múltiples cadenas de texto
print(letter)                       # S
print(type(letter))                 # <class 'str'>

name = "Sara Mejia"                 # Se pueden definir con comillas dobles " "
print(name)                         # Sara
print(type(name))                   # <class 'str'>
alias = 'srismejiasanchez'          # Se pueden definir con comillas simples ' '
print(type(alias))                  # <class 'str'>

multiline_string = """\nEste es un string
con multiples
lineas\n"""
print(multiline_string)             # String multilinea con caracter de escape para salto de linea

multiline_string = '''Este también
es un string
con multiples
lineas'''
print(multiline_string)

# Acceso a caracteres específicos
print("\nAcceso a caracteres específicos".upper())

language = "Python"
# En programación los índices comienzan en cero
print(language[0])              # P
print(language[2])              # t
print(f"Último carácter: {language[-1]}")   # El recorrido inverso comienza en -1

# Subcadenas
print("\nSubcadenas".upper())
text = "Roadmap Retos de Programacion"
text_slice = text[7::]  # Retos de Programacion
print(f"Texto original: {text}")
print(f"Slicing: {text_slice}")

# Longitud
print("\nLongitud".upper())
text = "Thirty Days Of Python"
print(f"La longitud de la cadena {text} es {len(text)} caracteres.")

# Concatenación
print("\nConcatenación".upper())
name = "Sara"
surname = "Mejia"
age = 31

full_name = name, surname
print("Mi nombre es:", name , surname)      # Mi nombre es: Sara Mejia

information = "Nombre: " + name + ", Apellido: " + surname + ", Edad: " + str(age)
print(information)      # Nombre: Sara, Apellido: Mejia, Edad: 31

information = f"Mi nombre es {name} {surname}, y tengo {age} años."
print(information)      # Mi nombre es Sara Mejia, y tengo 31 años.

print("\n --Secuencias de Escape--".upper())
print("(\\n) Salto de línea: \nHola!")   # Salto de línea
print("(\\t) Esto es un \t tabulador.")   # Tabulación (4 espacios)
print('(\\) Símbolo backslash (\\)') # Simbolo backslash
print('Asi se incluye un texto entre comillas: "Hello, World!\"') # Comillas dobles dentro de comillas simples

# Repetición
print("\nRepetición".upper())
text = "Hello, Python! "
print(text * 4)     # Hello, Python! Hello, Python! Hello, Python! Hello, Python!

# Recorrido
print("\nRecorrido".upper())
language = "Python"

# Recorrido de izquierda a derecha
for letter in language:
    print(letter)

# Recorrido inverso y paso a mayúscula
for letter in language[::-1]:
    print(letter.upper())


# Conversión a mayúsculas y minúsculas
print("\nConversión a mayúsculas y minúsculas.. y métodos adicionales".upper())
course = "Roadmap Retos Programación"
print(f"Mayúscula: {course.upper()}")
print(f"Minúscula: {course.lower()}")
# Convierte el primer caracter del string a letra capital
print(f"Letra Capital: {course.capitalize()}")  # Roadmap retos programacion
text = "texto para titulo"
# Convierte a mayúscula inicial cada letra inicial del texto
print(f"Titulo: {text.title()}")    # Texto Para Titulo


# Reemplazo
print("\nReemplazo".upper())
# Replace the word coding in the string 'Coding For All' to Python.
text = "Coding For All"
print(text.replace("Coding", "Python"))

# División
print("\nDivisión".upper())
text = "Roadmap Retos Programacion"
print(text.split(" "))  # Separa la cadena por espacios en blanco
text = "Manzana,Naranja,Platano"
print(text.split(","))  # Separa la cadena por comas

# Tambien podríamos convertir el string a lista
text = list(text)
print(f"String a lista: \n{text}")

# Unión
print("\nUnión".upper())

languages = ['Python', 'JavaScript', 'Java', 'C#']
result = ', '.join(languages)
print(f"Lenguajes: {languages}")
print(f"Unión: {result}")

# Interpolación
print("\nInterpolación".upper())

# f-strings
name = "Sara"
surname = "Mejia"
saludo = f"Hola {name} {surname}! ¿Cómo estás?"
print(result)   # Hola Sara Mejia! ¿Cómo estás?

# format
saludo = "Hola {} {}! ¿Cómo estás?".format(name, surname)
print(saludo)

# %
saludo = "Hola %s %s. ¿Cómo estás?" % (name, surname) # %s strings
print(saludo)   # Hola Sara Mejia. ¿Cómo estás?

"""
* DIFICULTAD EXTRA (opcional):
* Crea un programa que analice dos palabras diferentes y realice comprobaciones
* para descubrir si son:
* - Palíndromos
* - Anagramas
* - Isogramas
"""
print("\nDIFICULTAD EXTRA")
from collections import Counter

def check_words(word_1, word_2):
    # Convertimos las palabras a minúsculas para evitar diferencias entre mayúsculas y minúsculas
    word_1, word_2 = word_1.lower(), word_2.lower()
    
    # Palíndromos
    # Palabras que se leen igual de izquierda a derecha y viceversa.
    print(f"¿{word_1} es Palindromo?: {word_1 == word_1[::-1]}")
    print(f"¿{word_2} es Palindromo?: {word_2 == word_2[::-1]}")

    # Anagramas
    # Ambas palabras tienen las mismas letras, solo en diferente orden.
    """
    Counter crea un diccionario donde las claves son los caracteres y los valores son las frecuencias de esos caracteres.
    """
    print(f"¿{word_1} y {word_2} son Anagramas?: {Counter(word_1) == Counter(word_2)}")

    # Isogramas
    # Palabras en las que ninguna letra se repite.
    print(f"¿{word_1} es Isograma?: {len(word_1) == len(set(word_1))}")
    print(f"¿{word_2} es Isograma?: {len(word_2) == len(set(word_2))}")

    
check_words("oso", "reconocer")
check_words("acto", "taco")
check_words("cielo", "mundo")