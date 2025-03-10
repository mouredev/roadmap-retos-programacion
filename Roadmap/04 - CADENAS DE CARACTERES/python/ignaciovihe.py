"""
Muestra ejemplos de todas las operaciones que puedes realizar con cadenas de caracteres
en tu lenguaje. Algunas de esas operaciones podrían ser (busca todas las que puedas):
- Acceso a caracteres específicos, subcadenas, longitud, concatenación, repetición, recorrido,
  conversión a mayúsculas y minúsculas, reemplazo, división, unión, interpolación, verificación...
"""

"""
Operaciones de Cadenas de caracteres
"""

#Creación

my_string = 'Permite incluir comillas "dobles"'
my_other_string ="Permite incluircomillas 'simples'"
#con comillas triple se incluyen todos los espacion y saltos de linea pudiendo formatear el texto.
my_new_string = """
Opciones:
    1. Jugar
    2. Opciones
    3. Salir
"""

print(my_new_string)

print(my_new_string[15]) #Acceso a un caracter especifico
print(my_new_string[15:23]) # Slicing de subcadenas
print(len(my_new_string)) # Longitud de cadena

print(my_new_string + my_string) # Concatenación de cadenas
print(my_string * 3) #Repeticion de cadenas

for char in my_new_string: #Recorrido de cadenas.
    print(char)

my_string ="mi Cadena en minusculas"
print(my_string.upper()) #Convierte todo a mayusculas
print(my_string.capitalize()) # Convierte solo el primer caracter a mayusculas. Cuidado espacios al inicio.
print(my_string.lower()) #Conbierte todo a minusculas.
print(my_string.title()) # Convierte la primera letra de cada palabra en mayus.

texto1 = "Straße"  # "Straße" es "calle" en alemán
texto2 = "STRASSE"
print(texto1.lower())   # "straße"
print(texto1.casefold()) # "strasse" Convierte todo a minusculas de forma mas agresiva. ß --> ss

my_string= " Texto con espacios inicial y final " 
print(my_string.strip()) # Elimina espacios al principio y al final.

my_new_string = """
Opciones:
    1. Jugar
    2. Opciones
    3. Salir
"""
#Se reemplaza el primer parametro con el segundo. Crea una nueva cadena.
my_string = my_new_string.replace("Salir", "Cerrar") 
print(my_string)

words = my_new_string.split("\n") #División de cadenas
print(words)

palabras = ["Python", "es", "genial"]
resultado = " ".join(palabras) # Union de cadenas con join
print(resultado)

print(resultado.find("es")) #devuelve el indice de la primera aparicion de la cadena pasada dentro de otra

#Interpolación

name = "Ignacio"
edad = 40
print(f"Me llamo {name} y tengo {edad} años") # con f-strings
print("Me llamo {} y tengo {} años".format(name, edad)) # Con format.

# Verificación

texto = "Python es increíble"
print("Python" in texto)   #Verificacion de existencia
print("Java" in texto) 
print("Java" not in texto) #Verificacion de no existencia.

archivo = "documento.pdf"
print(archivo.startswith("doc")) #Verificacion de prefijo
print(archivo.endswith(".pdf")) # Verificacion de sufijo
print(archivo.endswith(".doc"))

cadena1 = "12345"
cadena2 = "Python"
cadena3 = "Python123"
cadena4 = " "
cadena5 = "3.14"
print(cadena1.isdigit())   # True (solo números)
print(cadena2.isalpha())   # True (solo letras)
print(cadena3.isalnum())   # True (letras y números)
print(cadena4.isspace())   # True (solo espacios)
print(cadena5.isnumeric()) # False porque tiene un punto

texto = "HOLA"
print(texto.isupper())  #Verificacion de mayusculas 
texto = "hola"
print(texto.islower())  #Verificación de minusculas

# Operaciones adicionales

cadena = "Python, Java , Python, c#"
print(cadena.count("Python")) #Cuenta las ocurrencias de una cadena dentro de otra.
print(cadena.find("Java")) # Devuelve el index de la primera ocurrencia de la cadena pasada en otra. -1 si no esta.
print(cadena.ljust(50, "-"))
print(cadena.rjust(50, "-"))
new_str = cadena.center(50,"_") #centrado de cadenas
print(new_str)


print(f"2 == 2.0: {2 == 2.0}")

"""
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que analice dos palabras diferentes y realice comprobaciones
 * para descubrir si son:
 * - Palíndromos
 * - Anagramas
 * - Isogramas
 */
"""

def check(word_1: str, word_2: str):


    def is_isogramm(word: str) -> bool:
        counter_dict = {letter: word.count(letter) for letter in word}
        if len(set(counter_dict.values())) != 1:
            return False
        return True
    

    #Palindromo
    print(f"{word_1} es un palíndromo?: {word_1 == word_1[::-1]}")
    print(f"{word_2} es un palíndromo?: {word_2 == word_2[::-1]}")


    #Anagrama
    print(f"{word_1} y {word_2} son anagramas?: {sorted(word_1) == sorted(word_2)}")


    #Isograma
    print(f"{word_1} es un isograma?: {is_isogramm(word_1)}")
    print(f"{word_2} es un isograma?: {is_isogramm(word_2)}")

check("radar", "murcielagomurcielago")

