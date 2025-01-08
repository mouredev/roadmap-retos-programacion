# EJERCICIO:
# Muestra ejemplos de todas las operaciones que puedes realizar con cadenas de caracteres
# en tu lenguaje. Algunas de esas operaciones podrían ser (busca todas las que puedas):
# - Acceso a caracteres específicos, subcadenas, longitud, concatenación, repetición, recorrido,
#   conversión a mayúsculas y minúsculas, reemplazo, división, unión, interpolación, verificación...

# Asignacion de una string a una variable
greeting = "Hello, World!"
print(greeting)

# Los Strings son Arrays
"""
Como muchos otros lenguajes de programación populares, las cadenas en Python son matrices de bytes que representan caracteres unicode.
Sin embargo, Python no tiene un tipo de datos carácter, un carácter es simplemente una cadena con una longitud de 1.
Se pueden utilizar corchetes para acceder a los elementos de la cadena.
"""
# Acceso a caracteres específicos
greeting = "Hello, World!"
print(greeting[1])

# Recorrer una cadena en Bucle
for c in "banana":
    print(c)

# Longitud de cadena
greeting = "Hello, World!"
print(len(greeting))

# Para comprobar si una frase o un caracter esta dentro de una cadena, utilizamos "in"
txt = "The best things in life are free!"
print("free" in txt)

# Tambien se puede utilizar en una condicional if:
txt = "The best things in life are free!"
if "free" in txt:
    print("Yes, 'free' is present.")

# Para comprobar si una frase o un caracter no esta dentro de una cadena, utilizamos "not in"
txt = "The best things in life are free!"
print("expensive" not in txt)

# Tambien se puede utilizar en una condicional if:
txt = "The best things in life are free!"
if "expensive" not in txt:
    print("No, 'expensive' is NOT present.")

# Slicing (rebanar)
# Consigue los caracteres de la posición 2 a la posición 5 (no incluidas):
b = "Hello, World!"
print(b[2:5])

# Rebanar desde el principio hasta la posicion 5(no incluida)
b = "Hello, World!"
print(b[:5])

# Rebanar hasta el final
# Obtener los caracteres desde la posicion 2 hasta el final
b = "Hello, World!"
print(b[2:])

# Indexación Negativa
# Se utilizan los indices negativos para empezar el corte desde el final de la cadena de texto:
# Obtener los caracteres:
# Desde: "o" en "World!" (posicion -5)
# hasta pero no incluido el caracter "d" en "World" (posicion -2)
b = "Hello, World!"
print(b[-5:-2])

# Python - string methods
# Mayusculas - upper()
a = "Hello, World!"
print(a.upper())

# Minusculas - lower()
a = "Hello, World!"
print(a.lower())

# Eliminar espacios en blanco que se encuentren al inicio o al final de la cadena de texto - strip()
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"

# Sustituir Cadena - replace()
a = "Hello, World!"
print(a.replace("H", "J"))

# Dividir Cadena - split()
# El método split() devuelve una lista en la que el texto entre el
# separador especificado se convierte en los elementos de la lista.
a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']

# Concatenacion de cadenas
a = "Hello"
b = "World"
c = a + b
print(c)

# Para agregar espacio entre ambas cadenas:
a = "Hello"
b = "World"
c = a + " " + b
print(c)

# Para concatenar una lista de strings con "join"
cadenas = ["Hola", "Jose Luis", ",", "¿cómo", "estás?"]
print(" ".join(cadenas))

# DIFICULTAD EXTRA (opcional):
# Crea un programa que analice dos palabras diferentes y realice comprobaciones
# para descubrir si son:
# - Palíndromos
# - Anagramas
# - Isogramas

def main():
    string_1 = input("Type the first word: ").lower().strip()
    string_2 = input("Type the second word: ").lower().strip()
    palindrome(string_1, string_2)
    anagram(string_1, string_2)
    isogram(string_1, string_2)

# Function Palindrome
def palindrome(word_1, word_2):
    words = [word_1, word_2]

    for word in words:
        list_1 = []
        list_2 = []
        for char in word:
            list_1.append(char)

        for char in reversed(list_1):
            list_2.append(char)

        if list_1 == list_2:
            print(f"The word {word} is a palindrome.")
        else:
            print(f"The word {word} isn't a palindrome.")

# Function anagram
def anagram(word_1, word_2):

    if sorted(word_1) == sorted(word_2):
        print(f"The words {word_1} and {word_2} are anagrams.")
    else:
        print(f"The words {word_1} and {word_2} aren't anagrams.")

# Function isogram
def isogram(word_1, word_2):
    words = [word_1, word_2]

    for word in words:
        my_dict = dict()
        for char in word:
            if char in my_dict:
                my_dict[char] += 1
            else:
                my_dict[char] = 1

        first_value = list(my_dict.values())[0]

        if all(value == first_value for value in my_dict.values()):
            print(f"The word {word} is an isogram.")
        else:
            print(f"The word {word} isn't an isogram.")

main()
