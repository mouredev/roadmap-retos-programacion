"""
EJERCICIO:
  Muestra ejemplos de todas las operaciones que puedes realizar con cadenas de caracteres
  en tu lenguaje. Algunas de esas operaciones podrían ser (busca todas las que puedas):
  - Acceso a caracteres específicos, subcadenas, longitud, concatenación, repetición, recorrido,
    conversión a mayúsculas y minúsculas, reemplazo, división, unión, interpolación, verificación...
 """
 
# OPERACIONES CON CADENAS DE CARACTERES

s1 = "Hola"
s2 = "Daniel"

# Concatenacion
print(s1 + ', ' + s2)

# Repeticion
print(s1 * 5)

# Indexacion
print(s1[0])
print(s1[1])
print(s1[2])
print(s1[3])

# Longitud
print(len(s2))

# Slicing 
print(s1[0:3])
print(s1[3:])
print(s2[:2])

# Busqueda
print(s1.find('a')) # Busqueda de 'a' en la cadena
print('a' in s1) # Verificacion de si hay una 'a' en la cadena

# Reemplazo
s3 = s1.replace('a', 'e')
print(s3)

# Division
print(s2.split('i'))

# Mayusculas y minusculas, capitalizacion
s4 = s2.upper()
print(s4)

s5 = s2.lower()
print(s5)

s6 = s2.title()
print(s6)

# VERIFICACION DE CADENAS
# Verificacion de caracteres
print(s1.isalpha())
print(s1.isalnum())

# Verificacion de numeros
print(s2.isdecimal())
print(s2.isdigit())

# Verificacion de espacios
print(s1.isspace())

# Verificacion de capitalizacion
print(s2.istitle())

# Verificacion de capitalizacion
print(s2.islower())

# Eliminacion de espacios
print(' Hello Python '.strip())

# Formateo de cadenas
name = 'Daniel'
last_name = 'Quiros'
language = 'pythton'
print('Me llamo {} {}. Y aprendo {}'.format(name, last_name, language))

# Interpolacion de cadenas   
name = 'Daniel'
age = 25   
print('My name is {} and I am {} years old.'.format(name, age))
print(f'My name is {name} and I am {age} years old.')

#Transformacion de cadenas
s1 = 'Hello Python'
s2 = list(s1)
print(s2)

# Transformacion de listas a cadena
l1 = ['H', 'e', 'l', 'l', 'o', ' ', 'P', 'y', 't', 'h', 'o', 'n']
s3 = ''.join(l1)
print(s3)

# Transformacion numerica
n1 = "123456789"
n2 = int(n1)
print(n2)

n3 = '123.456'
n4 = float(n3)
print(n4)
   

"""
DIFICULTAD EXTRA (opcional):
  Crea un programa que analice dos palabras diferentes y realice comprobaciones
  para descubrir si son:
  - Palíndromos
  - Anagramas
  - Isogramas 
 """

print('\n--- EJERCICIO EXTRA ---\n')

def extra():
    palabra1 = input('Ingrese la primera palabra: ')
    palabra2 = input('Ingrese la segunda palabra: ')
    
    # Palindromo
    '''
    Un palindromo es una palabra que se lee igual en ambos sentidos.
    Por ejemplo: 
        - madam
        - racecar
        - aba
        - radar
    '''
    print(f'¿{palabra1} es un palindromo?: {palabra1 == palabra1[::-1]}')
    print(f'¿{palabra2} es un palindromo?: {palabra2 == palabra2[::-1]}')

    # Anagrama
    '''
    Una palabra es un anagrama de otra si ambas palabras ordenadas alfabéticamente son iguales.
    Por ejemplo:
        - amor -> roma
        - cosa -> asco
        - teresa -> aretes
        - madam -> damma
    '''
    print(f'¿{palabra1} es un anagrama de {palabra2}?: {sorted(palabra1) == sorted(palabra2)}')
   
    # Isograma
    '''
    Una palabra es un isograma si cada letra aparece una sola vez.
    Por ejemplo:
        - amor
        - cosa
        - python
    '''
    print(f'¿{palabra1} es un isograma?: {len(palabra1) == len(set(palabra1))}')
    print(f'¿{palabra2} es un isograma?: {len(palabra2) == len(set(palabra2))}')


extra()