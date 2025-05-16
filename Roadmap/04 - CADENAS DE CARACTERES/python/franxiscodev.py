'''
Cadenas de caracteres
'''

# concatenación
print("Hola " + "Franxisco")  # Hola Franxisco
print("Hola " "Franxisco")  # Hola Franxisco    # no recomendado
# Hola Franxisco  # recomendado   # f-string  # python 3.6
print(f"Hola Franxisco")
# Hola Franxisco  # recomendado   # python 3.6
print("Hola {}".format("Franxisco"))
print("Hola %s" % "Franxisco")  # Hola Franxisco  # recomendado   # python 2.7
print("Hola " * 3)  # Hola Hola Hola    # repetición

str1 = "Hola"
str2 = "Python"
print(str1 + str2)  # HolaPython
print(str1 + " " + str2)  # Hola Python   # concatenación   # recomendado
print(str1, str2)  # Hola Python    # concatenación   # recomendado
print(str1, str2, sep=" ")  # Hola Python    # concatenación   # recomendado
print(str1 * 3)  # HolaHolaHola    # repetición  # recomendado
print(f"{str1} {str2}")  # Hola Python    # f-string   # recomendado
print(" ".join([str1, str2]))  # Hola Python    # concatenación   # recomendado
print("Hola", "Python")  # Hola Python    # concatenación   # recomendado
# Hola Python    # concatenación   # recomendado
print("Hola", "Python", sep=" ")

# indexación strings
my_str = "Hola Franxisco"
print(my_str[0])  # H   # primer caracter
print(my_str[-1])  # o   # último caracter
print(my_str[0:4])  # Hola   # rango de caracteres  # [start:stop]
# Franxisco   # rango de caracteres  # [start:]  # hasta el final
print(my_str[5:])
# Hola   # rango de caracteres  # [:stop]  # desde el principio  # hasta stop
print(my_str[:4])
# Fra   # rango de caracteres  # [start:stop]   # desde start  # hasta stop
print(my_str[5:8])
# Hl rns o   # rango de caracteres  # [start:stop:step]  # desde start  # hasta stop  # con paso step   # recomendado
print(my_str[::2])
# ocsixnarF aloH   # rango de caracteres  # [::-1]  # invertir cadena   # recomendado
print(my_str[::-1])
# nix   # rango de caracteres  # [start:stop:step]  # desde start  # hasta stop  # con paso step  # recomendado  # invertido
print(my_str[8:5:-1])
# rango de caracteres  # [start:stop]  # desde start  # hasta stop  # recomendado   # no hay caracteres
print(my_str[8:5])
# Fra   # rango de caracteres  # [start:stop:step]  # desde start  # hasta stop  # con paso step  # recomendado
print(my_str[5:8:1])
# longitud string
print(len(my_str))  # 14

# slicing strings
my_str = "Hola Franxisco"   # 14
print(my_str[0:4])  # Hola

# busqueda en strings
my_str = "Hola Franxisco"
# True   # buscar si una cadena está en otra cadena
print("Franxisco" in my_str)    # True
# False   # buscar si una cadena no está en otra cadena  # recomendado  # más legible
print("Franxisco" not in my_str)    # False

# reemplazo en strings
my_str = "Hola Franxisco Franxisco"
# Hola Python   # reemplazar una cadena por otra cadena
print(my_str.replace("Franxisco", "Python"))  # Hola Python
# Hola Python   # reemplazar una cadena por otra cadena  # recomendado
# Hola Python  # 1 reemplazo
print(my_str.replace("Franxisco", "reemplaza solo el primero q encontro", 1))
# Hola Python   # reemplazar una cadena por otra cadena  # recomendado  # case sensitive
# Hola Franxisco  # no hay reemplazo
print(my_str.replace("franxisco", "Python"))
# Hola Franxisco   # reemplazar una cadena por otra cadena  # recomendado  # case sensitive # no hay reemplazo  # más legible
# Hola Franxisco  # 1 reemplazo    # más legible   # recomendado   # case sensitive    # no hay reemplazo
print(my_str.replace("franxisco", "Python", 1))

