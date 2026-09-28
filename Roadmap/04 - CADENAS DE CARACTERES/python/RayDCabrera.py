mensaje = "Hola Mundo"

#concatenación
print(mensaje + " Cruel")

#multiplicacion
print(mensaje*3)

#Se puede saber si una cadena esta contenida en otra    
print("Hola" in mensaje) #true  

#Longitud de una cadena
print(len(mensaje))

#Se pueden indexar las cadenas como una lista
print(mensaje[0]) #H
print(mensaje[-1]) #o

#Se pueden crear cadenas mas pequeñas usando el mismo metodo    
print(mensaje[0:2])

#Si no se indica ningun valor a la derecha de los : se llega hasta el final 
print(mensaje[2:])

#Tambien podemos saltear sin necesidad de que sea continuo, añadiendo un [] mas    
print(mensaje[0:5:2])
print(mensaje[0:5:1])

print(mensaje[0::2])

#-----------Metodos----------------
cadena = 'metodo'
print(cadena.capitalize()) #devuelve la primera letra en mayúsculas

print(cadena.lower()) # en minúsculas

print(cadena.swapcase()) # invierte mayúsculas y minúsculas

print(cadena.upper()) # en mayúsculas

print(cadena.count("o")) # cuenta la cantidad de veces que hay una cadena en otra

print(cadena.isalnum()) # devuelve True si en la cadena hay solo alfanumericos
print(cadena.isalpha()) # devuelve true si todos son alfabeticos

print(cadena.strip()) # elimina a la izquierda y derecha el caracter que se le introduce    

print(cadena.join(["1","2"]))


#------------  EXTRA =============


def es_palindromo(palabra1, palabra2):
    lista = [palabra1, palabra2]
    for p in lista:
        if p == p[::-1]:
            print(f"La palabra {p}, es palindromo")
        else:
            print(f"La palabra {p}, no es palindromo")

def es_anagrama(palabra1, palabra2):
    if sorted(palabra1) == sorted(palabra2):
        print("Las palabras son anagrama")
    else:
        print("Las palabras no son anagramas")

def es_isograma(palabra1, palabra2):
    lista = [palabra1, palabra2]
    for p in lista:
        if len(set(p)) == len(p):
            print("Es isograma")
        else:
            print("No es isograma")

es_palindromo("oso","rata")
es_anagrama("amor","calculo")
es_anagrama("amor","roma")
es_isograma("amor", "casa")


