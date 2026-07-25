######## CADENAS DE CARACTERES (Tipo de dato inmutable) #######################

cadena = "Hola que tal"

print('Concatenación: ' + cadena + cadena)

print('Repetición: ' + cadena*3)

print('Indexación: ' + cadena[0] + cadena[1])

print('Longitud de la cadena (len): ' + str(len(cadena)))

# Las cadenas se pueden recorrer

cadena = 'informática'

for caracter in cadena:
  print(caracter, " " ,  end="")
  
'''
Operadores de pertenencia: Se puede comprobar si un elemento (subcadena) pertenece o no 
a una cadena de caracteres con los operadores in y not in.
'''
print('á' in cadena)

print('p' in cadena)

print('p' not in cadena)

"""
Slice (rebanada): Puedo obtener una subcadena de la cadena de caracteres. 
Se indica el carácter inicial, y el carácter final, además podemos indicar opcionalmente un salto. 
Si no se indica el carácter inicial se supone que es desde el primero, sino se indica el carácter final 
se supone que es hasta el final. 
Por último podemos usar salto negativo para empezar a contar desde el final.
"""

cadena = "inteligencia artifical"

print(cadena[2:5]) # Desde el tercer carácter hasta el quinto

print(cadena[2:7:2]) # Desde el tercer carácter hasta el séptimo con salto de 2

print(cadena[:5]) # Desde el primer carácter hasta el quinto

print(cadena[5:]) # Desde el quinto carácter hasta el final

print(cadena[-1:-3]) # Desde el último carácter hasta el penúltimo

print(cadena[::-1]) # Invertir la cadena

print(cadena[::-2]) # Invertir la cadena con salto de 2

# Podemos convertir cualquier número en una cadena de caracteres utilizando la función str()
num = str(123)

print(type(num))

# Conversión a mayúsculas y minúsculas
print(cadena.upper())
print(cadena.lower())

# Title: Convierte la primera letra de cada palabra en mayúscula
print(cadena.title())

# Capitalize: Convierte la primera letra de la cadena en mayúscula
print(cadena.capitalize())

# Reemplazar elementos dentro de una cadena
print(cadena.replace("i", "@"))

# Eliminar espacios en blanco
cadena = "    Hola que tal    "
cadena_sin_espacios = cadena.strip()
print(cadena_sin_espacios)

# Podemos separar una cadena de caracteres y el resultado se almacena en una lista.
words = cadena_sin_espacios.split(" ")
print(words)
print(type(words))

######## FIN CADENAS DE CARACTERES (Tipo de dato inmutable) #######################

######## EXTRA #######################

word1 = input("Introduce la palabra 1: ")
word2 = input("Introduce la palabra 2: ")

while word1 == "" or word2 == "":
  print("Debes introducir palabras")
  word1 = input("Introduce la palabra 1: ") if word1 == "" else word1
  word2 = input("Introduce la palabra 2: ") if word2 == "" else word2

# Comprobar si las palabras son iguales
if word1.lower() == word2.lower():
  print("Las palabras son iguales")
else:
    print("Las palabras son diferentes")

# Comprobar si las palabras son anagramas
if sorted(word1.lower()) == sorted(word2.lower()):
  print("Las palabras son anagramas")
else:
    print("Las palabras no son anagramas")

# Comprobar si las palabras son palíndromas
print('La palabra 1 es palíndroma') if word1.lower() == word1[::-1].lower() else print('La palabra 1 no es palíndroma')
print('La palabra 2 es palíndroma') if word2.lower() == word2[::-1].lower() else print('La palabra 2 no es palíndroma')

# Comprobar si las palabras son Isogramas
isograma = True
for char in word1.lower():
    if word1.lower().count(char) > 1:
        isograma = False
        break
if isograma:    
    print(f'{word1} es un Isograma porque cada caracter aparece una sola vez en la palabra')
else:
    print(f'{word1} no es un Isograma porque {char} se repite más veces en la palabra')    

isograma = True

for char in word2.lower():
    if word2.lower().count(char) > 1:
        isograma = False
        break
if isograma:    
    print(f'{word2} es un Isograma porque cada caracter aparece una sola vez en la palabra')
else:
    print(f'{word2} no es un Isograma porque {char} se repite más veces en la palabra')
    
######## FIN EXTRA #######################