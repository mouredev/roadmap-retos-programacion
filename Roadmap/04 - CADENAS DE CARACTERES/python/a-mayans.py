# Cadena de caracteres
cadena_caracteres = 'Bienvenido a Python'

# Acceso a caracteres específicos
print(cadena_caracteres[13]) # devuelve la letra que hay en la posicion indicada

# subcadenas
subcadena = cadena_caracteres[13:19]
print(subcadena) # indicando dos posiciones, desde donde (13) hasta donde (19 - 1)

# longitud
longitud = len(cadena_caracteres) # len calcula cuantos caracteres contiene la cadena, incluyendo los espacios
print(longitud)

# concatenación
nombre = 'Alex'
concatenado = cadena_caracteres + ' ' + nombre
print(concatenado)

# repetición
nickname = 'Mayi13 '
repeticion = nickname * 3 # la cadena se repite por las veces que se ha multiplicado
print(repeticion)

# recorrido
for caracter in cadena_caracteres: # recorre cada uno de los caracteres de la cadena
    print(caracter) # imprime caracter por caracter

# conversión a mayúsculas
conversion_mayusculas = cadena_caracteres.upper() # con upper devuelve la cadena entera en mayusculas
print(conversion_mayusculas)

# conversión a minúsculas
conversion_minusculas = cadena_caracteres.lower() # con lower devuelve la cadena entera en minusculas
print(conversion_minusculas)

# reemplazo
reemplazo = cadena_caracteres.replace('Bienvenido a', 'Aprendiendo') # indicando primero que queremos cambiar y por que lo queremos cambiar
print(reemplazo)

# división
cadena_dividida = cadena_caracteres.split(' ') # con split e indicando por donde queremos dividir la cadena, devuelve una lista de elementos
print(cadena_dividida)

# unión
cadena_unida = ' '.join(cadena_dividida) # unimos la lista de elementos en una cadena de nuevo separandolos con el espacio indicado ( ' ' )
print(cadena_unida)

# interpolación
interpolado = f'Hola, {cadena_caracteres.lower()}, {nombre}' # lo hacemos poniendo f antes de abrir comillas, y utilizando los {} para las variables
print(interpolado)

# verificación (retornará True o False)
print(cadena_caracteres.isalnum()) # retorna True si todos los caracteres de la cadena son alfanuméricos. Si esta vacio o no son alfanumericos retorna False
print(cadena_caracteres.isalpha()) # retorna True si todos los caracteres de la cadena son alfabéticos y si como mínimo hay uno.Si la cadena contiene espacios retorna False
print(cadena_caracteres.isascii()) # retorna True si la cadena de caracteres está vacía, o si todos los caracteres de la cadena son ASCII, en caso contrario, retorna False
print(cadena_caracteres.isdecimal()) # retorna True si todos los caracteres de la cadena son caracteres decimales y hay, al menos, un carácter, en caso contrario, retorna False
print(cadena_caracteres.isdigit()) # retorna True si todos los caracteres de la cadena son dígitos y hay, al menos, un carácter, en caso contrario, retorna False
print(cadena_caracteres.islower()) # retorna True si todos los caracteres son en minusuclas
print(cadena_caracteres.isupper()) # retorna True si todos los caracteres son en mayusculas
print(cadena_caracteres.isprintable()) # retorna True si todos los caracteres de la cadena son imprimibles o si la cadena esta vacia. De lo contrario retorna False
print(cadena_caracteres.isspace()) # retorna True si verifica que todos los caracteres en la cadena son caracteres de espacio en blanco
print(cadena_caracteres.istitle()) # retorna True si las palabras en la cadena tienen forma de título, de lo contrario retorna False
print(cadena_caracteres.startswith('Bien')) # retorna True si la cadena empieza por lo indicado. Es case sensitive (distingue entre mayusuclas y minusculas)
print(cadena_caracteres.endswith('n')) # retorna True si la cadena termina por lo indicado. Es case sensitive (distingue entre mayusuclas y minusculas)


# -------------------------------------------------------------------------------------------------------------------------------------------------------#

'''
/*
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que analice dos palabras diferentes y realice comprobaciones
 * para descubrir si son:
 * - Palíndromos
 * - Anagramas
 * - Isogramas
 */
'''

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

def palabras():
    palabra1 = input("Ingresa la primera palabra: ")
    palabra2 = input("Ingresa la segunda palabra: ")

    if palindromo(palabra1):
        print(f"{palabra1} es un palíndromo.")
    else:
        print(f"{palabra1} no es un palíndromo.")
    
    if palindromo(palabra2):
        print(f"{palabra2} es un palíndromo.")
    else:
        print(f"{palabra2} no es un palíndromo.")

    if anagrama(palabra1, palabra2):
        print(f"{palabra1} y {palabra2} son anagramas.")
    else:
        print(f"{palabra1} y {palabra2} no son anagramas.")

    if isograma(palabra1):
        print(f"{palabra1} es un isograma.")
    else:
        print(f"{palabra1} no es un isograma.")

    if isograma(palabra2):
        print(f"{palabra2} es un isograma.")
    else:
        print(f"{palabra2} no es un isograma.")

palabras()