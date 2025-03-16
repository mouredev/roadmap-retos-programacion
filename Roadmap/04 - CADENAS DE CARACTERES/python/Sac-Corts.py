s1 = "Hola"
s2 = "Python"

# Concatenación
print(s1 + ", " + s2 + "!")

# Repetición
print(s1 * 3)

# Indexación
print(s1[0] + s1[1] + s1[2] + s1[3])

# Longitud
print(len(s2))

# Slicing (porción)
print(s2[2:6])
print(s2[2:])
print(s2[0:2])
print(s2[:2])

# Busqueda
print("a" in s1)
print("i" in s1)

# Reemplazo
print(s1.replace("o", "a"))

# División
print(s2.split("t"))

# Mayúsculas, minúsculas y letras en mayúsculas
print(s1.upper())
print(s1.lower())
print("brais moure".title())
print("brais moure".capitalize())

# Eliminación de espacios al principio y al final
print(" brais moure ".strip())

# Búsqueda al principio y al final
print(s1.startswith("Ho"))
print(s1.startswith("Py"))
print(s1.endswith("la"))
print(s1.endswith("thon"))

s3 = "Brais Moure @mouredev"

# Búsqueda de posición
print(s3.find("moure"))
print(s3.find("Moure"))
print(s3.find("M"))
print(s3.lower().find("m"))

# Búsqueda de ocurrencias
print(s3.lower().count("m"))

# Formateo
print("Saludo: {}, lenguje: {}!".format(s1, s2))

# Interpolación
print(f"Saludo: {s1}, lenguje: {s2}!")

# Tranformación en lista de caracteres
print(list(s3))

# Transformación de lista en cadena
l1 = [s1, ", ", s2, "!"]
print("".join(l1))

# Transformaciones numéricas
s4 = "123456"
s4 = int(s4)
print(s4)

s5 = "123456.123"
s5 = float(s5)
print(s5)

# Comprobaciones varias
s4 = "123456"
print(s1.isalnum())
print(s1.isalpha())
print(s4.isalpha())
print(s4.isnumeric())

"""
  DIFICULTAD EXTRA
"""

# Un palíndromo es una palabra que se lee igual hacia adelante y hacia atrás.
# Un anagrama es una palabra formada reordenando las letras de otra palabra, utilizando todas las letras originales exactamente una vez.
# Un isograma es una palabra en la que ninguna letra se repite.

# Entradas
def solicitar_cadena_1():
    while True:
        cadena = input("Por favor, ingresa la primera palabra: ")
        # Verifica que la cadena solo contenga caracteres alfabéticos
        if cadena.isalpha():
            # Convierte la cadena en minúsculas
            cadena_minusculas = cadena.lower()
            return cadena_minusculas
        else:
            print("Entrada inválida. Por favor, ingresa una palabra que no contenga números, espacios o caracteres especiales.")


def solicitar_cadena_2():
    while True:
        cadena = input("Por favor, ingresa la segunda palabra: ")
        if cadena.isalpha():
            cadena_minusculas = cadena.lower()
            return cadena_minusculas
        else:
            print("Entrada inválida. Por favor, ingresa una palabra que no contenga números, espacios o caracteres especiales.")

# Comprobaciones

# Función para validar si es un palíndromo
def es_palindromo(string):
    cadena_invertida = "".join(reversed(string))
    if string == cadena_invertida:    
        print(f"'{string}'. Es un palíndromo.") 
    else: 
        print(f"'{string}'. No un es palíndromo.")

# Función para validar si son anagramas
def es_anagrama(string_1, string_2):
    palabra_ordenada_1 = sorted(string_1)
    palabra_ordenada_2 = sorted(string_2)
    if palabra_ordenada_1 == palabra_ordenada_2:
        print(f"'{string_1}' y '{string_2}'. Son anagramas.")
    else:
        print(f"'{string_1}' y '{string_2}'. No son anagramas.")


# Función para validar si es un isograma
def es_isograma(string):
    palabra_unica = set()
    for char in string:
        if char in palabra_unica:
            return False    
        else:
            palabra_unica.add(char) 
    return True


# Llamada de funciones
cadena_1 = solicitar_cadena_1()
cadena_2 = solicitar_cadena_2()

es_palindromo(cadena_1)

es_anagrama(cadena_1, cadena_2)

if es_isograma(cadena_1):
    print(f"'{cadena_1}'. Es un isograma.")
else:
    print(f"'{cadena_1}'. No es un isograma.")
 