
"""
 * EJERCICIO:
 * Muestra ejemplos de todas las operaciones que puedes realizar con cadenas de caracteres
 * en tu lenguaje. Algunas de esas operaciones podrían ser (busca todas las que puedas):
 * - Acceso a caracteres específicos, subcadenas, longitud, concatenación, repetición, recorrido,
 *   conversión a mayúsculas y minúsculas, reemplazo, división, unión, interpolación, verificación...
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que analice dos palabras diferentes y realice comprobaciones
 * para descubrir si son:
 * - Palíndromos
 * - Anagramas
 * - Isogramas
 */
"""

### OPERACIONES CON CADENAS DE CARACTERES ###

# Acceso a caracteres específicos
cadena = "Hola mundo"
print(cadena[0]) # H

# Subcadenas
print(cadena[0:4]) # Hola

# Longitud
print(len(cadena)) # 10

# Concatenación
cadena2 = "Adios mundo"
print(cadena + " " + cadena2) # Hola mundo Adios mundo

# Repetición
print(cadena * 3) # Hola mundoHola mundoHola mundo

# Recorrido
for i in cadena:
    print(i) # H o l a   m u n d o
    
# Conversión a mayúsculas y minúsculas
print(cadena.upper()) # HOLA MUNDO
print(cadena.lower()) # hola mundo

# Reemplazo
print(cadena.replace("Hola", "Adios")) # Adios mundo

# División
print(cadena.split(" ")) # ['Hola', 'mundo']

# Unión
print(" ".join(cadena.split(" "))) # Hola mundo

# Interpolación
print("Hola %s" % "mundo") # Hola mundo

# Verificación
print("Hola" in cadena) # True
print("Hola" not in cadena) # False


## Sirven con cadenas de carácteres y con palabras ##
# Buscar posición de un caracter
print(cadena.find("o")) # 1

# Buscar posición de un caracter desde el final
print(cadena.rfind("o")) # 7

# Conteo de caracteres
print(cadena.count("o")) # 2

# Comprobar si una cadena empieza por un caracter
print(cadena.startswith("H")) # True

# Comprobar si una cadena termina por un caracter
print(cadena.endswith("o")) # True

# Eliminar espacios en blanco al principio y al final
cadena3 = "  Hola mundo  "
print(cadena3.strip()) # Hola mundo

# f-strings
nombre = "Jota"
edad = 23
print(f"Hola {nombre}, tienes {edad} años") # Hola Jota, tienes 23 años

# Format
print("Hola {}, tienes {} años".format(nombre, edad)) # Hola Jota, tienes 23 años

# Comprobar si una cadena es alfanumérica
print(cadena.isalnum()) # False

# Comprobar si una cadena es alfabética
print(cadena.isalpha()) # False

# Comprobar si una cadena es numérica
print(cadena.isnumeric()) # False

# Comprobar si una cadena es decimal
print(cadena.isdecimal()) # False

# Comprobar si una cadena es un dígito
print(cadena.isdigit()) # False

# Comprobar si una cadena es un identificador válido
print(cadena.isidentifier()) # False

# Comprobar si una cadena es imprimible
print(cadena.isprintable()) # True

# Comprobar si una cadena es un espacio
print(cadena.isspace()) # False

# Capitalización de la primera letra de cada palabra
print(cadena.title()) # Hola Mundo

# Cambiar de mayúsculas a minúsculas y viceversa
print(cadena.swapcase()) # hOLA MUNDO
print(cadena.swapcase().swapcase()) # Hola mundo







### PALÍNDROMOS, ANAGRAMAS E ISOGRAMAS ###

## PALÍNDROMOS
# Los palíndronos son palabras que se leen igual de izquierda a derecha que de derecha a izquierda

# Función óptimizada
def isPalindromo(cadena):
    cadena = cadena.lower()
    return cadena == cadena[::-1]

