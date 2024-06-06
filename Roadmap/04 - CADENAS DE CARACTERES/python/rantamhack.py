

print("\n\n===============================OPERACIONES CON STRINGS===============================\n\n")

# Concatenacion
a = "Hello"
b = " World"
print(a + b)

# Multiplicar cadenas
a = "Hello World\n" * 3
print(a)

# Añadir texto al final de una cadena
a = "Hello World "
a += "Estamos aprendiendo python"
print(a)

# Acceso a caracteres especificos
a = "Hello World"
print(a[0])
print(a[7])

# Recorrido
a = "Hello World"
for character in a:
    print(character)
    
# Conversion a mayusculas y minusculas
a = "Hello World"
print(a.upper())
print(a.lower())
print(a.capitalize())

# Reemplazar
a = "Hello World"
print(a.replace("World", "Python" ))

# Buscar la longitud de la cadena
string = "¡Es cierto! Siempre he sido nervioso, muy nervioso, terriblemente nervioso."
print(len(string))

# Eliminar espacios en blanco
string = "¡Es cierto! Siempre he sido nervioso, muy nervioso, terriblemente nervioso."
print(string.replace(" ",""))

# Buscar
print(string.find("r"))

# Contar
print(f"El numero de r que hay  en la frase son: {string.count('r')}")

# Subcadenas
print(string[12:36] )

# Division 
print(string.split())
print(string.split(",", 1)) # El segundo parametro indica las veces que quieres dividir con el separador ","

# Interpolacion
string = "¡Es cierto! Siempre he sido nervioso, muy nervioso, terriblemente nervioso."
author = "Edgar Allan Poe"
print(f"El texto: {string} es el comienzo de una novela de {author}")

# verificacion
print(type(string))

print("\n\n===============================DIFICULTAD EXTRA===============================\n\n")

def palindromo(texto):
    if texto.lower().replace(" ","") == texto[::-1].lower().replace(" ",""):
        return True
    else:
        return False

print(palindromo("Luz azul"))


def anagrama(word1, word2):
    word1 = word1.lower()
    word2 = word2.lower()
    array1 = list(word1)
    array2 = list(word2)
    array1.sort()
    array2.sort()
    if array1 == array2:
        print(f"Las palabras {word1.capitalize()} y {word2.capitalize()} son un anagrama")
    else:
        print(f"Las palabras {word1} y {word2} no son un anagrama")
    
anagrama("Enfriamiento", "Refinamiento")
