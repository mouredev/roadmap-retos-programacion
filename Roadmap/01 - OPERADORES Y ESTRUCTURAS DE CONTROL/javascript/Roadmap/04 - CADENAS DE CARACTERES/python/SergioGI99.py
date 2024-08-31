"""
--------------------
CADENA DE CARACTERES
--------------------
EJERCICIO:
Muestra ejemplos de todas las operaciones que puedes realizar con cadenas de caracteres
en tu lenguaje. Algunas de esas operaciones podrían ser (busca todas las que puedas):
- Acceso a caracteres específicos, subcadenas, longitud, concatenación, repetición,
  recorrido, conversión a mayúsculas y minúsculas, reemplazo, división, unión,
  interpolación, verificación...

DIFICULTAD EXTRA (opcional):
Crea un programa que analice dos palabras diferentes y realice comprobaciones
para descubrir si son:
- Palíndromos
- Anagramas
- Isogramas
"""

# Ejercicio

my_string: str = "Esto es un string de prueba "
my_otherString: str = "Esto es otro string de prueba"

# Acceso a caracteres específicos
print(my_string.find("es"))

# Subcadenas
my_subString: str = my_string[11:17]
print(my_subString)

my_other_subString: str = "es"
print(my_other_subString in my_string) # Devuelve un bool

# Longitud
print(len(my_string)) # my_string tiene 27 caracteres

# Concatenación
print(my_string + my_otherString)

# Repetición
print(my_string * 2)

# Mayusculas
print(my_string.upper())

# Reemplazo
my_new_string: str = my_string.replace("un string", "una cadena de texto")
print(my_new_string)

# División
divided_string: str = my_string[11:17]
print(divided_string)

# Interpolación
print(f"Esto es un {divided_string.upper()} interpolado")

# Verificación
print(my_string.isalpha()) # Devuelve False porque los espacios no son alfabeticos
my_last_string = "Hola"
print(my_last_string.isalpha()) # Devuelve True


# EJERCICIO EXTRA

print("Vamos a comprovar si dos palabras son Palíndromos, Anagramas o Isogramas")
word_one: str = (input("Primera palabra: ")).lower()
word_two: str = (input("Segunda palabra: ")).lower()

def invertir_cadena(cadena):
    cadena_invertida = ""
    for letra in cadena:
        cadena_invertida = letra + cadena_invertida
    return cadena_invertida

def esAnagrama(cad1, cad2):
    return sorted(cad1) == sorted(cad2)

def esIsograma(word: str) -> bool:
    leter_dict = {}
    for leter in word:
        if leter in leter_dict:
            leter_dict[leter] += 1
        else:
            leter_dict[leter] = 1

    values = list(leter_dict.values())
    isogram_len = values[0]
    for leter_count in values:
        if leter_count != isogram_len:
            return False
    return True

if invertir_cadena(word_one) == word_two:
    print(f"{word_one} y {word_two} son palíndromos")
else:
    print(f"{word_one} y {word_two} no son palíndromos")

if esAnagrama(word_one, word_two):
    print(f"{word_one} y {word_two} son anagramas")
else:
    print(f"{word_one} y {word_two} no son anagramas")

if esIsograma(word_one):
    print(f"{word_one} es un Isograma")
else:
    print(f"{word_one} no es un Isograma")

if esIsograma(word_two):
    print(f"{word_two} es un isograma")
else:
    print(f"{word_two} no es un isograma")