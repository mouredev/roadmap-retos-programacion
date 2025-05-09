#Cadenas de caracteres 

"""
Operaciones 
"""

s1 = "Hola"

S2 = "Python"

#Operaciones de concatenación

print (s1 + "," + S2 + "!") 

#Repetición 

print (s1 * 3)

#Indexación 

print ( s1 [0]  )

print ( s1 [0] + s1 [1] + s1 [2]  +s1 [3])

#Longitud

print (len(S2))

#Slicing (porción)

print (S2 [2:5])
print (S2 [2:6])
print (S2 [2:])  #le indico que llegue hasta el final de la cadena de texto
print (S2 [0:2])
print (S2 [:2])  #le indico que vaya del 0 hasta el 2


#Busqueda: intento buscar si de verdad  una letra o caracter existe en una cadena de texto

print ( "a" in s1)
print ( "i" in s1)

#Reemplazo: Tengo una cadena de texto y la puedo reemplazar y decir que donde aparezca una letra tengamos otra

print (s1.replace("a", "o"))
print (s1.replace("o", "a"))

#División de cadena de caracteres

print (S2.split("t"))

#Mayúsculas y Minúsculas

print (s1.upper())
print (s1.lower())

#Mayúsculas, minúsculas y primera letra en mayúsculas

print ("yanines barr".title()) #imprime Yanines Barr

print ("yanines barr".capitalize())  #imprime Yanines barr la primera letra de la primera palabra en mayúscula

#Eliminación de espacios al principio y al final

print ("    Yanines Barr     ".strip) # imprime sin espacios 
print ("    Yanines Barr     ".strip () + "@yanines")  #imprime Yanines Barr@yanines

#Búsqueda al principio y al final: pregunta devuelve booleano

print (s1.startswith("Ho"))  #devuelve True
print (s1.startswith("Py"))  ##evuelve False
print (s1.endswith("la"))  #final devuelve True
print (s1.endswith("thon"))  #final devuelve false


s3 = "Yanines yanines2025@"

#Búsqueda de posición

print ("Yanines yanines2025@gmail.com".find ("yanines"))
print ("Yanines yanines2025@gmail.com".find ("Yanines"))
print ("Yanines yanines2025@gmail.com".find ("Y"))
print ("Yanines yanines2025@gmail.com".lower ().find("y")) # se queda con la primera ocurrencia que conincide con el criterio de busqueda sea mayúsla o minúscula

#Búsquedas de ocurrencias

print (s3.lower().find ("y"))
print (s3.lower().find ("I"))
print (s3.lower().find ("A"))

print (s3.lower().count("a"))

#Formateo de una cadena de texto

print ("Saludo: {}, lenguaje: {}".format(s1, S2))


#Interpolación

print (f"Saludo: {s1}, lenguaje: {S2}") #resultado igual que el item anterior 

#Tranformación en lista de caracteres: crea una lista con todos los caracteres que hay en la cadena de texto

print (list(s3))

#Tranformación de lista en cadena

l1 = [s1, ",", S2, "!"] #array
print ("".join(l1)) #operación que sirve para concatenar resultados de una lista
print ("-".join(l1))


#Transformaciones numéricas 

s4 = "123456"
S4 = int(s4)
print (s4)


S5 = "123.23"
S5 = float (S5)
print (S5)

#Comprobaciones varias 
s4 = "123456"
print (s1.isalnum())  #devuelve booleano
print (s1.isalpha())
print (s4.isalpha())
print (s4.isnumeric())

"""
Extra

"""

def check(word1: str, word2: str):

    #Palíndromos: son las palabras capicúas, pueden leerse igual al derecho y al revés ej: Menem
    print (f"¿{word1} es un palíndromo?: {word1 ==word1 [::1]}")
    print (f"¿{word2} es un palíndromo?: {word2 ==word2 [::1]}")

    #Anagramas
    print (f"¿{word1} es anagrama de {word2}?: {sorted(word1) == sorted(word2)}")
   
   #Isograma
    #print (len   (word1))

    #print (f"¿{word1} es un isograma  de {word2}?: {sorted(word1) == sorted(word2)}")
    #print (f"¿{word2} es un isograma?: {len (word2) == len (set(word2))}")
    #print (f"¿{word1} es un isograma  de {word1}?: {sorted(word1) == sorted(word1)}")
    
    #print (len (word1) == len (set(word1)))

    def isogram (word: str) ->bool:    # funciones dentro de funciones 

        word_dict = dict ()
        for word in word: 
            #print (word)
            word_dict[word] = word_dict.get (word, 0) + 1
        
        isogram = True
        values = list(word_dict.values())
        #print (values)
        isogram_len = values [0]
        #isogram_len = word_dict [0]
        for word_count in values: 
            if word_count != isogram_len:
                isogram = False
                break
        return isogram
        
    #print (isogram)

    #print (word_dict)

    print (f"¿{word1} es un isograma?: {isogram(word1)}")
    print (f"¿{word2} es un isograma?: {isogram(word2)}")


check ("radar", "pythonpythonpythonpython")
#check ("amor", "roma")


