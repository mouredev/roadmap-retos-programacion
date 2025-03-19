### Cadena de Caracteres

'''
EJERCICIO:
 * Muestra ejemplos de todas las operaciones que puedes realizar con cadenas de caracteres
 * en tu lenguaje. Algunas de esas operaciones podrían ser (busca todas las que puedas):
 * - Acceso a caracteres específicos, subcadenas, longitud, concatenación, repetición,
 *   recorrido, conversión a mayúsculas y minúsculas, reemplazo, división, unión,
 *   interpolación, verificación...
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que analice dos palabras diferentes y realice comprobaciones
 * para descubrir si son:
 * - Palíndromos
 * - Anagramas
 * - Isogramas
 '''
'''
Operaciones
'''
# Concatenacion
s1 = 'Hola '
s2 = 'Python'
print(s1 + ' ' + s2 +'!')

# Repeticion
print(s1 * 3)

# Indexacion
print(s1[0] + s1[1] + s1[2] + s1[3])

# Longitud
print(len(s2))

# Slicing
print(s2[2:6])
print(s2[2:])
print(s2[0:2])
print(s2[:2])

# Busqueda
print('a' in s1)

# Reemplazo
print(s1.replace('o', 'a'))

# Division
print(s2.split('t'))

# Mayusculas y minusculas
print(s1.upper())
print(s1.lower())
print('adolfo loza'.title())
print('adolfo loza'.capitalize())

# Eliminacion de espacios al principio y al final
s3 = ' Adolfo Loza '
print(s3.strip() + '@adolfolozaa')

# Busqueda al principio y al final
print(s1.startswith('Ho'))
print(s1.startswith('Py'))
print(s1.endswith('la '))
print(s2.endswith('n'))

# Busqueda de Posicion
print('Adolfo Loza @adolfolozaa'.find('folo')) #empieza en 0
print('Adolfo Loza @adolfolozaa'.find('Loza'))
print('Adolfo Loza @adolfolozaa'.find('L'))
print('Adolfo Loza @adolfolozaa'.find('o'))

# Busqueda de ocurrencias
print('Adolfo Loza @adolfolozaa'.count('o'))
print('Adolfo Loza @adolfolozaa'.count('lo'))

# Formateo
print('Saludo: {} Lenguaje: {}'.format('Adolfo', 'Python'))

# Interpolar
print(f'Saludo: {s1} Lenguaje: {s2}')

# Transformacion cadena en lista de caracteres
print(list(s3))

# Transformacion de lista en cadena 
l1 = [s1, ', ', s2, '!']
print(l1)
print(''.join(l1))
print('-'.join(l1))

# Transformaciones numericas
s4 = '1234'
s5 = int(s4)
print(type(s5))
s6 = '1234.56'
s7 = float(s6)
print(type(s7))

s8 = 5
# Comprobaciones varias
print(s1.isalnum()) 
print(s3.isalpha())
print(s4.isnumeric()) #solo aplica a str

'''
DIFICULTAD EXTRA (opcional):
 * Crea un programa que analice dos palabras diferentes y realice comprobaciones
 * para descubrir si son:
 * - Palíndromos
 * - Anagramas
 * - Isogramas
 '''
print( 'Analisis de Palabras')
print('--------------------')

# Ingreso de palabras
def enter_words():
    print('Por favor ingrese dos palabras ')
    global w1, w2
    w1 = input('Palabra nupero 1: ')
    w2 = input('Palabra numero 2: ')
    print(f'Las palabras ingresadas son: {w1} y {w2}')
    global w1_1
    w1_1 = w1.lower()
    global w2_1
    w2_1 = w2.lower()
    print(w1_1 + ' '+ w2_1)
    w2_1

enter_words()

# Palindromos
def palin():
    print('\n\nanalisis de polindromos')
    print('--------------------')
    reversed_w2_1 = w2_1[::-1]  # de inicio a fin a la inversa
    #print(reversed_w2_1)
    if w1_1 == reversed_w2_1:
        print(f'Las palabras {w1} y {w2} --SI-- son palindromos')
    else:
        print(f'Las palabras {w1} y {w2}  --NO-- palindromos')

palin()

# Anagramas
def ana():
    print('\n\nanalisis de anagramas')
    print('--------------------')
    if len(w1_1) != len(w2_1):
        print(f'Las palabras {w1_1} y {w2_1} --NO-- son Anagramas')
        bandera = 0
    else:
        bandera = 1
    counter =0
    for letra in w1_1:
        if letra not in w2_1:
            break
        else:
            counter +=1
    if counter == len(w2_1):

        print(f'Las palabras {w1_1} y {w2_1} --SI-- son Anagramas')
    else:
        if bandera == 1:
            print(f'Las palabras {w1_1} y {w2_1} --NO-- son Anagramas')
ana()

# Isogramas

def check(w1_1 : str, w2_1 : str ):
    print('\n\nanalisis de isogramas')
    print('--------------------')
    def isogram(word: str) -> bool:
        word_dict = dict()
        for character in word:
            word_dict[character] = word_dict.get(character, 0) + 1
        isogram = True
        values = list(word_dict.values())
        print(values)
        isogram_len = values[0]
        for word_count in values:
            if word_count != isogram_len:
                isogram = False
                break
        return isogram
    
    print(f"{w1_1} es un isograma?: {isogram(w1_1)}")
    print(f"{w2_1} es un isograma?: {isogram(w2_1)}")

check(w1_1, w2_1)
