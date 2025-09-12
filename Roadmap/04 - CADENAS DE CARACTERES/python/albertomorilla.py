# #04 CADENAS DE CARACTERES

"""
EJERCICIO:
 * Muestra ejemplos de todas las operaciones que puedes realizar con cadenas de caracteres
 en tu lenguaje. Algunas de esas operaciones podrían ser (busca todas las que puedas):
  - Acceso a caracteres específicos, subcadenas, longitud, concatenación, repetición, recorrido,
   conversión a mayúsculas y minúsculas, reemplazo, división, unión, interpolación, verificación...
"""
# Ejemplo de acceso a caracteres específicos
cadena = "I am Alberto"
print(cadena [4]) #Imprime A (INDEXACION)

indice = cadena.find("H") #Encuentra un caracter 
if indice != -1:
    print(f"La letra H se encuentra en la posición {indice}")
else:
    print("La letra H no se encuentra en la cadena")

# Subcadenas
print(cadena[0:4]) #Imprime I am (SLICING)

# Longitud
print(len(cadena)) #Imprime 9
print(cadena.count("a")) #Imprime 1

# Concatenación
cadena2 = "My city is Sevilla"
print(cadena + " " + cadena2) #Imprime I am Alberto My city is Sevilla

# Repeticion
print(cadena * 2) #Imprime I am AlbertoI am Alberto
print(cadena + cadena) #Imprime I am AlbertoI am Alberto

# Recorrido
for caracter in cadena:
    print(caracter) #Imprime cada caracter de la cadena

for i in range(len(cadena)):
    print(cadena[i]) #Imprime cada caracter de la cadena
    
# Conversion Mayúsculas y Minúsculas
print(cadena.upper()) #Imprime I AM ALBERTO
print(cadena.lower()) #Imprime i am alberto
print(cadena.capitalize()) #Imprime I am alberto
print(cadena.title()) #Imprime I Am Alberto
print(cadena.swapcase()) #Imprime i AM aLBERTO
print(cadena.casefold()) #Imprime i am alberto

# Reemplazo
print(cadena.replace("Alberto", "Juan")) #Imprime I am Juan

# División
print(cadena.split(" ")) #Imprime ['I', 'am', 'Alberto']

# Unión
cadena3 = ["Hello", "Alberto ", "Morilla"]
cadena_unida = " ".join(cadena3)
print(cadena_unida) #Imprime Hello Alberto Morilla

# Interpolación
name = "Alberto"
age = 36
cadena2_unida = "Hello, my name is {} and I am {} years old".format(name, age)
print(cadena2_unida) #Imprime Hello, my name is Alberto and I am 36 years old.

cadena3_unida = f"Hello, my name is {name} and I am {age} years old."
print(cadena3_unida) #Imprime Hello, my name is Alberto and I am 36 years old.

# Verificación
print(cadena.startswith("I")) #Imprime True
print(cadena.endswith("o")) #Imprime True
print(cadena.isdigit()) #Imprime False si no es int
print(cadena.isalpha()) #Imprime False si no es string
print(cadena.isalnum()) #Imprime False si no es string o int
print(cadena.islower()) #Imprime True si es todo minusculas
print(cadena.isupper()) #Imprime False si no es todo mayusculas


"""
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que analice dos palabras diferentes y realice comprobaciones
  para descubrir si son:
 * - Palíndromos
 * - Anagramas
 * - Isogramas
"""

def check(word1: str, word2: str):

    # Palíndromos
    print (f"¿{word1} es un palíndromo?: {word1 == word1[::-1]}")  
    print (f"¿{word2} es un palíndromo?: {word2 == word2[::-1]}")

    # Anagrama
    print(f"¿{word1} es anagrama de {word2}?: {sorted(word1) == sorted(word2)}")

    # Isograma
    print(f"¿{word1} es un isograma?: {len(word1) == len(set(word1))}")
    print(f"¿{word2} es un isograma?: {len(word2) == len(set(word2))}")

    def isogram(word: str) -> bool:
        word_dict = dict()
        for character in word:
            word_dict[character] = word_dict.get(character, 0) +1

        isogram = True
        values = list(word_dict.values())
        isogram_len = values[0]
        for word_count in word_dict:
            if len(word_count) != isogram_len:
                isogram = False
                break
            
        return isogram
    
    print(f"¿{word1} es un isograma?: {len(word1) == len(set(word1))}")
    print(f"¿{word2} es un isograma?: {len(word2) == len(set(word2))}")


check("radar", "pythonpythonpython")
#check("amor", "roma")