"""
* EJERCICIO:
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
"""
cadena = "Esto es una cadena de caracteres" # Asignación
cadena2 = " para hacer pruebas en Python"

print(cadena + cadena2) # Concatenación

print(cadena * 3) # Repetición

print(cadena[9]) # Acceso a caracteres específicos

print(len(cadena)) # Longitud de la cadena

# Porciones de cadena
print(cadena[2:6])
print(cadena[:6])
print(cadena[2:])

print('e' in cadena) # Búsqueda
print(cadena.startswith('H')) # Búsqueda al principio
print(cadena.endswith('H')) # Búsqueda al final
print(cadena.find('J')) # Búsqueda de posición

print(cadena.replace('e', 'j')) # Reemplazo

print(cadena.capitalize()) # Convertir la primera letre a mayúsculas

print(cadena.upper()) # Convertir a mayúsculas

print(cadena.lower()) # Convertir a minúsculas

print(cadena.title()) # Cada palabra con letra capital

print(cadena.split('t')) # Eliminar el carácter indicado

print(cadena.join('ta')) # Pone la t al comienzo de la cadena y la a como última letra

print(cadena2.strip()) # Quita espacios al principio y al final

print(cadena.count('e')) # Conteo de caracteres

# Formateo
print('cadena tiene {} y cadena2 tiene {}'.format(cadena, cadena2)) # Con format()
print(f'cadena tiene {cadena} y cadena2 tiene {cadena2}') # Con f-string

print(list(cadena)) # Transformación en una lista

# Casting de cadenas en números
num1 = "123456"
print(type(num1))
nu = int(num1) # A entero
print(type(nu))
num2 = "123456.75"
print(type(num2))
nu2 = float(num2) # A decimal
print(type(nu2))

print(cadena.isalpha()) # Comprobar si sólo tiene letras

print(cadena.isnumeric()) # Comprobar si es número

print(cadena.endswith('r')) # Finaliza con un carácter o un conjunto de caracteres

print(cadena.startswith('r')) # Comienza con un carácter o un conjunto de caracteres

print(cadena.isalnum())

# * DIFICULTAD EXTRA (opcional):
def palindromo(palabra1:str, palabra2:str):
    print(f'¿{palabra1} se lee igual?: {palabra1 == palabra1[::-1]}')# Se recorre la palabra de principio a fin, y con -1 desde atrás haca adelante
    print(f'¿{palabra2} se lee igual?: {palabra2 == palabra2[::-1]}')
        
palindromo('hola', 'radar')

def anagrama(palabra1:str, palabra2:str):
    print(f'¿{palabra1} es ANAGRAMA de {palabra2}?: {sorted(palabra1) == sorted(palabra2)}') # Si al ordenar alfabéticamente palabra1 y palabra2, son iguales, es que son ANAGRAMAS

anagrama('amor', 'roma')

def isograma(palabra1:str, palabra2:str):
    print(len(palabra1)) # Longitud de la palabra
    print(len(set(palabra1))) # Número de letras no repetidas en la palabra, ya que los sets no permiten repeticiones
    print(len(palabra2))
    print(len(set(palabra2)))
    print(f'¿{palabra1} es un isograma?: {len(palabra1) == len(set(palabra1))}')
    print(f'¿{palabra2} es un isograma?: {len(palabra2) == len(set(palabra2))}')
    
    # Comprobar que tipo de isograma es
    diccionario:dict = dict()
    
    for l in palabra1:
        diccionario[l] = diccionario.get(l,0) + 1 # En diccionario guardo l (letra), de existir ya en diccionario, le suma 1, en caso contrario, la da de alta y le asigna 0+1=1
    print(diccionario)
    
isograma('hola', 'radar')