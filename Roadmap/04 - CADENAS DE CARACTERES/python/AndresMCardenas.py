"""
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
"""

# Acceso a caracteres específicos
cadena = "Hola Mundo"
print(cadena[0]) # Imprime H ya que es el caracter de la cadena ubicado en la posicion 0

# Subcadenas
cadena = "Hola Mundo"
print(cadena[0:4]) # Imprime Hola ya que es la subcadena de la cadena ubicada en la posicion 0 a la 4

# Longitud
cadena = "Hola Mundo"
print(len(cadena)) # Imprime 10 ya que es la longitud de la cadena

# Concatenación 
cadena = "Hola"
cadena2 = " Mundo"
print(cadena + cadena2) # Imprime Hola Mundo ya que es la concatenacion de las dos cadenas

# Repetición
cadena = "Hola"
print(cadena * 3) # Imprime HolaHolaHola ya que es la cadena repetida 3 veces

# Recorrido
cadena = "Hola"
for i in cadena:
    print(i) # Imprime Hola ya que recorre la cadena y la imprime caracter por caracter

# Conversión a mayúsculas y minúsculas
cadena = "Hola Mundo"
print(cadena.upper()) # Imprime HOLA MUNDO ya que convierte la cadena a mayusculas
print(cadena.lower()) # Imprime hola mundo ya que convierte la cadena a minusculas 

# Reemplazo
cadena = "Hola Mundo"
print(cadena.replace("Hola", "Hello")) # Imprime Hello Mundo ya que reemplaza la palabra Hola por Hello

# División
cadena = "Hola Mundo"
print(cadena.split(" ")) # Imprime ['Hola', 'Mundo'] ya que divide la cadena en una lista de dos elementos

# Unión
cadena = "Hola Mundo"
print(" ".join(cadena)) # Imprime H o l a   M u n d o ya que une la cadena con un espacio entre cada caracter

# Interpolación
cadena = "Hola Mundo"
print(f"La cadena es: {cadena}") # Imprime La cadena es: Hola Mundo ya que interpola la cadena en el texto

# Verificación
cadena = "Hola Mundo"
print(cadena.isalpha()) # Imprime False ya que verifica si la cadena es alfanumerica

# Palíndromos
cadena = "ana"
if cadena == cadena[::-1]:
    print("Es palindromo") # Imprime Es palindromo ya que verifica si la cadena es palindromo

# Anagramas
cadena = "roma"
cadena2 = "amor"
if sorted(cadena) == sorted(cadena2):
    print("Es anagrama") # Imprime Es anagrama ya que verifica si la cadena es anagrama

# Isogramas
cadena = "murcielago"
if len(cadena) == len(set(cadena)):
    print("Es isograma") # Imprime Es isograma ya que verifica si la cadena es isograma

# DIFICULTAD EXTRA (opcional):
# Crea un programa que analice dos palabras diferentes y realice comprobaciones

cadena1 = input("Ingrese la primera palabra: ")
cadena2 = input("Ingrese la segunda palabra: ")

def palindromo(cadena1, cadena2):
  if cadena1 == cadena1[::-1] and cadena2 == cadena2[::-1]:
    print("Las dos palabras son palindromos") # Imprime Las dos palabras son palindromos ya que verifica si las dos cadenas son palindromos
  elif cadena1 == cadena1[::-1]:
    print("La primera palabra es palindromo")
  elif cadena2 == cadena2[::-1]:
    print("La segunda palabra es palindromo")
  else:
    print("Ninguna de las dos palabras es palindromo")  

def anagramas(cadena1, cadena2):
  if sorted(cadena1) == sorted(cadena2):
    print("Las dos palabras son anagramas") # Imprime Las dos palabras son anagramas ya que verifica si las dos cadenas son anagramas
  elif sorted(cadena1) == sorted(cadena2):
    print("La primera palabra es anagrama")
  elif sorted(cadena2) == sorted(cadena1):
    print("La segunda palabra es anagrama")
  else:
    print("Ninguna de las dos palabras es anagrama")

def isogramas(cadena1, cadena2):
  if len(cadena1) == len(set(cadena1)) and len(cadena2) == len(set(cadena2)):
    print("Las dos palabras son isogramas") # Imprime Las dos palabras son isogramas ya que verifica si las dos cadenas son isogramas
  elif len(cadena1) == len(set(cadena1)):
    print("La primera palabra es isograma")
  elif len(cadena2) == len(set(cadena2)):
    print("La segunda palabra es isograma")
  else:
    print("Ninguna de las dos palabras es isograma")


if (type(cadena1)) != str or (type(cadena2)) != str:
  print("No ingreso palabras o cadena de texto") # Imprime No son palabras ya que verifica si las cadenas son palabras 
else:
  palindromo(cadena1, cadena2)
  anagramas(cadena1, cadena2)
  isogramas(cadena1, cadena2)