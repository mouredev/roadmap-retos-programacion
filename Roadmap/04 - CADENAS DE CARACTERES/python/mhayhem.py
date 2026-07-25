# Muestra ejemplos de todas las operaciones que puedes realizar con cadenas de caracteres
# en tu lenguaje. Algunas de esas operaciones podrían ser (busca todas las que puedas):
# - Acceso a caracteres específicos, subcadenas, longitud, concatenación, repetición, recorrido,
#   conversión a mayúsculas y minúsculas, reemplazo, división, unión, interpolación, verificación...

my_string = "hola python"

# acceso por índice
print(my_string[3]) # "a"

# convertir string en minusculas
print(my_string.casefold()) # hola python a diferencia de lower actua con caracteres especiales de algunos idiomas
print(my_string.lower()) # hola python

# convertir string a mayusculas
print(my_string.upper()) # HOLA PYTHON  transforma todos los caracteres a mayúsculas
print(my_string.capitalize()) # Hola Python solo transforma la primera letra del string
print(my_string.title()) # Hola Python transforma las primera letra despues de un espacio

# reemplazar caracteres
print(my_string.swapcase()) # HOLA PYTHON invierte las mayúsculas y minúsculas
print(my_string.replace("a", "4")) # hol4 python reemplaza un carácter por otro

# comprobación
print(my_string.isalnum()) # False comprueba si es un número
print(my_string.isalpha()) # False comprueba si todos los caracteres son letras, si hay números, espacios, simbolos o signos de puntuación devuelve devuelve False
print(my_string.isascii()) # True comprueba que todos los caracteres sean caracteres dentro de ASCII
print(my_string.startswith("h")) # True comprueba que el string empiece por un caracter específico
print(my_string.endswith("n")) # True comprueba que la string finalice con un csracter específico 

# operaciones varias
print(" ".join(["hola", "mundo"])) # hola mundo  une elementos interables(lista, tupla) con lo que haya en la cadena
print(my_string.encode()) # b'hola python' transforma la string en una secuencia de bytes
print(my_string.count("o")) # 2 cuenta el numero de veces que aparece el carárater indicado
print(my_string.find("s")) # -1 busca el caracter indicado y devuelve su índice, si no encontrase el carácter devuelve -1
print(my_string.split(" ")) # ["hola", "python"] devuelve una lista las subcadenas que se crean ha partir del carácter indicado
print("esto es un {}".format(my_string)) # esto es un hola python inserta una variable en una string, actualmente se usa mas f"str {var}"


# DIFICULTAD EXTRA (opcional):
# Crea un programa que analice dos palabras diferentes y realice comprobaciones
# para descubrir si son:
# - Palíndromos
# - Anagramas
# - Isogramas


def checking_words(text_1, text_2):
    print(f"¿Las palabras {text_1} y {text_2} son isogramas? {set(text_1.lower()) != set(text_2.lower())}")
    print(f"¿Las palabras {text_1} y {text_2} son anagramas? {sorted(text_1.lower()) == sorted(text_2.lower())}")
    print(f"¿Las palabras {text_1} y {text_2} son palíndromas entre sí? {text_1.lower() == text_2.lower()[::-1]}")
    print(f"¿La palabra {text_1} es palíndroma? {text_1.lower() == text_1.lower()[::-1]}")
    print(f"¿La palabra {text_2} es palíndroma? {text_2.lower() == text_2.lower()[::-1]}")
    
checking_words("Dany", "Ynad")