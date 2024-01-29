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
# Declaracion cadena
my_string = "esto es una cadena"
my_string = 'esto es una cadena'

#Acceso a caracteres especificos
print(my_string[3])

#Subcadenas
print(my_string[12:])
print(my_string[:4])

#Longitud de una cadena
print(len(my_string))

#Concatenación
my_second_string = my_string + " y esto es otra cadena"
print(my_second_string)

#Repetición
print(my_second_string * 5)
#Recorrido
for letter in my_second_string:
    print(letter)
    
#Convertir a mayusculas
print(my_second_string.upper())

#Convertir primera letra en mayúscula
print(my_second_string.capitalize())


#Convertir primera letra de cada palabra en mayúscula
print(my_second_string.title())

#Convertir en minúsculas
my_second_string_upper = "ESTO ES OTRA CADENA MAS"
print(my_second_string_upper.lower())

#Dividir cadenas
my_third_string = "División de cadenas"

print(my_third_string.split(" "))

#Unión de cadenas
my_third_string = ['División', 'de', 'cadenas']

print(" ".join(my_third_string))

#Busqueda
my_string = "Hola, Python"
posicion = my_string.find("Python")
print(posicion)

#Reemplazo
my_string = "Hola, Java"
new_string = my_string.replace("Java", "Python")
print(new_string)

#Interpolación de cadenas
my_other_string = "muchas cadenas"
print(f"Aqui hay {my_other_string}")

#Verificación de cadenas
my_verify_string = "Esto es una cadena para verificar"

print(my_verify_string.isalnum()) #Devuelve True si la cadena es alfanumérica, de lo contrario False.
my_verify_string = "Esto"
print(my_verify_string.isalpha()) #Devuelve True si la cadena es alfabética, de lo contrario False.
my_verify_string = "777"
print(my_verify_string.isdigit()) #Devuelve True si la cadena es numérica, de lo contrario False.
my_verify_string = "Hola"
print(my_verify_string.islower()) #Devuelve True si la cadena contiene solamente minúsculas, de lo contrario False.
my_verify_string = "HOLA"
print(my_verify_string.isupper()) #Develve True si la cadena contiene solamente mayúsculas, de lo contrario False.
my_verify_string = " "
print(my_verify_string.isspace()) #Devuelve True si la cadena contiene solamente espacios en blanco, de lo contrario False.

#DIFICULTAD EXTRA

#PALINDROMO

def words(first_word, second_word):
    if (first_word == second_word[::-1]):
        print(f"{first_word} y {second_word}, son palíndromos")
    else:
        print(f"{first_word} y {second_word}, no son palíndromos")
        
        
words("hola","aloh")


#ANAGRAMA

def words(first_word, second_word):
    
    first_temp = first_word.lower()
    second_temp = second_word.lower()
    
    first_temp = list(first_temp)
    second_temp = list(second_temp)
    
    first_temp.sort()
    second_temp.sort()
    
    first_temp = "".join(first_temp)
    second_temp = "".join(second_temp)

    if(first_temp == second_temp):
        print(f"{first_word} y {second_word} son anagramas")
    else:
        print(f"{first_word} y {second_word} no son anagramas")
    
words("monja","jamon")

#ISOGRAMA
def contar_letras(text):
    letras = dict()
    for letra in text:
        if letra in letras.keys():
            letras[letra] += 1
        else:
            letras[letra] = 1
    return letras
        
def isograma(text):
    counter = 0
    for repeat in contar_letras(text).values():
        if counter == 0:
            counter = repeat
        if counter != repeat:
            return False
    return True

print(isograma("pepe"))
            
        