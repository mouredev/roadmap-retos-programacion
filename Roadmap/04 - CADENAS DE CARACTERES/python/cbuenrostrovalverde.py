'''
 * EJERCICIO:
 * Muestra ejemplos de todas las operaciones que puedes realizar con cadenas de caracteres
 * en tu lenguaje. Algunas de esas operaciones podrían ser (busca todas las que puedas):
 * - Acceso a caracteres específicos, subcadenas, longitud, concatenación, repetición, recorrido,
 *   conversión a mayúsculas y minúsculas, reemplazo, división, unión, interpolación, verificación...
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que analice dos palabras diferentes y realice comprobaciones
 * para descubrir si son:
 * - Palíndromos
 * - Anagramas
 * - Isogramas
 '''

# Acceso a caracteres específicos:
cadena = 'Hola Mundo'
print(cadena[0])

# Subcadenas(Indexación)
print(cadena[:7])

# Longitud
print(len(cadena))

# Concatenación
cadena1 = 'Hola'
cadena2 = 'Mundo'

print(cadena1 + cadena2)
print(cadena1 + ' ' + cadena2 + '!')

# Repetición
print(cadena1 + cadena1 + cadena1)
print(cadena1 * 3)

# Slicing (porción)
print(cadena2[2:5])
print(cadena2[2:]) # Que empiece desde donde quiero hasta el final
print(cadena2[0:2])
print(cadena2[:2])

# Búsqueda
print("H" in cadena1)
print("M" in cadena1)

# Reemplazo
print(cadena1.replace("o", "a"))

# División
print(cadena1.split("l"))

# Mayúsculas y minúsculas
print(cadena1.upper())
print(cadena2.lower())
print('carlos buenrostro'.title())
print('carlos buenrostro'.capitalize())

# Eliminación de espacions al principio y al final
print('carlos buenrostro valverde'.strip() + ' ' + '@carlosbuenrostrovalverde')

# Búsqueda al principio y al final
print(cadena1.startswith('H'))
print(cadena1.startswith('M'))

# Búsqueda de posición
print('Carlos Buenrostro Valverde @cbuenrostrovalverde'.find('@'))
print('Carlos Buenrostro Valverde @cbuenrostrovalverde'.find('l'))
print('Carlos Buenrostro Valverde @cbuenrostrovalverde'.lower().find('v'))

cadena3 = 'Carlos Buenrostro Valverde @cbuenrostrovalverde'

# Búsqueda de ocurrencias
print(cadena3.lower().find('n'))

# Formateo
print('Saludo: {}, Dirigido: {}'.format(cadena1, cadena2) )

# Interpolación
print(f'Saludo: {cadena1}, lenguaje: {cadena2}!')

# Transformación en lista de caracteres:
print(list(cadena3))

# Transformación de lista en cadena:
cadena4 = [cadena1, ' ', cadena2, '!']

print(''.join(cadena4))

# Transformaciones numéricas:

cadena5 = '123456789'
cadena5 = int(cadena5)
print(cadena5)

# Comprobaciones varias:

print(cadena1.isalnum())
print(cadena1.isalpha())

'''
Extra
'''

'''Crea un programa que analice dos palabras diferentes y realice comprobaciones
 * para descubrir si son:
 * - Palíndromos
 * - Anagramas
 * - Isogramas
 '''

def check(word1: str, word2: str):
    # Palíndromos: Si inviertes el orden, obtendríamos la misma palabra (radar, asa, etc...)
    print(f'¿{word1} es una palabra palíndroma?: {word1 == word1[::-1]}')
    print(f'¿{word2} es una palabra palíndroma?: {word2 == word2[::-1]}')

    # Anagramas: Palabra que resulta de la transposiciónde todas las letras de una palabra. Cambio de orden de las letras.
    print(f'¿{word1} es una anagrama de {word2}?: {sorted(word1) == sorted(word2)}')

    # Isograma
    print(f'¿{word1} es una isograma?: {len(word1) == len(set(word1))}')
    print(f'¿{word2} es una isograma?: {len(word2) == len(set(word2))}')

    word_dict = dict()
    for word in word1:
        word_dict[word] = word_dict.get(word, 0) + 1

    isogram = True
    isogram_len = word_dict.values
    for word_count in word_dict:
        if len(word_count) != isogram_len:
            isogram = False
            break

# check('roma', 'amor')
check('radar', 'python')
