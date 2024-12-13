'''
/*
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
 '''

# Operaciones con cadenas de caracteres
cadena = "Hola Mundo"
cadena2 = "Alejandro"
cadena3 = ""
print(cadena[0]) # Acceso a un caracter específico
print(cadena[0:4]) # Subcadena
print(len(cadena)) # Longitud
print(f"{cadena} {cadena2}") # Concatenación
print(cadena * 2) # Repetición
for char in cadena: # Recorrido
    print(char)
print(cadena.upper()) # Conversión a mayúsculas
print(cadena.lower()) # Conversión a minúsculas
print(cadena2.replace("Alejandro", "Alex")) # Reemplazo
print(cadena.split(" ")) # División
print(cadena3.join([cadena, cadena2])) # Unión
print(f"{cadena} {cadena2}") # Interpolación
print(f"{cadena.isalnum()} {cadena.isalpha()} {cadena.isdecimal()} {cadena.isdigit()} {cadena.isidentifier()} {cadena.islower()} {cadena.isupper()} {cadena.isspace()} {cadena.istitle()} {cadena.isnumeric()} {cadena.isprintable()}") # Verificación

# DIFICULTADO EXTRA
#region Palíndromos
# 1
def is_palindrome(word): # Verifica si una palabra es palíndromo
    return word == word[::-1] # Compara la palabra con su inversa
print(is_palindrome("ana")) # True
# 2
print("Vamos a verificar si una palabra es palíndromo")
cadena = input("Introduce una palabra: ").lower()
list_cadena = list(cadena)
list_cadena_reverse = list(cadena)
list_cadena_reverse.reverse()
while "" in list_cadena:
    list_cadena.remove(" ")
while "" in list_cadena_reverse:
    list_cadena_reverse.remove(" ")
if list_cadena == list_cadena_reverse:
    print(f"La palabra {cadena} es un palíndrono")
else:
    print(f"La palabra {cadena} NO es un palíndrono")
#endregion
#region Anagramas
def is_anagrama(palabra1, palabra2): 
    return sorted(palabra1) == sorted(palabra2) # Compara si las palabras ordenadas son iguales
print("Vamos a verificar si dos palabras son anagramas")
palabra1 = input("Introduzca la primera l¡palabra: ").lower()
palabra2 = input("Introduzca la segunda palabra: ").lower()
print(f"¿Las palabras '{palabra1}' y '{palabra2}' son anagramas?\n{is_anagrama(palabra1, palabra2)}")
#endregion
#region Isogramas
def is_isograma(plaabra):
    return len(plaabra) == len(set(plaabra)) # Compara la longitud de la palabra con la longitud de la palabra sin caracteres repetidos (si son iguales, no hay caracteres repetidos)
print("Vamos a verificar si una palabra es un isograma")
palabra = input("Introduzca una palabra ").lower()
print(f"¿Es la palabra '{palabra}' un isograma?\n{is_isograma(palabra)}")
#endregion
