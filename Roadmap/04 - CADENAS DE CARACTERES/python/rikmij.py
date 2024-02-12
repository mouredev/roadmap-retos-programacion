string_ejemplo = "Esta es la cadena de caracteres de ejemplo"
print(string_ejemplo)

print("\n\t-> Acceso a caracteres específicos:")
print(f"-> En la posición {string_ejemplo.index('a')} se encuentra la letra {string_ejemplo[3]}")

print("\n\t-> Subcadenas")
print("~ Acceso a una subcadena:")
print(string_ejemplo[3:13])
print("~ Está 'X' subcadena e una cadena:")
print("cadena" in string_ejemplo)
print("mondongo" in string_ejemplo)

print("\n\t-> Longitud")
print(f"{len(string_ejemplo)} caracteres")

print("\n\t-> Concatenación")
string2 = "y me uno a la cadena 1"
print(string_ejemplo + ' ' + string2)
print(string_ejemplo + " soy un añadido")

print("\n\t-> Repetición")
print("~ Repetimos una cadena:")
print((string_ejemplo + ' ')*2)

print("\n\t-> Recorrido")
for elem in string_ejemplo:
    print(elem) #imprime cada letra

for elem in string_ejemplo.split():
    print(elem) #imprime cada palabra

print("\n\t-> Conversión a mayúsculas y minúsculas")
print("~ A mayúsculas")
print(string_ejemplo.upper())
print("~ La primera en mayúsculas")
print(string_ejemplo.capitalize())
print("~ A minúsculas")
print(string_ejemplo.lower())

print("\n\t-> Reemplazo")
word = string_ejemplo.split()
word[1] = "no es"
print(" ".join(word))

print("\n\t-> División")
print(string_ejemplo.split())

print("\n\t-> Interpolación")
print(f"La cadena principal era: \"{string_ejemplo}\", como recuerdo")

print("\n\t-> Verificación")
if type(string_ejemplo) == str:
    print("Es un string")
else:
    print("Pues no es un string")

print("\n\t-> Pertenencia")
print("ejemplo" in string_ejemplo)
print("mondongo" in string_ejemplo)


print('\n','~'*5, ' EJERCICIO EXTRA ', '~'*5)
# palíndromo = se lee igual al derecho que al revés
# anagrama = cambian de orden las letras para formar otra
# isograma = palabra o frase que cada letra aparece el mismo número de veces

def palindrome(word):
    if word == word[::-1]:
        return "Es un palíndromo"
    else:
        return "No es un palíndromo"


def anagrama(word1, word2):
    letters1 = []
    letters2 = []

    for l in word1.lower():
        letters1.append(l)
    
    for l2 in word2.lower():
        letters2.append(l2)
    
    letters1.sort()
    letters2.sort()

    if letters1 == letters2:
        return "Son anagramas"
    else:
        return "No son anagramas"


def isograma(word):
    count_letters = {}

    for letter in word:
        if letter in count_letters:
            count_letters[letter] += 1
        else:
            count_letters[letter] = 1

    set_compr = set(count_letters.values())

    if len(set_compr) == 1:
        return "Es un isograma"
    else:
        reps = []
        for key, value in count_letters.items():
            if value >= 2:
                reps.append(key)
        return f"No es un isograma, se repiten: {reps}"


def verification_words():
    w1 = input("Palabra 1 que quieres comprobar: ")
    w2 = input("Palabra 2 que quieres comprobar: ")

    print("Palabra 1: ", palindrome(w1))
    print("Palabra 2: ", palindrome(w2))
    print("Estas 2 palabras: ", anagrama(w1, w2))
    print("Palabra 1: ", isograma(w1))
    print("Palabra 2: ", isograma(w2))

verification_words()
