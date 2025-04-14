#  * EJERCICIO:
#  * Muestra ejemplos de todas las operaciones que puedes realizar con cadenas de caracteres
#  * en tu lenguaje. Algunas de esas operaciones podrían ser (busca todas las que puedas):
#  * - Acceso a caracteres específicos, subcadenas, longitud, concatenación, repetición, recorrido,
#  *   conversión a mayúsculas y minúsculas, reemplazo, división, unión, interpolación, verificación...
#  *
#  * DIFICULTAD EXTRA (opcional):
#  * Crea un programa que analice dos palabras diferentes y realice comprobaciones
#  * para descubrir si son:
#  * - Palíndromos
#  * - Anagramas
#  * - Isogramas

# Creacion y acceso:

s = 'Hola mundo' # Creacion de la cadena
s[5]             # Acceder a un caracter en concreto
s[2:6]           # Acceder a un tramo de la cadena [a:b]
len(s)           # funcion que cuenta el numero de caracteres de la cadena

# Comparaciones y busquedas:

# s1 == s2, s1 != s2, s1 > s2, etc.   ---> Comparaciones
'mundo' in s                         #---> Verifica si contiene una subcadena
s.find('mundo')                      #---> Indica la primera aparicion del texto
s.index('mundo')                     #---> Igual que la anterior pero imprime error si no existe
s.startswith('Hola')                 #---> Indica si el texto inicia con ('texto')
s.endswith('Mundo')                  #---> Indica si el texto termina con ('texto')
s.count('o')                         #---> Cuenta las ocurrencias de un caracter

# Modificacion y transformacion:

s.lower()                           #---> Transforma el texto a minusculas
s.upper()                           #---> Transforma el texto a mayusculas
s.title()                           #---> Transforma el texto a altas y bajas
s.capitalize()                      #---> Transforma en mayuscula la pirmera letra
s.swapcase()                        #---> Intercambia mayusculas y minusculas
s.replace('a','e')                  #---> Intercambia subcadenas
s.strip()                           #---> Elimina espacios al principio (o caracteres) o al final
s.rstrip(), s.lstrip()              #---> Elimina espacios a la derecha o a la izquierda respectivamente
s.zfill(5)                          #---> Rellena con ceros los caracteres indicaciones
s.center(10), 
s.ljust(10),                        #---> Alineación
s.rjust(10) 

# Union y separacion

# ' '.join(lista)                   #---> Une elementos con un separador
s.split()                           #---> Separa cadenas de texto por los espacios ( )
s.split(',')                        #---> Separa cadenas de texto por un caracter especifico (',')
s.partition('x')                    #---> Divide en 3 partes (antes, separador, después)
s.rsplit()                          #---> Separa cadenas de texto desde la derecha

# Verificacion (booleanas):

s.isalpha()                         # ---> Verifica si en la cadena hay solo letras
s.isdigit()                         # ---> Verifica si en la cadena hay solo numeros
s.isalnum()                         # ---> Verifica si hay letras y numeros
s.islower()                         # ---> Verifica si son todo minusculas
s.isupper()                         # ---> Verifica si son todo mayusculas
s.isspace()                         # ---> Verifica si son espacios 
s.istitle()                         # ---> Verifica si esta en altas y bajas (o titulo)

# Formateo de cadenas:

# nombre = 'juan'

# f"Hola {nombre}" # f-strings
# "Hola {}".format(nombre) # Método format
# "Hola %s" % nombre # Formato tipo C
# s.format_map(diccionario) # Formato con diccionarios

# Otros Útiles

# import re
# re.sub(), re.search()               # Expresiones regulares
# ord('a'), chr(97)                   # Unicode <-> caracter

#  * DIFICULTAD EXTRA (opcional):
#  * Crea un programa que analice dos palabras diferentes y realice comprobaciones
#  * para descubrir si son:
#  * - Palíndromos
#  * - Anagramas
#  * - Isograma

# Palindromo:
# Un palíndromo es una palabra, frase o número que se lee igual de izquierda a derecha
# que de derecha a izquierda, como "anana" o "12321"

# Anagrama:
# Un anagrama es una palabra o frase nueva que se obtiene al cambiar el orden de las 
# letras de otra palabra o frase. Por ejemplo, "Pedro" se puede transformar en "poder". 

# Isograma:

# Un isograma, es una palabra o frase en la que cada letra aparece el mismo número de veces. 
# Si cada letra aparece solo una vez será un heterograma, si aparece dos, un isogroma de 
# segundo orden y así sucesivamente. 

def descomponer(palabra):
    descomposicion = []
    for i in palabra:
        descomposicion.append(i)
    return descomposicion

def es_pali(lista):
    tupla_i = lista[::-1]
    if tupla_i == lista:
        return True
    else:
        return False
    
def es_ana(palabra1,palabra2):
    tf = []
    a = len(palabra1)
    b = len(palabra2)
    palabra1.sort()
    palabra2.sort()
    for i in range(len(palabra1)) and range(len(palabra2)):
        if palabra1[i] == palabra2[i]:
            tf.append(True)
        else:
            break
    
    if a == b and a == len(tf):
        return True
    else:
        return False
    
    
def es_iso(palabra):
    for i in palabra:
        if palabra.count(i) == 1:
            continue
        elif palabra.count(i) >= 2:
            return True
    return False


palabra1 = input(str('Introduzca la primera palabra:\n'))
palabra2 = input(str('Introduzca la segunda palabra:\n'))

a = descomponer(palabra1)
b = descomponer(palabra2)

if es_pali(a) == True:
    print(f'La palabra {palabra1} es un palindromo.')
    
elif es_ana(a,b) == True:
    print (f'Las palabras {palabra1} y {palabra2} son un anagrama.')
    
elif es_iso(palabra1) == True:
    print(f'La palabra {palabra1} es un Isograma.')
    
if es_pali(b) == True:
    print(f'La palabra {palabra2} es un palindromo.')
    
elif es_iso(palabra2) == True:
    print(f'La palabra {palabra2} es un Isograma.')
