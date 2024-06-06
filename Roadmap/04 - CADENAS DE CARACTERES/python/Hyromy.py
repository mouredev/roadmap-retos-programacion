print("hola buenas".capitalize()) #convertir a letra capital
print("MINUSCULAS".casefold()) #convertir agresivamente a minusculas (util para comparaciones)
print("centrado".center(20)) #centar un texto con un ancho especifico
print("esternocleidomastoideo".count("e")) #contar cuantas veces aparece el string especificado
print("Hyromy".endswith("my")) #comprueba que el string termine con otro string
print("hola buenas tardes".find("buenas")) #encontrar el indice de la primera aparicion de un substring
print("Hyromy".index("m")) #devuelve el indice de la primera aparicion de un substring especificado
print("04Python".isalnum()) #comprueba si el string posee caracteres alphanumericos (solo numeros y letras)
print("Alpha".isalpha()) #comprueba que todo el string sean letras alfabeticas
print("Codigo Ascii".isascii()) #comprueba si el string posee caracteres ascii
print("55".isdecimal()) #comprueba si el string es un numero (no admite punto decimal)
print("minusculas".islower()) #comprueba si esta escrito en minusculas
print("Hola\nbuenas".isprintable()) #comrprueba es imprimible (no posee caracteres de instruccion)
print("\n\t  ".isspace()) #comrpueba que el string sean espacios en blanco, saltos de linea o tabulados
print("Nuevo Titulo".istitle()) #comprueba que cada palabra del string empiece por mayuscula
print("MAYUSCULAS".isupper()) #comprueba que el string este en mayusculas
print(" - ".join(["Hyromy", "Luis", "Paco"])) #usa el string original como separador y concatena el resto de elementos que reciba
print("Hola".ljust(8, "-")) #posiciona el string a la izquierda y rellena con un caracter hasta lograr un largo especificado
print("MAYUS".lower()) #convierte a minusculas
print("     _buenas_".lstrip()) #elimina los espacios en blanco a la izquierda del string
print("Hola, mundo".partition(",")) #divide el string en 3 partes, inicial, central y final deacuerdo a un substring
print("!ping".removeprefix("!")) #remueve el prefijo de un string
print("hola...".removesuffix("...")) #remueve un sufijo de un string
print("Hola buenas tardes".replace("a", "4")) #reemplaza todas las apariciones de un substring por otro
print("hola buenas tardes".rfind("a")) #devuelve el indice de la ultima aparicion del substring
print("Hola".rjust(8, "-")) #acomoda el string a la derecha rellenando con un substring a un largo especificado
print("Hola buenas tardes".split(" ")) #divide el string apartir de un substring especificado
print("hola ¿como estas?".startswith("hola")) #comrpueba que el string comience con otro substring
print("    hola    ".strip()) #elimina los espacios en blanco al inicio y al final
print("DiFiCiL dE lEeR".swapcase()) #invierte el case del string
print("sistema digestivo".title()) #convierte a un titulo
print("mayusculas".upper()) #convierte a mayusculas

# ---- DIFICULTAD EXTRA ----

#la palabra debe de leerse igual al derecho y al reves
def palindromo(string:str):
    string = string.casefold()
    original, copy = "", ""

    for i in string:
        if i != " ":
            original += i
            copy = i + copy
    
    for o, c in zip(original, copy): #agrupar 2 iterables diferentes (deben tener la misma longitud)
        if o != c:
            return False
    else:
        return True


#ambas palabras deben contener las mismas letras
def anagrama(string:str, compare:str):
    string = string.casefold()
    compare = compare.casefold()

    alpha = []
    for i in range(26): #a-z (97-122)
        alpha.append([chr(i + 97), 0])

    for s in string:
        for a in alpha:
            if s == a[0]:
                a[1] += 1
                break

    for c in compare:
        for a in alpha:
            if c == a[0]:
                a[1] -= 1
                break
    
    for i in alpha:
        if i[1] != 0:
            return False
    else:
        return True


#la palabra no debe de tener letras repetidas
def isograma(string:str):
    string = string.casefold()

    alpha = []
    for i in range(26):
        alpha.append([chr(i + 97), 0])

    for s in string:
        for a in alpha:
            if s == a[0]:
                a[1] += 1
                break

    for i in alpha:
        if i[1] > 1:
            return False
    else:
        return True

palabra_1 = input("Dime una palabra => ")
palabra_2 = input("Dime otra palabra => ")
print()

if palindromo(palabra_1):
    print(f"{palabra_1} Es un palindromo")
else:
    print(f"{palabra_1} NO es un palindromo")
if palindromo(palabra_2):
    print(f"{palabra_2} Es un palindromo")
else:
    print(f"{palabra_2} NO es un palindromo")
print()

if anagrama(palabra_1, palabra_2):
    print(f"{palabra_1} y {palabra_2} Son anagramas")
else:
    print(f"{palabra_1} y {palabra_2} NO son anagramas")
print()

if isograma(palabra_1):
    print(f"{palabra_1} Es un isograma")
else:
    print(f"{palabra_1} NO es un isograma")
if isograma(palabra_2):
    print(f"{palabra_2} Es un isograma")
else:
    print(f"{palabra_1} NO es un isograma")