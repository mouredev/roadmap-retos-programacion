text = "Hola Python"

#Acceso a caracteres especificos
print(text[0])
print(text[6])
print(text[3])

#Slicing Subcadenas
print(text[0:4])
print(text[5:11])
print(text[:4])
print(text[5:])

#Longitud
print(len(text))

#Concatenaciion
name = "Tomas"
print(text + " " + name)

#reptiticion
print( name * 3)

#Recorrido
for letra in text:
    print(letra)

#Mayusculas
print(text.upper())

#Minusculas
print(text.lower())

#Primera letra mayuscula
print(text.capitalize())

#Tipp titulo (cada primer letra de cada palabra es mayuscula)
print(text.title())

#Remplazo
print(text.replace("Python", "Tomas"))

#Division (split)
print(text.split())

#Union (Join)
words = ["Hola" , "Python"]
print("=".join(words))

#Eliminar espacios
word= "      Hola Python    "
print(word.strip())

#Buscar donde empieza el Texto
print(text.find("Python"))

#Verificar si existe
print("Hola" in text)

#Verificar al inicio
print(text.startswith("python"))

#Verificar si al final
print(text.endswith("Hola"))

#Contar apaticiones
sentence = "Hola soy tomas soy yo"
print(sentence.count("soy"))
print(sentence.count("o"))

#Interpolacion
names = "Tomas"
age  = 20
print(f"Me llamo {names} y tengo {age} anos")

#verificar si son letras
print("Python".isalpha())

#verificar si son numeros
print("Python".isalnum())

#verificar si son alfanumericos
print("Python22".isalpha())

#Invertit una lista
print(text[::-1])

#Covertir a una lista
print(list(text))

#format
print("Hola, me llamo {} y tengo {}".format(names, age))

"""Extra"""

def poli (word1,word2):
    if word1 == word1[::-1] and word2 == word2[::-1] :
        print(f"La palabra {word1}  y la palabra {word2} son pilindromas")
    else:
        print("Una de las palabras ingresadas no es polindroma")
poli("radar", "prueba")

def anagramas(word1,word2):

    if sorted(word1) == sorted(word2):
        print(f"La palabra {word1} y la palabra {word2} son anagramas")
    else:
        print("Las palabras introducidas no los son")
anagramas("roca", "orca")
def isogramas (word1, word2):
    def isogram(word : str) -> bool:
        
        word_dict = dict()
        for letter in word:
            word_dict[letter] = word_dict.get(letter,0) + 1
        
        
        isogram = True
        values = list(word_dict.values())
        isogram_len = values[0]
        for word_count in values:
            if word_count != isogram_len:
                isogram = False
                break
        return isogram
    print(f"¿{word1} es un isograma?: {isogram(word1)} ")
    print(f"¿{word2} es un isograma?: {isogram(word2)} ")

isogramas("radar" , "python")

#Versionde BRAIS
def check(word1: str, word2: str):

    # Palíndromos
    print(f"¿{word1} es un palíndromo?: {word1 == word1[::-1]}")
    print(f"¿{word2} es un palíndromo?: {word2 == word2[::-1]}")

    # Anagramas
    print(f"¿{word1} es anagrama de {word2}?: {sorted(word1) == sorted(word2)}")

check("amor", "roma")
# check("amor", "roma")