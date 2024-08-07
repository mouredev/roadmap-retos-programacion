#04 CADENAS DE CARACTERES

"""
 * EJERCICIO:
 * Muestra ejemplos de todas las operaciones que puedes realizar con cadenas de caracteres
 * en tu lenguaje. Algunas de esas operaciones podrían ser (busca todas las que puedas):
 * - Acceso a caracteres específicos, subcadenas, longitud, concatenación, repetición, recorrido,
 *   conversión a mayúsculas y minúsculas, reemplazo, división, unión, interpolación, verificación...
"""

# Manipulación de casos y formato

string = "ergO prOxy"
print(f"Este es la cadena original: {string}")                   # String original
print(f"Ahora se capitaliza la primera letra: {string.capitalize()}")      # Convierte la primera letra a mayúscula
print(f"Todas las letras en mayús: {string.upper()}")           # Convierte la cadena a mayúsculas
print(f"Todas las letras en minús: {string.lower()}")           # Convierte la cadena a minúsculas            
print(f"Invirtiendo minús y mayús: {string.swapcase()}")        # Invierte mayús y minús
print(f"Ahora, en formato título: {string.title()}")           # Convierte la cadena a formato título
print(f"Normalizado a minús: {string.casefold()}")        # Normaliza a minús el texto de forma más agresiva que lower()

# Alineación y relleno          
palin = "Jelenovi pivo nelej"   

print(f"Centrado de la frase con *: {palin.center(25,'*')}")     # Centra el texto a un ancho determinado con caracteres determinados
print(f"Centrado de la frase con -: {palin.center(25,'-')}")     
print(f"Centrado de la frase con \" \": {palin.center(25,' ')}")     
print(f"Ajuste por la izquierda: {palin.ljust(25,'*')}")      # Ajusta el texto por la izquierda, rellenando con caracteres
print(f"Ajuste por la derecha: {palin.rjust(25,'*')}")      # Ajusta el texto por la derecha, rellenando con caracteres
print(f"Agrega 0 al comienzo: {palin.zfill(25)}")          # Añade 0 al comienzo de la cadena hasta rellenar un ancho determinado

# Comprabaciones y validaciones 
s = "123 por mi"                
print(f"¿Es {s} alfanumérico? {s.isalnum()}")              # Comprueba si es alfanumérico
print(f"¿Es {s} solo letras? {string.isalpha()}")         # Comprueba si son letras
print(f"¿Es {s} ASCII? {string.isascii()}")         # Comprueba si es ASCII
s2 = "123"                       
print(f"¿Es {s2} decimal? {s.isdecimal()}")            # Comprueba si es decimal
print(f"¿Es {s2} un digito? {s.isdigit()}")              # Comprueba si son digitos
print(f"¿Es {s2} un id váldio? {string.isidentifier()}")    # Comprueba si es un identificador válido / Un identificador es el nombre de la variable, puede ser Aa_09
print(f"¿Está {s} en minús? {string.islower()}")         # Devuelve True si todos los caracteres están en minús
print(f"¿Es {s2}? {s.isnumeric()}")            # Devuelve True si todos los caracteres son numéricos
print(f"¿Es {s} imprimible? {string.isprintable()}")     # Devuelve True si todos los caracteres son printables o si la cadena está vacía.
print(f"¿Todo es \" \" en {s}? {string.isspace()}")         # Devuelve True si todos los caracteres son espacios en blanco
print(f"¿Está {s} en forma de título? {string.istitle()}")         # Devuelve True si todas las palabras están en forma de título
print(f"¿Está {s} en mayús? {string.isupper()}")         # Devuelve True si todos los caracteres están en mayús

