"""
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
 """
my_string = "esto es un string"
print(len(my_string)) #retorna el numero de caracteres
print(my_string[5]) #retorna el caracter en la posicion 5
print(my_string[2:9]) #retorna una subcadena
print(my_string * 3) #repite la cadena 3 veces
print("e" in my_string) #busca el caracter en el string
for element in my_string: #recorre una cadena
    print(element)
my_other_string = " esto es otro string"
print(my_string + " "+ my_other_string) #concatena dos cadenas
print(my_string.upper()) #retorna el string en mayusculas
print(my_string.lower()) #retorna el string en minuscula
print(my_string.title()) #devuelve una copia usando el titulo como referencia
print(my_string.replace("o","O")) # reemplaza la primera ocurrencia indicada
print(my_other_string.lstrip()) #elimina espacios en blanco al principio
print(my_other_string.rstrip()) #elimina espacios en blanco al final
print(my_other_string.split("o")) # devuelve una lsita separada por el parametro indicado
print(my_string.startswith("es")) #busca al principio la primera ocurrencia
print(my_string.endswith("es")) #busca al final la primera ocurrencia
print("Cadena1:  {}, cadena2: {}".format(my_string,my_other_string) )

#DIFICULTAD EXTRA
def comprobar(word1, word2):
    #palindromo
    reverse_word1= word1[::-1]
    reverse_word2= word2[::-1]
    print(f"la palabra {word1} es palindromo?: {word1==reverse_word1}")
    print(f"la palabra {word2} es palindromo?: {word2==reverse_word2}")

    #anagrama
    print(f"las palabras {word1} y {word2} son anagrama?: {sorted(word1)==sorted(word2)}")

    #isograma
    print(f"{word1} es isograma?: {len(word1) == len(set(word1))}") #funciona si el string no se repite
    print(f"{word2} es isograma?: {len(word2) == len(set(word2))}")

    def is_isogram(word):
        word_dict = dict()
        for element in word:
            word_dict[element] = word_dict.get(element, 0) + 1
        isogram = True
        values = list(word_dict.values())
        len_isogram = values[0]
        for word_count in values:
            if word_count != len_isogram:
                isogram = False
                break
        return isogram
    print(f"{word1} es isograma?: {is_isogram(word1)}")
    print(f"{word2} es isograma?: {is_isogram(word2)}")

comprobar("retos", "programacion")
