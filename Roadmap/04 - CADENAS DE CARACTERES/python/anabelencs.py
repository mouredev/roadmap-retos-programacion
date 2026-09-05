print("\n#04 CADENAS DE CARACTERES")

'''
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
'''

s1 = "Hola"
s2 = "Belén"

print("\nConcatenación:")
print(s1 + ", " + s2 + "!")
print("Probando con comas: ",s1,", ",s2,"!") # No es igual, deja espacios aunque los elimine entre los elementos.

print("\nRepetición:")
print(s1*3)

print("\nIndexación:")
print(s2[0]+s2[1]+s2[2]) # Así o espaciado, da igual.

print("\nLongitud:")
print(len(s2))

print("\nSlicing (porción):")
print(s2[0:2])
print(s2[2:5])
print(s2[:2])
print(s2[2:])

print("\nBúsqueda:")
print("e" in s2)
print("é" in s2)
print("i" in s2)

print("\nReemplazo:")
print(s1.replace("l","r"))
print(s1.replace("Ho","O"))
print(s1.replace("H",""))
print(s1.replace("H","M"), s1.replace("o","i",), s1.replace("l","r")) # Imprime Mola Hila Hora
print(s1.replace("H","M") and s1.replace("o","i",) and s1.replace("l","r")) # Imprime Hora
    # El operador and no combina textos, sino que evalúa si los valores son True o False de izquierda a derecha.
    # Cuando usas and entre varios valores verdaderos, Python los evalúa en orden y devuelve el último valor evaluado.
print(s1.replace("H","M") + s1.replace("o","i",) + s1.replace("l","r")) # Imprime MolaHilaHora
print(s1.replace("H","M").replace("o","i",).replace("l","r")) # Imprime Mira

print("\nDivisión:")
print(s2.split("l"))

s3 = "ana belén castillo"

print("\nMayúsculas, minúsculas, títulos y primera letra en mayúscula:")
print(s1.upper())
print(s1.lower())
print(s3.upper())
print(s3)
print(s3.title())
print(s3.capitalize())

print("\nEliminación de espacios al inicio y al final")
print("  Ana Belén C. ")
print("  Ana Belén C. ".strip())

print("\nBúsqueda al principio y al final")
print(s1.startswith("H"))
print(s1.startswith("ho")) # Distingue mayúsculas y minúsculas.
print(s1.endswith("ola"))
print(s1.endswith("A"))

s4 = "Ana Belén Castillo @anabelencs"
s5 = s4.lower()

print("\nBúsqueda de posición")
print(s4.find("Ana"))
print(s4.find("ana"))
print(s4.find("B"))
print(s4.find("b"))
print(s4.lower().find("B")) # Imprime -1. No hay B mayúscula.
print(s4.lower().find("b"))
print(s4.find("Z")) # Imprime -1. No hay Z.

print("\nBúsqueda de ocurrencias")
print(s5.count("a")) # Cuántas veces hay un caracter en una cadena.

print("\nFormateo")
print("Saludo: {}, nombre: {}!".format(s1, s2)) # Lo mismo que interpolación pero de otra forma.

print("\nInterpolación")
print(f"Saludo: {s1}, nombre: {s2}!")

print("\nTransformación en lista de caracteres")
print(list(s1)) # Separa los caracteres uno por uno y los pone en formato lista.

print("\nTransformación de lista en cadena")
l1 = [s1,", ",s2,"!"]
print(l1)
print("".join(l1)) # Convierte una lista en cadena.

print("\nTransformaciones numéricas")
s6 = "123"
s6 = int(s6) # Convierte a número entero.
s7 = 321
s8 = s6 + s7
print(s8)
s9 = "123.45"
s9 = float(s9) # Convierte a número decimal.
s10 = 543.21
s11 = s9 + s10 # Imprime 666.6600000000001
print(s11)
s11 = round (s9 + s10,2) # Imprime 666.66
print(s11)

print("\nComprobaciones alfanuméricos / alfabéticos / alfanuméricos / numéricos")
print(s1.isalnum())
print(s1.isalpha())
#print(s11.isalpha()) # Error, ver por qué.
#print(s6.isnumeric())


print("\n--- DIFICULTAD EXTRA ---\n")

intro:str = input("Inserte la palabra a verificar si es palíndromo, anagrama, e isograma: ")
palabra = intro.lower()
intro2:str = input("Inserte la palabra con la cual se desea verificar si son un anagrama: ")
palabra2 = intro2.lower()

# Es un palíndromo?

if palabra == palabra[::-1]: # Se usa slicing con -1 para voltear todos los caracteres de la cadena.
    print(f"La palabra {intro} es un palíndromo.")
else:
    print(f"La palabra {intro} no es un palíndromo.")

# Es un anagrama?

if sorted(list(palabra)) == sorted(list(palabra2)): # No era necesario que fuera una lista, podía hacerse sorted con las cadenas.
    print(f"La palabra {intro} es un anagrama con la palabra {intro2}.")
else:
    print(f"La palabra {intro} no es un anagrama con la palabra {intro2}.")

# Es un isograma?

if len(palabra) == len(set(palabra)):
    print(f"La palabra {intro} es un isograma.")
else:
    print(f"La palabra {intro} no es un isograma.")