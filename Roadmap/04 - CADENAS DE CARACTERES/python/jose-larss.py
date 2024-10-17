"""
Cadena de Caracteres
"""
cadena1 = "Esto es una cadena de caracteres o string"
cadena2 = "cadena 2"

# Acceso a caracteres específicos
if 'e' in cadena1:
    print("hay e")
print('o' in cadena1)
# Subcadenas

# Longitud
print(f"La longitud de la cadene es: {len(cadena1)}")

# Concatenación
cadena3 = cadena1 + cadena2
print(f"La concatenación de la cadena 1 mas la cadena2 es: {cadena3}")

# Repetición
print(f"La repeticion es {cadena1 * 3}")

# Indexación
print(cadena1[0] + cadena1[5] + cadena2[0] + cadena2[5])

# Slicing (Porción)
print(cadena1[2:6])

# Recorrido
for letra in cadena1:
    print(letra)

# Conversión a mayúsculas y Minúsculas
print(cadena1.upper()) # mayúsculas
print(cadena1.lower()) # minúsculas
print(cadena1.capitalize())
print(cadena1.title())

# Reemplazo
print(cadena1.replace('o', 'a'))

# División
print(cadena1.split(" "))

# Eliminación de espacios al principio y al final
print(" brais moure ".strip())

# Búsqueda al principio y al final
print(cadena1.startswith("Ho"))
print(cadena1.startswith("Py"))
print(cadena1.endswith("la"))
print(cadena1.endswith("thon"))

s3 = "Brais Moure @mouredev"

# Búsqueda de posición
print(s3.find("moure"))
print(s3.find("Moure"))
print(s3.find("M"))
print(s3.lower().find("m"))

# Interpolación
print(f"Saludo: {cadena1}, lenguje: {cadena2}!")

# Formateo
print("Saludo: {}, lenguaje: {}!".format(cadena1, cadena2))

# Verificación

# Tranformación en lista de caracteres
print(list(cadena2))

# Transformación de lista en cadena
l1 = [cadena1, ", ", cadena2, "!"]
print("".join(l1))

# Transformaciones numéricas
s4 = "123456"
s4 = int(s4)
print(s4)

s5 = "123456.123"
s5 = float(s5)
print(s5)

# Comprobaciones varias
s4 = "123456"
print(cadena1.isalnum())
print(cadena2.isalpha())
print(s4.isalpha())
print(s4.isnumeric())

"""
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que analice dos palabras diferentes y realice comprobaciones
 * para descubrir si son:
 * - Palíndromos
 * - Anagramas
 * - Isogramas
 */
"""
def check(word1: str, word2: str):
    print(word1)
    print(word1[::-1])
    print(sorted(word1))
    print(sorted(word2))
    # Palíndromos
    print(f"¿{word1} es un palíndromo?: {word1 == word1[::-1]}")
    print(f"¿{word2} es un palíndromo?: {word2 == word2[::-1]}")

    # Anagramas
    print(f"¿{word1} es anagrama de {word2}?: {sorted(word1) == sorted(word2)}")

    # Isogramas

    def isogram(word: str) -> bool:

        word_dict = dict()
        for character in word:
            if character in word_dict:
                word_dict[character] += 1
                word_dict.get()
            else:
                word_dict[character] = 1
            #word_dict[character] = word_dict.get(character, 0) + 1
        print(word_dict)
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
#check("amor", "roma")
#check("cara", "arca")