"""
CADENAS DE CARACTERES

 * Muestra ejemplos de todas las operaciones que puedes realizar con cadenas de caracteres
 * en tu lenguaje. Algunas de esas operaciones podrían ser (busca todas las que puedas):
 * - Acceso a caracteres específicos, subcadenas, longitud, concatenación, repetición,
 *   recorrido, conversión a mayúsculas y minúsculas, reemplazo, división, unión,
 *   interpolación, verificación...
"""

my_string = "Mi nombre es Alex"
# Acceso a caracteres específicos
print("Acceso a caracteres específicos")
print(f"Podemos acceder a caracteres específicos por medio del índice del string, por ejemplo, en \"{my_string}\", para acceder al caracter en la posición 4 my_string[4] --> {my_string[4]}")
print(f"O en la posición 7 my_string[7] --> {my_string[7]}")
print(f"O desde el final contando con que el último caracter tendría el índice -1 y hacia el primer caracter sería incremental, por ejemplo my_string[-12]: {my_string[-12]}")
# Longitud
print("\n")
print("Longitud")
print(f"Podemos obtener la longitud con len(my_string): {len(my_string)}")
# Subcadenas
print("\n")
print("Subcadenas")
print(f"Podemos crear subcadenas especificando dos índices, uno inicial y otro final, por ejemplo my_string[3:12]: {my_string[3:12]}")
print(f"Solo el índice inicial y nos mostrará desde ese índice hasta el final, my_string[5:]: {my_string[5:]}")
print(f"O únicamente el índice del final que nos mostrará desde el inicio hasta ese caracter, my_string[:9]: {my_string[:9]}")
print(f"O subcadenas con índices negativos, my_string[:-3]: {my_string[:-3]}, o my_string[-11:-5]: {my_string[-11:-5]} o my_string[-14:]: {my_string[-14:]}")
# Cadenas y Subcadenas inversas
print("\n")
print("Cadenas y Subcadenas inversas")
print(f"También podemos crear cadenas invertidas con my_string[::-1]: {my_string[::-1]}, que devolvería la cadena inversa completa")
print(f"o si usamos un índice -2 por ejemplo my_string[::-2], nos de vuelve la cadena inversa menos los caractéres en los múltiplos de 2: {my_string[::-2]}")
# Mayúsuclas y minúsculas
print("\n")
print("Mayúsuclas y minúsculas")
print(f"podemos pasar a mayúsuclas todo con upper(): {my_string.upper()}")
print(f"O a minúsuclas con lower():{my_string.lower()}")
print(f"O también poner las primeras letras de cada palabra en mayúsculas con title(): {my_string.title()}")
print(f"O con capitalize(), solo la primera palabra con mayúscula: {my_string.capitalize()}")
# Repetición
print("\n")
print("Repetición")
print(f"Podemos contar las ocurrencias de una serie de caractéres dentro de la cadena con count, por ejemplo my_string.count(\"e\"): La letra \"e\" aparece {my_string.count("e")} veces")
# Recorrido
print("\n")
print("Recorrido")
print("Podemos recorrer el string con un bucle del tipo \"for char in my_string:\" e ir imrimiendo cada caracter")
for char in my_string:
    print(char)

print("\n")
print("O usando un índice + un rango del tipo \"for index in range(0,len(my_string))\". También podría hacerse con un While")
for index in range(0,len(my_string)):
    print(my_string[index])
#Reemplazo
print("\n")
print("Reemplazo")
print(f"También podemos reemplazar un caracter o una subcadena con replace() {my_string.replace("e","a")}")
# División
print("\n")
print("División")
print(f"Podemos crear una lista a partir de split(), dándole como argumento lo que \"separará\" cada elemento de esa lista: {my_string.split(" ")}")
# Concatenación
print("\n")
print("Concatenación")
print(f"Lo más sencillo para unir o concatenar dos strings es con el operador \"+\": {my_string + " y me gusta Python"}")
print(f"Aunque también se pueden usar \"*\" para repetir un texto y que quede concatenado: {"Hola "* 5}")
# Búsqueda
print("\n")
print("Búsqueda")
print(f"podemos utilizar find() para obtener el índice de la primera ocurrencia de un caracter o una subcadena: {my_string.find("Alex")}")
print(f"Obtendremos el mismo resultado con index(): {my_string.index("Alex")}, aunque funciona es un método que se usa en listas")
# Formatos
print("\n")
print("Formatos")
print(f"Podemos aplicar un formato al texto, tipo tabulación con métodos como center(): {my_string.center(55,"*")}")
#Verificación inicio/fin
print("\n")
print("Verificación inicio/fin")
print(f"Se puede comprobar si una cadena comienza por un caracter o subcadena con startswith(): {my_string.startswith("Mi")}")
print(f"O si finaliza con otro: {my_string.endswith("Alex")}")
#Verificación
print("\n")
print("Verificación")
print(f"Podemos comprobar si una cadena solo contiene números con isnumeric(): {"1234".isnumeric()} o con isdigit(): {"1234".isnumeric()}")
print(f"Si es alfanumérica con isalnum(): {"AlexS117".isalnum()}")
print(f"Si contiene solo caracteres del alfabeto con isalpha(): {"Alejandro".isalpha()}")
print(f"Si todas las letras son minúsculas con islower(): {"hola que tal".islower()}, o mayúsculas con isupper(): {"HOLA QUE TAL".isupper()}")

print("\n")
"""
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que analice dos palabras diferentes y realice comprobaciones
 * para descubrir si son:
 * - Palíndromos
 * - Anagramas
 * - Isogramas
"""
def normalize_string(one_text):
    special_chars={
            "á":"a",
            "é":"e",
            "í":"i",
            "ó":"o",
            "ú":"u",
            "ü":"u"
    }
    one_text = one_text.lower()
    for key in special_chars:
        one_text = one_text.replace(key,special_chars[key])
    return one_text

def is_palindrome (string_one, string_two):
    if len(string_one) != len(string_two):
        return False
    else:
        string_one = normalize_string(string_one)
        string_two = normalize_string(string_two)
        inverted_string = string_one[::-1]
        for index in range (0,len(string_two)):
            if string_two[index] != inverted_string[index]:
                return False    
        return True

def is_anagram(string_one,string_two):
    if len(string_one) != len(string_two):
        return False
    else:
        string_one = normalize_string(string_one)
        string_two = normalize_string(string_two)
        set_string_one = set()
        for char in string_one:
            set_string_one.add(char)
        for char in string_two:
            if char not in set_string_one:
                return False
        return True
    
def is_isogram(string_one,string_two):
    new_string = string_one + string_two
    string_one = normalize_string(string_one)
    string_two = normalize_string(string_two)
    limit = new_string.count(new_string[0])
    for char in new_string:
        if new_string.count(char)!= limit:
            return False
        
    return True

    
print(is_palindrome("AniMaL","lÁMina"))

print(is_anagram("Frase","freSA"))

print(is_isogram("aaabbb","cccddd"))
