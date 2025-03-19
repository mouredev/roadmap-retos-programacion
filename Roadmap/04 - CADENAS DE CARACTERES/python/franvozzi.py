mensaje = 'Hola Mundo' # Declaración de variables

# Concatenación de caracteres
mensaje1 = 'Hola' + ' ' + 'Mundo'
print(mensaje1)

# Multiplicación de caracteres
mensaje2A = 'Hola ' * 3
mensaje2B = 'Mundo'
print(mensaje2A + mensaje2B)

# Añadir caracteres (desde aquí 'String Methods')
mensaje3 = 'Hola'
mensaje3 += ' '
mensaje3 += 'Mundo'
print(mensaje3)

# Extensión de caracteres
mensaje4 = 'hola' + ' ' + 'mundo'
print(len(mensaje4))

# Encontrar caracteres
mensaje5 = "Hola Mundo"
mensaje5A = mensaje5.find("Mundo")
print(mensaje5A)

# Minúsculas
mensaje6 = "HOLA MUNDO"
mensaje6A = mensaje6.lower()
print(mensaje6A)

# Reemplazo
mensaje7 = "Hola mundo"
mensaje7A = mensaje7.replace("L", "pizza")
print(mensaje7A)

"""
Extra
"""
def check(word1: str, word2: str):
    # Palíndromos
    print(f"¿{word1} es un palíndromo?  {word1 == word1[::-1]}")
    print(f"¿{word2} es un palíndromo?  {word2 == word2[::-1]}")
    
    # Anagrama
    print(f"¿{word1} es un anagrama de {word2}?  {sorted(word1) == sorted(word2)}")

    # Isogramas
    
    def isogram(word: str) -> bool:
        wordDict = dict()
        for word in word1:
            wordDict[word] = wordDict.get(word, 0) + 1
    
        isogram = True
        values = list(wordDict.values())
        print(values)
        isogramLen = values[0]
        for wordCount in values:
            if wordCount != isogramLen:
                isogram = False
                break
        
        return isogram
            
    
    print(f"¿{word1} es un isograma?  {isogram(word1)}")
    print(f"¿{word2} es un isograma?  {isogram(word2)}")

    
    print(isogram)
    
check("radar", "reconocer")
check("amor", "roma")