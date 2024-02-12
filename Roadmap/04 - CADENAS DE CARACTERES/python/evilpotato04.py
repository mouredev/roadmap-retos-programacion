
#/*
# * EJERCICIO:
# * Muestra ejemplos de todas las operaciones que puedes realizar con cadenas de caracteres
# * en tu lenguaje. Algunas de esas operaciones podrían ser (busca todas las que puedas):
# * - Acceso a caracteres específicos, subcadenas, longitud, concatenación, repetición, recorrido,
# *   conversión a mayúsculas y minúsculas, reemplazo, división, unión, interpolación, verificación...

citacion = "Hello"

citacion += " world!" # concatenación - manera 01
print(citacion)

nombre = input("Tu nombre: ")
citacion = "Tu nombre es {a}".format(a=nombre) # concatenación - manera 02
print(citacion)

edad = int(input("Tu edad: "))
citacion = "Tu tuenes %d años de edad" % (edad) # concatenación - manera 03 (solo numeros)
print(citacion)

pasatiempo = input("Tu pasatiempo: ")
citacion = f"Tu pasatiempo es {pasatiempo}" # concatenación - manera 04 (interpolación)
print(citacion)

# ------
citacion = "Beetlejuice! " # repetición
print(citacion*3)

print(len(citacion)) # longitud

print(citacion[4]) # accesando el caracter específico L en "Beetlejuice"

print(citacion[:6]) # subcadena "Beetle"
print(citacion[6:]) # subcadena "juice!"
print(citacion[4:8]) # subcadena "leju"

for x in citacion:
    print(x) # recorrido

print(citacion.upper()) # conversión a mayúsculas
print(citacion.lower()) # conversión a minúsculas

print("Beetle" in citacion)     # verificación (resulta en True)
print("juice" not in citacion)  # verificación (resulta en False)

citacion = " ".join(["My", "Instagram", "is", "@samy_witch"]) # unión
print(citacion)

citacion = "Feel free to add me" # división
print(citacion.split(" "))

# *
# * DIFICULTAD EXTRA (opcional):
# * Crea un programa que analice dos palabras diferentes y realice comprobaciones
# * para descubrir si son:
# * - Palíndromos
# * - Anagramas
# * - Isogramas
# */

def analisis_palindromo(palabra_1, palabra_2):
    letras_palabra_2 = []
    palabra_2_invertida = ""

    for letra in palabra_2:
        letras_palabra_2.append(letra)
    
    letras_palabra_2.reverse()

    for letra in letras_palabra_2:
        palabra_2_invertida += letra

    return True if palabra_1 == palabra_2_invertida else False

def analisis_anagrama(palabra_1, palabra_2):
    es_anagrama = True
    
    for letra in palabra_2:
        if letra not in palabra_1:
            es_anagrama = False
    
    if palabra_1 == palabra_2:
        es_anagrama = False
    
    return es_anagrama

def analisis_isograma(palabra):
    lista_de_letras = []

    for letra in palabra:
        if letra not in lista_de_letras:
            lista_de_letras.append(letra)

    return True if len(palabra) == len(lista_de_letras) else False

def analisis_de_palabras():
    palabra_1 = input("palabra 1: ")
    palabra_2 = input("palabra 2: ")
    es_palindromo = False
    es_anagrama = False
    es_isograma = False
    
    # * - Palíndromos
    es_palindromo = analisis_palindromo(palabra_1, palabra_2)
    print("Son Palíndromos") if es_palindromo == True else print("No son Palíndromos")
    
    # * - Anagramas
    es_anagrama = analisis_anagrama(palabra_1, palabra_2)
    print("Son Anagramas") if es_anagrama == True else print("No son Anagramas")
    
    # * - Isogramas
    es_isograma = analisis_isograma(palabra_1)
    print(f"{palabra_1} es Isograma") if es_isograma == True else print(f"{palabra_1} no es Isograma")

    es_isograma = analisis_isograma(palabra_2)
    print(f"{palabra_2} es Isograma") if es_isograma == True else print(f"{palabra_2} no es Isograma")

analisis_de_palabras()
