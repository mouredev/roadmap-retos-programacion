# #04 - Python -> Jesus Antonio Escamilla

"""
EJERCIÓ
"""
#---STRING---
s1 = 'Hola Mundo'
print(f'String -> {s1}')

#---SUB-CADENA---
sub_s1 = s1[5:10]
print(f'Sub-Cadena -> {sub_s1}')

#---LONGITUD---
length = len(s1)
print(f'Longitud -> {length}')

#---CONCATENACIÓN---
s11 = 'Hola'
s12 = 'Mundo'
result = s11 + s12
print(f'Concatenación -> {result}')

#---REPETICIÓN---
repeated = s1 * 3
print(f'Repetición -> {repeated}')

#---MAYÚSCULAS Y MINÚSCULAS---
upper = s1.upper()
lower = s1.lower()
print(f'Mayúsculas -> {upper}')
print(f'Minúsculas -> {lower}')

#---REEMPLAZO---
replaced = s1.replace("Mundo", "Python")
print(f'Reemplazo -> {replaced}')

#---DIVISION---
s1_ = "Hola,Mundo,Python"
parts = s1_.split(",")
print(f'Division -> {parts}')

#---UNION---
words = ["Hola", "Mundo", "Python"]
joined = " ".join(words)
print(f'Union -> {joined}')

#---INTERPOLACIÓN---
nombre = "Antonio"
s1__ = "Hola {}".format(nombre)
print(f'Interpolación -> {s1__}')

#---VERIFICACIÓN---
# --IGUALDAD--
s3 = "Hola Mundo"
is_equal = s1 == s3
print(f'Verificación-Igualdad (Hola Mundo == Hola Mundo) -> {is_equal}')

# --EMPIEZA--
starts_with = s1.startswith("Hola")
print(f'Verificación-Empieza (Hola Mundo == Hola) -> {starts_with}')

# --TERMINA--
ends_with = s1.endswith("Mundo")
print(f'Verificación-Termina (Hola Mundo == Mundo) -> {ends_with}')

# --CONTIENE--
contains = "Mundo" in s1
print(f'Verificación-Contiene (Hola Mundo == Mundo) -> {contains}')



"""
EXTRA
"""
def es_palíndromo(word):
    word = word.lower()
    return word == word[::-1]

def son_anagramas(word1, word2):
    word1 = word1.lower()
    word2 = word2.lower()
    return sorted(word1) == sorted(word2)

def es_isograma(word):
    word = word.lower()
    return len(set(word)) == len(word)

def EXTRA(palabra1: str, palabra2: str):
    #Palíndromo
    print(f'{palabra1} es un Palíndromo: {es_palíndromo(palabra1)}')
    print(f'{palabra2} es un Palíndromo: {es_palíndromo(palabra2)}')
    
    #Anagrama
    print(f'{palabra1} es Anagrama de {palabra2}: {son_anagramas(palabra1, palabra2)}')
    
    #Isograma
    print(f'{palabra1} es un Isograma: {es_isograma(palabra1)}')
    print(f'{palabra2} es un Isograma: {es_isograma(palabra2)}')

EXTRA('radar', 'roma')