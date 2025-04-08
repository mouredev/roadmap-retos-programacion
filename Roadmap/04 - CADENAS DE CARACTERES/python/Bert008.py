'''
/*
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
 */
'''

cadena1 = "hola"
cadena2 = "mundo"

# longitud de las cadenas
print(len(cadena1)) # 4
print(len(cadena2)) # 5

# acceso a caracteres especificos
print(cadena1[3:]) # a
print(cadena2[0:1]) # m
cadena_nueva = cadena1 + " " + cadena2
cadena_con_o = [x for x in cadena_nueva.split() if "o" in x]
print(cadena_con_o)
cadena_con_o = [x for x in cadena_nueva.split() if "la" in x]
print(cadena_con_o)

# subcadenas
cadena = "Hola mundo, hola Python."
subcadena = cadena[:10]
print(subcadena)
subcadena = cadena[11: ]
print(subcadena)
print(subcadena.strip())
cadena1, cadena2 = cadena.split(",")
print("Cadena 1 = ",cadena1)
print("Cadena 2 = ",cadena2.strip())

# concatenacion
cadena1 = "Hola"
cadena2 = "mundo"
cadena3 = "python"
cadena4 = cadena1 + " " + cadena2
cadena5 = cadena1 + " " + cadena3
print(cadena4)
print(cadena5)

# repeticion
print(cadena1 * 3)
print("*" * 3)

# recorrido
for i in cadena1:
    print(i, end = " ")
print(" ")

# conversion de mayusculas y minusculas
print(cadena1.upper())
print(cadena1.lower())
print(cadena1.capitalize())
print(cadena.title())

# remplazo
print(cadena.replace("Python", "amigo"))

# division
division = cadena.split(" ")
print(division)

# union
print(", ".join(cadena1))

# interpolacion
print(f"{cadena1} a todos y {cadena1} al {cadena2}")

# Verificacion
print(cadena1 in cadena) # Hola en Hola mundo, hola python.
print(cadena2 in cadena) # mundo en Hola mundo, hola python.
print("abc1234".isalnum())
print("HOLA".isupper())
print(" ".isspace())
print("abc".isalpha())
print("123".isdigit())

# Extra

def palindromos(word1, word2):
    # palindromos
    word1 = word1.lower()
    word2 = word2.lower()
    palindromo1 = word1 == word1[::-1]
    palindromo2 = word2 == word2[::-1]
    
    
    if palindromo1 and palindromo2:
        print("Ambos son palindromos")
    elif palindromo1 == True and palindromo1 == False:
        print("palabra 2 es un palindromo")
    elif palindromo1 == True and palindromo2 == False:
        print("palabra 1 es palindromo")
    
def anagramaIsagrama(word1, word2):
    word1 = word1.lower()
    word2 = word2.lower()
    if word1 == word2[::-1]:
        print("Palabra 2 es un anagrama de 1")
    elif word2 == word1[::-1]:
        print("Palabra 1 es un anagrama de 2")
    else:
        print("Ambas palabras son isogramas")

while True:
    print("Para salir escriba salir en ambas entradas")
    word1 = input("Palabra 1: ")
    word2 = input("Palabra 2: ")

    if word1 == word1[::-1] or word2 == word2[::-1]:
        palindromos(word1, word2)
    elif word1 == "salir" and word2 == "salir":
        break
    else:
        anagramaIsagrama(word1, word2)