# Búsqueda y conteo             
x = "Parangaricutirimicuaro"             
print(f"Cuantas veces aparece \"ar\": {x.count('ar')}")            # Cuenta la ocurrencia de una subcadena
print(f"El índice de la primera ocurrencia \"ga\" es: {x.find('ga')}")             # Encuentra el índice de la primera ocurrencia de la subcadena
print(f"El índice de la primera ocurrencia \"cua\" es: {x.index('cua')}")           # Encuentra el índice de la primera ocurrencia, si no, lanza una excepción
print(f"El índice de la última ocurrencia \"o\" es: {x.rfind('o')}")             # Encuentra el índice de la última ocurrencia de la subcadena      
print(f"El índice de la última ocurrencia \"a\" es: {x.rindex('a')}")            # Última ocurrencia de la subcadena o lanza una excepción
print(f"Comienza con \"Pa\": {x.startswith('Pa')}")       # Comprueba si una cadena comienza con un prefijo
print(f"Termina con \"ro\": {x.endswith('ro')}")       # Comprueba si la cadena termina con un sufijo
print(f"La extensión de {x} es: {len(x)}")                   # Devuelve la extensión de la cadena

# Transformaciones y reemplazos

y = "Charlotte"
print(f"Remplazando 't' por 'x' en {y}: {y.replace('t','x')}")       # Reemplaza la ocurrencia de la subcadena
table = y.maketrans('aeiou','12345')    # Realiza una tabla de referencia para translate
print(f"Reemplazando 'aeiou' por '12345': {y.translate(table)}")       # Traduce según la tabla

# División y unión
z = "Cantaba la noche con susurros de tristeza, en la mesa, el mate se enfriaba"
print(z.split(sep=','))         # Divide la cadena en una lista de subcadenas. El parámetro sep indica un separador, el parámetro maxsplit indica un maximo de divisiones que puedan realizarse
print(z.rsplit('a'))            # Divide la cadena en subcadenas desde el final
z = "Cantaba la noche \ncon susurros de tristeza\n en la mesa\n el mate se enfriaba"
print(z.splitlines(keepends=False)) # Divide la cadena en una lista de líneas (salto de lineas, tabulaciones, etc...)
z = "Cantaba la noche con susurros de tristeza, en la mesa, el mate se enfriaba"
print(z.partition(','))         # Divide la cadena en tres partes usando el separador
print(z.rpartition(','))        # Divide la cadena en tres partes usando el separador, comienza desde el final
u = '-'
print(u.join(['Edipo','Rey']))  # Une un iterable de cadena con la cadena como delimitador
print(z[8:41])                  # Realiza un slice de la cadena, creando una subcadena
print('Edipo' + ' Rey')         # Concatenación de cadena con el operador +
print(u*3)                      # Multiplica la cadena con el operador *
print(f"{y} y su inversión es: {y[::-1]}") # El slicing [::-1] invierte el orden de la cadena


# Eliminación de espacios y caracteres
d = "***oso***"
print(d.strip('*'))             # Elimina los caracteres
print(d.lstrip('*'))            # Elimina los caracteres de la izquierda
print(d.rstrip('*'))            # Elimina los caracteres de la derecha

# Codificación y expansión
e = "Der mishk kalen"
print(e.encode(                 # Retorna la cadena codificada a bytes. Defecto = utf_8, posibles: ascii, utf_32....
    encoding='utf-8',
    errors='strict'
))               
e = "Der\t mishk\t kalen"
print(e.expandtabs(tabsize=15)) # Retorna una copia de la cadena, con los caracteres tipo tab \t reemplazados por espacios.

## Formato

# Format
print("Since we're feeling {}".format("so anesthetized"))           # Formato posicional. Se utilizan los {} para formatear
print("In our comfort {name}".format(name="zone"))                  # Formato nombrado. Ademas de los {}, se llama una variable con el contenido del formato
print("Reminds {} the second {lt}".format("me of",lt="time"))       # Mixto, posicional y nombrado
print("That I f{0}llow{1}d you h{0}m{1}".format("o","e"))           # Con índices. En orden creciente, desde 0, se indican los parámetros 