# Función no óptimizada
def isPalindromo2(cadena):
    tamano = len(cadena)
    cadena = cadena.lower()
    if tamano/2 == 0:
        for i in range(0, tamano/2): # Si el tamaño es par
            if cadena[i] != cadena[tamano - i]:
                return False
    else:
        tamano = tamano - 1 # la palabra tiene 3 letras, y los indices van de 0 a 2. 
        for i in range(0, tamano//2): # Si el tamaño es impar, tamano//2 redondea hacia abajo
            if cadena[i] != cadena[tamano - i]:
                return False
    return True

## ANAGRAMAS 
# Los anagramas son palabras que tienen las mismas letras pero en diferente orden

# Función óptimizada
def isAnagrama(cadena1, cadena2):
    cadena1 = sorted(cadena1.lower())
    cadena2 = sorted(cadena2.lower())
    print(f"cadena1: {cadena1} cadena2: {cadena2}")
    return cadena1 == cadena2

# Función no óptimizada (fallo, cuando una letra se repite en la primera palabra y en la segunda se repite una letra diferente)
# Ejemplo: retener y enteere, da positivo al tener el mismo tamaño y las mismas palabras únicas, pero la e se repite 3 y 4 veces. 
def isAnagrama2(cadena1, cadena2):
    cadena1 = cadena1.lower()
    cadena2 = cadena2.lower()
    letras1 = {}
    letras2 = {}
    for letra in cadena1:
        letras1[letra] = letras1.get(letra, 0) + 1
                           
    for letra in cadena2:
        letras2[letra] = letras2.get(letra, 0) + 1

    return letras1 == letras2    

# Prueba palíndromos
print("*** PALÍNDROMOS ***")
palabra = "Anabel"
palabra2 = "Holaaloh"

print(isPalindromo(palabra)) # True
print(isPalindromo(palabra2)) # False

print(isPalindromo2(palabra)) # True
print(isPalindromo2(palabra2)) # False

# Prueba anagramas
print("*** ANAGRAMAS FALSE***")
palabra3 = "retener"
palabra4 = "entere"

print(isAnagrama(palabra3, palabra4)) # False
print(isAnagrama2(palabra3, palabra4)) # False

print("*** ANAGRAMAS TRUE***")
palabra3 = "retener"
palabra4 = "enterre"

print(isAnagrama(palabra3, palabra4)) # True
print(isAnagrama2(palabra3, palabra4)) # True

## ISOGRAMAS de primer orden
# Los isogramas son palabras que no tienen letras repetidas y todas ellas se repiten el mismo número de veces

# Función óptimizada
def isIsograma(cadena):
    cadena = cadena.lower()
    return len(cadena) == len(set(cadena))

# Función sin optimizar
def isIsograma2(cadena):
    letras = {}
    for letra in cadena:
        letras[letra] = letras.get(letra, 0) + 1
        if letras[letra] > 1:
            return False
    return True

# Prueba isogramas
print("*** ISOGRAMAS ***")
palabra5 = "murcielago"
palabra6 = "murcielagoos"

print(isIsograma(palabra5)) # True
print(isIsograma(palabra6)) # False

print(isIsograma2(palabra5)) # True
print(isIsograma2(palabra6)) # False

## Isogramas de orden N 

def isogramasN(cadena):
    cadena = cadena.lower()
    letras = {}
    for letra in cadena:
        letras[letra] = letras.get(letra, 0) + 1
    #Compruebo que todas las letras tengan el mismo número de repeticiones
    repeticiones = letras.get(cadena[0])
    for letra in letras:
        if letras[letra] != repeticiones:
            return False
    return repeticiones

# Prueba isogramas de orden N

print("*** ISOGRAMAS DE ORDEN N ***")
palabra = "murcielago"
print(f"La palabra {palabra} es un isograma de orden {isogramasN(palabra)}") # 1

palabra = "murcielagomurcielago"
print(f"La palabra {palabra} es un isograma de orden {isogramasN(palabra)}") # 2

palabra = "murcielagomurcielagomurcielago"
print(f"La palabra {palabra} es un isograma de orden {isogramasN(palabra)}") # 3
