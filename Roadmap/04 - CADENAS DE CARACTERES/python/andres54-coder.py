'''
opereaciones con cadenas de caracteres
'''

name = "Andres"
lastname = "Rapster21"

#concatenar
print(name + " " + lastname)

#repetir
print(f"{name} " * 3)

#indexacion
print(name[0], name[1], name[2], name[3], name[4], name[5])

#slicing
print(name[0:3])

#buscar
print("d" in name)

#longitud
print(len(name))

#mayusculas
print(name.upper())

#minusculas
print(name.lower())

#capitalizar
print(name.capitalize())

#reemplazar
print(name.replace("A", "X"))

#buscar
print(name.find("d"))

#contar
print(name.count("e"))

#eliminar espacios
print("   Andres  Rapster21  ".strip())

#comparar
print(name == "Andres")

#saber si empieza con
print(name.startswith("A"))

#saber si termina con
print(name.endswith("s"))

#separar
print(name.split("n"))

#unir
print(" ".join(name))

#interpolacion
print(f"{name} {lastname}")

#formatear
print("{} {}".format(name, lastname))

#formatear
print("{1} {0}".format(name, lastname))

#formatear
print("{lastname} {name}".format(name=name, lastname=lastname))

#formatear
print("{lastname} {name}".format_map({"name": name, "lastname": lastname}))

s3 = "Andres Rapster21 @gmail"

#transformacion en lista de caracteres
print(list(s3))

#comprobacion de caracteres
print(s3.isalnum())
print(s3.isalpha())
print(s3.isascii())
print(s3.isdecimal())
print(s3.isdigit())
print(s3.isidentifier())
print(s3.islower())
print(s3.isnumeric())
print(s3.isprintable())
print(s3.isspace())
print(s3.istitle())
print(s3.isupper())

'''
Extra
'''

def check(word1: str, word2: str) -> bool:
    
    def is_isogram() -> bool:
        word_dict = dict()
        for word in word2:
            word_dict[word] = word_dict.get(word, 0) + 1
            
        isogram = True
        values = list(word_dict.values())
        isogramlen = values[0]
        for wordcount in values:
            if isogramlen != wordcount:
                isogram = False
                break
        return isogram
    #palindromo
    print(f"¿{word1} es palindromo?: {word1 == word1[::-1]}") 
    print(f"¿{word2} es palindromo?: {word2 == word2[::-1]}") 
    #anagrama
    if sorted(word1) == sorted(word2):
        print(f"La palabra {word1} es anagrama de {word2}")
    #isograma
    print(f"¿{word2} es isograma?: {is_isogram()}")
    
    
check("amor", "romaroma")