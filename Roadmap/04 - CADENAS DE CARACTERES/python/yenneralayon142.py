"""
Operaciones
"""
c1 = "Yenner"
c2 = "Alayon"
#Concatenacion
print(c1 + " " +  c2)
#Repetición
print(c1 * 3)
#Indexación
print(c1[0] + c1[1])
#Longitud
print(len(c1))
#Slicing
print(c1[2:4])
#Busqueda
print("a" in c1)
print("b"in c2)
#Reemplazo
print(c1.replace("Y" , "J"))
#Division
print(c1.split("Y"))
#Busqueda al principio y al final
print(c1.startswith("Ye"))
print(c1.startswith("Je"))
print(c1.endswith("er"))
#Busqueda de Ocurrencias
print(c1.lower().count("y"))
#Formateo
print("Saludo:{} lenguaje:{}!".format(c1,c2))
#Interpolación
print(f"Saludo {c1} , lenguaje{c2}")
#Transformar una cadena a lista
print(list(c1))
#Transformar una lsta a cadena
l1 = [c1,", ",c2,"!"]
print("".join(l1))
#Transformaciones númericas
s1 = "12345"
s1 = int(s1)
print(type(s1))
#Comprobaciones Varias
print(c1.isalnum())
print(c1.isalpha())
"""
EXTRA
"""
def comprobaciones(word1:str, word2:str):
    #Palindromos
    print(f"¿{word1} es un palindromo?: {word1 == word1[::-1]}")
    print(f"¿{word2} es un palíndromo?: {word2 == word2[::-1]}")
    #Anagramas 
    print(f"¿{word1} es Anagrama de {word2}?: {sorted(word1) == sorted(word2)}")
    #Isogramas
    def isogram(word:str ) -> bool:
        word_dict = dict()
        for character in word:
            word_dict[character] = word_dict.get(character,0) + 1
        isogram = True
        values = list(word_dict.values())
        isogram_len = values[0]
        for word_count in values:
            if word_count != isogram_len:
                isogram = False
                break
        return isogram
    print(f"¿{word1} es un isograma?: {isogram(word1)}")
    print(f"¿{word2} es un isograma?:{isogram(word2)}")
comprobaciones("radar","pythonpythonpythonnnnn")
