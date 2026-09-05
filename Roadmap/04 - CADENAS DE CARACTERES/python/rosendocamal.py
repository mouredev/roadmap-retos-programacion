"""
 * EJERCICIO:
 * Muestra ejemplos de todas las operaciones que puedes realizar con cadenas de caracteres
 * en tu lenguaje. Algunas de esas operaciones podrían ser (busca todas las que puedas):
 * - Acceso a caracteres específicos, subcadenas, longitud, concatenación, repetición, recorrido,
 *   conversión a mayúsculas y minúsculas, reemplazo, división, unión, interpolación, verificación...
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que analice dos palabras diferentes y realice comprobaciones
 * para descubrir si son:
 * - Palíndromos
 * - Anagramas
 * - Isogramas
"""

# === OPERACIONES CON CADENAS

# Creación de cadenas
text1: str = str()
text2: str = ""
text3: str = ''
text4: str = "Hello, World!"
text5: str = "Hello, Python!"
text6: str = "Hello"
text7: str = "Python"
print(text1, text2, text3, text4, text5, text6, text7)
print()

# Concatenación
new_text1: str = text6 + ", " + text7 + "!"
print(new_text1)
print()

# Repetición
new_text2: str = text7 * 9
print(new_text2)
new_text2: str = (text7 + " ") * 9
print(new_text2)
print()

# Acceso a carácteres y subcadenas
print(new_text2[len(new_text2) - 1])
print(new_text2[-1])
print(new_text2[0: len(text7) - 1])
print(new_text2[:])
print()

# Invertir una cadena:
print(new_text2[::-1])
print()

# Pertenencia y ausencia
pertenencia: bool = text7 in new_text2
ausencia: bool = text4 not in new_text2
print(pertenencia, ausencia)
print()

# Comparación de cadenas
cadena1, cadena2, cadena3, cadena4 = "Hola", "Hola", "Hola ", "hola"
print(cadena1 == cadena1)
print(cadena1 != cadena3)
print(cadena3 >= cadena4)
print(cadena1 <= cadena2)
print(cadena1 == cadena2)
print(cadena1 < cadena3)
print(cadena3 > cadena4)
print()

# Iteración sobre una cadena
cadena: str = "CADENA"
for character in cadena:
    print(character)
else:
    print()

# Conversión a lista, a tupla y a conjunto
cadena2: list = list(cadena)
print(cadena2)
cadena2: tuple = tuple(cadena)
print(cadena2)
cadena2: set = set(cadena)
print(cadena2)
print()

# === TRANSFORMACIÓN DE CADENAS

a, b, c, d = "Cadena A", "Cadena B", "Cadena C", "Cadena D"
print(a.lower().capitalize())
print(b.upper())
print(c.casefold())
print(d.swapcase())
print(d.lower().title())
print(a.lower())
print(b.replace("Cadena", "Texto"))
"""c.translate()"""
"""d.maketrans()"""
print(a.removeprefix("Cadena"))
print(a.removesuffix("A"))
print()

# === MÉTODOS DE DIVISIÓN Y UNIÓN
print(b.split())
print(b.split("a"))
print(b.rsplit())
print(f"{c}\n{c}\n{c}\n".splitlines())
print(d.partition(" "))
print(d.rpartition(" "))
print("-".join(['ab', 'pq', 'rs']))
print()

# === MÉTODOS DE ELIMINACIÓN DE ESPACIOS Y CARÁCTERES
a, b, c, d, e = "HOla", "Hello", "Hi", "Nihâo\t", " Konichiwa  "
print(d, e.strip(), e.strip("i"))
print(d, e.rstrip(), a.rstrip("O"))
print(b, b.lstrip("o"))
print()

# === MÉTODOS DE RELLENO
print(d.center(35))
print(d.ljust(35))
print(d.rjust(35))
print(d.zfill(34))
print(d.expandtabs(350))
print()

# === MÉTODOS DE VALIDACIÓN
print("5", "5".isalnum())
print("a", "a".isalpha())
print("242".isascii(), "^".isascii)
print("1".isdecimal())
print("9".isdigit())
"""isidentifier()"""
print("minúsculas".islower(), "minusculas".islower())
print("525".isnumeric())
print("ſ€¶@".isprintable())
print("Hola Hola".isspace())
print("Hola Hola".istitle())
print("HOLA HOLA".isupper())
print()

# === FORMATEO
var: str = "String"
lol: int = 123
abc: float = 23542.2341234
print("%s" % var)
print("%i" % lol)
print("%f" % abc)

print("Cadena: {}, Entero: {}, Flotante: {}".format(var, lol, abc))
"""'{}'.format_map(diccionario)"""
print(f"{var}_{lol}_{abc}")
print(repr(ascii(var)))
print(ascii(var))
print()

# === EXTRA

# Palíndromos

def is_palindromo(palabra: str) -> bool:
    if not isinstance(palabra, str):
        return False
    if palabra.strip().lower() == palabra.strip().lower()[::-1]:
        return True
    return False
    
# Anagramas

def is_anagrama_v1(palabra1: str, palabra2: str) -> bool:
    if not isinstance(palabra1, str) or not isinstance(palabra2, str):
        return False
    set_palabra1, set_palabra2 = set(palabra1), set(palabra2)
    if not (set_palabra1 == set_palabra2):
        return False
    for character in set_palabra1:
        contador_p1, contador_p2 = 0, 0
        for i in palabra1:
            if character == i:
                contador_p1 += 1
        for i in palabra2:
            if character == i:
                contador_p2 += 1
        if contador_p1 != contador_p2:
            return False
    return True

def is_anagrama_v2(palabra1: str, palabra2: str) -> bool:
    if sorted(palabra1.lower().strip()) == sorted(palabra2.lower().strip()):
        return True
    return False

# Isogramas

def is_isograma(palabra: str) -> bool:
    if not isinstance(palabra, str):
        return False
    count: dict[str, int] = {}
    set_palabra: set = set(palabra.lower().strip())
    for key in set_palabra:
        count[key] = 0

    for i in set_palabra:
        for j in palabra.strip().lower():
            if j == i:
                count[i] += 1

    for value in count.values():
        if value != 1:
            return False

radar: str = "radAr "
ardor: str = " ARDOR"
amor: str = " amor"

print(radar, is_palindromo(radar))
print(ardor, is_palindromo(ardor))
print(amor, is_palindromo(amor))
print()

print(radar, ardor, is_anagrama_v1(radar, ardor))
print(radar, ardor, is_anagrama_v2(radar, ardor))
print(radar, amor, is_anagrama_v1(radar, amor))
print(radar, amor, is_anagrama_v2(radar, amor))
print()

print(radar, is_isograma(radar))
print(ardor, is_isograma(ardor))
print(amor, is_isograma(amor))