# split strings
my_str = "Hola Franxisco"
# ['Hola', 'Franxisco']   # separar una cadena por un caracter
print(my_str.split(" "))
# ['Hola', 'Franxisco']   # separar una cadena por un caracter  # recomendado   # más legible
# ['Hola', 'Franxisco']  # 1 separación  # recomendado
print(my_str.split(" ", 1))
# ['Hola', 'Franxisco']   # separar una cadena por un caracter  # recomendado   # más legible   # case sensitive
# ['Hola', 'Franxisco']  # 1 separación  # recomendado  # case sensitive
print(my_str.split(" ", 1))
# ['Hola', 'Franxisco']   # separar una cadena por un caracter  # recomendado   # más legible   # case sensitive    # no hay separación
# ['Hola', 'Franxisco']  # 2 separaciones  # recomendado  # case sensitive  # no hay separación
print(my_str.split(" ", 2))
# ['Hola', 'Franxisco']   # separar una cadena por un caracter  # recomendado   # más legible   # case sensitive    # no hay separación # más legible   # recomendado
# ['Hola', 'Franxisco']  # 2 separaciones  # recomendado  # case sensitive  # no hay
print(my_str.split(" ", 2))
# ['Hola', 'Franxisco']   # separar una cadena por un caracter  # recomendado   # más legible   # case sensitive    # no hay separación # más legible   # recomendado                                       # case sensitive

# minusculas y mayusculas - capitalización - títulos
my_str = "Hola Franxisco"
# hola franxisco   # convertir a minúsculas
print(my_str.lower())
# HOLA FRANXISCO   # convertir a mayúsculas
print(my_str.upper())
# Hola Franxisco   # convertir a capitalización
print(my_str.capitalize())
# Hola franxisco   # convertir a capitalización
print(my_str.title())
# Hola franxisco   # convertir a capitalización  # recomendado

# espacios en blanco
my_str = " Hola Franxisco "
# Hola Franxisco   # eliminar espacios en blanco al principio y al final
print(my_str.strip())
# Hola Franxisco   # eliminar espacios en blanco al principio y al final  # recomendado
print(my_str.strip())
# Hola Franxisco   # eliminar espacios en blanco al principio
print(my_str.lstrip())
# Hola Franxisco   # eliminar espacios en blanco al principio  # recomendado
print(my_str.lstrip())
# Hola Franxisco   # eliminar espacios en blanco al final
print(my_str.rstrip())
# Hola Franxisco   # eliminar espacios en blanco al final  # recomendado
print(my_str.rstrip())

# encontrar  la posicion de una cadena
my_str = "Hola Franxisco @franxiscodev"
# 5   # encontrar la posición de una cadena en otra cadena
print(my_str.find("Franxisco"))  # 5
# -1   # encontrar la posición de una cadena en otra cadena  # recomendado
print(my_str.find("Python"))    # -1    # no encontrado     # recomendado
print(my_str.find("f"))    # 16    # @franxiscodev
print(my_str.lower().find("f"))    # 5    # Franxisco -> franxisco x el lower
print(my_str.lower().count("f"))    # 2 veces
print(my_str.count("f"))    # 1 vez la otra es MAY

# interpolación de strings
my_str = "Franxisco"
# Hola Franxisco   # interpolación de strings   # recomendado
print(f"Hola {my_str}")  # Hola Franxisco    # recomendado
# Hola Franxisco   # interpolación de strings

# transformar strings en listas
my_str = "Hola Franxisco"
# ['H', 'o', 'l', 'a', ' ', 'F', 'r', 'a', 'n', 'x', 'i', 's', 'c', 'o']   # transformar una cadena en una lista
print(list(my_str))

# transformar lista en string
my_list = ["H", "o", "l", "a", " ", "F",
           "r", "a", "n", "x", "i", "s", "c", "o"]
# Hola Franxisco   # transformar una lista en una cadena
print("".join(my_list))

'''
Extra
'''


def check_palindrome(word: str) -> bool:
    return word == word[::-1]   # invertir cadena


def check_anagram(word_1: str, word_2: str) -> bool:
    return sorted(word_1) == sorted(word_2)   # ordenar cadena


def check_isogram(word: str) -> bool:
    return len(word) == len(set(word))   # no repetir caracteres


# isogramas
def check_isograms(word: str) -> str:
    word_dict = {}  # diccionario
    for char in word:
        word_dict[char] = word_dict.get(char, 0) + 1

    is_isogram = True
    # tomar el len de la primera pos y todas deben ser del mismo valor
    values_word_dict = list(word_dict.values())
    isogram_len = values_word_dict[0]   # tomar el len de la primera pos
    for char_count in values_word_dict:
        if char_count != isogram_len:
            is_isogram = False
            break   # salir del ciclo

    return is_isogram


print("--------- Isogramas ---------")
palabra = "murcielago"
# True
print(f"la palabra {palabra} es un isograma {check_isograms(palabra)}")
