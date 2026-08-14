"""Operaciones"""

str1 = "Hola"
str2 = "esto es Python"

# Concatenación
print(str1 + ", " + str2 + "!")

# Repetición
print(str1*3)

#Indexación
print(str1[0] + str1[1] + str1[2])

#Longitud
print(str2[2:5])

#Búsqueda
print("Ho" in str1)
print("P" in str2)

#Reemplazo
print(str1.replace("Hola", "Holi"))

#División
print(str2.split("h"))

#Mayúsculas y minúsculas

print(str1.upper())
print(str2.lower())
print("carla val".title())
print("carla val".capitalize())

#Eliminación de espacios al principio y al final

print(" carla  val ".strip())

#Búsqueda al principio y al final

print(str1.startswith("H"))
print(str2.endswith("n"))

#Búsqueda de posición
print("Carla Val @astrea".find("astrea"))
print("Carla Val @astrea".find("a"))
print("Carla Val @astrea".lower().find("c"))

#Búsqueda de ocurrencias

s3 = "Carla Val @astrea"

print(s3.lower().count("a"))

#formatear una cadena

print("Saludo: {}. Lenguaje: {}!".format(str1, str2))

#interpolacion fstring

print(f"Todo lo que tengo en llaves {str1} hace referencia a un string")

#Transformación en lista de caracteres

print(list(str2))

#Transformación en lista de cadenas

l1 =[str1, ", ", str2, "!"]
print("".join(l1)) #criterio espacio en blanco

#Transformaciones numéricas

s4 = "3456576"
s4 = int(s4)
print(s4)

s4 = "4344.343"
s4 = float(s4)
print(s4)

s4 = "3456576"

#comprobaciones varias

print(str1.isalnum())
print(str2.isalpha())
print(s4.isnumeric())


def check(word1:str, word2:str):

    #Palíndromos
    print(f"¿{word1} es un palíndromo?: {word1 == word1[::-1]}")
    print(f"¿{word2} es un palíndromo?: {word2 == word2[::-1]}")

    #Anagrama
    print(f"¿{word1} es anagrama de {word2}?: {sorted(word1) == sorted(word2)}")   

    #Isograma 
    def isogram(word:str) -> bool:
        word_dict = dict()
        for character in word:
                 word_dict[character] = word_dict.get(character,0) + 1

        isogram = True
        values = list(word_dict.values())
        isogram_len = values[0]
        for word_count in values:
            if(word_count != isogram_len):
                isogram = False
                break
        return isogram

    print(f"¿{word1} es isograma de {word1}?: {isogram(word1)}")  
    print(f"¿{word2} es isograma de {word2}?: {isogram(word2)}")  




#check("Python","Radar")
#check("amor","roma")

check("pythonpython","radar")