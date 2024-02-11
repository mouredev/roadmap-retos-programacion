"""04 CADENAS DE CARACTERES
Dificultad: Media | Publicación: 22/01/24 | Corrección: 29/01/24

Ejercicio

/*
 * EJERCICIO:
 * Muestra ejemplos de todas las operaciones que puedes realizar con cadenas de caracteres
   en tu lenguaje. Algunas de esas operaciones podrían ser (busca todas las que puedas):
 * - Acceso a caracteres específicos, subcadenas, longitud, concatenación, repetición, recorrido,
 *   conversión a mayúsculas y minúsculas, reemplazo, división, unión, interpolación, verificación...
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que analice dos palabras diferentes y realice comprobaciones
   para descubrir si son:
 * - Palíndromos
 * - Anagramas
 * - Isogramas
 */"""


texto_1 = "    la casa es roja y dentro está la caja"
texto_2 = "el coche tiene cuatro ruedas"
texto_3 = "2342"

print(":::::::::::::::::::: MÉTODOS CON CADENAS ::::::::::::::::::::")
print()
print(f"Texto original 1: {texto_1.capitalize()}")
print(f"Texto original 2: {texto_2.capitalize()}")
print()

# Capitalize: pone la primera letra del string en mayúscula
print(f"Método capitalize: {texto_1.capitalize()}")

# Center: centra el texto con dejando un espacio en los laterales con el número de caracteres indicado o un caracter
#         en caso de poner un segundo parámetro
print(f"Método center: [{texto_1.center(30)}] ")
print(f"Método center: [{texto_1.center(30, '*')}] ")

# Endswith: devuelve true o false si la cadena termina con el argumento especificado
print(f"Método endswith: la frase acaba en ja --> {texto_1.endswith("ja")}")
print(f"Método endswith: la frase acaba en on --> {texto_1.endswith("on")}")


# Startswith: devuelve true o false si la cadena termina con el argumento especificado
print(f"Método startswith: la frase empieza con un espacio --> {texto_1.startswith(" ")}")
print(f"Método startswith: la frase empieza por 'on' --> {texto_1.startswith("on")}")


# Find: devuelve la primera ocurrencia en una cadena de la subcadena indicada en el parámetro. Con un segundo parámetro,
#       se especifica en qué posición empieza a buscar
print(f"Método find: posición {texto_1.find("ro")}")
print(f"Método find: posición {texto_1.find("ro", 12)}")


# Isalnum: cualquier elemento de cadena que no sea un dígito o una letra hace que el método regrese False.
#          Los espacios en blanco no cuentan como letra ni número, por tanto, de haberlos resultará False.
if texto_1.isalnum():
    print(f"Método Isalnum: '{texto_1}' solo contiene letras y/números")
else:
    print(f"Método Isalnum: '{texto_1}' no contiene letras ni números")


# Isalpha: comprueba que todos los caracteres de la cadena sean letras. De ser así, dará True. El espacio no cuenta como
#          letra, por tanto, de haberlo dará False.
if texto_1.isalpha():
    print(f"Método isalpha: el texto solamente contiene letras")
else:
    print(f"Método isalpha: el texto contiene algo que no son letras")


# Isdigit: comprueba que todos los caracteres de la cadena sean dígitos. De ser así, dará True. El espacio no cuenta
#          como dígito, por tanto, de haberlo dará False.
if texto_3.isdigit():
    print(f"Método isdigit: el texto solamente contiene dígitos")
else:
    print(f"Método isdigit: el texto contiene algo que no son dígitos")


# Islower: comprueba que solo haya minúsculas. Los espacios no se tienen en cuenta.
if texto_1.islower():
    print(f"Método islower: el texto solamente contiene minúsculas")
else:
    print(f"Método islower: el texto contiene algo que no son minúsculas")


# Isupper: comprueba que solo haya mayúsculas. Los espacios no se tienen en cuenta.
if texto_1.isupper():
    print(f"Método isupper: el texto solamente contiene mayúsculas")
else:
    print(f"Método isupper: el texto contiene algo que no son mayúsculas")


# isspace: comprueba si sólamente hay espacios en blanco (si hay algún otro caracter, da false)
if texto_1.isspace():
    print(f"Método isspace: el string solamente contiene espacios")
else:
    print(f"Método isspace: el string no contiene solamente espacios")


