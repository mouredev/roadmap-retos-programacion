#Concatenacion
str1 = "Hola"
str2 = " mundo"
str1+str2
print(str1+str2)

#Repetiocion
cadena = "Hola "
print(cadena * 3)

#Longitud
cadena = "Hola Python"
print(len(cadena))

#Slicing
subcadena = cadena[4:]
print(subcadena)


#EXTRA
#Palindromo
def es_palindromo(str1: str):
    return True if str1[::-1] == str1 else False

#Anagrama
def es_anagrama(str1:str,str2:str):
    return True if sorted(str1) == sorted(str2) else False

#Isograma
def es_isograma(str1:str):
    contador = str1.count(str1[0])
    for i in str1:
        if str1.count(i) != contador:
            return False
    return True
print(es_palindromo('awa')) 
print(es_palindromo('abc'))    

print(es_anagrama('hola','aloh'))
print(es_anagrama('xd','uwu'))

print(es_isograma('abcabcabcddd'))