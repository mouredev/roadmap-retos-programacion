
string1 = 'juanrcoder'
string2 = 'pythonRoadMap'

print(string1[1])                               #Acceso a carateres especificos
print(len(string1))                             #Longitud de carateres de un string.
print(string1 + string2)                        #Concatenacion de string.
print(string1*3)                                #Repeticion del string.
print([i for i in string1])                     #Recorrido en el string.
print(string1.upper())                          #Convertir el string a mayuscula.
print(string2.lower())                          #Convertir el string a minuscula.
print(string1.replace('rcoder','cito'))         #Reemplazar pedazos del string.
print(string1[1])                               #Acceso a carateres especificos.
print('-'.join(string1))                        #Union con - de cada caracter.
print(f"{string1} aprende en el {string2}")     #Interpolacion de string.
print(string2.isdigit())                        #Verifica si tiene digitos.
print(string1[1:5])                             #Subcadena de string1.
print(string2.split('o'))                       #Division de la cadena por cada 'o'.


#  * DIFICULTAD EXTRA (opcional):
def isPalindromo(str):
    str = str.lower().replace(" ", "")
    return str == str[::-1]

print(isPalindromo('reconocer'))


def isAnagramas(str, str2):
    str, str2 = list(set(str.lower())), list(set(str2.lower()))
    str.sort()
    str2.sort()
    str , str2 = ''.join(str), ''.join(str2)
    return str == str2

print(isAnagramas('pedro','drope'))


def isIsograma(str):
    str = str.lower()
    obj = {}
    for i in str:
        if i in obj:
            obj[i] += 1
        else:
            obj[i] = 1
            
    for _, v in obj.items():
        if v > 1:
            return False
    return True

print(isIsograma('murcielago'))
