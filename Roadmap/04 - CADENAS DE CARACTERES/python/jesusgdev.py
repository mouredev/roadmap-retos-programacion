"""
#04
CADENAS DE CARACTERES
/*
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
 */
"""

'''
Operaciones con Strings
'''

message = "Esto es una cadena de texto"
name = "Jesus"
age = 30

# 1. Acceso a una ubicacion o indice especifico dentro de una cadena de texto (indices)
# Devuelve el caracter indicado dentro de una cadena de texto especifica.

print(message[0])   # E (Primer caracter ubicado en el indice 0)
print(message[8])   # u (Octavo caracter unbicado en el indice 8)
print(message[-1])  # o (Ultimo caracter de la cadena ya que el los indices negativos reccoren la cadena a la inversa)


# 2 Subcadenas (slicing)
# Extrae una parte de una cadena usando rangos.

print(message[0:7])    # Esto es (desde el indice 0 hasta el indice 7, sin incluir el 7)
print(message[8:])    # una cadena de texto (desde el indice 8 hasta el final)
print(message[:11])    # Esto es una (desde el inicio hasta el indice 11, sin incluir el indice 11)

# 3. Longitud de cadena (len)
# Devuelve el tamaño o numero de caracteres de la cadena.

print(len(message))    # 27

# 4. Concatenacion de cadenas (+)
# Une dos cadenas de texto

greet = "Hello" + name
print(greet)    # Hello Jesus

# 5. Repeticion de cadenas
# Devuelve la cadena varias veces

print("Hello " * 4)    # Hello Hello Hello Hello

# 6. Recorrido de una cadena (con bucles)
# Recorre cada caracter de la cadena de texto con un ciclo for y lo imprime

for char in name:
    print(char)

# 7. Mayusculas y minusculas
# Cambia el formato del texto

print(name.upper())    # JESUS (todo en mayusculas)
print(name.lower())    # jesus (todo en minusculas)
print(name.capitalize())    # Jesus (primera en mayusculas)

# 8. Reemplazo de texto
# Cambia una parte del texto por otra

print(greet.replace("Jesus", "Python"))    # Hola Python

# 9. Division (split)
# Dividir un texto por palabras o separadores.
# Ideal para convertir textos en listas.

print(message.split(" "))    # ['Esto', 'es', 'una', 'cadena', 'de', 'texto']

# 10. Transformacion en lista de caracteres
# Separa cada caracter dentro de la cadena y los devuelve en una lista
print(list(name))    # ['J', 'e', 's', 'u', 's']

# 11. Union (join)
# Unir elementos de una lista en una sola cadena.

List = ['Esta', 'es', 'una', 'lista']
print(" ".join(List))    # Esta es una lista

# 12. Interpolacion (Insercion de variables de texto)
# Dos formas modernas de insertar variables en cadenas:

# a. Usando f-strings:
print(f"Me llamo {name} y tengo {age} años")    # Me llamo Jesus y tengo 30 años

# b. Usando format():
print("Me llamo {} y tengo {} años".format(name, age))    # Me llamo Jesus y tengo 30 años

# 13. Verificacion o busqueda

# a. Devuelve True si una cadena contiene una palabra especifica
print("cadena" in message)    # True

# b. Devuelve True si una cadena empieza con una palabra especifica
print(message.startswith("Esta"))    # True

# c. Devuelve True si una cadena termina con una palabra especifica
print(message.endswith("texto"))    # True

# d. Devuelve True si la cadena es alfanumerica 
print("Hi5".isalnum())    # True (Debe ser una cadena continua sin espacios)

# e. Devuelve True si contiene solo numeros
print("2025".isdigit())    # True (Debe ser una cadena continua sin espacios)

# f. Devuelve True si contiene solo letras
print("Texto".isalpha())    # True (Debe ser una cadena continua sin espacios)

# 14. Eliminar espacios
with_spaces = " Cadena con espacios "

# a. Elimina los espacios al principio y al final de la cadena
print(with_spaces.strip())    # "Cadena con espacios"

# b. Elimina los espacios al inicio
print(with_spaces.lstrip())    # "Cadena con espacios "

# c. Elimina los espacios al final
print(with_spaces.rstrip())    # " Cadena con espacios"

# 15. Contar apariciones
fruit = "banana"

print(fruit.count("a"))    # 3 (Devuelve la cantidad de apariciones de un caracter especifico dentro de una cadena de texto)

# 16. Encontrar posicion de algo
print("Python".find("h"))    # 3 (Devuelve el indice de la posicion del caracter indicado en la busqueda)
print("Python".find("r"))    # -1 (Devuelve -1 si no hay ninguna coincidencia)

# 17. Transformaciones o casting
print(type(age))    # <class 'int'>
age_str = str(age)
print(type(age_str))    # <class 'str'>

'''
Extra
'''

def word_comparator():

    while True:

        print("")
        print("COMPARADOR DE PALABRAS")
        print("1. Palindromo")
        print("2. Anagrama")
        print("3. Isograma")
        print("4. Salir")

        option = input("\nSelecciona una opcion: ")

        match option:
            case "1":
                word = input("Introduzca una palabra: ")

                if word == word[::-1]:
                    print(f"\nLa palabra {word} es un palindromo!")
                else:
                    print(f"\nLa palabra {word} no es un palindromo!")

                
            case "2":
                word1 = input("Introduzca la primera palabra: ")
                word2 = input("Introduzca la segunda palabra: ")
                word3 = word2

                for char in word1:
                    word3 = word3.replace(char, "")

                if len(word3) == 0:
                    print(f"\nLa palabra {word1} es un Anagrama de {word2}!")
                    
                else:
                    print(f"\nLa palabra {word1} no es un Anagrama de {word2}!")
                    
            
            case "3":
                word = input("Introduzca una palabra: ")
                char_count = []

                for char in word:
                    char_count.append(word.count(char))

                if len(set(char_count)) == 1:
                    print(f"\nLa palabra {word} es un Isograma!")
                    
                else:
                    print(f"\nLa palabra {word} no es un Isograma!")
            
            case "4":
                print("Gracias por usar el comparador de palabras!")
                break

            case _:
                print("\n Opcion invalida. Intenta de nuevo")

word_comparator()           