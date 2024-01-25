"""
Muestra ejemplos de las operaciones con cadenas de caracteres
Acceso a caracteres especificos, subcadenas, longitud, concatenación
repetición, recorrido
Conversión a mayusculas y minusculas, reemplazo división, union, interpolación
verificación etc
"""

# Concatenación
cad_1 = "Hola"
cad_2 = " mundo"
concatena = cad_1+cad_2
print(concatena)

# Replica de una cadena
cadena = "Hola "
resultado = cadena * 3
print(resultado)

# Longitud de una cadena
cadena = "Hola Python"
longitud = len(cadena)
print(longitud)

# Acceso a caracteres
cadena = "Hola Python"
primer_caracter = cadena[0]
sexto_caracter = cadena[5]
print(primer_caracter, sexto_caracter)

# Acceso a caracteres
ultimo_caracter = cadena[-1]
anteultimo_caracter = cadena[-2]
print(ultimo_caracter, anteultimo_caracter)

# subcadena
cadena = "Python hello"
subcadena = cadena[4:9]
print(subcadena)


cadena = "Hola, Mundo!"
Palabras = ["hola", "mundo", "python"]

# Poner en mayúsculas toda la cadena
mayusculas = cadena.upper()
print(mayusculas)

# Poner en minúsculas toda la cadena
minusculas = cadena.lower()
print(minusculas)

# Quitar los espacios a la cadena
sin_espacios = cadena.strip()
print(sin_espacios)

# Reeplazar la cadena o parte de la cadena
reemplazar = cadena.replace("Hola", "Saludos")
print(reemplazar)

# Separar en cadenas
separa = cadena.split(" ")
print(separa)

# Unir varias cadenas de texto
unir = " ".join(Palabras)
print(unir)

# interpolación de varaibles
nombre = "Aldroide"
edad = 40
interpolar = f"Soy {nombre} y tengo {edad} años"
print(interpolar)

# Revisar si es numero o digito
mi_numero = "123435"
print(mi_numero.isdigit())
print(mi_numero.isnumeric())

cadena = "Aldroide"
print(cadena.isalpha())
print(cadena.isalnum())
print(cadena.startswith("R"))
print(cadena.endswith("f"))
print(cadena.islower())
print(cadena.isupper())
print(cadena.isspace())

cadena = "esta cadena inicia en minúscula"
print(cadena.capitalize())


"""
Ejercicio extra 
Crear un programa que analice dos palabras diferentes
y realice comprobaciones para descubrir si son:
 * Palindromos
 * Anagramas
 * Isogramas
"""


def palindromo(palabra):
    palabra = palabra.lower().replace(" ", "")
    return palabra == palabra[::-1]


def anagrama(palabra1, palabra2):
    palabra1 = palabra1.lower().replace(" ", "")
    palabra2 = palabra2.lower().replace(" ", "")
    return sorted(palabra1) == sorted(palabra2)


def isograma(palabra):
    palabra = palabra.lower().replace(" ", "")
    return len(set(palabra)) == len(palabra)


palabra1 = input("Introduce la primera palabra: ")
palabra2 = input("Introduce la segunda palabra: ")

print(
    f"La palabra {palabra1} ¿Es anagrama de {palabra2}?: {anagrama(palabra1, palabra2)}")
print(f"La palabra {palabra1} ¿Es palindromo?: {palindromo(palabra1)}")
print(f"La palabra {palabra2} ¿Es palindromo?: {palindromo(palabra2)}")
print(f"La palabra {palabra1} ¿Es isograma?: {isograma(palabra1)}")
print(f"La palabra {palabra2} ¿Es isograma?: {isograma(palabra2)}")
