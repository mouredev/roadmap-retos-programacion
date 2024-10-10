""" Cadenas de carácteres """
# Las cadenas de caracteres conocidas como strings, son inmutables

# Operaciones

text = "Duban"
print(text[0]) # Accediendo al primer valor
print(text[-1]) # Accediendo al último valor

#Definiendo mas textos de varias formas
text = 'Hola, mi nombre es "Duban"'
print(text)
text = "Hola, mi nombre es 'Duban'"
print(text)
text = "Hola, mi nombre es \"Duban\"" # Utilizando formateo de carácteres
print(text)
large_text = """Esta es un texto de varias líneas. 
Primero se declara la variable, luego se utilizan las
'triple comillas dobles'"""
print(large_text)
large_text = ("Este es otro ejemplo de un texto de varias líneas,"
"para ello se utiliza separando las comillas por medio de la coma (,)") # Texto unido por literales de cadena
print(large_text)

#Subcadenas o indices(slices), cortes o rebanadas

text = "Duban Quiroga"
# Los slices mantienen la siguiente estructura
print(text[:5] + text[5:])
first_name = text[0:5]
lastname = text[6:]
print(first_name, lastname)
#Saltos de carácteres
hello = "Hello World"
print(hello[::2]) # HloWrd
#Invertir una cadena
print(hello[::-1]) # dlroW olleH

# Longitud de una cadena

print(len(text)) # 13 😏 Tu número fav

# Concatenación de cadenas
first_name = "Duban"
lastname = "Quiroga"

complete_name = first_name + " " + lastname
print(complete_name) # Duban Quiroga
print(complete_name * 3) # Podemos multiplicar las cadenas, a esto se le llama Repetición

# Recorrido de una cadena

for letter in complete_name:
    print(letter) # Imprime cada letra de la cadena

for letter in complete_name:
    print(letter, end="")
print()

# Conversión a mayus y minus

print(complete_name.upper())
print(complete_name.lower())

#Reemplazo
print(complete_name.replace(complete_name, "Brais Moure"))

# División

first_name, lastname = complete_name.split(" ") # Separa cuando encuentra el espacio
print(first_name)
print(lastname)

# Unión
# Siguiendo la siguiente lógica de concatenación de listas
name = ["Duban"]
l_name = ["Quiroga"]
full_name = name + l_name
print(full_name)
print(", ".join([first_name] + [lastname])) # Duban, Quiroga

# Formateo de cadenas

print(f"{first_name} {lastname}") # Utilizando f-String
print("%s %s"%(first_name, lastname))

# Verificación

does_d_in_duban = "D" in first_name
print(does_d_in_duban) # True


""" Dificultad Extra """

"""
Crea un programa que analice dos palabras diferentes y realice comprobaciones
 * para descubrir si son:
 * - Palíndromos
 * - Anagramas
 * - Isogramas
"""
def main(word1, word2):

    def is_palindrome(word1, word2):
        word2 = word2[::-1]
        return word1 == word2 # Retorna True o False

    def is_anagrama(word1:str, word2:str) -> bool:
        word1 = sorted(word1.replace(" ", "").lower())
        word2 = sorted(word2.replace(" ", "").lower())
        return word1 == word2


    def is_isograma(word:str):
        word = word.lower().replace(" ", "")

        return len(word) == len(set(word))
        
    
    if is_palindrome(word1, word2):
        print(f"{word1} y {word2} Son palindromos")
    else:
        print(f"{word1}, {word2} No son palindromos")
    

    if is_anagrama(word1, word2):
        print(f"{word1}, {word2} Son anagramas")
    else:
        print(f"{word1}, {word2} No son anagramas")
    

    if is_isograma(word1):
        print(f"La palabra: {word1} es Isograma")
    else:
        print(f"La palabra: {word1} no es isograma")

    if is_isograma(word2):
        print(f"La palabra: {word2} es Isograma")
    else:
        print(f"La palabra: {word2} no es Isograma")

    return f"{is_palindrome(word1, word2)}, {is_anagrama(word1, word2)}, {is_isograma(word1)}, {is_isograma(word2)}" 


print(main("Toledo", "el todo"))

