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
 """

nombre_cadena = 'Alfabeto'
cadena = "abcd-efg-hijk"

 # Acceso a caracteres específicos

print(cadena[1])

 # Subcadenas

print(cadena[5:8])

 # Longitud

print(len(cadena))

 # Concatenación

print(nombre_cadena + ":" + cadena)
print(nombre_cadena, ":", cadena)
print(f"{nombre_cadena}: {cadena}")

 # Repetición 

print(cadena * 4)

 # Recorrido

for c in cadena:
    print(c)

 # Conversión a mayúsculas y minúsculas

print(cadena.upper())
print(nombre_cadena.lower())

 # Reemplazo

print(cadena.replace('a', 'z'))

 # División y Unión

cadena = cadena.split('-')
print(cadena)

cadena = ' '.join(cadena)
print(cadena)

 # Interpolación

print(f"Este es el {nombre_cadena.lower()}, que comienza con: {cadena}")

 # Verificación

print(isinstance(cadena, str))
print(type(nombre_cadena))

"""
/////////////////////////////////////////////////  DIFICULTAD EXTRA  /////////////////////////////////////////////////
"""

palabra1 = "adan"
palabra2 = "nada"

# Funciones que comprueban si son palíndromos, anagramas y/o isogramas

def palindromo(palabra1, palabra2):
    list_palabra1 = [*palabra1] # Divide cada caracter en un elemento de un listado.
    list_palabra2 = [*palabra2]

    list_palabra2.reverse()

    if list_palabra1 == list_palabra2:
        return "Palíndromos."
    else:
        return "No son palíndromos."

def anagrama(palabra1, palabra2):
    list_palabra1 = [*palabra1] # Divide cada caracter en un elemento de un listado.
    list_palabra2 = [*palabra2]

    list_palabra1.sort()
    list_palabra2.sort()

    if list_palabra1 == list_palabra2:
        return "Anagramas."
    else:
        return "No son anagramas."

def isograma(palabra):
    count = 0 # Cuenta cuánto se repite una letra.

    for a in range(len(palabra)):
        for k in palabra:

            if palabra[a] == k:
                count += 1
                if count == 2:  #En el momento que una letra se repite dos veces, deja de ser Isograma.
                    return "No es Isograma."
        
        count = 0
    
    return "Es Isograma."

print(palindromo(palabra1, palabra2))
print(anagrama(palabra1, palabra2))
print(isograma(palabra2))