# Lstrip: elimina todos los espacios en blanco de una cadena. Si tiene un argumento, eliminar todos los carateres
#          iniciales que estén en dicho argumento
print(f"Método lstrip: {texto_1.lstrip()}")
print(f"Método lstrip con argumento: {texto_1.lstrip(" la")}")


# Rstrip: lo mismo que lstrip pero empezando por el final de string
print(f"Método rstrip: {texto_1.rstrip()}")
print(f"Método rstrip con argumento: {texto_1.rstrip(" la")}")


# Replace: con dos parámetros devuelve una copia de la cadena original en la que todas las apariciones del primer
#          argumento han sido reemplazadas por el segundo argumento.
print(f"Método replace: {texto_1.replace(" ", "*")}")


# Split: El método split() divide la cadena y crea una lista de todas las subcadenas detectadas. El método asume que
#        las subcadenas están delimitadas por espacios en blanco, los espacios no participan en la operación y no se
#        copian en la lista resultante.
print(f"Método split: {texto_1.split()} ")


# Strip: combina los efectos causados por rstrip() y lstrip(), crea una nueva cadena que carece de todos los espacios
#        en blanco iniciales y finales.
print(f"Método strip: {texto_1.strip()}")


# Swapcase: crea una nueva cadena intercambiando todas las letras por mayúsculas o minúsculas dentro de la cadena
#           original: los caracteres en mayúscula se convierten en minúsculas y viceversa.
print(f"Método swapcase{texto_1.swapcase()}")


# Upper: hace una copia de la cadena de origen, reemplaza todas las letras minúsculas con sus equivalentes en
#        mayúsculas, y devuelve la cadena como resultado.
print(f"Método upper: {texto_1.upper()}")

# Lower: hace una copia de la cadena de origen, reemplaza todas las letras mayúsculas con sus equivalentes en
#        minúsculas, y devuelve la cadena como resultado.
print(f"Método lower: {texto_1.lower()}")


print()
print("::::::::::::::::::::::::::::::::::::: EXTRA :::::::::::::::::::::::::::::::::::::")
print()

# Palíndromo:
def palindromo(texto):

    texto_sin_espacios = texto.replace(" ", "")
    texto_invertido_sin_espacios = texto[::-1].replace(" ", "")

    if texto_sin_espacios == texto_invertido_sin_espacios:
        print(f"'{texto}' es palíndromo.\n")
    else:
        print(f"'{texto}' no es palíndromo.\n")


# Anagrama:
def anagrama(palabra_1, palabra_2):
    palabra_1_minusculas = palabra_1
    palabra_2_minusculas = palabra_2

    if sorted(palabra_1_minusculas) == sorted(palabra_2_minusculas):
        print(f"las plabras '{palabra_1_minusculas}' y '{palabra_2_minusculas}' son anagramas.\n")
    else:
        print(f"las plabras '{palabra_1_minusculas}' y '{palabra_2_minusculas}' no son anagramas.\n")


# Isograma:
def isograma(palabra):

    lista_letras = []
    isograma = False

    for letra in palabra:

        if letra not in lista_letras:
            lista_letras.append(letra)
            isograma = True
        else:
            isograma = False
            print(f"No es un isograma, hay letras repetidas en la palabra '{palabra}'.")
            break

    if isograma:
        print(f"La palabra '{palabra}' es un isograma: no tiene letras repatidas.")



opcion_elegida = 0

while opcion_elegida != 4:

    # Creación del menú y bucle
    print(

        """¿Qué deseas hacer?:

              [1] - Comprobar palíndromo
              [2] - Comprobar anagramas
              [3] - Comprobar isograma
              [4] - Salir"""
    )

    opcion_elegida = int(input())

    match opcion_elegida:
        case 1:
            texto = input("Introduce palabra o frase para comprobar si es un palíndromo: ")
            palindromo(texto)
        case 2:
            palabra_1 = input("Introduce la primera palabra para comprobar si es un anagrama de la segunda: ")
            palabra_2 = input("Introduce la primera palabra para comprobar si es un anagrama de la primera: ")
            anagrama(palabra_1, palabra_2)
        case 3:
            palabra = input("Introduce palabra o frase para comprobar si es un isograma: ")
            isograma(palabra)
        case 4:
            print("Gracias por utilizar el comprobador de cadenas. ¡Hasta pronto!")
            opcion_elegida = 4
            pass