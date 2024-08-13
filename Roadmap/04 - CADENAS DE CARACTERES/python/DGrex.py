"""
 * EJERCICIO:
 * Muestra ejemplos de todas las operaciones que puedes realizar con cadenas de caracteres
   en tu lenguaje. Algunas de esas operaciones podrían ser (busca todas las que puedas):
 * Acceso a caracteres específicos, subcadenas, longitud, concatenación, repetición,
   recorrido, conversión a mayúsculas y minúsculas, reemplazo, división, unión,
   interpolación, verificación...
"""

strings_one = "Soy"
strings_two= "DGrex"

# concatenacion
concatenacion = "(Hola, " + strings_one + " " + strings_two + ")"
print(concatenacion)

# Repeticion
print(concatenacion * 3)

# Indexación
print(concatenacion[1]+strings_one[1]+concatenacion[3]+concatenacion[4])

# Longitud
print(len(concatenacion))

# Slicing o Porción
print(concatenacion[7:])
print(concatenacion[7:16])
print(concatenacion[:17])
print(concatenacion[1:5])

# Busqueda
print("oy" in strings_one)
print("rex" in strings_one)

# Reemplazo
print(strings_two.replace("e", "i"))

# División
#La función split() se utiliza para dividir una cadena en una lista de subcadenas
Lenguajes = "Python Java C++"

print(strings_two.split("G")) 
print(Lenguajes.split()) # Cuando hay parametro tomara los espacios como referencia

# Mayúsculas, minúsculas
print(strings_two.lower())
print(strings_two.upper())
print("soy dgrex".title()) # Primera letra de cada palabra en mayuscula
print("soy dgrex".capitalize()) # Primera letra en mayuscula

# Eliminación de espacios al principio y al final de una cadena
print(" Soy DGrex      ".strip())

# Búsqueda al principio y al final
print(strings_two.startswith("DG"))
print(strings_two.startswith("re"))
print(strings_two.endswith("ex"))

# Búsqueda de posición
string_thre = "Soy DGrex @DGrex__"

print(string_thre.find("DGrex"))
print(string_thre.find("dgrex")) # -1 es subcadena no encontrada
print(string_thre.lower().find("dgrex"))

# Búsqueda de ocurrencias
print(string_thre.upper().count("E"))

# Formateo
print("Hola {} {}.".format(strings_one, strings_two))

# Interpolación
print(f"Hola {strings_one} {strings_two}.")

# Tranformación en lista de caracteres
print(list(string_thre))

# Transformación de lista en cadena
my_name = ["D","G","r","e","x"]
print("".join(my_name))

# Transformaciones numéricas
number = "123456"
number = int(number)
print(f"{number} it's from the  {type(number)}")

number = "123456.123"
number = float(number)
print(f"{number} it's from the  {type(number)}")

# Comprobaciones varias
strings_two= "DGrex"
number = "123456"
print(strings_two.isalnum()) # Es numerico, es alfa, es alfanumerico, si esta vacío da False 
print(strings_two.isalpha()) #Es alfa
print(number.isalpha()) #Es alfa
print(number.isnumeric()) # Es numerico
print(number.isdecimal())

print(isinstance(number, float)) # Compara el tipo de dato de una variable

"""
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que analice dos palabras diferentes y realice comprobaciones
   para descubrir si son:
 * - Palíndromos
 * - Anagramas
 * - Isogramas

"""
def palindromos_anagramas_isogramas(word_one, word_two):
  print

  # Palíndromos

  if word_one.lower() == word_one[::-1].lower():
    print(f"La palabra {word_one} es un palindromo.")
  else:
    print(f"La palabra {word_one} no es un palindromo.")

  if word_two.lower() == word_two[::-1].lower():
    print(f"La palabra {word_two} es un palindromo.")
  else:
    print(f"La palabra {word_two} no es un palindromo.") 

  # Anagramas
 
  if "".join(sorted(word_one.lower())) == "".join(sorted(word_two.lower())):
    print(f"{word_one} y {word_two} si son anagramas.")
  else:
    print(f"{word_one} y {word_two} no son anagramas.")

# Isogramas

  if len(word_one.lower()) == len(set(word_one.lower())):
    print(f"La palabra {word_one} es un isograma.")
  else:
    print(f"La palabra {word_one} no es un isograma.")

  if len(word_two.lower()) == len(set(word_two.lower())):
    print(f"La palabra {word_two} es un isograma.")
  else:
    print(f"La palabra {word_two} no es un isograma.")

palindromos_anagramas_isogramas("ROMA","amor")
#palindromos_anagramas_isogramas("Radar","teclado")

"""
La funcion set crear un conjunto.
Un conjunto es una colección de elementos únicos y desordenados.
Los conjuntos eliminan los duplicados.
"""
