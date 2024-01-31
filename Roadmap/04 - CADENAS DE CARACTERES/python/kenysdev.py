# ╔══════════════════════════════════════╗
# ║ Autor:  Kenys Alvarado               ║
# ║ GitHub: https://github.com/Kenysdev  ║
# ║ 2024 -  Python                       ║
# ╚══════════════════════════════════════╝
# ************************
# 1. cadenas de caracteres.
# ************************
# Las cadenas en Python, son de tipo inmutable, lo que
# implica que al realizar operaciones con ellas se accede
# a una copia y no al valor original.
str1 = "Esto es una cadena" # commilas dobles.
str2 = 'Esto es una cadena' # comillas simples.
print(type(str2)) #<class 'str'>

# comillas dentro de una cadena
str3 = "comilla doble \" - comilla simple \'"

# Salto de linea: \n
str4 = "Primer linea\nSegunda linea"
print(str3)

# ASCI y Unicode
print("\361") # octal-Unicode de la 'ñ'.

# raw strings: tratar una cadena como literal.
print(r"\361") # \361

# para textos muy largo.
print("""Primer linea
Segunda linea
Tercer linea""")

# Longitud de la cadena.
s = "abcdef"
print(len(s)) # 6

# Acceso a caracteres individuales:
print(s[1]) # b

# Obtener porciones específicas de una cadena.
print(s[1:4]) # bcd
print(s[3:])  # def

# para revertir una cadena
print("abcd"[::-1])

# ------------------------
# Formateo de cadenas:
# ------------------------
# concatenación
s1 = "hola"
s2 = "python"
print(s1 + ", " + s2) #Parte 1 Parte 2

# Interpolación (inserción de valores en la cadena)
a = 5; b = 10
s = f"Los números son {a} y {b}"
print(s) 

s = "Los números son %d y %d." % (5, 10)
print(s)

s = "Los números son {a} y {b}".format(a=5, b=10)
print(s)

# replicación o repetición de cadenas:
s = "Hola "
print(s*3) #Hola Hola Hola

# valor numérico que lo representa y viceversa.
print(chr(241)) # ñ
print(ord("ñ")) # 241

# ordenar
print(sorted("cdba")) # abcd

# ------------------------
# Metodos:
# ------------------------
# búsqueda de subcadenas (in, find, index)
s = "Hello, python!"
print("pyth" in s)  # True
print(s.find("python"))  # 7

# Reemplazo de subcadenas 
print(s.replace("python", "Ben"))

# devuelve una cadena con su primera letra en mayúscula.
print("mi cadena".capitalize()) #Mi cadena

# convierte en minúscula.
print("MI CADENA".lower()) #mi cadena

#  intercambia el caso de cada letra en una cadena.
print("mI cAdEnA".swapcase()) # Mi CaDeNa

# convierte en mayúsculas.
print("mi cadena".upper())

# Letras del inicio.
print("mi cadena".title()) # Mi Cadena

# conteo de repetición de una cadena en otra.
s = "Cantando y llorando."
print(s.count("ando")) #2

# si son alfanuméricos.
print("aeiou1234".isalnum()) # True

# si son alfabéticos.
print("abcdefg".isalpha()) # True

# son numéricos.
print("12345".isdigit())  # True

# considera una gama más amplia de dígitos
print("²346½".isnumeric())  # True

# si están en minúsculas.
print("abc".islower())  # True

# si están en mayúsculas.
print("ABC".isupper())  # True

# si son espacios en blanco.
print("   ".isspace())  # True

# espacios o caracteres específicos al principio y al final.
print("  abc  ".strip()) # abc

# rellena la cadena con ceros a la izquierda.
print("123".zfill(5)) #00123

# devuelve la primera cadena unida a cada uno de los elementos
s = " y ".join(["1", "2", "3"])
print(s) #1 y 2 y 3

# División de cadenas.
lista_ = "a,b,c".split(",")  # ['a', 'b', 'c']
print(lista_)

# ************************
# 1. EJERCICIO:
# ************************
'''
 * Crea un programa que analice dos palabras diferentes y realice comprobaciones
 * para descubrir si son:
 * - Palíndromos
 * - Anagramas
 * - Isogramas
'''

def analizar(str1, str2):
    print(f"""
    "{str1}" es un palíndromo?: {str1 == str1[::-1]}
    "{str2}" es un palíndromo?: {str2 == str2[::-1]}
 
    "{str1}" es un anagrama de "{str2}"?: {sorted(str1) == sorted(str2)}

    "{str1}" es un isograma?: {len(str1) == len(set(str1))}
    "{str2}" es un isograma?: {len(str2) == len(set(str2))}
    """)

analizar("reconocer","vida")
analizar("notas","santo")
analizar("héroe","radar")