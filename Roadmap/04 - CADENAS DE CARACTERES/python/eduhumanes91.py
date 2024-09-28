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

# Concatenación
cadena1 = "Hola"
cadena2 = " Mundo"
cadena3 = cadena1 + cadena2
print(cadena3)

# Repetición
cadena4 = "Hola" * 3
print(cadena4)

# Acceso a caracteres específicos
print(cadena1[0])

# Subcadenas
print(cadena1[0:2])

# Longitud
print(len(cadena1))

# Recorrido
for letra in cadena1:
    print(letra)

# Conversión a mayúsculas y minúsculas
print(cadena1.upper())
print(cadena1.lower())

# Reemplazo
print(cadena1.replace("o", "a"))

# División
print(cadena1.split("o"))

# Unión
print("o".join(cadena1))

# Interpolación
print(f"{cadena1} Mundo")

# Verificación
print("Hola" in cadena1)
print("Hola" not in cadena1)

#Extra
# Palíndromos, Anagramas e Isogramas

    #Isogramas
    
def check(word1: str, word2: str):

    # Palíndromos
    print(f"¿{word1} es un palíndromo?: {word1 == word1[::-1]}")
    print(f"¿{word2} es un palíndromo?: {word2 == word2[::-1]}")

    # Anagramas
    print(f"¿{word1} es anagrama de {word2}?: {sorted(word1) == sorted(word2)}")

    # Isogramas

    def isogram(word: str) -> bool:

        word_dict = dict()
        for character in word:
            word_dict[character] = word_dict.get(character, 0) + 1

        isogram = True
        values = list(word_dict.values())
        isogram_len = values[0]
        for word_count in values:
            if word_count != isogram_len:
                isogram = False
                break

        return isogram

    print(f"¿{word1} es un isograma?: {isogram(word1)}")
    print(f"¿{word2} es un isograma?: {isogram(word2)}")


check("radar", "pythonpythonpythonpython")
check("amor", "roma")
    
    
