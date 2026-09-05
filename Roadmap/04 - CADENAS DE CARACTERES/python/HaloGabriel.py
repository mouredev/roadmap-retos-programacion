# EJERCICIO
# Muestra ejemplos de todas las operaciones que puedes realizar con cadenas de caracteres
# en tu lenguaje. Algunas de esas operaciones podrían ser (busca todas las que puedas):
# - Acceso a caracteres específicos, subcadenas, longitud, concatenación, repetición, recorrido,
#   conversión a mayúsculas y minúsculas, reemplazo, división, unión, interpolación, verificación.

my_string = "Halo Gabriel"
print(f"Mi string: {my_string}")

# Conversión a mayúsculas y minúsculas
print(f"En mayúsculas: {my_string.upper()}")
print(f"En minúsculas: {my_string.lower()}")
print(f"Cada palabra con una mayúscula inicial: {my_string.title()}")
print(f"Invirtiendo mayúsculas y minúsculas: {my_string.swapcase()}")

# Convertir letra inicial a mayúscula
print(f"Letra inicial en mayúscula: {my_string.capitalize()}")

# Obtener longitud de string
print(f"Número de caracteres: {len(my_string)}")

# Centrar y rellenar
print(f"Rellenar y centrar mi string con 6 #: {my_string.center(len(my_string) + 6, "#")}")
print(f"Rellenar y centrar mi string con 5 #: {my_string.center(len(my_string) + 5, "#")}")
print(f"Rellenar mi string con 5 # a la izquierda: {my_string.rjust(len(my_string) + 5, "#")}")
print(f"Rellenar mi string con 5 # a la derecha: {my_string.ljust(len(my_string) + 5, "#")}")

# Concatenación
my_other_string = "- Python 2026"
print(f"Concatenando strings: {my_string + " " + my_other_string}")
print("Concatenando strings:", my_string, my_other_string)

print(f"Llenando '2026' de 3 ceros a la izquierda: {my_other_string[-4:].zfill(7)}")

my_list = ["ABC", "DEF", "GHI", "JKL"]
print(f"Mi lista: {my_list}")
my_list = "-".join(my_list)
print(f"Mi lista unida: {my_list}")
my_list = my_list.split("-")
print(f"Mi lista separada otra vez: {my_list}")
my_list = "--".join(my_list)
print(f"Mi lista unida otra vez: {my_list}")
print(f"Mi lista separada otra vez de a 2 (rsplit): {my_list.rsplit("--", 2)}")
print(f"Mi lista separada otra vez de a 2 (split): {my_list.split("--", 2)}")

 
# Multiplicar
print(f"Multiplicar por 2: {(my_string + " ") * 2}")
print(f"Multiplicar por 3: {(my_string + " ") * 3}")
print()

# Formateo
my_float = 45.90
print("Username: %s" %(my_string))
print(f"Mi float: {my_float}")
print("Mi float formateado como int: %d" %(my_float))
print("Mi float formateado con un decimal: %.1f" %(my_float))
print("Mi float formateado sin decimales: %.0f" %(my_float))
print("Username: {}".format(my_string))
print("Mi float formateado con un decimal: {:.1f}".format(my_float))
print("Mi float formateado sin decimales: {:.0f}".format(my_float))

mi_info = {
    "nombre": "Gabriel",
    "tecnologias": ["Python", "Java", "C#"]
}

print("Me llamo {nombre} y sé de {tecnologias}".format_map(mi_info))
print()

# Recorrer un string
str_list = []
for i in range(len(my_string)):
    str_list.append(my_string[i])
print(f"Mi string rebanado: {str_list}")

# Otra forma de recorrer un string
a, b, c, d, e, f, g, h, i, j, k, l = my_string
print(f"Mi string rebanado:", a, b, c, d, e, f, g, h, i, j, k, l)

# Recorrer un string al reves:
str_list = []
for i in range(len(my_string) - 1, -1, -1):
    str_list.append(my_string[i])
print(f"Mi string rebanado a la inversa: {str_list}")

# Otra forma de recorrer un string al revés
a, b, c, d, e, f, g, h, i, j, k, l = my_string[::-1]
print(f"Mi string rebanado a la inversa:", a, b, c, d, e, f, g, h, i, j, k, l)

# Subcadenas
print(f"Los 3 primeros caracteres de mi string: {my_string[:3]}")
print(f"Los 3 últimos caracteres de mi string: {my_string[-3:]}")
print(f"Saltando caracteres 2 en 2: {my_string[::2]}")

print(f"Los 2 caracteres del centro:", end = "")
str_medio_uno = my_string[len(my_string) // 2 - 1]
str_medio_dos = my_string[len(my_string) // 2]
print(f"'{str_medio_uno}' & '{str_medio_dos}'")

my_texto = """Python es un lenguaje de alto nivel de programación interpretado cuya filosofía
hace hincapié en la legibilidad de su código."""

print(f"Mi texto: {my_texto}")
print(f"Omitiendo las 5 primeras palabras y saltando caracteres de 2 en 2: {my_texto[25::2]}")
print(f"Omitiendo las 5 primeras y 5 últimas palabras: {my_texto[25:-29]}")

print(f"Separando mi texto con la palabra 'programación' en un set: {my_texto.partition("programación")}")
print(f"Mi texto sin las 5 primeras palabras: {my_texto.removeprefix("Python es un lenguaje de ")}")
print(f"Mi texto sin las 5 últimas palabras: {my_texto.removesuffix(" la legibilidad de su código.")}")

# Reemplazo
print(f"Reemplazar 'Python' con 'Java': {my_texto.replace('Python', 'Java')}")
print(f"Reemplazar cada 'a' con 'A': {my_texto.replace('a', 'A')}")

print(f"Separando líneas de mi texto: {my_texto.splitlines()}")
print()

# Verificaciones
print(f"Número de 'a' en mi texto: {my_texto.count("a")}")
print(f"Número de 'de' en mi texto: {my_texto.count("de")}")
print(f"Número de 'a' en mi texto a partir de la quinta palabra: {my_texto.count("a", 25)}")
print(f"Número de 'de' en mi texto omitiendo las últimas 5 palabras: {my_texto.count("de", 0, -29)}")
print()

print(f"¿Mi string termina en 'l'? {"Falso" if not my_string.endswith('l') else "Verdadero"}")
print(f"¿Mi string termina en 'Gabriel'? {"Verdadero" if my_string.endswith('Gabriel') else "Falso"}")
print(f"¿Mi string termina en 'Halo'? {"Verdadero" if my_string.endswith('Halo') else "Falso"}")
print(f"¿Mi string empieza en 'H'? {"Verdadero" if my_string.startswith('H') else "Falso"}")
print(f"¿Mi string empieza en 'Halo'? {"Verdadero" if my_string.startswith('Halo') else "Falso"}")
print(f"¿Mi string empieza en 'Gabriel' {"Falso" if not my_string.startswith('Gabriel') else "Verdadero"}")
print()

string_x = "30"
string_y = "Treinta"
print(f"String X: '{string_x}'")
print(f"String Y: '{string_y}'")

print(f"¿Es string X alfanumérico? {string_x.isalnum()}")
print(f"¿Es string Y solo letras? {string_y.isalpha()}")
print(f"¿Es string X un número? {string_x.isdecimal()}")
print(f"¿Es string Y solo dígitos? {string_y.isdigit()}")
print(f"¿Es string X númerico? {string_y.isnumeric()}")
print(f"¿Está string X en ASCII? {string_x.isascii()}")
print(f"¿Se puede imprimir el string Y? {string_y.isprintable()}")
print(f"¿Es string X espacios en blanco? {string_x.isspace()}")
print(f"¿Es string Y un título? {string_y.istitle()}")

print(f"¿Es string Y un nombre de variable válido? {string_y.isidentifier()}")
print(f"¿Es string X un nombre de variable válido? {string_x.isidentifier()} (empieza con un número)")

print(f"¿Está '{string_y}' en mayúsculas? {string_y.isupper()} (solo la T está en mayúscula)")
print(f"¿Está '{string_y}' en minúsculas? {string_y.islower()} (la T está en mayúscula)")
print()

# Búsqueda
print(f"Index del primer 'de' en mi texto: {my_texto.find('de')}")
print(f"Index del primer 'Java' en mi texto: {my_texto.find('Java')} (no se encontró)")
print(f"Index del último 'de' en mi texto: {my_texto.rfind('de')}")
print(f"Index del último 'C#' en mi texto: {my_texto.rfind('C#')} (no se encontró)")
print(f"Index del primer 'a' en mi texto: {my_texto.index('a')}")
print(f"Index del último 'a' en mi texto: {my_texto.rfind('a')}")
print()

# Secuencias de escape
print("Secuencias de escape:")
print("1. Nueva\nlínea (\\n)")
print("2. Tab\tulación (\\t)")
print("3. Expandir\ttabulaciones\t(expandtabs())".expandtabs())
print("4. Expandir\ttabulaciones\t(expandtabs(10))".expandtabs(10))

# Encode
my_final_string = "Adiós Python"
print(f"Mi string final: {my_final_string}")
print(f"Mi string final encoded: {my_final_string.encode()}")
my_tabla = str.maketrans("Adiós", "Holas")
print(f"Usando maketrans(): {my_final_string.translate(my_tabla)}")


# DIFICULTAD EXTRA (opcional):
# Crea un programa que analice dos palabras diferentes y realice comprobaciones
# para descubrir si son:
# - Palíndromos
# - Anagramas
# - Isogramas

from unidecode import unidecode

print("############################")
print("### ANÁLISIS DE PALABRAS ###")
print("############################")

continuar = True

def validar_continuacion() -> bool:
    rpta = input("¿Deseas continuar? ").strip().lower()
    if rpta not in ['yes', 'y', 'si', 'sí', 's']:
        return False
    return True

def identificar_palindromo(palabra: str) -> bool:
    minusculas = palabra.lower()
    if minusculas[::-1] == minusculas:
        print(f"'{palabra}' es un Palíndromo.")
        return True
    return False

def list_sin_espacios(palabra: str) -> list:
    palabra = unidecode(palabra)
    lista = []
    for i in range(len(palabra)):
        caracter = palabra[i]
        if (caracter != " "
            and (caracter.isnumeric() or caracter.isalpha())):
            lista.append(caracter)
    return lista

def identificar_anagramas(primera_palabra: str, segunda_palabra: str) -> bool:
    primera_en_lista = list_sin_espacios(primera_palabra.lower())
    segunda_en_lista = list_sin_espacios(segunda_palabra.lower())
    primera_en_lista.sort()
    segunda_en_lista.sort()
    if primera_en_lista == segunda_en_lista:
        print(f"'{primera_palabra}' y '{segunda_palabra}' son Anagramas de la otra.")
        return True
    return False

def identificar_isograma(palabra: str, orden: int) -> bool:
    if orden != 1 and orden != 2:
        print(f"Orden de isograma no válido.")
        return False
    lista_caracteres = list_sin_espacios(palabra.lower())
    set_caracteres = set(lista_caracteres)
    for caracter in set_caracteres:
        if lista_caracteres.count(caracter) != orden:
            return False
    print(f"'{palabra}' es un Isograma de ", end = "")
    print("primer" if orden == 1 else "segundo", end = "")
    print(" orden.")
    return True

while continuar:
    primera_palabra = input("Ingresar primera palabra: ").strip()
    segunda_palabra = input("Ingresar segunda palabra: ").strip()

    chk_uno = identificar_palindromo(primera_palabra)
    chk_dos = identificar_palindromo(segunda_palabra)

    if not chk_uno and not chk_dos:
        print(f"Ni '{primera_palabra}' ni '{segunda_palabra}' son Palíndromos.")

    if not identificar_anagramas(primera_palabra, segunda_palabra):
        print(f"'{primera_palabra}' y '{segunda_palabra}' no son Anagramas de la otra.")

    chk_uno = identificar_isograma(primera_palabra, 1)
    chk_dos = identificar_isograma(segunda_palabra, 1)
    chk_tres = identificar_isograma(primera_palabra, 2)
    chk_cuatro = identificar_isograma(segunda_palabra, 2)

    if not chk_uno and not chk_dos and not chk_tres and not chk_cuatro:
        print(f"Ni '{primera_palabra}' ni '{segunda_palabra}' son Isogramas.")

    continuar = validar_continuacion()

print("ANÁLISIS FINALIZADO")