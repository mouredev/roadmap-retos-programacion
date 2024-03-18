# Acceso a caracteres especificos
# con indices
phrase = "esta es una cadena de caracteres"
# Acceso al primer caracter
print("Acceso al primer caracter")
print(phrase[0])

#con slices
# Acceso a los caracteres de las posiciones pares
print(f"Acceso a los caracteres de las posiciones pares de la frase {phrase}")
print(phrase[::2])

#Subcadenas
# Encontrar la posición de una subcadena en una cadena
print("Encontrar la posición de una subcadena en una cadena")
print(f"Encontrar la posición de la subcadena cadena en la phrase {phrase}" )
print(phrase.find("cadena"))

# Contar subcadenas
# Contar los espacios en blanco en la phrase
print(f"Contar los espacios en blanco en la phrase {phrase}")
print(phrase.count(" "))

# Longitud
print(f"La longitud de la cadena {phrase} es: {len(phrase)}")

# Concatenación
complement = "Mucho más grande"
print(f"Concatenar la frase {phrase} con {complement}")
print(phrase + " " + complement)

# Repetición
# Repetir el compplemento
print(f"Repetir el complemento {complement} 4 veces")
print(complement * 4)

# Recorrido
# Recorer cada letra de la frase
print(f"Recorer cada letra de la frase {phrase}")
for letter in phrase:
    print(letter)

# Conversión a mayusculas
print(f"Convertir a mayuculas la frase {phrase}")
print(phrase.upper())

# Conversión a minusculas
print(f"Convertir a minusculas la frase {phrase}")
print(phrase.lower())

# Convertir a mayuscula la primer letra de la frase
print(f"Convertir a mayuculas la primer letra de la frase {phrase}")
print(phrase.capitalize())

# Convertir a mayusculas la primer letra de cada palabra de la frase
print(f"Convertir a mayusculas la primer letra de cada palabra de la frase {phrase}")
print(phrase.title())

other = "Agustin Rojas Moreno"
# Intercambiar mayusculas y minusculas en la frase
print(f"Intercambiar mayusculas y minusculas en la frase {other}")
print(other.swapcase())

# Reemplazo
# Remplazar Rojas por Ramirez en la frase
print(f"Remplazar Rojas por Ramirez en la frase {other}")
print(other.replace("Rojas", "Ramirez"))

# Eliminar espacios en blanco a principio y al final
second_phrase = " " + phrase + " "
print(f"Eliminar espacios en blanco de la frase:{second_phrase}")
print(phrase.strip())

# División
# Dividir en subacadenas la frase
print(f"Dividir en subacadenas la frase {phrase}")
print(phrase.split())

# Unión
# Unir con  coma cada letra de la frase
print(",".join(phrase))

# Interpolación
# La interpolación es con f string
print(f"Esta es la interpolacion de la frase {phrase} con other {other}")

# Verificación
# Verificar si es alfanumerica
print(f"Verifica si es alfanumerica la frase {phrase}")
print(phrase.isalpha())

# Otrasverificaciones
print(f"Otras verificaciones para la frase {phrase}")
print(f"Es ascii?: {phrase.isascii()}")
print(f"Es decimal?: {phrase.isdecimal()}")
print(f"Es minusculas?: {phrase.islower()}")
print(f"Es digito?: {phrase.isdigit()}")

# Extra
def analysys_of_words(first_word, second_word):
    
    def is_isogram(word):
        for letter in word:
            if word.count(letter) > 1:
                return False
            
        return True


    print(f"Es palindromo {first_word}? {first_word == first_word[::-1]}")
    print(f"Es palindromo {second_word}? {second_word == second_word[::-1]}")
    
    print(f"Es anagrama {first_word}  de {second_word}? {sorted(first_word) == sorted(second_word)}")

    print(f"Es isograma {first_word}? {is_isogram(first_word)}")
    print(f"Es isograma {second_word}? {is_isogram(second_word)}")

if __name__ == "__main__":
    analysys_of_words("oro", "ana")
    analysys_of_words("cara", "arca")
    analysys_of_words("nido", "nodo")
    

    


