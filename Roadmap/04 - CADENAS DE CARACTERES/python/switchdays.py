"""
 * EJERCICIO:
 * Muestra ejemplos de todas las operaciones que puedes realizar con cadenas de caracteres
 * en tu lenguaje. Algunas de esas operaciones podrían ser (busca todas las que puedas):
 * - Acceso a caracteres específicos, subcadenas, longitud, concatenación, repetición,
 *   recorrido, conversión a mayúsculas y minúsculas, reemplazo, división, unión,
 *   interpolación, verificación...
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que analice dos palabras diferentes y realice comprobaciones
 * para descubrir si son:
 * - Palíndromos
 * - Anagramas
 * - Isogramas
 """


# Los palíndromos son palabras que se leen igual para alante que para atrás. Ejemplo: oso
def palindromo(palabra):
    lista = list(palabra)
    lista_reverse = lista.copy()
    lista_reverse.reverse()
    return lista == lista_reverse

# Dos palagbras son anagramas si contienen las mismas letras. Ejemplo: roma y amor
def anagrama(palabra_1, palabra_2):
    lista_1 = list(palabra_1)
    lista_2 = list(palabra_2)
    lista_1.sort()
    lista_2.sort()
    return lista_1 == lista_2

# Un isograma es una palabra en la que todas sus letras son diferentes. Ejemplo: murciélago
def isograma(palabra):
    lista = list(palabra)
    conjunto_letras = set()
    for letra in lista:
        if letra in conjunto_letras:
            return False
        else:
            conjunto_letras.add(letra)
    return True

palabra_1 = input("Introduce la primera palabra: ")
palabra_2 = input("Introduce la segunda palabra: ")

if palindromo(palabra_1):
    print(palabra_1, "Es un palíndromo.")
else:
    print(palabra_1, "No es un palíndromo")

if palindromo(palabra_2):
    print(palabra_2, "Es un palíndromo")
else:
    print(palabra_2, "No es un palíndromo")

if anagrama(palabra_1, palabra_2):
    print(palabra_1, "y ", palabra_2, "son anagramas.")
else:
    print(palabra_1, "y ", palabra_2, "no son anagramas.")

if isograma(palabra_1):
    print(palabra_1, "Es un isograma.")
else:
    print(palabra_1, "No es un isograma")

if isograma(palabra_2):
    print(palabra_2, "Es un isograma")
else:
    print(palabra_2, "No es un isograma")