"""
CADENAS DE CARACTERES"""

tx1 = 'Hola'
tx2 = 'Python'
tx3 = 'Esto es una variable'

#Concatenacion
print(tx1+ ' ' + tx2+ '!!')

#Repeticion
print(tx1 * 5)

#indexacion
print(tx1[0] + tx1[1] + tx1[2]+ tx1 [3])

#Longitud
print(len(tx2))

#slicing (porcion)
print(tx2[0:3]) #el ultimo indice no se incluye
print(tx2[3:])

#busqueda
print('th' in tx2);

#remplazo
print(tx1.replace('o', 'a'))


#division
print(tx2.split('t'))


#mayuscula, minuscula y primera letra mayuscula
print(tx2.upper())
print(tx2.lower())
print('carro rojo'.title()) #primera letra de cada palabra mayuscula
print('carro rojo'.capitalize()) #solo la primera letra mayuscula


#Eliminacion de espacio al principio y al final
print(' carro rojo '.strip())


#Busqueda al principio y al final
print(tx1.startswith('Ho'))
print(tx2.startswith('a'))
print(tx1.endswith('lo'))
print(tx2.endswith('n'))

#Busqueda de posicion
print('Este es un ejemplo'.find('es')) #5
print('Este es un ejemplo'.lower().find('es')) #0

#busquda de ocuerrencia
print('Este es un ejemplo'.lower().count('es')) #2


#Formateo
print('Saludo: {}, Lenguaje {}!'.format(tx1,tx2))

#Interpolacion
print(f'Saludo: {tx1}, Lenguaje {tx2}!')


#Transformacion en lista de caracteres
print(list(tx3))

#Transformacion de lista en cadena
l1 = [tx1, ', ', tx2, '!' ]
print(''.join(l1)) #join: concatenar resultados de una lista


#Transformaciones numericas
txt4 = '124312.821'
txt4 = float(txt4)
print(txt4)


#comprobaciones varias
txt4 = '124312.821'
print(tx2.isalnum()) #True
print(tx2.isnumeric()) #False
print(txt4.isnumeric())



"""
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que analice dos palabras diferentes y realice comprobaciones
 * para descubrir si son:
 * - Palíndromos
 * - Anagramas
 * - Isogramas"""


def comprobar_palabra(palabra : str, palabra2 : str):

    #Palindromos: Se lee igual al derecho y al revés.
    print(f"La palabra {palabra} Es un palindromo?  {palabra == palabra[::-1]}")
    print(f"La palabra {palabra2} Es un palindromo?  {palabra2 == palabra2[::-1]}")

    #Anagrama: Palabra formada al reorganizar las letras de otra.
    print(f"La palabra {palabra} Es un analagrama de la palabra {palabra2}? {sorted(palabra) == sorted(palabra2)}")

    ##Isograma: Ninguna letra se repite.
    ##print(f"La palabra {palabra} es un Isograma? {len(palabra) == len(set(palabra))} ")
    ##print(f"La palabra {palabra2} es un Isograma? {len(palabra2) == len(set(palabra2))} ")

    #isograma: si todas las letras aparecen la misma cantidad de veces.
    def isograma(word: str) -> bool:

        palabra_dict = dict()
        for caracter in word:
            palabra_dict[caracter] = palabra_dict.get(caracter, 0) + 1

        isograma = True
        values = list(palabra_dict.values())
        isograma_len = values[0]
        for palabra_contada in values:
            if palabra_contada != isograma_len:
                isograma = False
                break
        return isograma

    print(f'{palabra} es un isograma?: {isograma(palabra)}')
    print(f'{palabra2} es un isograma?: {isograma(palabra2)}')



comprobar_palabra('reconocer', 'radar' )
comprobar_palabra('amor', 'roma')

comprobar_palabra('ropa', 'pythonpython')