"""
Operaciones
"""
s1 = "hola"
s2 = "Python"

# CONCATENACIÓN
print(s1 +" , "+ s2 + "!")

# REpetición
print(s1 * 3)

# Indexación
print(s1[0])

# lONGUITUD
print(len(s2))

# Slicing (porción)
print(s2[2:6])
print(s2[2:])
print(s2[:3])
print(s2[::-1])

# Búsqueda
print( "Ho" in s2)
print( "Ho" in s1)
print( "ho" in s1)
# REEMPLAZO
print(s1.replace("o", "a"))

# DIVISIÓN
print(s2.split("t"))
print(type(s2.split("t")))
# MAYÚSCULAS Y minúsculas y 1ra letra en MAYÚSCULA
print(s1.upper())
print(s1.lower())
print("ricardo gonzales".title())
print("ricardo gonzales".capitalize())

# Eliminación de espacios al principio y al final
print("  Ricardo Gonzales  ")
print("  Ricardo Gonzales  ".strip())
# Búsqueda al principio y al final
print(s1.startswith("ho"))
print(s1.startswith("py"))
print(s2.startswith("Py"))
print(s1.endswith("la"))
print(s1.endswith("py"))
print(s2.endswith("hon"))

s3= "Brais Moure @mouredev"

# BÚSQUEDA DE POSICIÓN
print(s3.find("moure"))
print(s3.find("Moure"))
print(s3.find("M"))
print(s3.lower().find("m"))

#Búsqueda de Ocurrencias
print(s3.lower().count("m"))
print(s3.lower().count("moure"))
print(s3.lower().count("mouredev"))

#FORMATEO
print("Saludo :{}   , Lenguaje :{}".format(s1, s2))

# INTERPOLACIÓN
print(F"SALUDO : {s1}, LENGUAJE:{s2}")

# TRANSFORMACIÓN EN LISTA DE CARACTERES
print(list(s3))

# TRANSFORMACIÓN DE LISTA EN CADENA
l1 = [s1, "," , s2, "!"]
print("-".join(l1))

# TRANSFORMACIONES NUMÉRICAS
s4 = "123456"
print (s4 *3)
s4 = int (s4)
print(s4*3)

s5 = "123456.123"
s5 = float(s5)
print(s5)

# COMPROBACIONES varias
print(s1.isalnum())
print(s1.isalpha())

s4= "12345"
print(s4.isalpha())
print(s4.isalnum())

"""E X T R A
"""
def check( word1: str, word2: str):
    
    #Palíndromos
    print(f"¿{word1} es un palíndromo? : {word1.lower() == word1.lower()[::-1]}")
    print(f"¿{word2} es un palíndromo? : {word2 == word2[::-1]}")
    
   #Anagramas
    print(f"¿{word1} es anagrama de {word2}? : {sorted(word1) == sorted(word2)}")
   
    #Isogramas
    print(len(word1))
    print(len(set(word1)))
    
    print(f"{word1} es isograma : {len(word1) == len(set(word1))}")
    print(f"{word2} es isograma : {len(word2) == len(set(word2))}")


    def isogram(word: str) -> bool:
        
        word_dict = dict()
        for character in word :
            word_dict[character] = word_dict.get(character,0) +1 
        
        isogram = True 
        values = list(word_dict.values())
        isogram_len = values[0]  
        for word_count in values:
            if word_count != isogram_len:
                isogram = False
                break
        return isogram
    
    print(f"{word1} es un isograma : {isogram(word1)}")    
    print(f"{word2} es un isograma : {isogram(word2)}")  
    

check("radar", "pythonpython")
#check("amor", "roma") 

"""    word_dict = dict()
    for word in word1 :
        word_dict[word] = word_dict.get(word,0) +1 
    
    isogram = True 
    values = list(word_dict.values())
    isogram_len = values[0]  
    for word_count in values:
        if word_count != isogram_len:
            isogram = False
            break
    
    print(isogram)     
    
    print(word_dict)
        

check("radar", "pythonpython")
#check("amor", "roma") """
