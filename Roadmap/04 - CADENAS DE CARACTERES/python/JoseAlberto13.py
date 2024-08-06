"""
 * EJERCICIO:
 * Muestra ejemplos de todas las operaciones que puedes realizar con cadenas de caracteres
 * en tu lenguaje. Algunas de esas operaciones podrían ser (busca todas las que puedas):
 * - Acceso a caracteres específicos, subcadenas, longitud, concatenación, repetición, recorrido,
 *   conversión a mayúsculas y minúsculas, reemplazo, división, unión, interpolación, verificación...
"""
mi_string = "Hola Python"
mi_string2 = "Hola GitHub!"
nombre = "José"
edad = 26


# Acceso a caracter específico
print(mi_string[5])
print(mi_string[6])
print(mi_string[7])
print(mi_string[8])
print(mi_string[9])
print(mi_string[10])
"""Python"""


# Subcadenas
print(mi_string[2:7])
"""slicing = la Py"""

print(mi_string[-6:])
"""slicing = Python (Ultimos caracteres)"""

print(mi_string[::-1])
"""slicing reversa"""

print(mi_string[::2])
"""slicing salto de caracteres """

cadena_string = "@JoseAlberto13 programando en python desde el 2024"
print(cadena_string.split()) # Este método crea una lista de subcadenas

reversa = reversed(nombre) #reversa una palabra, es necesario transformarla en una lista para su impresion 
print(list(reversa)) #transformamso la variable string en lista para su impresion


# Subcadenas "Búsqueda"
otraString = "Git"

print(otraString in mi_string2) # retorna un boleano si encuentra o no la palabra dentro "in" de la cadena de texto

print(mi_string2.find(otraString)) # Este metodo retorna la posicion donde encuentra el primer caracter de la palabra buscada "find"

print(mi_string.startswith("Hola")) # Este método retorna un valor booleano si encuentra o no la palabra al inicio de la cadena de texto

print(mi_string.endswith("thon")) # Este método retorna un valor booleano si encuentra o no la palabra al final de la cadena de texto

print(cadena_string.count("de")) # Este método cuenta las veces que aparece la palabra "de" dentro cadena de texto


# Longitud
print(mi_string," tiene " , len(mi_string) , " caracteres" )


# Concatenación
print(mi_string + mi_string2)

print(mi_string + " " + mi_string2)

print("Mi nombre es {} y tengo {} años".format(nombre, edad))

print(f"{mi_string}, mi nombre es {nombre} y tengo {edad} años")


# Alineado 
print('{:<15}''{:<7}''{:<4}'.format(mi_string,nombre,edad)) # Alineado a la derecha

print('{:>15}''{:>7}''{:>4}'.format(mi_string,nombre,edad)) # Alineado a la izquierda

print('{:^15}''{:^7}''{:^4}'.format(mi_string,nombre,edad)) # Alineado al centro

print('{:*^15}''{:*^7}''{:*^4}'.format(mi_string,nombre,edad)) # usa '*' para rellenar y ver el sentido de la alineación

print('{:*>15}''{:*>7}''{:*>4}'.format(mi_string,nombre,edad)) # usa '*' para rellenar y ver el sentido de la alineación


# Repetición
print(mi_string2, mi_string2, mi_string2)

print(mi_string2 * 3)


# Recorrido
for i in mi_string:
    print(i)
print("")
i = 0
while i < len(mi_string):
    i+=1
    print(mi_string[i *-1])


# Conversión a Mayúsculas y Minúsculas
print(cadena_string.upper())

print(cadena_string.lower())

print("jose".capitalize()) # Convierte en mayúscula la primera letra

print(cadena_string.title()) # Formatea el texto, colocando al inicio de cada palabra en mayúscula

print(mi_string.swapcase()) # Alterna las mayúsculas por minúsculas y viceversa


# Reemplazo
print("Jose".replace("e","é"))

print(cadena_string.replace(" ","")) # Quitamos los espacios con replace

print(cadena_string.replace("o","oooo")) 

print("Jos@ Alb@rto Figu@roa Luc@na".replace("@", "e"))

print("José Alberto @JoseAlberto13".replace("e", "E", 1)) # El número indica la cantidad de caracteres reemplazará

print("   Esto es un texto con espacios al inicio y al final  ".strip()) # Quita los espacios al inicio y al final del texto

# Reemplazo por medio de indiciese "Mejor usar el método anterior xd"
nombre = "Alverto"
print(nombre)
nombre = nombre[:2] + "b" + nombre[3:] # Dividimos la cadena en 2, y en la intersección agregamos el caracter que deseemos cambiar [inicio:fin] + "caracter" + [inicio:fin]
print(nombre)

numero = "27287281"
print(type(numero), numero)
numero = int(numero)
print(type(numero), numero)
numero = str(numero)

# División
print(cadena_string.split("en")) #divide la cadena de texto en la palabra o caracter indicado y si este no es definido, lo divide en cada espacio en blanco

print(cadena_string.split("e",2)) # donde estaba la "e" es dividido las veces que se le es indicado, si no se le indica la veces que hara la division, esta sera ilimitada
print(type(cadena_string.split("e",2))) # lo transforma en una lista

colores = "amarillo,azul,rojo,blanco"
print(colores)
colores = colores.split(",") # Divideremos los colores por las comas
print(colores)

# División con indices
print(cadena_string[:15] + " / " + cadena_string[22:])


# Unión
print(" ".join(colores))

# Verificación // Comprobación
print("HOLA".isupper()) # Comprueba si un texto esta en mayúsculas
print("Hola".islower()) # Comprueba si un texto esta en minúsculas
print(cadena_string.isnumeric()) 
print(cadena_string.isalnum())
print(cadena_string.isprintable())
print(cadena_string.isascii())
print(numero.isdigit())

"""
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que analice dos palabras diferentes y realice comprobaciones
 * para descubrir si son:
 * - Palíndromos
 * - Anagramas
 * - Isogramas
"""

def palindromo(text1:str, text2:str):
    text1min = text1.lower()
    text2min = text2.lower()
    print(f"'{text1}' es palindromo: {text1min == text1min[::-1]}")
    print(f"'{text2}' es palindromo: {text2min == text2min[::-1]}")

def anagrama(text1:str, text2:str):
    text1min = text1.lower()
    text2min = text2.lower()
    print(f"'{text1} y {text2}' son anagramas: {sorted(text2min)==sorted(text1min)}")

def isograma(text1:str, text2:str):
    text1min = text1.lower()
    text2min = text2.lower()
    print(f"'{text1}' es un isograma: {len(text1min) == len(set(text1min[::-1]))}")
    print(f"'{text2}' es un isograma: {len(text2min) == len(set(text2min[::-1]))}")

palindromo("Anna","Roncar")

anagrama("Gato", "Toga")

isograma("Rancho","Roncando")
