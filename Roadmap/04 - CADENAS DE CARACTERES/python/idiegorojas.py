# Cadenas de Caracteres

# Concatenacion
# Unir dos o mas cadenas
cadena_1 = 'Hola'
cadena_2 = 'Mundo'
resultado = cadena_1 + ' ' + cadena_2
print(resultado)

# Repeticion
# Repetir una cadena varias veces
cadena = 'Python'
resultado = cadena * 3
print(resultado)

# Acceso a caracteres
# Acceder a un caracter de la cadena mediante su indice
cadena = 'Python'
print(cadena[0])
print(cadena[-1])

# Subcadenas (slicing)
cadena = 'Python'
resultado = cadena[1:4]
print(resultado)

# Longitud
cadena = 'Python'
longitud = len(cadena)
print(longitud)

# Busqueda se subcadenas
cadena = 'Python es genial.'
posicion = cadena.find('es')
print(posicion)

# Reemplazar
cadena = 'Python es genial.'
nueva_Cadena = cadena.replace('genial', 'increible')
print(nueva_Cadena)

# Division
cadena = 'Python es genial.'
lista = cadena.split(" ")
print(lista)

# Union
lista = ['Python', 'es', 'genial.']
union = " ".join(lista)
print(union)

# Mayusculas y minusculas
cadena = 'Python'
mayuscula = cadena.upper()
minuscula = cadena.lower()
print(mayuscula)
print(minuscula)

# Eliminacion de espacios
# Elimina espacios en blanco al inicio y al final de una cadena
cadena = ' Python '
limpia = cadena.strip()
print(limpia)

# Formateo de cadenas
nombre = 'Python'
version = 3.12
mensaje = f'{nombre} version {version}'
print(mensaje)

mensaje = '{} version {}'.format(nombre, version)
print(mensaje)

# comprobacion de prefijos y sufijos.
cadena = 'Python es genial.'
print(cadena.startswith('Python'))
print(cadena.endswith('genial.'))

# Conversion a lista de caracteres
cadena = 'Python'
lista = list(cadena)
print(lista)

# Inversion de una cadena
cadena = 'Python'
invertida = cadena[::-1]
print(invertida)

# Comprobar contenido
cadena = 'Python 3.12'
print(cadena.isalpha()) # False por que contiene numeros
print(cadena.isdigit()) # False por que contiene letras
print(cadena.isalnum()) # True por que contiene letras y numeros

# Capitalizacion
cadena = 'python es genial.'
capitalizar = cadena.capitalize()
print(capitalizar)

# Conteo de subcadenas
cadena = 'Python es genial, Python esta en la version 3.12'
conteo = cadena.count('Python')
print(conteo)

# Verificacion de espacios
cadena = " "
print(cadena.isspace())

# Interpolacion de cadenas
nombre = 'Python'
version = 3.12
mensaje = 'Lenguaje: %s, Version: %.1f'%(nombre, version)
print(mensaje)


# Extra
def programa_palabras():
    
    palabra_1 = input('Por favor ingrese la primera palabra: ')
    palabra_2 = input('Por favor ingrese la segunda palabra: ')

    def limpiar_palabra(palabra):
        return palabra.replace(" ", "").lower()

    palabra_1_limpia = limpiar_palabra(palabra_1)
    palabra_2_limpia = limpiar_palabra(palabra_2)

    def palindromo():
        return palabra_1_limpia == palabra_2_limpia[::-1]

    def anagrama():
        return sorted(palabra_1_limpia) == sorted(palabra_2_limpia)

    def isograma(palabra):
        return len(palabra) == len(set(palabra))

    if palindromo():
        print(f'Las palabras "{palabra_1}" y "{palabra_2}" son palíndromos.')
    else:
        print(f'Las palabras "{palabra_1}" y "{palabra_2}" no son palíndromos.')

    if anagrama():
        print(f'Las palabras "{palabra_1}" y "{palabra_2}" son anagramas.')
    else:
        print(f'Las palabras "{palabra_1}" y "{palabra_2}" no son anagramas.')

    if isograma(palabra_1_limpia) and isograma(palabra_2_limpia):
        print(f'Las palabras "{palabra_1}" y "{palabra_2}" son isogramas.')
    else:
        print(f'Las palabras "{palabra_1}" y "{palabra_2}" no son isogramas.')

programa_palabras()