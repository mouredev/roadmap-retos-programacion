#Cadenas de caracteres
myCadena = 'esta ES mi CAdena'
print(myCadena[0]) # Acceder a caracteres, como si fuera una lista
print(myCadena.capitalize()) # Primer caracter en mayuscula
print(myCadena.upper()) #Todos los caracteres en mayuscula
print(myCadena.casefold()) #Todos los caracteres en minuscula
print(myCadena.count('e')) #Todas las ocurrencuas de 'e' (2 para este ejemplo)
print(myCadena.find('E')) # Index de la primera ocuurencia de 'E'
print(myCadena.find('q'))
try:
    print(myCadena.index('q'))
except ValueError:
    print('Item not found')
print(myCadena.isascii()) #True si todos los caracteres son ascii
print(myCadena.isalpha()) #True si todos los caracteres son letras, en este caso hay espacios entonces False

myCadenaLista=['esta','era','una','lista']
myCadenaString = ' '.join(myCadenaLista) # list to string
print(myCadenaString, type(myCadenaString))
print('La longitud de myCadenaString es '+ str(len(myCadenaString)))

cadenaA = 'Cadena A'
cadenaB = 'Cadena B'
print(cadenaA + ' ' + cadenaB) #Concatenacion

cadenaC = 'Esta es la cadena C'
print(cadenaC)
print('Cadena C convertida en lista ->')
print(cadenaC.split())

####### Dificultad Extra
def isPalindrom(wordA, wordB):
    if wordA == wordB[::-1]:
        print('Las palabras son palindromas')
    else:
        print('Las palabras no son palindromas')

def isAnagram(wordA, wordB):
    listA = list(wordA)
    listB = list(wordB)
    if sorted(listA) == sorted(listB):
        print('Las palabras son anagramas')
    else:
        print('Las palabras no son anagrams')

def isIsogram(wordA):
    count = 0
    for i in range (len(wordA)//2):                
        if wordA.count(wordA[i]) > 1:            
            count += 1
    if count >  2:
        print('Is isogram')

isPalindrom('anilina','anilina')
isAnagram('peinar','pierna')
isIsogram('acondicionar')




