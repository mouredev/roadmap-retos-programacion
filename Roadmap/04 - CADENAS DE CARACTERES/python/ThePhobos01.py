#Diferentes opciones que tenemos con cadenas de caracteres (String) en Pyuthon

#Imprimir una cadena
print('Hola mundo!')

#Concatenar
print('Hola ' + 'Mundo')

#Multiplicar
print('Hola ' * 3 + 'Mundo')

#Longitud

print(len('Hola mundo!'))

#Encontrar

saludo = 'Hola Mundo!'

saludo = saludo.find('Mundo!')

print(saludo)

#Poner en minusculas
print('Hola mundo!'.lower())

#Poner en mayusculas
print('Hola Mundo!'.upper())

#Reemplazar
print('Hola Mundo!'.replace('Mundo!', 'Python!'))

#Cortar
print('Hola Mundo!'[1:8])


#Dificultad extra

def es_palindromo(palabra):
    palabra = palabra.replace(" ", "").lower()
    return palabra == palabra[::-1]

def es_anagrama(palabra1, palabra2):
    palabra1 = palabra1.replace(" ", "").lower()
    palabra2 = palabra2.replace(" ", "").lower()
    return sorted(palabra1) == sorted(palabra2)

def es_isograma(palabra):
    palabra = palabra.replace(" ", "").lower()
    return len(palabra) == len(set(palabra))

def analizar_palabras(palabra1, palabra2):
    print(f"Analizando las palabras: '{palabra1}' y '{palabra2}'")
    
    if es_palindromo(palabra1):
        print(f"'{palabra1}' es un palíndromo.")
    if es_palindromo(palabra2):
        print(f"'{palabra2}' es un palíndromo.")
    
    if es_anagrama(palabra1, palabra2):
        print(f"'{palabra1}' y '{palabra2}' son anagramas.")
    else:
        print(f"'{palabra1}' y '{palabra2}' no son anagramas.")
    
    if es_isograma(palabra1):
        print(f"'{palabra1}' es un isograma.")
    else:
        print(f"'{palabra1}' no es un isograma.")
    if es_isograma(palabra2):
        print(f"'{palabra2}' es un isograma.")
    else:
        print(f"'{palabra2}' no es un isograma.")

analizar_palabras("reconocer", "roma")