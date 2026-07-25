'''
EJERCICIO:
Muestra ejemplos de todas las operaciones que puedes realizar con cadenas de caracteres en tu lenguaje. Algunas de esas operaciones podrían ser (busca todas las que puedas):
- Acceso a caracteres específicos, subcadenas, longitud, concatenación, repetición, recorrido, conversión a mayúsculas y minúsculas, reemplazo, división, unión, interpolación, verificación...
'''
# Cadenas de carácteres
s1 = 'Hola'
s2 = 'Python'
s3 = 'Brais Moure @mouredev'
s4 = '1234'

l1 = [s1, ', ', s2, '!']

# Concatenación e interpolación
print(s1+ ' ' +s2) # Resultado - Hola Python
print(f'{s1} {s2}') # Resultado - Hola Python

# Repetición
print((f'{s1} {s2}\n') * 3) 
'''
Resultado - 
Hola Python
Hola Python
Hola Python
'''

# Indexación
print(f'{s1[0]}{s1[1]}{s1[2]}{s1[3]}') # Resultado - Hola

# Longitud
print(len(s2)) # Resultado - 6

# Slicing (Porción)
print(s2[2:6]) # Resultado - thon
print(s2[2:]) # Resultado - thon
print(s2[:2]) # Resultado - Py
print(f'{s2[:2]}{s2[2:]}') # Resultado - Python

# Busqueda
print('a' in s1) # Resultado - True
print('Ho' in s1) # Resultado - True
print('i' in s1) # Resultado - False

# Reemplazo
print(s1.replace('o', 'a')) # Resultado - Hala

# División
print(s2.split('t')) # Resultado - ['Py', 'hon']

# Mayúsculas y minúsculas
print(s1.upper()) # Resultado - HOLA
print(s1.lower()) # Resultado - hola
print('Gabriel herling'.title()) # Resultado - Gabriel Herling
print('gabriel herling'.capitalize()) # Resultado - Gabriel herling

# Eliminación de espacios al principio y al final
print(' Gabriel Herling ') # Resultado - ' Gabriel Herling '
print(' Gabriel Herling '.strip()) # Resultado - 'Gabriel Herling'

# Busqueda al principio y al final
print(s1.startswith('Ho')) # Resultado - True
print(s2.startswith('Pyt')) # Resultado - True
print(s1.endswith('a')) # Resultado - True
print(s1.endswith('thon')) # Resultado - False

# Búsqueda de posición
print(s3.find('m')) # Resultado - 13
print(s3.lower().find('m')) # Resultado - 6

# Búsqueda de ocurrencias
print(s3.lower().count('m')) # Resultado - 2
print(s3.lower().count('x')) # Resultado - 0

# Formateo
print('Saludo: {}, Lenguaje: {}'.format(s1, s2)) # Resultado - Saludo: Hola, Lenguaje Python

# Transformación en lista de carácteres
print(list(s3)) # Resultado - ['B', 'r', 'a', 'i', 's', ' ', 'M', 'o', 'u', 'r', 'e', ' ', '@', 'm', 'o', 'u', 'r', 'e', 'd', 'e', 'v']

# Transformación de lista a cadena
print("".join(l1)) # Resultado - Hola, Python!
print("-".join(l1)) # Resultado - Hola-, -Python-!
print(" ".join(l1)) # Resultado - Hola ,  Python !

# Transformaciones numéricas
print(s4.isnumeric()) # Resultado - True
print(s1.isnumeric()) # Resultado - False
print(s4) # Resultado - 1234
# print(s4 + 5) # Resultado - Error
print(int(s4) + 5) # Resultado - 1239

# Comprobaciones varias
print(s1.isalnum()) # Resultado - True
print(s1.isalpha()) # Resultado - True
print(s4.isalpha()) # Resultado - False

print('------------------------------------------------------')

'''
DIFICULTAD EXTRA (opcional):
Crea un programa que analice dos palabras diferentes y realice comprobaciones para descubrir si son:
- Palíndromos
- Anagramas
- Isogramas
'''
p1 = input('Introduce una palabra: ').strip().lower()
p2 = input('Introduce otra palabra: ').strip().lower()
i1 = ''
i2 = ''

# Sólo toma la primera palabra de cada cadena en caso de que halla espacios
def eliminar_espacio(p):
    if ' ' in p:
        p = p[:p.find(' ')]
    
    return p

p1 = eliminar_espacio(p1)
p2 = eliminar_espacio(p2)

# Verifica si una palabra es palíndromo
def es_palindromo(p):
    i = p[::-1]
    
    if p == i:
        print(f'La palabra "{p}" es palíndromo')
    else:
        print(f'La palabra "{p}" no es palíndromo')
        
# Verifica si 2 palabras son anagramas
def son_anagramas(p1, p2):
    if sorted(p1) == sorted(p2):
        return 'Ambas palabras son anagramas'
    else:
        return 'Las palabras no son anagramas'

# Verifica si una palabra es isograma
def esisograma (p):
    l = list(p)
    cont = 0
    
    for i in range(len(l)):
        for j in range(len(l)):
            if i != j:
                if l[i] == l[j]:
                    cont =+ 1
    
    if cont == 0:
        return f'La palabra {p} es un isograma'
    else:
        return f'La palabra {p} no es un isograma'

# Palíndromos
es_palindromo(p1)
es_palindromo(p2)
    
print('------------------------------------------------------')

# Anagramas
print(son_anagramas(p1, p2))

print('------------------------------------------------------')

# Isogramas
print(esisograma(p1))
print(esisograma(p2))