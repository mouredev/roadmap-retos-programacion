#operaciones con strings

string1 = "Hola mi nombre es,"
string2 = "Daniel"

concatenacion = string1+string2
print(concatenacion)

repeticion = string2*10
print(repeticion)

acceso_a_caracter = string1[0]
print(f"La primera letra de la palabra {string2} es: {acceso_a_caracter}")

acceso_a_palabra = string1[:4]
print(acceso_a_palabra)

longitud = len(string2)
print(f"La longitud de la cadena es: {longitud}")

for letra in string2:
    if letra in "aeiou":
        print(f"La letra {letra} es una vocal")
    else:
        print(f"La letra {letra} es una consonante")

conversion_a_mayuscula = string2.upper()
print(string2, conversion_a_mayuscula)

conversion_a_minuscula = conversion_a_mayuscula.lower()
print(conversion_a_minuscula)

print(string1)
reemplazo = string1.replace("Hola", "Buenos dias")
print(reemplazo)

division = string1.split(" ")
print(division)

# Unión (join)
palabras = ['Hola', 'cómo estás', 'amigo']
nueva_frase = " ".join(palabras)
print(nueva_frase)

interpolacion = f"{string1}, David"
print(interpolacion)

verificacion = string2.isalpha()
print(f"¿{string1} es alpha? {verificacion}")



#DIFICULTAD EXTRA

def is_palindrome(palabra):
    return palabra == palabra[::-1]

def anagrams(palabra1, palabra2):
    return sorted(palabra1) == sorted(palabra2)

def isograms(palabra):
    letras=list()
    verificacion = True
    for letra in palabra:
        if letra in letras:
            verificacion = False
            break
        else:
            letras.append(letra)
    return verificacion
 
def analizar_palabra(palabra, palabra2):
    if is_palindrome(palabra):
        print(f"La palabra {palabra}: es un palindromo")
    if isograms(palabra):
        print(f"La palabra {palabra} es un isograma")
        
    if is_palindrome(palabra2):
        print(f"La palabra {palabra2}: es un palindromo")
    if isograms(palabra2):
        print(f"La palabra {palabra2} es un isograma")
        
    if anagrams(palabra, palabra2):
        print("Las dos palabras son anagramas")

        
palabra1 = input("Escribe la primera palabra: ") 
palabra2 = input("Escribe la segunda palabra: ") 
analizar_palabra(palabra1, palabra2)         