print("Binario: {0:b}, Hex: {0:x}, Octal: {0:o}".format(42))        # Formato numérico "Binary: 101010, Hex: 2a, Octal: 52"
print("Número formateado: {:.3f}".format(3.14159))                  # Formato numérico con decimales. 3f siginifica 3 float, o 3 decimales

# format_map
letra = {"4f":"We're running out of alibis", "5f":"On the second of may"}
print("{4f}\n{5f}".format_map(letra))                               # Usa las keys en los {} y devuielve los valores de las keys    

# f-string
letra =  "of the summertime"
print(f"Reminds me {letra}")                                        # Pasando una variable entre los {}
a = "winters"
b = " day"
print(f"On this {a + b}")                                           # Utilizando expresiones dentro del formateo
pi = 3.14159
print(f"Pi es: {pi:2f}")                                            # Formato numérico con dos decimales

# Operador %
letra = "See you at the bitter end"
caracteres = 25
division = 25/106
print("%s es una frase que contiene %d caracteres que corresponden al %.2f de este mensaje" %(letra,caracteres,division))


## Desafio extra ##
"""
 * Crea un programa que analice dos palabras diferentes y realice comprobaciones
 * para descubrir si son:
 * - Palíndromos    anna > Palabra que se espeja, por ejemplo, an|na
 * - Anagramas      nana > Palabra con la que puede formarse otra anna -> nana | odio -> oido
 * - Isogramas      abcd > Palabra en la que no se repite ni una letra, o, en la que se repiten todas las letras el mismo número de veces
"""

from collections import Counter

def anagrama(w1,w2):
    w1 = "".join(c.lower() for c in w1 if c.isalpha())
    w2 = "".join(c.lower() for c in w2 if c.isalpha())    
    # Quitar caracteres no alfanumericos 
    # w1 = w1.lower().replace(" ","").replace("-","").replace("/","")
    # w2 = w2.lower().replace(" ","").replace("-","").replace("/","")
    
    if len(w1) != len(w2):
        return ("Las palabras no son anagrama")
    
    counterw1 = Counter(w1)
    counterw2 = Counter(w2)

    # Contar palabras sin Counter
    # for l1,L2 in zip(w1,w2):
    #     if l1 in counterw1:
    #         counterw1[l1] += 1
    #     else:
    #         counterw1[l1] = 1  
    #     if l2 in counterw2:
    #         counterw2[l2] += 1
    #     else:
    #         counterw2[l2] = 1

    if counterw1 == counterw2:   
        return print("Las palabras son anagrama")
    
    return print("Las palabras no son anagrama")

anagrama("an/na","nana-")
anagrama("odio","oido")
anagrama("pajaro","jarron")

import re

def palindromo(word):
    word = re.sub(r'[^a-zA-Z]','',word.lower())  # re.sub(rule, replace, string)
# Otras formas de quitar los caracteres
#   word = "".join(c.lower() for c in word if c.isalpha())
#   word = word.lower().replace(" ","").replace("-","").replace("/","").replace(",","").replace(";","").replace(":","")
    revword = word[::-1]

    if len(word) == 0:
        return print (f"La palabra \"{word}\" está vacía o no contiene caracteres alfanuméricos")

    if word == revword:
        return print (f"La palabra \"{word}\" es palíndromo")
    
    return print (f"La palabra no es palíndromo: \"{word}\" != \"{revword}\"")


palindromo("anna")
palindromo("As I pee sir, I see Pisa")
palindromo("oceano")
palindromo("---   ")


def isograma(word):
    word = re.sub(r'[^a-zA-Z]','',word.lower())  # re.sub(rule, replace, string)
    cword = Counter(word)
    repword = []

    if len(set(list(cword.values()))) == 1:
        return print (f"La palabra \"{word}\" es isograma")
    
    repword = [l for l,f in cword.items() if f > 1]

    repword_count = {l: cword[l] for l in repword}

    return print (f"La palabra \"{word}\" no es isograma, se repite: {repword_count}")

isograma("murcielago")
isograma("gaga")
isograma("programming")

