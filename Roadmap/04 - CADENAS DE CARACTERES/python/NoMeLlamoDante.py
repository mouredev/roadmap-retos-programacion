"""
#! EJERCICIO:
 * Muestra ejemplos de todas las operaciones que puedes realizar con cadenas de caracteres
 * en tu lenguaje. Algunas de esas operaciones podrían ser (busca todas las que puedas):
 * - Acceso a caracteres específicos, subcadenas, longitud, concatenación, repetición, recorrido,
 *   conversión a mayúsculas y minúsculas, reemplazo, división, unión, interpolación, verificación...
"""
texto = "hola, me dicen Dante"
texto_completo = "hola, me dicen Dante\ty soy un programador"
numeros = "1234567890"
print(texto)

#! Convierte caracteres
print(texto.capitalize()) #Primero mayuscula, resto minusculas
print(texto.casefold()) #Convierte a minusculas
print(texto.lower()) #Convierte a minusculas
print(texto.swapcase()) #Invierte mayusculas y minusculas
print(texto.title()) #Convierte a titulo (primera letra de cada palabra en mayuscula)
print(texto.upper()) #Convierte a mayusculas

#! Elimina los espacios en blanco 
print(texto.lstrip()) #A la izquierda
print(texto.strip()) #A ambos lados
print(texto.rstrip()) #Elimina los espacios en blanco a la derecha

#! Verifica si todos los caracteres coinciden con un criterio
print(texto.isalnum()) #Alfanumerico
print(texto.isalpha()) #Alfabetico
print(texto.isascii()) #ASCII

print(numeros.isdecimal()) #Decimal
print(numeros.isdigit()) #Digito
print(numeros.isnumeric()) #Numerico

print(texto.islower()) #Minusculas
print(texto.isupper()) #mayusculas

print(texto.isidentifier()) #Identificador
print(texto.isprintable()) #Imprimible
print(texto.isspace()) #Espacios
print(texto.istitle()) #Titulo (Primera letra de cada palabra en mayuscula)

#! Justifica Caracteres de acuerdo a un ancho especificado
print(texto.ljust(50)) #Justificado a la izquierda
print(texto.center(50)) #Al centro
print(texto.rjust(50)) #Justificado a la derecha

#! Buscar dentro de la cadena
#Cuenta cuantas veces aparece una subcadena, con un origen dado
print(texto.count(" ", 8)) 
#Verifica si la cadena termina con una subcadena
print(texto_completo.endswith("programador")) 
#Verifica si la cadena comienza con una subcadena
print(texto_completo.startswith("hola"))
#Devuelve la posicion de la primera ocurrencia de una subcadena
print(texto_completo.find("pr"))
#Devuelve la posicion de la ultima ocurrencia de una subcadena
print(texto_completo.rfind("pr")) 
#Devuelve la posicion de la primera ocurrencia de una subcadena
print(texto.index("Dante")) 
#Devuelve la posicion de la ultima ocurrencia de una subcadena
print(texto_completo.rindex("Dante")) 

#! Cambia el valor de las tabulaciones por el numero especificado de espacios
print(texto_completo.expandtabs(2))

#! Formatea la cadena con los valores especificados
texto2 = "Estoy practicando {lenguaje} con los ejercicios prácticos de {autor}"
print(texto2.format(lenguaje="Python", autor="Mouredev"))

print(f"el texto de ejemplo es: \" {texto} \"")

print(texto2.format_map({
            "lenguaje":"Python",
            "autor":"Mouredev"
        })
    )

print(texto.zfill(50)) #Rellena con ceros a la izquierda

#! Cadenas y subcadenas
#Une una lista de cadenas con un separador
print("-".join(["hola", "mundo", "python"])) 
#Divide la cadena en una tupla con tres elementos con el separador especificado
print(texto_completo.partition("Dante")) 
#Divide la cadena en una tupla con tres elementos con el separador especificado
print(texto_completo.rpartition("Dante")) 
#Reemplaza una subcadena dentro del texto
print(texto.replace("Dante", "Mouredev"))
#Divide la cadena en una lista de subcadenas con el separador especificado
print(texto.split(" ")) 
#Divide la cadena en una lista de subcadenas con el separador especificado
print(texto.rsplit(" ")) 
#Divide la cadena en una lista de subcadenas con el separador especificado
print(texto.split(" ")) 
#Divide la cadena en una lista de subcadenas con el separador de salto de linea
print(texto.splitlines()) 

#! Permite tablas de reemplazo de caracteres
texto_ejemplo = "tata"
tabla_conversion = str.maketrans("t", "p")
print(texto_ejemplo.translate(tabla_conversion))

"""
#! DIFICULTAD EXTRA (opcional):
 * Crea un programa que analice dos palabras diferentes y realice comprobaciones
 * para descubrir si son:
 * - Palíndromos
 * - Anagramas
 * - Isogramas
"""
#Todo Palíndromos
def es_palindromo(text, ignore_spaces = True):
    text = text.lower()
    if ignore_spaces:
        text = text.replace(" ", "")
    return text == reverse(text)

def reverse(text):
    return text[::-1]


print(es_palindromo("lavanderia"))
print(es_palindromo("eva usaba rimel y le miraba suave"))

#Todo Anagramas
def es_anagrama(text1, text2):
    list1 = list(text1.lower())
    list1.sort()
    list2 = list(text2.lower())
    list2.sort()
    return list1 == list2

print(es_anagrama("rosa", "arroz"))
print(es_anagrama("roma", "amor"))

#Todo Isogramas (Todas las letras se repiten el mismo numero de veces)
def contador_caracteres(text:str):
    text = text.lower()
    if text.isalpha():
        caracteres = {}
        for char in text:
            if char in caracteres.keys():
                caracteres[char] += 1
            else:
                caracteres[char] = 1
        return caracteres
    return False

def es_isograma(text:str):
    caracteres = contador_caracteres(text)
    num_caracteres = list(caracteres.values())
    return num_caracteres.count(num_caracteres[0]) == len(num_caracteres)
    
print(es_isograma("intestines"))
print(es_isograma("Vivienne"))
print(es_isograma("alondra"))