"""
/*
 * EJERCICIO:
 * Muestra ejemplos de todas las operaciones que puedes realizar con cadenas de caracteres
 * en tu lenguaje. Algunas de esas operaciones podrían ser (busca todas las que puedas):
 * - Acceso a caracteres específicos, subcadenas, longitud, concatenación, repetición,
 *   recorrido, conversión a mayúsculas y minúsculas, reemplazo, división, unión,
 *   interpolación, verificación...
 */
"""

# Indices
texto = "Python"
print(texto[0])   # P
print(texto[3])   # h
print(texto[-1])  # n (último)

# Subcadenas (slicing)
texto = "Python"
print(texto[0:3])   # Pyt 
print(texto[2:])    # thon
print(texto[:4])    # Pyth
#* Regla -> inicio : fin (fin no incluido)

# Longitud
texto = "Python"
print(len(texto))  # 6

# Concatenación
nombre = "Lio"
lenguaje = "Python"

print(nombre + " aprende " + lenguaje)

# Repetición
print("🔥" * 3)
print("Hola " * 2)

# Recorrer un string
for letra in "Python":
    print(letra)

# Mayusculas y minusculas
texto = "PyThOn"

print(texto.upper())
print(texto.lower())
print(texto.capitalize())

# Reemplazo 
texto = "Hola mundo"
print(texto.replace("mundo", "Python"))

# División (split)
frase = "Python es brutal"
palabras = frase.split(" ")
print(palabras)

# Union (join)
palabras = ["Python", "es", "brutal"]
frase = " ".join(palabras)
print(frase)

# Interpolación (f strings)
nombre = "Lio"
edad = 26

print(f"{nombre} tiene {edad} años")

# Verificación
texto = "Python123"

print(texto.isalpha())   # False #* ¿Solo letras?
print(texto.isdigit())   # False #* ¿Solo números?
print(texto.isalnum())   # True #* ¿Letras y/o números?
print("Python" in texto) # True #* ¿Solo espacios?

# Busqueda
print("P" in texto)

# Mayusculas y minusculas
string = "Hola Python"
print(string.upper()) # Mayusculas
print(string.lower()) # Minusculas
print(string.title()) # Primer letra de cada palabra en Mayusculas


"""
* DIFICULTAD EXTRA (opcional):
* Crea un programa que analice dos palabras diferentes y realice comprobaciones
* para descubrir si son:
* - Palíndromos
* - Anagramas
* - Isogramas
"""

palabra1 = input("Ingresa una palabra: ").strip().lower()
palabra2 = input("Ingresa otra palabara: ").strip().lower()

# Función que verifica si una palabra es un palíndromo
# Un palíndromo se lee igual de izquierda a derecha y viceversa
def palindromo(palabra):
    # palabra[::-1] invierte el string
    return palabra == palabra[::-1]

# Función que verifica si dos palabras son anagramas
# Dos palabras son anagramas si contienen las mismas letras en distinto orden
def anagrama(p1, p2):
    # sorted() ordena las letras de cada palabra y devuelve una lista
    # Si ambas listas son iguales, las palabras son anagramas
    return sorted(p1) == sorted(p2)

# Función que verifica si una palabra es un isograma
# Un isograma no repite letras
def isograma(palabra):
    # set(palabra) elimina letras duplicadas
    # Si la longitud del set es igual a la del string original, significa que no había letras repetidas
    return len(palabra) == len(set(palabra))

print("\nRESULTADOS")

print(f"¿'{palabra1}' es palindromo?: {palindromo(palabra1)}")
print(f"¿'{palabra2}' es palindromo?: {palindromo(palabra2)}")

print(f"¿Son anagramas?: {anagrama(palabra1, palabra2)}")

print(f"¿'{palabra1}' es isograma?: {isograma(palabra1)}")
print(f"¿'{palabra2}' es isograma?: {isograma(palabra2)}")

