"""
/*
EJERCICIO:
Muestra ejemplos de todas las operaciones que puedes realizar con cadenas de caracteres
en tu lenguaje. Algunas de esas operaciones podrían ser (busca todas las que puedas):
- Acceso a caracteres específicos, subcadenas, longitud, concatenación, repetición, recorrido,
  conversión a mayúsculas y minúsculas, reemplazo, división, unión, interpolación, verificación...

DIFICULTAD EXTRA (opcional):
Crea un programa que analice dos palabras diferentes y realice comprobaciones
para descubrir si son:
- Palíndromos
- Anagramas
- Isogramas

 """
 
#*-------------------------------------------------------------------------------------------------------------#
print("-----------------------------------------------------------------------------------------------------")

#ACCESO A CARACTERES
print("Acceso a los caracteres: ")
palabra = "Python"
print(f"El primer caracter de {palabra} es {palabra[0]}")
print(f"El quinto caracter de {palabra} es {palabra[4]}")
print("-----------------------------------------------------------------------------------------------------")

#SUBCADENAS
print("Subcadenas: ")
print(f"Una subcadena de {palabra} en la que se selecciona los primeros cuatro elementos será: {palabra[0:4]}")
print(f"Una subcadena de {palabra} en la que selecciona los primeros tres elementos pero escogerá los elementos de dos en dos será: {palabra[0:4:2]}")
print("-----------------------------------------------------------------------------------------------------")

#LONGITUD
print("Longitud: ")
print(f"La longitud de {palabra} es {len(palabra)}")
print("-----------------------------------------------------------------------------------------------------")

#CONCATENACION
print("Concatenación: ")
print(f"{palabra + " es el lenguaje utilizado para este reto"}")
print("-----------------------------------------------------------------------------------------------------")


#CONCATENACION
print("Concatenación: ")
print(f"{palabra + " es el lenguaje utilizado para este reto"}")
print("-----------------------------------------------------------------------------------------------------")

#REPETICIÓN
print("Repetición: ")
shoo = "shoo "
bee = "bee "
print(f"Kendrick - Euphoria: Part II Intro: {shoo * 6 , bee * 6} ")
print("-----------------------------------------------------------------------------------------------------")

#RECORRIDO
print("Recorrido: ")
for i in palabra:
    print(i)
print("-----------------------------------------------------------------------------------------------------")

#CONVERSIÓN A MAYÚSCULAS Y MINÚSCULAS
print("Conversión a Mayúsculas y Minúsculas: ")
print(f"{palabra} en mayúsculas: {palabra.upper()} ")
print(f"{palabra} en minúsculas: {palabra.lower()} ")

print("-----------------------------------------------------------------------------------------------------")

#REEMPLAZO
print("Reemplazo: ")
print(f"{palabra} va a ser reemplaza por: {palabra.replace("Python", "Cobol")} ")
print("-----------------------------------------------------------------------------------------------------")

#DIVISIÓN
print("División: ")
palabra_dos = "Tyler the Creator: Chromakopia"
print(f"{palabra_dos} va a ser divida en: {palabra_dos.split(" ")} ")
print("-----------------------------------------------------------------------------------------------------")

#UNIÓN
print("Unión: ")
split_palabra_dos = palabra_dos.split(" ")
print(f"{split_palabra_dos} va a ser unida en: {"".join(split_palabra_dos)} ")
print("-----------------------------------------------------------------------------------------------------")

#INTERPOLACIÓN
print("Interpolación: ")
numero = 3673
print(f"El lenguaje {palabra} es el más usado y tiene más de {numero} scripts.")
print("-----------------------------------------------------------------------------------------------------")

#Verificación
print("Verificación: ")

if "Tyler" in palabra_dos:
    print(f"Tyler se encuentra en la cadena: {palabra_dos}")
print("-----------------------------------------------------------------------------------------------------")

#*-------------------------------------------------------------------------------------------------------------#

"""
DIFICULTAD EXTRA (opcional):
Crea un programa que analice dos palabras diferentes y realice comprobaciones
para descubrir si son:
- Palíndromos
- Anagramas
- Isogramas
""" 
def palabras():

    def palindromo(palabra):
        return palabra == palabra[::-1]

    def anagrama(palabra1, palabra2):
        return sorted(palabra1) == sorted(palabra2)

    def isograma(palabra):
        return len(palabra) == len(set(palabra))

    def input_palabra(mensaje):
        while True:
            palabra = input(mensaje)
            if isinstance(palabra, str) and palabra.isalpha():
                return palabra
            else:
                print("Por favor, introduzca solo letras (sin números ni caracteres especiales).")
    
    primera_palabra = input_palabra("Introduzca la primera palabra: ")
    segunda_palabra = input_palabra("Introduzca la segunda palabra: ")
    print("****************************************************************************")
    print("Palindromo: ")
    print(f" La palabra {primera_palabra} es un palíndromo? {palindromo(primera_palabra)}")
    print(f" La palabra {segunda_palabra} es un palíndromo? {palindromo(segunda_palabra)}")
    print("****************************************************************************")
    print("Anagrama: ")
    print(f" Las palabras {primera_palabra} y {segunda_palabra} son anagramas? {anagrama(primera_palabra, segunda_palabra)}")
    print("****************************************************************************")
    print("Isograma: ")
    print(f" La palabra {primera_palabra} es un isograma? {isograma(primera_palabra)}")
    print(f" La palabra {segunda_palabra} es un isograma? {isograma(segunda_palabra)}")
    print("****************************************************************************")
palabras()

#*-------------------------------------------------------------------------------------------------------------#