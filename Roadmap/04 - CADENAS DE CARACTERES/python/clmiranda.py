# CADENAS DE CARACTERES

# Acceso a caracteres específicos
cadena = "Hola Mundo"
print(cadena[0], cadena[5], cadena[-1])

# Subcadenas
print(cadena[:10])
print(cadena[::2])

# Verificación
subcadena = "Mundo"
print(subcadena in cadena)
print("valor" in cadena)


# Longitud
print(f"La cantidad de caracteres de la cadena es: {len(cadena)}")

# Concatenación
concatenar = " y mas!"
print(cadena + concatenar)

# Interpolación #1
nombre = "Cliver"
print(f"{cadena}, mi nombre es {nombre}")

# Interpolación #2
lenguaje, experiencia = "Python", 2
print("Soy desarrollador {lng} con {exp} años de experiencia".format(lng=lenguaje, exp=experiencia))

# Unión
caracter = "-"
print(caracter.join("cadena unida"))

# Repetición
print("bugs " * 3)

# Recorrido
print([i for i in cadena])

# Conversión a Mayúsculas
print(cadena.upper())

# Conversión a Minúsculas
print(cadena.lower())

# Conversión a Capitalizada
capitalizada = "lunes en la mañana"
print(capitalizada.capitalize())

# Reemplazo
print(cadena.replace("Hola", "Adios"))

# División
cad2 = "cadena separada por espacios"
print(cad2.split(" "))



# EJERCICIO - DIFICULTAD EXTRA

def palindrome(word) -> bool:
    return True if word[::-1] == word else False

def anagram(word1, word2) -> bool:
    counter, aux_word = 0, word2
    for i in word1:
        if i in word2:
            counter += 1
            word2.replace(i, "")
    return True if counter == len(aux_word) else False

def isogram(word) -> bool:
    return True if len(word) == len(set(word)) else False


print(f"'reconocer' es palíndromo: {palindrome("reconocer")}")
print(f"'materialismo' y 'memorialista' son anagramas: {anagram("materialismo", "memorialista")}")
print(f"'centrifugado' es isograma: {isogram("centrifugado")}")
