"""
Cadenas de caractéres
"""

msg1 = '¿Sabes de qué trabajo?'
msg2 = 'De programador'

# Curiosidades sobre print()
print(msg1, msg2) # Concatenación
print(msg1, msg2, sep="|")
print(msg1, msg2, end="!!")

print("")

"""Conversión a mayúsculas y minúsculas"""

my_string = "esta es una CAdena de caracteres"

print(my_string.capitalize()) # Cambia el primer caracter de la cadena por mayúscula.
print(my_string.upper()) # Cambia todos los caracteres por mayúsculas.
print(my_string.lower()) # Cambia todos los caracteres por minúsculas.
print(my_string.title()) # El primer caracter de cada palabra será convertido en mayúscula.
print(my_string.swapcase()) # Convierte las minúsculas en mayúsculas, y viceversa.

"""Longitud"""

print(len(my_string)) # Longitud de la cadena de caracteres.

"""Repetición"""

print(my_string * 4) # Repetir cadenas.

"""Obtención de caracteres"""

print(my_string[1]) # Obtener un caracter.
print(my_string[-1])

"""Subcadenas"""

print(my_string[4:]) # Obtener sub-cadenas.
print(my_string[:20]) # Todos los caracteres hasta el índice 20.
print(my_string[0:15]) # Caracteres desde el indice 0 hasta el 15.
print(my_string[5:11:2]) # Caracteres desde el índice 5 hasta el 11 haciendo saltos de 2.

"""Pertenencia"""

print("esta" in my_string)
print("no" is not my_string)
print("hola" in my_string)

number = "\n\t     18234612\n\n\n   \n\t"

# Eliminar caracteres
print(number.strip()) # Elimina todos los caracteres al principio y final de la cadena.
print(number.rstrip()) # Elimina todos los caracteres que estén a la derecha de la cadena.
print(number.lstrip()) # ELimina todos los caracteres que estén a la izquierda de la cadena.

"""Búsquedas"""

large_text = """Python es un lenguaje de programación
que se utiliza para Backend, Automatización
Ciencia de datos, Análisis de datos, etc.
"""

print(large_text.startswith("Python")) # Comprueba si empieza con la subcadena dada.
print(large_text.endswith("programación")) # Comprueba si termina con la subcadena dada.

print(large_text.find('Backend')) # Devuelve el índice donde se encuentra la subcadena, si no la encuentra, devuelve -1.
print(large_text.index('Análisis')) # Devuelve el índice donde se encuentra la subcadena, si no la encuentra, devuelve un error.

print(large_text.count('de')) # Contabiliza el número de veces que aparece una subcadena

"""Reemplazo"""

text = "Quien mal anda mal acaba"

print(text.replace('mal', 'bien')) # El primer argumento es la subcadena a reemplazar, el segundo es la subcadena de reemplazo.
print(text.replace('mal', 'bien', 1)) # Podemos indicar las veces que queremos reemplazar una subcadena.

"""Identificación"""

print('rd29'.isalnum()) # Detecta si los caracteres de una cadena son letras o numeros.
print('asj-29'.isalnum())

print('183'.isnumeric()) # Detecta si los caracteres de una cadena son numeros.
print('3.14'.isnumeric())

print('abcdef'.isalpha()) # Detecta si los caracteres de una cadena son letras.
print('a-b-c-d'.isalpha())

print('UPPER'.isupper()) # Detecta si los caracteres de una cadena son mayúsculas.
print('lower'.islower()) # Detecta si los caracteres de una cadena son minúsculas.
print('Hola Python'.istitle()) # Detecta si las palabras de una cadena empiezan con mayúscula.

"""Interpolación"""

name = 'Augusto'
age = 20
birthday = '28-08'

f_string = f'Me llamo {name}, tengo {age} años y mi cumpleaños es el {birthday}'
print(f_string)

# Formato a valores enteros

current_year = 2024

print(f'{current_year:10d}') # d viene de 'entero decimal'
print(f'{current_year:010d}')

# Formato a valores flotantes

PI = 3.14159265

print(f'{PI:f}') # Por defecto son 6 decimales
print(f'{PI:3f}') # f viene de 'flotante'

# Formato a cadenas de texto

my_text1 = "how"
my_text2 = "are"
my_text3 = "you"

print(f'{my_text1:<7s}|{my_text2:^11s}|{my_text3:>7s}')
print(f'{my_text1:-<7s}|{my_text2:.^11s}|{my_text3:->7s}')

"""Recorrido"""

language = 'Español'

for x in language:
    print(x)

"""División"""

programing_languages = "Python, Java, PHP, JavaScript, Dart"
print(programing_languages.split(',')) # Divide la cadena en una lista. En este caso lo separamos según las comas.

"""Unión"""

my_list = programing_languages.split(',')
print(" -".join(my_list)) # Une los valores de la lista en un string. En este caso separamos los elementos con " -"

"""
Dificultad EXTRA
"""

def analyze_words(word1, word2):

    print(f'¿{word1} y {word2} son anagramas? -> {sorted(word1) == sorted(word2)}')

    def no_space(text):
        nuevo_texto = ""
        for char in text:
            if char != " ":
                nuevo_texto += char
        return nuevo_texto
    
    def es_palindromo(text):
        text = no_space(text)
        result = ''
        for char in text:
            result += char
        if result[::-1].capitalize() == text:
            return True
        else:
            return False
    
    return (f'¿{word1} y {word2} son palíndromos? -> {es_palindromo(word1)}, {es_palindromo(word2)}')
        
print(analyze_words('Amo la paloma', 'Oso'))
print(analyze_words('Abba', 'Reconocer'))
print(analyze_words('Hola Mundo', 'Somos o no somos'))
print(analyze_words('lacteo', 'coleta'))