"""
CADENAS DE CARÁCTERES
"""
#cadenas de texto que vamos a usar
s1= "Hola"
s2 = "Python"


#Concatenación
print(s1 + " " + s2)

#Repetición
print(s1 * 3)

#Indexación -> para acceder a un caracter concreto de una cadena de texto
print(s1[0] + s1[1] + s1[0])

#Longitud
print(len(s1))

#Porción
print(s2[2:6]) #siempre poner uno de más pork sino el último no se tiene en cuenta
print(s2[2:]) #si no ponemos nada va hasta el final
print(s2[:2])

#Busqueda -> para ver si un caracter existe en una cadena de texto
print("a" in s1)
print("i" in s1)

#Remplazo
print(s1.replace("o","a")) #para cambiar una letra por otra nueva

#División
print(s2.split("t")) #si tuvieramos dos t en la palabra, cortaría por ambas

#Conversión a mayúsculas, minúsculas y priméra letra en mayúsculas
print(s1.upper())
print(s1.lower())
print("hosi eloso".title()) #pone las primeras letras en mayus
print("hosi eloso".capitalize()) #pone solo la primera letra en mayus

#Eliminación de espacios al principio y al final
print("  hosi eloso    ".strip())

#Búsqueda al principio y al final
print(s1.startswith("Ho"))
print(s1.startswith("Py"))
print(s1.endswith("la"))
print(s1.endswith("on"))

s3 = "Hosi Eloso hosi@gmail.com"

#Búsqueda de posición
print(s3.find("Eloso"))
print(s3.find("o")) #te da la posición de la primera coincidencia

#Búsqueda de ocurrencias
print(s3.lower().count("o")) #cuenta las o de la cadena

#Formato
print("Saludo: {}, lenguaje: {}!".format(s1,s2))
print(f"Saludo: {s1}, lenguaje: {s2}!")

#Transformación de cadena en lista
print(list(s3))

#Transformación de lista en cadena
l1 = [s1, ", ", s2, "!"]
print("".join(l1))

#Transformaciones numéricas
s4 = "123456"
s4 = int(s4) #número entero
print(s4)

s5 ="123.456"
s5 = float(s5) #número decimal
print(s5)

#Comprobaciones varias
print(s1.isalnum())
print(s1.isalpha())
print(s4.is_integer())
print(s1.isnumeric())

"""
EXTRA
"""
'''
* Crea un programa que analice dos palabras diferentes y realice comprobaciones
 * para descubrir si son:
 * - Palíndromos
 * - Anagramas
 * - Isogramas
'''

    

def analizador():

    def palindromo():
        l=len(b)-1
        i=0
        b=b.lower()
        while i!=l:
            if b[i]==b[l]:
                if l-i==1:
                    l=i
                else:
                    i+=1
                    l-=1
            else:
                break
        if i==l:
            print(f"{p} es un palíndromo")
        else:
            print(f"{p} no es un palíndromo")

    def anagrama():
        i=0
        if len(l1)==len(l2):
            while i<=len(l1)-1:
                if l1[i]==l2[i]:
                    i+=1
                else:
                    print("Las palabras no son anagramas")
                    break
        if i==len(l1):
            print("Las palabras son anagramas")
        else:
            print("Las palabras no son anagramas")

    def isograma():
        i=1
        while i<len(l):
            if l.count(l[i-1])==l.count(l[i]):
                i+=1
            else:
                print(f"{p} no es un isograma")
                break
        if i==len(l):
            print(f"{p} es un isograma")

             

    while True:

        p1 = input("\nIntroduce la primera palabra: ").strip()
        p2 = input("\nIntroduce la segunda palabra: ").strip()
        b1 = p1.replace(" ","")
        b2 = p2.replace(" ","")
        if not b1.isalpha() or not b2.isalpha():
            print("\nIntroduce palabras o frases válidas.")
        else:
            break
   
    print("\n¿Son palíndromos?")
    p=p1
    b=b1
    palindromo()
    p=p2
    b=b2
    palindromo()

    l1=list(p1)
    l2=list(p2)
    l1.sort()
    l2.sort()

    print("\n¿Son anagramas?")
    anagrama()

    print("\n¿Son isogramas?")
    l=l1
    p=p1
    isograma()
    l=l2
    p=p2
    isograma()
    

analizador()
print("")


"""
SU SOLUCIÓN:

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
# check("amor", "roma")

"""