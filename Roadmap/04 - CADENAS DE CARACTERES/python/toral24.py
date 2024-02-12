'''
EJERCICIO:
Muestra ejemplos de todas las operaciones que puedes realizar con cadenas de caracteres en tu lenguaje. Algunas de esas operaciones podrían ser (busca todas las que puedas):
- Acceso a caracteres específicos, subcadenas, longitud, concatenación, repetición, recorrido, conversión a mayúsculas y minúsculas, reemplazo, división, unión, interpolación, verificación...
'''

cadena = 'Hola mundo'

print(len(cadena)) #Ver la longitud de una cadena

print(cadena[3]) # Ver una letra de la cadena

print(cadena[2:6]) # Ver una subcadena

print(cadena.upper()) # Convertir la cadena en mayusculas

print(cadena.lower()) # Convertir la cadena en minusculas

for i in cadena:
    print(i) # Recorrer una cadena

print('La frase más utilizada en la programación es: '+ cadena) # Concatenación

print(cadena*3) # Repetición de una cadena

print(cadena.replace('a','@')) # Reemplazo de letras

print(cadena[:4].isalpha()) # Verificar que se trata de una cadena (se ha puesto solo las 4 primeras letras porque al tener un espacio devolveria False)

cadena = cadena.split(' ') # Divide la cadena en una lista en función del parametro que se le pasa como separador

print(cadena) 

cadena = ' '.join(cadena) # Une una lista en una cadena (deshace la operación anterior)

print(cadena)

n = 22

print("%d esto es una cadena con interpolación %s" %(n,cadena)) # Interpolación, se utiliza % + n,d,f,x o o en función del tipo de dato

'''
DIFICULTAD EXTRA (opcional):
Crea un programa que analice dos palabras diferentes y realice comprobaciones para descubrir si son:
    - Palíndromos
    - Anagramas 
    - Isogramas
'''

palabra1 = input('Introduce la primera palabra')

palabra2 = input('Introduce la segunda palabra')

def ver_palindromo(a,b):
    cont1 = 0
    cont2 = len(a) -1
    while cont1 < cont2:
        if a[cont1] != b[cont2]:
            return False
        cont1 += 1
        cont2 -= 1
    return True

def ver_anagrama(a,b):
    return sorted(a)==sorted(b)

if ver_palindromo(palabra1,palabra2):
    print(f'la palabra {palabra1} es el palindromo de la {palabra2}')
else:
    print('las palabras introducidas no son palindromos')

if ver_anagrama(palabra1,palabra2):
    print(f'la palabra {palabra1} es anagrama de la {palabra2}')
else:
    print('las palabras introducidas no son palindromos')