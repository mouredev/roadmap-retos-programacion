# Operaciones con cadenas de caracteres
str1 = "Hola"
str2 = "Mundo"
print(str1[0]) # Acceso a caracteres específicos: H
print(str1[1:3]) # Subcadenas: Hola -> ol (slicing)
print(len(str1)) # Longitud: 4
print(str1 +', ' + str2) # Concatenación: Hola, Mundo
print(str1 * 3) # Repetición: HolaHolaHola
for i in str1: # Recorrido: Hola
    print(i)
print(str1.upper()) # Conversión a mayúsculas: HOLA
print(str1.lower()) # Conversión a minúsculas: hola
print('hola mundo'.capitalize()) # Capitalización: Hola mundo
print('hola mundo'.title()) # Capitalización de palabras: Hola Mundo
print('hola Mundo'.swapcase()) # Inversión de capitalización: HOLA mUNDO
print('  hola mundo  '.strip()) # Eliminación de espacios en blanco: hola mundo
print(str1.replace('o','a')) # Reemplazo: Hala
print(str1.split('o')) # División: ['H', 'la']
print(''.join([str1,str2])) # Unión: HolaMundo
print(f'{str1} {str2}') # Interpolación: Hola Mundo
print(str1.isalpha()) # Verificación: True. esta función verifica si la cadena contiene solo letras
print(str1.isalnum()) # Verificación: True. esta función verifica si la cadena contiene solo letras y números
print(str1.isdigit()) # Verificación: False. esta función verifica si la cadena contiene solo números
print(str1[0]+str1[1]+str1[2]+str1[3]) # Indexación: Hola
print(str1[::-1]) # Inversión: aloH
print(str1 == str1[::-1]) # Palíndromos: False (Hola != aloH)
print(sorted(str1) == sorted(str2)) # Anagramas: False (Hola != Mundo). anagrama es una palabra o frase que resulta de la transposición de letras de otra palabra o frase
print("a" in str1) #Búsqueda: True. verifica si la letra a está en la cadena
print('Saludo: {}, lenguaje: {}'.format(str1,str2)) #Formateo: Saludo: Hola, lenguaje, Mundo
print(list(str1)) # Transformacion de cadena a lista: ['H', 'o', 'l', 'a']

# EXTRA
'''Crea un programa que analice dos palabras diferentes y realice comprobaciones
 * para descubrir si son:
 * - Palíndromos: palabras que se leen igual de izquierda a derecha que de derecha a izquierda
 * - Anagramas: palabras que tienen las mismas letras pero en diferente orden
 * - Isogramas: palabras que no tienen letras repetidas'''

# quiero un programa que haga todas las comprobaciones en la misma funcion
def check(word1:str,word2:str):
    print(f'La palabra {word1} es un palíndromo?: {word1==word1[::-1]}')
    print(f'La palabra {word2} es un palíndromo?: {word2==word2[::-1]}')
    print(f'{word1} es un anagrama de {word2}?: {sorted(word1) == sorted(word2)}')
    print(f'{word1} es un isograma?: {len(set(word1)) == len(word1)}')
    print(f'{word2} es un isograma?: {len(set(word2)) == len(word2)}')

word1 = "reconocer"
word2 = "carrera"
word3 = "murcielago"
word4 = "anagrama"
word5 = 'amor'
word6 = 'roma'
check(word1,word2) 
check(word3,word4)
check(word5,word6)