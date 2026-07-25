texto = "Ejercicio cadenas de caracteres"
print(texto)
print(texto * 3) #Repite 3 veces la cadena
caracteres = len(texto)
print(caracteres)
texto2 = "Curso Mouredev"
concatenar = texto + ", " + texto2
print(concatenar)
print(texto[1]) #segundo caracter
print(texto[0:4]) #primeros 3 caracteres
print(texto[-1]) #ultimo caracter
print(texto[::-1]) #invierte texto
print(texto[-3:]) #ultimos 3 caracteres
print(texto[0:caracteres:2]) #salto caracteres
print(concatenar.capitalize()) #primera mayuscula
print(concatenar.title()) #primeras letras en mayuscula de todas la palabras
print(concatenar.count("c")) #cuenta las letras c
print(concatenar.upper()) #Todo mayusculas
print(concatenar.lower()) #Todo minusculas
print(concatenar.find("c")) #posicion de la cadena del caracter buscado
print(concatenar.rfind("c")) #posicion desde el final de la cadena del caracter buscado
print(concatenar.index("cadenas")) #posicion de inicio de la cadena de la cadena buscada
print(concatenar.isnumeric()) #si todos los caracteres son numericos
print("!".join(concatenar)) #une los caracteres con el simbolo
print(concatenar.replace("cadenas", "CADENA")) #Reemplazar una cadena
print(concatenar.split()) #Divide una cadena


"""
 * DIFICULTAD EXTRA:
 * Crea un programa que analice dos palabras diferentes y realice comprobaciones
 * para descubrir si son:
 * - Palíndromos
 * - Anagramas
 * - Isogramas
"""

#polindromo = "Radar"
#anagrama = "Amor", "Roma"
#isogramas = "" #Un isograma es una palabra o frase en la que cada letra aparece el mismo número de veces
def isograma(word)-> bool:
    word_dict = dict()
    for contador in word:
        word_dict[contador] = word_dict.get(contador, 0) + 1
        isograma = True
        valores = list(word_dict.values())
        isograma_len = valores[0]
        for word_count in valores:
            if word_count != isograma_len:
                isograma = False
                break

        return isograma


def tipo_palabra (palabra1, palabra2):
    if palabra1.lower() == palabra1[::-1].lower() and palabra2.lower() == palabra2[::-1].lower():
        print(f"{palabra1} y {palabra2} son políndromos")
    elif sorted(palabra1.lower()) == sorted(palabra2.lower()):
        print(f"{palabra1} y {palabra2} son anagramas")
    elif isograma(palabra1) == True:
        print(f"{palabra1} es un isograma")
        
    return

tipo_palabra("Carlos", "Roma")
