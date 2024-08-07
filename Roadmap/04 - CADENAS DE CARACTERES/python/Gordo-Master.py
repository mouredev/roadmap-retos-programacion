"""
Cadena de caracteres
"""



my_string = "¡Hola Comunidad!"

# Metodos comunes de una secuencia

print(my_string[1]) # Acceso

for x in my_string: # Recorriendo el str(es una secuencia inmutable)
    print(x)

print("m" in my_string) # Presencia
print("m" not in my_string)

print(my_string + " 2 veces") # Concatenación

print(my_string * 3)    # Multiplicación/Repetición

print(my_string[2:6])   # Slice (porción)
print(my_string[:5])   # Slice desde el principio
print(my_string[5:])   # Slice hasta el final
print(my_string[2:15:2]) # Slice con salto
print(my_string[::-1]) # Slice revirtiendo

print(len(my_string))   # Longitud

print(min(my_string))   # Minimo. Segun valor unicode
print(max(my_string))   # Maximo. Segun valor unicode

print(my_string.index("l")) # Buscar la posicion de la primera ocurrencia
print(my_string.count("o")) # Contar las ocurrencias


# Metodos propios de string
my_string = "hola Comunidad de Retos de Programación"

print(my_string.upper()) # Convertir a mayuscula
print(my_string.lower()) # Convertir a minuscula
print(my_string.strip("dH!¡")) # Recortar el inicio y el final de caracteres
print(my_string.replace("u","O"))   # Reemplazar valores
print(my_string.split(" ",2)) # Separar en una lista, hasta "2" ocurrencias

print(my_string.capitalize()) # Mayuscula primera palabra
print(my_string.casefold()) # Vuelve todo minuscula, pero con busqueda con esteroides
print(my_string.center(72,"-")) # Centra el texto
print(my_string.count("o")) #  Cuenta las ocurrencias
print(my_string.encode()) # Codifica el texto, por defecto en utf-8
print(my_string.endswith("ión")) # boolean: final de string
print("H\to\tl\ta".expandtabs(3)) # Cambia los tab por espacios
print(my_string.find("ad")) # Busca la posición de la expersión
print(my_string.index("ad")) # Busca la posición de la expersión, error = no found
print(my_string.isalnum()) # Es alfanumerico
print(my_string.isalpha()) # Es alfabetico 
print("Hola".isascii()) # Es ascii
print("45".isdecimal()) # Es decimal (0-9)
print(my_string.isdigit()) # Es un digito (decimal y mas)
print("my_string".isidentifier()) # Es un identificador
print(my_string.islower()) # Es minuscula
print("\u2155".isnumeric()) # Es un numero (digito y mas)
print("\u2155") 
print(my_string.isprintable()) # Es imprimible
print(my_string.isspace())  # Es todo espacio
print("Hola Mundo".istitle())  # Es tipo titulo (mayuscula en palabras)
print("Hola Mundo".isupper()) # Es todo mayuscula
print("@".join(["tomas","cain","abel"]))  # Une iterables en str
print(my_string.ljust(72,"*")) # Justificado izquierdo
print(my_string.lstrip("ho"))    # Elimina los caracteres dados del comienzo
print(my_string.partition(" "))    #  Da una tupla de 3, de acuerdo al sep.
print(my_string.removeprefix("hola")) # Quita el prefijo (coincidencia exacta)
print(my_string.removesuffix("ción")) # Quita el sufijo (coincidencia exacta)
print(my_string.replace("hola","Hi"))  # Reemplaza los str dados 
print(my_string.rfind("ma")) # Un find que comienza desde la derecha
print(my_string.rindex("ma"))   # Un indes desde la derecha 
print(my_string.rjust(72,"*"))    # Justificación a la derecha
print(my_string.rpartition(" "))   # Partición desde la derecha 
print(my_string.rsplit(" "))   # Separa el str y da una lista, no devuelve el separador
print(my_string.rstrip("nó")) # Quita los caracteres dados desde el final
print(my_string.split(" ",maxsplit=2)) # Separa el string y da una lista, no devuelve el sep
print("String\ncon\nvarias\nlineas".splitlines()) # Retorna una lista de varias lineas de str, con separadores
print(my_string.startswith("hol")) # Si comienza con el caracter dado
print(my_string.strip("hol")) # el str no puede comenzar ni terminar con ninguno de los caracteres dados 
print(my_string.swapcase()) # Cambia mayuscula por minuscula y viceversa
print(my_string.title())    # Todas la palabras empiezan en mayuscula, resto minuscula 
print(my_string.zfill(72))  # Rellena de 0 hacia la izquierda, hasta tenes la longitud especificada
x = str.maketrans("hr","ei")    #(static) Hace un dict para usar en str.translate
print(x) 
print(my_string.translate(x)) # Transforma caracter por caracter segun el dict dado


# Formateo
print("Texto de {} formatado de {} maneras".format("Python",5*5))

mapa: dict ={
    "Nombre":"Python",
    "cantidad":"muchas"
}
print("Texto de {Nombre} formatado de {cantidad} maneras".format_map(mapa))



"""
Ejercicio extra
"""

# Palíndromos (se lee de igual comenzando desde la izquierda o la derecha)
def is_pal(text_1:str):
    if text_1 == text_1[::-1]:
        return f"La palabra '{text_1}' es un palindromo"
    return f"La palabra \"{text_1}\" NO es un palindromo"

# Anagramas (Se permutan sus letras para conseguir esas palabras)
def is_anag(text_1:str, text_2:str):
    x1 = sorted(text_1)
    x2 = sorted(text_2)
    if x1 == x2:
        return f"La palabra \"{text_1}\" y \"{text_2}\" son anagramas"
    return f"La palabra \"{text_1}\" y \"{text_2}\" NO son anagramas"

# Isogramas (cuando ni una letra se repite, al ser dos me imagino que una no contiene a otra)
def is_iso(text_1:str):
    contador = text_1.count(text_1[0])
    for i in text_1:
        if text_1.count(i)!=contador:
            return f"La palabra \"{text_1}\" NO es un isograma"
    return f"La palabra \"{text_1}\" es un isograma"

print(is_pal("radar"))
print(is_pal("pera"))
print(is_anag("sentido","destino"))
print(is_anag("intuición","logica"))
print(is_iso("murcielago"))
print(is_iso("jirafa"))